from Bubble_Sort import bubble_sort
from Insertion_Sort import insertion_sort
from Selection_Sort import selection_sort
from Quick_Sort_Lomuto import quick_sort_lomuto # Используем как пример неустойчивой
from collections import defaultdict

# Данные из методички
records1 = [("A1", 4), ("A2", 2), ("A3", 4), ("A4", 1), ("A5", 3), ("A6", 2), ("A7", 4), ("A8", 1), ("A9", 3), ("A10", 2)]
records2 = [("B1", 5), ("B2", 5), ("B3", 5), ("B4", 2), ("B5", 2), ("B6", 3), ("B7", 3), ("B8", 3), ("B9", 1), ("B10", 1)]
records3 = [("C1", 3), ("C2", 1), ("C3", 3), ("C4", 2), ("C5", 3), ("C6", 1), ("C7", 2), ("C8", 3), ("C9", 1), ("C10", 2), ("C11", 3), ("C12", 1)]

def check_stability(original, sorted_arr):
    """Проверяет, сохранился ли порядок элементов с одинаковыми ключами"""
    orig_order = defaultdict(list)
    for idx, (name, key) in enumerate(original):
        orig_order[key].append(name)
    
    sort_order = defaultdict(list)
    for name, key in sorted_arr:
        sort_order[key].append(name)
        
    for key in orig_order:
        if orig_order[key] != sort_order.get(key, []):
            return False
    return True

# --- Адаптеры для сортировки кортежей (id, key) по key ---

def bubble_sort_records(records):
    data = records.copy()
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if data[j][1] > data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped: break
    return data

def insertion_sort_records(records):
    data = records.copy()
    n = len(data)
    for i in range(1, n):
        key_item = data[i]
        j = i - 1
        while j >= 0 and data[j][1] > key_item[1]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key_item
    return data

def selection_sort_records(records):
    data = records.copy()
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j][1] < data[min_idx][1]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data

def quick_sort_records(records):
    """Неустойчивая быстрая сортировка для кортежей"""
    data = records.copy()
    
    def partition(low, high):
        pivot = data[high][1]
        i = low - 1
        for j in range(low, high):
            if data[j][1] <= pivot:
                i += 1
                if i != j:
                    data[i], data[j] = data[j], data[i]
        if i + 1 != high:
            data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def _qs(low, high):
        if low < high:
            pi = partition(low, high)
            _qs(low, pi - 1)
            _qs(pi + 1, high)
            
    _qs(0, len(data) - 1)
    return data

# --- Основная часть ---

algorithms = {
    "Bubble (Stable)": bubble_sort_records,
    "Insertion (Stable)": insertion_sort_records,
    "Selection (Unstable)": selection_sort_records,
    "Quick (Unstable)": quick_sort_records
}

for rec_name, records in [("records1", records1), ("records2", records2), ("records3", records3)]:
    print(f"\n=== Dataset: {rec_name} ===")
    print(f"Original: {records}")
    
    for algo_name, func in algorithms.items():
        sorted_rec = func(records)
        is_stable = check_stability(records, sorted_rec)
        print(f"{algo_name:25} | Stable? {is_stable} | Result: {sorted_rec}")

# --- Многокритериальная сортировка ---
print("\n\n=== Multi-criteria Sorting Experiment (records1) ===")
print("1. Sort by ID (Alphabetical)")
by_id = sorted(records1, key=lambda x: x[0])
print(f"   Sorted by ID: {by_id}")

print("\n2. Then Stable Sort by Key (Insertion)")
stable_result = insertion_sort_records(by_id)
print(f"   Result: {stable_result}")
print(f"   Is Order Preserved for Key=4? (A1, A3, A7 should be in order): {check_stability(by_id, stable_result)}")

print("\n3. Then Unstable Sort by Key (Selection)")
unstable_result = selection_sort_records(by_id)
print(f"   Result: {unstable_result}")
print(f"   Is Order Preserved for Key=4? (Likely No): {check_stability(by_id, unstable_result)}")