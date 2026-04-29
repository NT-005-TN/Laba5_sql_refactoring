from Coctail_Shaker_Sort import cocktail_shaker_sort
from Gnome_Sort import gnome_sort
from Bubble_Sort import bubble_sort

data1 = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
data2 = [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]
data3 = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]
data4 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

datasets = {"data1": data1, "data2": data2, "data3": data3, "data4": data4}

for name, data in datasets.items():
    print(f"\n=== Dataset: {name} ===")

    res_cocktail = cocktail_shaker_sort(data)
    print(f"Cocktail Shaker | Comp: {res_cocktail[1]}, Swaps: {res_cocktail[2]}, Passes: {res_cocktail[3]}")

    res_gnome = gnome_sort(data)
    print(f"Gnome Sort | Comp: {res_gnome[1]}, Swaps: {res_gnome[2]}, Steps: {res_gnome[3]}")

    res_bubble = bubble_sort(data)
    print(f"Bubble Sort (ref) | Comp: {res_bubble[1]}, Swaps: {res_bubble[2]}, Passes: {res_bubble[3]}")