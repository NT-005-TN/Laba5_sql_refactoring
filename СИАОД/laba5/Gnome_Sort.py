def gnome_sort(arr):
    """
    Гномья сортировка.
    """
    data = arr.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    steps = 0 # Число шагов гнома
    
    index = 0
    while index < n:
        steps += 1
        if index == 0:
            index += 1
        else:
            comparisons += 1
            if data[index] >= data[index - 1]:
                # Порядок верный, идем вперед
                index += 1
            else:
                # Порядок неверный, меняем и идем назад
                data[index], data[index - 1] = data[index - 1], data[index]
                swaps += 1
                index -= 1
                
    return data, comparisons, swaps, steps