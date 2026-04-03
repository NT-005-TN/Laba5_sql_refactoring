-- Размер таблиц
SELECT tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as total_size
FROM pg_tables WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Размер индексов
SELECT relname as tablename, indexrelname as indexname,
       pg_size_pretty(pg_relation_size(indexrelid)) as index_size
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;

-- Использование индексов
SELECT schemaname, relname as tablename, indexrelname as indexname,
       idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes WHERE idx_scan > 0
ORDER BY idx_scan DESC;

-- Неиспользуемые индексы
SELECT schemaname, relname as tablename, indexrelname as indexname
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND indexrelname NOT LIKE '%_pkey'
ORDER BY relname, indexrelname;

-- Статистика таблиц
SELECT relname as table_name, n_live_tup as row_count, n_dead_tup as dead_rows,
       last_vacuum, last_analyze
FROM pg_stat_user_tables ORDER BY n_live_tup DESC;