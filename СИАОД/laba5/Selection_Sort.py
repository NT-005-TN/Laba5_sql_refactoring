def selection_sort(arr):
    """
    Сортировка выбором.
    """
    data = arr.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n - 1):
        passes += 1
        min_index = i # Предполагаем, что минимум находится на позиции i
        
        # Поиск индекса минимального элемента в остатке массива
        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_index]:
                min_index = j
        
        # Если минимум не на своем месте, меняем местами
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            swaps += 1
            
    return data, comparisons, swaps, passes