def insertion_sort(arr):
    """
    Сортировка вставками.
    """
    data = arr.copy()
    n = len(data)
    comparisons = 0
    shifts = 0 # Число сдвигов (перемещений элементов вправо)
    passes = 0

    for i in range(1, n):
        passes += 1
        key = data[i] # Элемент, который нужно вставить
        j = i - 1
        
        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and data[j] > key:
            comparisons += 1
            data[j + 1] = data[j] # Сдвиг
            shifts += 1
            j -= 1
        
        # Учитываем последнее сравнение, которое остановило цикл (если j >= 0)
        if j >= 0:
            comparisons += 1 
            
        data[j + 1] = key # Вставка элемента на освободившееся место
        
    return data, comparisons, shifts, passes