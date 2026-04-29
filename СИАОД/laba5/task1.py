from Bubble_Sort import bubble_sort
from Selection_Sort import selection_sort
from Insertion_Sort import insertion_sort

data_random = [57, 12, 89, 34, 76, 11, 90, 43, 65, 28, 71, 5, 39, 84, 22]
data_sorted = [5, 11, 12, 22, 28, 34, 39, 43, 57, 65, 71, 76, 84, 89, 90]
data_reverse = [90, 89, 84, 76, 71, 65, 57, 43, 39, 34, 28, 22, 12, 11, 5]
data_almost_sorted = [5, 11, 12, 22, 28, 34, 43, 39, 57, 65, 71, 76, 84, 89, 90]

datasets = {
    "random": data_random,
    "sorted": data_sorted,
    "reverse": data_reverse,
    "almost_sorted": data_almost_sorted
}

for name, data in datasets.items():
    print(f"\n=== Dataset: {name} ===")

    res_bubble = bubble_sort(data)
    print(f"Bubble Sort | Comp: {res_bubble[1]}, Swaps: {res_bubble[2]}, Passes: {res_bubble[3]}")

    res_selection = selection_sort(data)
    print(f"Selection Sort | Comp: {res_selection[1]}, Swaps: {res_selection[2]}, Passes: {res_selection[3]}")

    res_insertion = insertion_sort(data)
    print(f"Insertion Sort | Comp: {res_insertion[1]}, Shifts: {res_insertion[2]}, Passes: {res_insertion[3]}")