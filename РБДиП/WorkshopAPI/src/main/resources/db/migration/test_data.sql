-- ============================================
-- ГЕНЕРАЦИЯ ТЕСТОВЫХ ДАННЫХ (ИСПРАВЛЕНА FK-ОШИБКА)
-- ============================================

-- 1. Пользователи (10 000)
INSERT INTO users (username, email, password_hash, role, enabled, email_verified)
SELECT 'user_' || i, 'user' || i || '@example.com', '$2a$10$abcdefghijklmnopqrstuv',
       CASE WHEN i % 10 = 0 THEN 'ADMIN' WHEN i % 3 = 0 THEN 'SELLER' ELSE 'CLIENT' END,
       (i % 5 = 0), (i % 5 = 0)
FROM generate_series(1, 10000) AS i;

-- 2. Клиенты (~5600)
INSERT INTO clients (user_id, first_name, last_name, patronymic, phone, is_permanent)
SELECT u.id, 'FirstName' || (u.id % 100), 'LastName' || (u.id % 200),
       CASE WHEN u.id % 3 = 0 THEN NULL ELSE 'Patronymic' || (u.id % 50) END,
       '+79' || LPAD((100000000 + u.id)::TEXT, 9, '0'), (u.id % 10 = 0)
FROM users u WHERE u.role = 'CLIENT' ORDER BY random() LIMIT 8000;

-- 3. Сотрудники (500)
INSERT INTO employees (user_id, position, department)
SELECT u.id, CASE WHEN u.id % 5 = 0 THEN 'Manager' ELSE 'Specialist' END,
       CASE WHEN u.id % 3 = 0 THEN 'Sales' ELSE 'Production' END
FROM users u WHERE u.role IN ('SELLER', 'ADMIN') ORDER BY random() LIMIT 500;

-- 4. Материалы (200)
INSERT INTO materials (name, description)
SELECT 'Material_' || i, 'Description for material ' || i
FROM generate_series(1, 200) AS i;

-- 5. Продукты (5 000)
INSERT INTO products (name, description, sku, weight, price, type, in_stock, is_available)
SELECT 'Product_' || i, 'Description for product ' || i, 'SKU_' || LPAD(i::TEXT, 6, '0'),
       ROUND((random() * 99 + 1)::NUMERIC, 3), ROUND((random() * 99900 + 1000)::NUMERIC, 2),
       CASE WHEN i % 5 = 0 THEN 'RING' WHEN i % 5 = 1 THEN 'NECKLACE' WHEN i % 5 = 2 THEN 'BRACELET'
            WHEN i % 5 = 3 THEN 'EARRINGS' ELSE 'PENDANT' END,
       (random() * 100)::INTEGER, (i % 10 != 0)
FROM generate_series(1, 5000) AS i;

-- 6. Связь продуктов с материалами (15 000)
INSERT INTO product_materials (product_id, material_id, quantity)
SELECT DISTINCT ON (pm.product_id, pm.material_id) pm.product_id, pm.material_id, ROUND((random() * 9 + 0.1)::NUMERIC, 3)
FROM (SELECT (random() * 4999 + 1)::BIGINT AS product_id, (random() * 199 + 1)::BIGINT AS material_id FROM generate_series(1, 20000)) pm
LIMIT 15000;

-- 7. Заказы (50 000) ✅ ИСПРАВЛЕНО: client_id в диапазоне существующих
INSERT INTO orders (client_id, status, total_amount, discount_amount, final_amount, order_datetime)
SELECT c.id,
       CASE WHEN sub.i % 10 = 0 THEN 'COMPLETED' WHEN sub.i % 10 = 1 THEN 'CANCELLED' WHEN sub.i % 10 = 2 THEN 'SHIPPED' ELSE 'PENDING' END,
       sub.total_val,
       sub.discount_val,
       sub.total_val - sub.discount_val,
       CURRENT_TIMESTAMP - (random() * 365 || ' days')::INTERVAL
FROM (
         SELECT i, ROUND((random() * 99000 + 1000)::NUMERIC, 2) as total_val,
                ROUND((random() * 4000)::NUMERIC, 2) as discount_val
         FROM generate_series(1, 50000) AS i
     ) sub
         CROSS JOIN LATERAL (
    SELECT id FROM clients OFFSET floor(random() * 5500) LIMIT 1
    ) c;

-- 8. Позиции заказов (150 000)
INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price)
SELECT o.id, (random() * 4999 + 1)::BIGINT, sub.qty, sub.price, sub.qty * sub.price
FROM (
         SELECT i, (random() * 9 + 1)::INTEGER as qty, ROUND((random() * 49000 + 1000)::NUMERIC, 2) as price
         FROM generate_series(1, 150000) AS i
     ) sub
         CROSS JOIN LATERAL (SELECT id FROM orders OFFSET floor(random() * 49000) LIMIT 1) o;

-- 9. Аудит (200 000)
INSERT INTO audit_log (user_id, action, table_name, record_id, old_values, new_values, ip_address, user_agent)
SELECT (random() * 9999 + 1)::BIGINT,
       CASE WHEN i % 3 = 0 THEN 'CREATE' WHEN i % 3 = 1 THEN 'UPDATE' ELSE 'DELETE' END,
       CASE WHEN i % 5 = 0 THEN 'orders' WHEN i % 5 = 1 THEN 'products' WHEN i % 5 = 2 THEN 'clients'
            WHEN i % 5 = 3 THEN 'users' ELSE 'order_items' END,
       (random() * 100000 + 1)::BIGINT,
       '{"old": "data"}'::JSONB, '{"new": "data"}'::JSONB,
       '192.168.1.' || (i % 255), 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
FROM generate_series(1, 200000) AS i;

ANALYZE;