from singly_linked_list import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        """Добавление элемента в вершину стека"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Получение элемента с удалением"""
        if not self.top:
            raise IndexError("Стек пуст")
        val = self.top.data
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self):
        """Получение элемента без удаления"""
        if not self.top:
            raise IndexError("Стек пуст")
        return self.top.data

    def size(self):
        """Получение количества элементов"""
        return self._size