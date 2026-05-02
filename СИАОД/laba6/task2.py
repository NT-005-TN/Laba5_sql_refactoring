from singly_linked_list import SinglyLinkedList

def main():
    print("--- Задание 2: Односвязный список ---")
    lst = SinglyLinkedList()
    
    # Добавить 5, 3, 5, 20
    for v in [5, 3, 5, 20]:
        lst.add_back(v)
        
    # Добавить 7 в конец
    lst.add_back(7)
    
    # Удалить первый элемент
    lst.remove_front()
    
    # Удалить последний элемент
    lst.remove_back()
    
    # Вывод итоговой последовательности
    print(f"Итоговая последовательность: {lst}")

if __name__ == "__main__":
    main()