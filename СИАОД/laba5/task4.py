from Quick_Sort_Hoare import quick_sort_hoare
from Quick_Sort_Lomuto import quick_sort_lomuto

# Данные из методички
orders_random = [57, 14, 83, 29, 61, 45, 72, 10, 34, 98, 21, 66, 39, 50, 7, 66, 28, 64, 72, 62, 66, 26, 8, 29, 89, 35, 15, 32, 27, 55, 3, 59, 100, 21, 56, 85, 36, 23, 75, 18, 49, 18, 78, 44, 59, 59, 96, 68, 23, 81, 89, 4, 25, 90, 92, 72, 8, 82, 89, 44, 82, 55, 49, 23, 49, 80, 22, 84, 67, 21, 88, 65, 73, 99, 88, 49, 92, 39, 83, 66, 83, 26, 53, 75, 56, 94, 59, 89, 71, 37, 64, 99, 96, 73, 83, 30, 79, 78, 29, 7]
orders_many_duplicates = [5, 3, 5, 2, 5, 1, 5, 4, 5, 0, 5, 3, 5, 2, 5, 1, 9, 7, 0, 10, 4, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 3, 6, 10, 5, 1, 9, 4, 0, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8]

datasets = {"random": orders_random, "duplicates": orders_many_duplicates}
strategies = ['first', 'mid', 'random']
schemes = {
    'Hoare': quick_sort_hoare, 
    'Lomuto': quick_sort_lomuto
}

for name, data in datasets.items():
    print(f"\n{'='*20} Dataset: {name} {'='*20}")
    
    for scheme_name, sort_func in schemes.items():
        print(f"\n--- Scheme: {scheme_name} ---")
        for strategy in strategies:
            # Запуск сортировки
            sorted_arr, stats = sort_func(data, pivot_strategy=strategy)
            
            print(f"\nStrategy: {strategy.upper()}")
            print(f"Comparisons: {stats['comparisons']}")
            print(f"Swaps:       {stats['swaps']}")
            print(f"Calls:       {stats['calls']}")
            print(f"Max Depth:   {stats['max_depth']}")
            
            # Вывод первых 3 шагов
            print("First 3 Recursion Steps:")
            for step in stats['steps_log']:
                print(f"  Step {step['step_num']}: Bounds {step['bounds']}, Pivot Value: {step['pivot_val']}")
                print(f"    Before: {step['array_before']}")
                print(f"    After:  {step['array_after']}")
                if 'return_j' in step:
                    print(f"    Return Index (j/pi): {step['return_j']}")
                elif 'return_pi' in step:
                    print(f"    Return Index (pi): {step['return_pi']}")