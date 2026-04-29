def bubble_sort(arr):
    """
    Сортировка пузырьком.
    Возвращает отсортированный массив и статистику.
    """
    # Создаем копию, чтобы не менять исходный массив
    data = arr.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n - 1):
        passes += 1
        swapped_flag = False # Флаг оптимизации: если обменов не было, массив уже отсортирован
        
        # Последний i элементов уже отсортированы, поэтому идем до n - 1 - i
        for j in range(0, n - 1 - i):
            comparisons += 1
            if data[j] > data[j + 1]:
                # Обмен элементов
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                swapped_flag = True
        
        # Если за весь проход не было обменов, выходим досрочно
        if not swapped_flag:
            break
            
    return data, comparisons, swaps, passes