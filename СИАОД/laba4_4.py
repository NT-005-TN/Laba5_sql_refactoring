import random

def linear_search_stats(arr, target):
    comps = iters = shifts = 0
    n = len(arr)
    arr.append(target)
    i = 0
    while True:
        iters += 1
        comps += 1
        if arr[i] == target: break
        i += 1
    arr.pop()
    return (i if i < n else -1), comps, iters, i

def binary_search_stats(arr, target):
    comps = iters = shifts = 0
    l, r = 0, len(arr) - 1
    while l <= r:
        iters += 1
        shifts += 1
        mid = (l + r) // 2
        comps += 1
        if arr[mid] == target: return mid, comps, iters, shifts
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
        comps += 1
        shifts += 1
    return -1, comps, iters, shifts

def interpolation_search_stats(arr, target):
    comps = iters = shifts = 0
    l, r = 0, len(arr) - 1
    while l <= r and target >= arr[l] and target <= arr[r]:
        iters += 1
        shifts += 1
        if l == r:
            comps += 1
            return (l if arr[l] == target else -1), comps, iters, shifts
        if arr[r] == arr[l]: break
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (target - arr[l]))
        comps += 1
        if arr[pos] == target: return pos, comps, iters, shifts
        elif arr[pos] < target: l = pos + 1
        else: r = pos - 1
        shifts += 1
    return -1, comps, iters, shifts

def _bs_range_stats(arr, l, r, target, iters, shifts):
    comps = 0
    while l <= r:
        iters += 1
        shifts += 1
        mid = (l + r) // 2
        comps += 1
        if arr[mid] == target: return mid, comps, iters, shifts
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1, comps, iters, shifts

def exponential_search_stats(arr, target):
    comps = iters = shifts = 0
    if not arr: return -1, comps, iters, shifts
    if arr[0] == target: return 0, comps+1, iters+1, shifts+1
    i = 1
    iters += 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
        iters += 1
        shifts += 1
    return _bs_range_stats(arr, i//2, min(i, len(arr)-1), target, iters, shifts)

if __name__ == "__main__":
    print("="*80)
    print("ЗАДАНИЕ 4: Внутренние метрики (N=10 000, успешный поиск)")
    print("="*80)
    arr = sorted([random.randint(0, 100000) for _ in range(10000)])
    target = arr[5000]
    
    print(f"{'Алгоритм':<20} | {'Индекс':<6} | {'Сравнения':<10} | {'Итерации':<9} | {'Сдвиги':<7}")
    print("-" * 80)
    
    algos = [
        ("Линейный (барьер)", linear_search_stats),
        ("Бинарный", binary_search_stats),
        ("Интерполяционный", interpolation_search_stats),
        ("Экспоненциальный", exponential_search_stats)
    ]
    
    for name, func in algos:
        idx, c, it, sh = func(arr.copy(), target)
        print(f"{name:<20} | {idx:<6} | {c:<10} | {it:<9} | {sh:<7}")