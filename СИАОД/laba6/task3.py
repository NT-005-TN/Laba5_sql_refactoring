from stack import Stack

def main():
    print("--- Задание 3: Стек ---")
    stack = Stack()
    
    # Поместить значения 5, 0, 1, 7, 9
    for v in [5, 0, 1, 7, 9]:
        stack.push(v)
        
    # Вывести верхний элемент без удаления
    print(f"Верхний элемент (peek): {stack.peek()}")
    
    # Удалить два элемента
    stack.pop()
    stack.pop()
    
    # Снова вывести верхний элемент
    print(f"Верхний элемент после 2 pop: {stack.peek()}")
    
    # Определить итоговый размер
    print(f"Итоговый размер стека: {stack.size()}")

if __name__ == "__main__":
    main()