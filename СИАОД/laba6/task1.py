from dynamic_array import DynamicArray

def main():
    print("--- Задание 1: Динамический массив ---")
    arr = DynamicArray()
    
    # Добавить значения
    values = [5, 0, 1, 7, 9, 4, 6, 2, 1]
    for v in values:
        arr.append(v)
    
    # Вставить 8 по индексу 7
    arr.insert(7, 8)
    
    # Удалить элемент по индексу 5
    arr.delete(5)
    
    # Вывод результатов
    print(f"Итоговое содержимое: {arr}")
    print(f"Размер списка: {arr.get_size()}")

if __name__ == "__main__":
    main()