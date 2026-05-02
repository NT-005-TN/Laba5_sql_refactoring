class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add_front(self, value):
        """Добавление значения в начало списка"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_back(self, value):
        """Добавление значения в конец списка"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def remove_front(self):
        """Удаление первого элемента"""
        if not self.head:
            raise IndexError("Список пуст")
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def remove_back(self):
        """Удаление последнего элемента (без tail)"""
        if not self.head:
            raise IndexError("Список пуст")
        
        # Если элемент один
        if not self.head.next:
            val = self.head.data
            self.head = None
            self._size -= 1
            return val
        
        # Поиск предпоследнего элемента
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        val = curr.next.data
        curr.next = None
        self._size -= 1
        return val

    def get(self, index):
        """Получение значения по индексу"""
        if not (0 <= index < self._size):
            raise IndexError("Индекс выходит за границы списка")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def size(self):
        """Получение размера списка"""
        return self._size

    def __str__(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return str(res)