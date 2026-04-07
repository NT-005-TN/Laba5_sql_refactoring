import time
import random

def linear_search_sentinel(arr, target):
    n = len(arr)
    arr.append(target)
    i = 0
    while arr[i] != target:
        i += 1
    arr.pop()
    return i if i < n else -1

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1

if __name__ == "__main__":
    print("="*70)
    print("ЗАДАНИЕ 3: Поиск порога K (N=100 000)")
    print("="*70)
    N = 100_000
    arr_unsorted = [random.randint(0, 2*N) for _ in range(N)]
    queries = [random.randint(0, 2*N) for _ in range(5000)]
    ks = [10, 50, 100, 200, 500, 1000]

    print(f"{'K':<5} | {'Линейный (с)':<13} | {'Сорт+Бин (с)':<14} | {'Выгоднее':<15}")
    print("-" * 70)
    for k in ks:
        # Линейный
        t_start = time.perf_counter()
        for q in queries[:k]: linear_search_sentinel(arr_unsorted.copy(), q)
        t_lin = time.perf_counter() - t_start

        # Сортировка + Бинарный
        t_start = time.perf_counter()
        arr_sorted = sorted(arr_unsorted)
        for q in queries[:k]: binary_search(arr_sorted, q)
        t_sb = time.perf_counter() - t_start

        winner = "Линейный" if t_lin < t_sb else "Сорт + Бин"
        print(f"{k:<5} | {t_lin:<13.6f} | {t_sb:<14.6f} | {winner:<15}")