-- ============================================
-- ПРОБЛЕМНЫЕ ЗАПРОСЫ (ДО ОПТИМИЗАЦИИ)
-- Для анализа с EXPLAIN ANALYZE
-- ============================================

-- Запрос 1: Поиск заказов по клиенту (без индекса)
EXPLAIN ANALYZE
SELECT id, order_number, status, final_amount, order_datetime
FROM orders
WHERE client_id = 123;

-- Запрос 2: Коррелированные подзапросы (проблема N+1)
EXPLAIN ANALYZE
SELECT
    c.id, c.first_name, c.last_name,
    (SELECT COUNT(o.id) FROM orders o WHERE o.client_id = c.id AND o.status = 'COMPLETED') as completedOrders,
    COALESCE((SELECT SUM(o.final_amount) FROM orders o WHERE o.client_id = c.id), 0) as lifetimeValue,
    (SELECT MAX(o.order_datetime) FROM orders o WHERE o.client_id = c.id) as lastPurchaseDate
FROM clients c
WHERE c.is_permanent = true
ORDER BY lifetimeValue DESC
LIMIT 100;

-- Запрос 3: Поиск с FUNCTION в WHERE (блокирует индекс)
EXPLAIN ANALYZE
SELECT id, first_name, last_name, phone
FROM clients
WHERE LOWER(last_name) LIKE LOWER('%ivanov%')
LIMIT 50;

-- Запрос 4: JOIN без индексов на FK
EXPLAIN ANALYZE
SELECT o.order_number, p.name, oi.quantity, oi.total_price
FROM orders o
         JOIN order_items oi ON o.id = oi.order_id
         JOIN products p ON oi.product_id = p.id
WHERE o.client_id = 123
LIMIT 100;

-- Запрос 5: SELECT * вместо конкретных полей
EXPLAIN ANALYZE
SELECT id, name, price, in_stock, is_available, type
FROM products
WHERE type = 'RING' AND is_available = true
LIMIT 100;

-- Запрос 6: Аудит по пользователю (без индекса)
EXPLAIN ANALYZE
SELECT id, action, table_name, created_at
FROM audit_log
WHERE user_id = 456
ORDER BY created_at DESC
LIMIT 50;

-- Запрос 7: Сортировка с CASE (не использует индексы)
EXPLAIN ANALYZE
SELECT id, last_name, created_at
FROM clients
ORDER BY
    CASE WHEN 'name' = 'name' THEN last_name END ASC,
    CASE WHEN 'name' = 'created' THEN created_at END DESC
LIMIT 100;

-- Запрос 8: Статистика продаж товаров
EXPLAIN ANALYZE
SELECT p.id, p.name, COUNT(oi.id) as orderCount, SUM(oi.quantity) as totalSold
FROM products p
         LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
ORDER BY totalSold DESC
LIMIT 100;