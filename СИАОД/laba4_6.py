import time
import random

def linear_search_sentinel(arr, target):
    n = len(arr)
    arr.append(target)
    i = 0
    while arr[i] != target: i += 1
    arr.pop()
    return i if i < n else -1

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return True
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return False

def interpolation_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r and target >= arr[l] and target <= arr[r]:
        if l == r: return arr[l] == target
        if arr[r] == arr[l]: break
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (target - arr[l]))
        if arr[pos] == target: return True
        elif arr[pos] < target: l = pos + 1
        else: r = pos - 1
    return False

def _bs_range(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return True
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return False

def exponential_search(arr, target):
    if not arr: return False
    if arr[0] == target: return True
    i = 1
    while i < len(arr) and arr[i] <= target: i *= 2
    return _bs_range(arr, i//2, min(i, len(arr)-1), target)

if __name__ == "__main__":
    print("="*90)
    print("ЗАДАНИЕ 6: Зависимость от размера N (среднее время 1 поиска, мс)")
    print("="*90)
    sizes = [10**3, 10**4, 10**5] # 10^6 можно добавить, но линейный поиск займёт ~15-20 сек
    reps = 100

    print(f"{'N':<7} | {'Линейный (мс)':<14} | {'Бинарный (мс)':<14} | {'Интерпол (мс)':<14} | {'Эксп (мс)':<10}")
    print("-" * 90)
    
    for N in sizes:
        arr = sorted([random.randint(0, 10*N) for _ in range(N)])
        target = random.choice(arr)
        
        t_start = time.perf_counter()
        for _ in range(reps): linear_search_sentinel(arr.copy(), target)
        t_lin = (time.perf_counter() - t_start) / reps * 1000
        
        t_start = time.perf_counter()
        for _ in range(reps): binary_search(arr, target)
        t_bin = (time.perf_counter() - t_start) / reps * 1000
        
        t_start = time.perf_counter()
        for _ in range(reps): interpolation_search(arr, target)
        t_int = (time.perf_counter() - t_start) / reps * 1000
        
        t_start = time.perf_counter()
        for _ in range(reps): exponential_search(arr, target)
        t_exp = (time.perf_counter() - t_start) / reps * 1000
        
        print(f"{N:<7} | {t_lin:<14.4f} | {t_bin:<14.4f} | {t_int:<14.4f} | {t_exp:<10.4f}")