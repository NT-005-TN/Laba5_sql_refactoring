def cocktail_shaker_sort(arr):
    """
    Шейкерная сортировка (перемешиванием).
    """
    data = arr.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    passes = 0
    
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False
        passes += 1
        
        # Проход слева направо (как пузырьковая)
        for i in range(left, right):
            comparisons += 1
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swaps += 1
                swapped = True
        
        # Если обменов не было, выходим
        if not swapped:
            break
            
        # Уменьшаем правую границу, так как последний элемент встал на место
        right -= 1
        swapped = False
        
        # Проход справа налево
        for i in range(right, left, -1):
            comparisons += 1
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
                swaps += 1
                swapped = True
        
        # Увеличиваем левую границу, так как первый элемент встал на место
        left += 1
        
    return data, comparisons, swaps, passes