def merge_sort_iterative(arr):
    """
    Итерационная сортировка слиянием.
    """
    data = arr.copy()
    n = len(data)
    comparisons = 0
    passes = 0 # Количество проходов (увеличение ширины)
    
    # width - размер текущего объединяемого блока
    width = 1 
    while width < n:
        passes += 1
        for i in range(0, n, 2 * width):
            # Определяем границы левого и правого подмассивов
            left = data[i : i + width]
            right = data[i + width : i + 2 * width]
            
            # Сливаем их
            merged = []
            l_idx, r_idx = 0, 0
            
            while l_idx < len(left) and r_idx < len(right):
                comparisons += 1
                if left[l_idx] <= right[r_idx]:
                    merged.append(left[l_idx])
                    l_idx += 1
                else:
                    merged.append(right[r_idx])
                    r_idx += 1
            
            merged.extend(left[l_idx:])
            merged.extend(right[r_idx:])
            
            # Записываем слитый блок обратно в основной массив
            data[i : i + len(merged)] = merged
            
        width *= 2 # Удваиваем размер блока
        
    return data, comparisons, passes