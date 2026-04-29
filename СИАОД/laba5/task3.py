
from Merge_Sort_Recursive import merge_sort_recursive
from Merge_Sort_Iterate import merge_sort_iterative

cargo_priority = [42, 17, 93, 58, 11, 76, 24, 65, 39, 88, 5, 71, 30, 54, 19, 93, 7, 80, 80, 48, 77, 98, 97, 56, 27, 94, 73, 74, 72, 47, 95, 70, 96, 93, 84, 53, 38, 90, 94, 85, 34, 88, 56, 29, 65, 84, 72, 60, 63, 59, 61, 61, 14, 42, 89, 97, 62, 27, 19, 36, 18, 89, 3, 64, 99, 38, 26, 99, 55, 40, 32, 99, 86, 44, 1, 100, 53, 74, 78, 68, 21, 24, 85, 32, 99, 68, 85, 12, 4, 18, 69, 46, 46, 50, 64, 7, 68, 27, 98, 77, 41, 76, 12, 12, 62, 75, 29, 52, 12, 91, 73, 14, 22, 47, 47, 16, 25, 64, 54, 66, 89, 20, 68, 82, 4, 7, 58, 42, 13, 3, 60, 10, 52, 25, 98, 64, 86, 48, 44, 38, 2, 33, 14, 28, 29, 40, 23, 83, 47, 35]

print("=== Cargo Priority Sorting ===")

res_recursive = merge_sort_recursive(cargo_priority)
print(f"Merge Sort Recursive | Comp: {res_recursive[1]}, Max Depth: {res_recursive[2]}")

res_iterative = merge_sort_iterative(cargo_priority)
print(f"Merge Sort Iterative | Comp: {res_iterative[1]}, Passes: {res_iterative[2]}")