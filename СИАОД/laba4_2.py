import time
import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    print("="*70)
    print("ЗАДАНИЕ 2: Сравнение на разных распределениях (N=100 000, 1000 запросов)")
    print("="*70)
    N = 100_000
    queries = np.random.randint(0, 10*N, 1000)

    dists = {
        "Равномерное": sorted(np.random.randint(0, 100*N, N)),
        "Квадратичное": sorted([(i**2) % (10*N) for i in range(N)]),
        "Экспоненциальное": sorted([int(1.001**i) for i in range(N)]),
        "Скошенное (skew)": sorted(np.random.randint(0, 1000, N//2).tolist() + np.random.randint(50000, 100000, N//2).tolist())
    }

    results = {}
    print(f"{'Распределение':<20} | {'Интерпол (с)':<13} | {'Бинарный (с)':<13} | {'Отношение':<10}")
    print("-" * 70)
    for name, arr in dists.items():
        t1 = time.perf_counter()
        for q in queries: interpolation_search(arr, q)
        t_int = time.perf_counter() - t1

        t2 = time.perf_counter()
        for q in queries: binary_search(arr, q)
        t_bin = time.perf_counter() - t2
        
        ratio = t_int / t_bin if t_bin > 0 else float('inf')
        results[name] = (t_int, t_bin, ratio)
        print(f"{name:<20} | {t_int:<13.6f} | {t_bin:<13.6f} | {ratio:<10.2f}x")

    # ==================== ПОСТРОЕНИЕ ГРАФИКА ====================
    plt.figure(figsize=(10, 6))
    x = np.arange(len(results))
    width = 0.35
    
    bars1 = plt.bar(x - width/2, [v[0]*1000 for v in results.values()], width, 
                   label='Интерполяционный', color='#4CAF50', edgecolor='black')
    bars2 = plt.bar(x + width/2, [v[1]*1000 for v in results.values()], width, 
                   label='Бинарный', color='#2196F3', edgecolor='black')
    
    plt.xlabel('Распределение данных', fontsize=11)
    plt.ylabel('Время выполнения (мс)', fontsize=11)
    plt.title('Рис. 2.1. Сравнение интерполяционного и бинарного поиска\nна массивах с различным распределением (N=100 000)', fontsize=12, fontweight='bold')
    plt.xticks(x, list(results.keys()), rotation=15, ha='right')
    plt.legend(fontsize=10)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Подписи значений на столбцах
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 0.1:  # не подписывать очень маленькие значения
                plt.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}', 
                        ha='center', va='bottom', fontsize=8)
    
    plt.savefig('fig_2_1_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("📊 График сохранён: fig_2_1_distribution.png")