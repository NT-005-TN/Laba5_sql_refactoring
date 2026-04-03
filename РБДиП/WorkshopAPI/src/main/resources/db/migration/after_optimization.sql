-- ============================================
-- ОПТИМИЗИРОВАННЫЕ ЗАПРОСЫ (ПОСЛЕ ОПТИМИЗАЦИИ)
-- Для сравнения с EXPLAIN ANALYZE
-- ============================================

-- Запрос 1: Поиск заказов по клиенту (с индексом)
EXPLAIN ANALYZE
SELECT id, order_number, status, final_amount, order_datetime
FROM orders
WHERE client_id = 123;

-- Запрос 2: Замена подзапросов на JOIN с GROUP BY
EXPLAIN ANALYZE
SELECT
    c.id, c.first_name, c.last_name,
    COUNT(CASE WHEN o.status = 'COMPLETED' THEN 1 END) as completedOrders,
    COALESCE(SUM(o.final_amount), 0) as lifetimeValue,
    MAX(o.order_datetime) as lastPurchaseDate
FROM clients c
         LEFT JOIN orders o ON o.client_id = c.id
WHERE c.is_permanent = true
GROUP BY c.id, c.first_name, c.last_name
ORDER BY lifetimeValue DESC
LIMIT 100;

-- Запрос 3: Поиск с функциональным индексом
EXPLAIN ANALYZE
SELECT id, first_name, last_name, phone
FROM clients
WHERE LOWER(last_name) LIKE LOWER('%ivanov%')
LIMIT 50;

-- Запрос 4: JOIN с индексами на FK
EXPLAIN ANALYZE
SELECT o.order_number, p.name, oi.quantity, oi.total_price
FROM orders o
         JOIN order_items oi ON o.id = oi.order_id
         JOIN products p ON oi.product_id = p.id
WHERE o.client_id = 123
LIMIT 100;

-- Запрос 5: Выборка конкретных полей + составной индекс
EXPLAIN ANALYZE
SELECT id, name, price, in_stock, is_available, type
FROM products
WHERE type = 'RING' AND is_available = true
LIMIT 100;

-- Запрос 6: Аудит с индексом на user_id + created_at
EXPLAIN ANALYZE
SELECT id, action, table_name, created_at
FROM audit_log
WHERE user_id = 456
ORDER BY created_at DESC
LIMIT 50;

-- Запрос 7: Простая сортировка (использует индекс)
EXPLAIN ANALYZE
SELECT id, last_name, created_at
FROM clients
ORDER BY last_name ASC
LIMIT 100;

-- Запрос 8: Статистика продаж с ограничением
EXPLAIN ANALYZE
SELECT p.id, p.name, COUNT(oi.id) as orderCount, SUM(oi.quantity) as totalSold
FROM products p
         LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY totalSold DESC
LIMIT 100;