-- Тест 1: Вставка заказов
EXPLAIN ANALYZE
INSERT INTO orders (client_id, status, total_amount, discount_amount, final_amount, notes)
SELECT c.id, 'PENDING', 1000.00, 0.00, 1000.00, 'Perf Test'
FROM generate_series(1, 1000) gs
         CROSS JOIN LATERAL (SELECT id FROM clients OFFSET floor(random()*5500) LIMIT 1) c;

-- Тест 2: Обновление статуса
EXPLAIN ANALYZE
UPDATE orders SET status = 'COMPLETED', completed_at = CURRENT_TIMESTAMP, updated_at = CURRENT_TIMESTAMP
WHERE id IN (SELECT id FROM orders WHERE status = 'PENDING' ORDER BY random() LIMIT 1000);

-- Тест 3: Обновление цен
EXPLAIN ANALYZE
UPDATE products SET price = price * 1.1, updated_at = CURRENT_TIMESTAMP
WHERE type = 'RING' AND is_available = true LIMIT 1000;