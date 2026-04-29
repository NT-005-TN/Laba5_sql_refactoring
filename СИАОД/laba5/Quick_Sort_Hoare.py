import random

def quick_sort_hoare(arr, pivot_strategy='first'):
    """
    Быстрая сортировка со схемой разбиения Хоара.
    :param arr: исходный массив
    :param pivot_strategy: 'first', 'mid', 'random'
    :return: (sorted_arr, stats_dict)
    """
    data = arr.copy()
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'calls': 0,
        'max_depth': 0,
        'steps_log': [] # Лог первых 3 шагов
    }

    def get_pivot_index(low, high):
        if pivot_strategy == 'first':
            return low
        elif pivot_strategy == 'mid':
            return (low + high) // 2
        elif pivot_strategy == 'random':
            return random.randint(low, high)
        return low

    def partition(low, high):
        # 1. Выбираем индекс опоры и меняем его с первым элементом (для стандартизации логики Хоара)
        pivot_idx = get_pivot_index(low, high)
        if pivot_idx != low:
            data[low], data[pivot_idx] = data[pivot_idx], data[low]
            stats['swaps'] += 1
            
        pivot_val = data[low]
        i = low - 1
        j = high + 1
        
        while True:
            # Двигаем i вправо
            while True:
                i += 1
                stats['comparisons'] += 1
                if data[i] >= pivot_val:
                    break
            
            # Двигаем j влево
            while True:
                j -= 1
                stats['comparisons'] += 1
                if data[j] <= pivot_val:
                    break
            
            if i >= j:
                return j
            
            # Обмен
            if i != j:
                data[i], data[j] = data[j], data[i]
                stats['swaps'] += 1

    def _quick_sort(low, high, depth=0):
        if low < high:
            stats['calls'] += 1
            if depth > stats['max_depth']:
                stats['max_depth'] = depth
            
            # Логирование первых 3 шагов
            if len(stats['steps_log']) < 3:
                step_info = {
                    'step_num': len(stats['steps_log']) + 1,
                    'bounds': (low, high),
                    'pivot_val': data[low], # Опора уже в начале
                    'array_before': data[low:high+1].copy()
                }
                stats['steps_log'].append(step_info)

            p = partition(low, high)
            
            # Завершаем логирование шага (результат после разбиения)
            if len(stats['steps_log']) <= 3 and stats['steps_log'][-1]['bounds'] == (low, high):
                stats['steps_log'][-1]['array_after'] = data[low:high+1].copy()
                stats['steps_log'][-1]['return_j'] = p

            # Рекурсивные вызовы по схеме Хоара: (low, p) и (p+1, high)
            _quick_sort(low, p, depth + 1)
            _quick_sort(p + 1, high, depth + 1)

    _quick_sort(0, len(data) - 1)
    return data, stats