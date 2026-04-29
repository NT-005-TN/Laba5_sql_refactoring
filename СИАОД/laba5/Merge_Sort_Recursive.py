def merge_sort_recursive(arr):
    """
    Рекурсивная сортировка слиянием.
    """
    comparisons = [0] # Используем список для изменения внутри вложенных функций
    max_depth = [0]

    def _merge_sort(data, depth=0):
        if len(data) <= 1:
            return data
        
        # Обновляем максимальную глубину рекурсии
        if depth > max_depth[0]:
            max_depth[0] = depth

        mid = len(data) // 2
        left_half = _merge_sort(data[:mid], depth + 1)
        right_half = _merge_sort(data[mid:], depth + 1)
        
        return _merge(left_half, right_half)

    def _merge(left, right):
        sorted_arr = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        # Добавляем оставшиеся элементы
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    sorted_data = _merge_sort(arr.copy())
    return sorted_data, comparisons[0], max_depth[0]