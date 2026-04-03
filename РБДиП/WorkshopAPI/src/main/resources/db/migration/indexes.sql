-- ============================================
-- СОЗДАНИЕ ИНДЕКСОВ ДЛЯ ОПТИМИЗАЦИИ
-- ============================================

-- Индексы на Foreign Keys (обязательные)
CREATE INDEX IF NOT EXISTS idx_clients_user_id ON clients(user_id);
CREATE INDEX IF NOT EXISTS idx_orders_client_id ON orders(client_id);
CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON order_items(order_id);
CREATE INDEX IF NOT EXISTS idx_order_items_product_id ON order_items(product_id);
CREATE INDEX IF NOT EXISTS idx_product_materials_product_id ON product_materials(product_id);
CREATE INDEX IF NOT EXISTS idx_product_materials_material_id ON product_materials(material_id);
CREATE INDEX IF NOT EXISTS idx_audit_log_user_id ON audit_log(user_id);
CREATE INDEX IF NOT EXISTS idx_employees_user_id ON employees(user_id);

-- Индексы для фильтрации и сортировки
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);
CREATE INDEX IF NOT EXISTS idx_orders_datetime ON orders(order_datetime);
CREATE INDEX IF NOT EXISTS idx_orders_status_datetime ON orders(status, order_datetime);
CREATE INDEX IF NOT EXISTS idx_order_items_created_at ON order_items(created_at);
CREATE INDEX IF NOT EXISTS idx_audit_log_table_name ON audit_log(table_name);
CREATE INDEX IF NOT EXISTS idx_audit_log_created_at ON audit_log(created_at);
CREATE INDEX IF NOT EXISTS idx_products_type ON products(type);
CREATE INDEX IF NOT EXISTS idx_products_in_stock ON products(in_stock);
CREATE INDEX IF NOT EXISTS idx_products_is_available ON products(is_available);
CREATE INDEX IF NOT EXISTS idx_products_type_available ON products(type, is_available);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
CREATE INDEX IF NOT EXISTS idx_users_enabled ON users(enabled);
CREATE INDEX IF NOT EXISTS idx_users_role_enabled ON users(role, enabled);

-- Функциональные индексы (для case-insensitive поиска)
CREATE INDEX IF NOT EXISTS idx_clients_lastname_lower ON clients(LOWER(last_name));
CREATE INDEX IF NOT EXISTS idx_clients_firstname_lower ON clients(LOWER(first_name));
CREATE INDEX IF NOT EXISTS idx_products_name_lower ON products(LOWER(name));

-- Обновление статистики после создания индексов
ANALYZE clients;
ANALYZE orders;
ANALYZE order_items;
ANALYZE products;
ANALYZE users;
ANALYZE audit_log;