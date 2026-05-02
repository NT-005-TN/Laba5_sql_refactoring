class DynamicArray:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def _resize(self):
        """Увеличивает емкость массива в 2 раза"""
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        """Добавление элемента в конец списка"""
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """Вставка элемента по индексу"""
        if not (0 <= index <= self.size):
            raise IndexError("Индекс выходит за границы списка")
        if self.size == self.capacity:
            self._resize()
        
        # Сдвиг элементов вправо от конца до индекса вставки
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        """Удаление элемента по индексу"""
        if not (0 <= index < self.size):
            raise IndexError("Индекс выходит за границы списка")
        
        # Сдвиг элементов влево
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i+1]
        
        self.array[self.size - 1] = None # Очистка ссылки для GC
        self.size -= 1

    def get(self, index):
        """Получение элемента по индексу"""
        if not (0 <= index < self.size):
            raise IndexError("Индекс выходит за границы списка")
        return self.array[index]

    def get_size(self):
        """Получение текущего размера"""
        return self.size

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])