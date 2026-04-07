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

def interpolation_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r and target >= arr[l] and target <= arr[r]:
        if l == r: return l if arr[l] == target else -1
        if arr[r] == arr[l]: break
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (target - arr[l]))
        if arr[pos] == target: return pos
        elif arr[pos] < target: l = pos + 1
        else: r = pos - 1
    return -1

def _bs_range(arr, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1

def exponential_search(arr, target):
    if not arr: return -1
    if arr[0] == target: return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return _bs_range(arr, i//2, min(i, len(arr)-1), target)

if __name__ == "__main__":
    print("="*60)
    print("ЗАДАНИЕ 1: Тестирование алгоритмов поиска")
    print("="*60)
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    arr_sorted = sorted(arr)
    targets = [8, 99] # 8 - есть, 99 - нет
    
    print(f"Исходный массив: {arr}")
    print(f"Отсортированный: {arr_sorted}\n")
    
    for t in targets:
        print(f" Ищем элемент: {t}")
        print(f"  Линейный (барьер)  : {linear_search_sentinel(arr.copy(), t)}")
        print(f"  Бинарный           : {binary_search(arr_sorted, t)}")
        print(f"  Интерполяционный   : {interpolation_search(arr_sorted, t)}")
        print(f"  Экспоненциальный   : {exponential_search(arr_sorted, t)}")
        print("-" * 30)