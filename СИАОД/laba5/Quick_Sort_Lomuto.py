import random

def quick_sort_lomuto(arr, pivot_strategy='last'):
    """
    Быстрая сортировка со схемой разбиения Ломуто.
    :param arr: исходный массив
    :param pivot_strategy: 'first', 'mid', 'random' 
                           (в классике Ломуто опора в конце, но мы будем менять её туда)
    :return: (sorted_arr, stats_dict)
    """
    data = arr.copy()
    stats = {
        'comparisons': 0,
        'swaps': 0,
        'calls': 0,
        'max_depth': 0,
        'steps_log': []
    }

    def get_pivot_index(low, high):
        if pivot_strategy == 'first':
            return low
        elif pivot_strategy == 'mid':
            return (low + high) // 2
        elif pivot_strategy == 'random':
            return random.randint(low, high)
        return high # default last

    def partition(low, high):
        # 1. Выбираем опору и меняем её с ПОСЛЕДНИМ элементом (стандарт Ломуто)
        pivot_idx = get_pivot_index(low, high)
        if pivot_idx != high:
            data[pivot_idx], data[high] = data[high], data[pivot_idx]
            stats['swaps'] += 1
            
        pivot_val = data[high]
        i = low - 1 
        
        for j in range(low, high):
            stats['comparisons'] += 1
            if data[j] <= pivot_val:
                i += 1
                if i != j:
                    data[i], data[j] = data[j], data[i]
                    stats['swaps'] += 1
        
        # Ставим опору на место
        if i + 1 != high:
            data[i + 1], data[high] = data[high], data[i + 1]
            stats['swaps'] += 1
            
        return i + 1

    def _quick_sort(low, high, depth=0):
        if low < high:
            stats['calls'] += 1
            if depth > stats['max_depth']:
                stats['max_depth'] = depth
            
            # Логирование
            if len(stats['steps_log']) < 3:
                # Для Лоумто опора в конце перед разбиением
                pivot_idx = get_pivot_index(low, high)
                pivot_val = data[pivot_idx]
                
                step_info = {
                    'step_num': len(stats['steps_log']) + 1,
                    'bounds': (low, high),
                    'pivot_val': pivot_val,
                    'array_before': data[low:high+1].copy()
                }
                stats['steps_log'].append(step_info)

            pi = partition(low, high)
            
            # Завершаем лог
            if len(stats['steps_log']) <= 3 and stats['steps_log'][-1]['bounds'] == (low, high):
                stats['steps_log'][-1]['array_after'] = data[low:high+1].copy()
                stats['steps_log'][-1]['return_pi'] = pi

            _quick_sort(low, pi - 1, depth + 1)
            _quick_sort(pi + 1, high, depth + 1)

    _quick_sort(0, len(data) - 1)
    return data, stats