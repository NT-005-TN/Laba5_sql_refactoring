import time
import random
import numpy as np

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return True
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return False

if __name__ == "__main__":
    print("="*70)
    print("ЗАДАНИЕ 5: Сравнение со встроенными средствами (N=50 000, 10 000 запросов)")
    print("="*70)
    N = 50_000
    arr = sorted([random.randint(0, 100000) for _ in range(N)])
    target = arr[N//2]
    queries = [target] * 10000

    # 1. Собственная реализация
    t = time.perf_counter()
    for q in queries: binary_search(arr, q)
    t_custom = time.perf_counter() - t

    # 2. Python in
    t = time.perf_counter()
    for q in queries: _ = q in arr
    t_in = time.perf_counter() - t

    # 3. Python index()
    t = time.perf_counter()
    for q in queries:
        try: arr.index(q)
        except: pass
    t_index = time.perf_counter() - t

    # 4. NumPy
    arr_np = np.array(arr)
    t = time.perf_counter()
    for q in queries: np.searchsorted(arr_np, q)
    t_np = time.perf_counter() - t

    print(f"{'Метод':<25} | {'Время (с)':<10}")
    print("-" * 40)
    print(f"{'Собственный бинарный':<25} | {t_custom:<10.6f}")
    print(f"{'Python оператор in':<25} | {t_in:<10.6f}")
    print(f"{'Python .index()':<25} | {t_index:<10.6f}")
    print(f"{'NumPy searchsorted':<25} | {t_np:<10.6f}")