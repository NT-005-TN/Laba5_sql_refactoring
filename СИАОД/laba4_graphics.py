#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Лабораторная работа №4: Алгоритмы поиска
Построение графиков для Задания 3 и Задания 6
"""

import time
import random
import matplotlib.pyplot as plt
import numpy as np

# ==================== АЛГОРИТМЫ ПОИСКА ====================

def linear_search_sentinel(arr, target):
    """Линейный поиск с барьерным элементом"""
    n = len(arr)
    arr.append(target)
    i = 0
    while arr[i] != target:
        i += 1
    arr.pop()
    return i if i < n else -1

def binary_search(arr, target):
    """Бинарный поиск (для отсортированного массива)"""
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def interpolation_search(arr, target):
    """Интерполяционный поиск (для отсортированного равномерно распределённого массива)"""
    l, r = 0, len(arr) - 1
    while l <= r and target >= arr[l] and target <= arr[r]:
        if l == r:
            return l if arr[l] == target else -1
        if arr[r] == arr[l]:
            break
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (target - arr[l]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            l = pos + 1
        else:
            r = pos - 1
    return -1

def _bs_range(arr, l, r, target):
    """Вспомогательная функция для бинарного поиска в диапазоне"""
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def exponential_search(arr, target):
    """Экспоненциальный поиск (для отсортированного массива)"""
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return _bs_range(arr, i // 2, min(i, len(arr) - 1), target)


# ==================== ЭКСПЕРИМЕНТ ДЛЯ ЗАДАНИЯ 3 ====================

def experiment_task3():
    """
    Исследование порога K: когда сортировка + бинарный поиск
    становится выгоднее многократного линейного поиска
    """
    print("=" * 70)
    print("ЗАДАНИЕ 3: Поиск порога эффективности (N = 100 000)")
    print("=" * 70)
    
    N = 100_000
    random.seed(42)
    
    # Генерация данных
    arr_unsorted = [random.randint(0, 2 * N) for _ in range(N)]
    queries = [random.randint(0, 2 * N) for _ in range(1000)]
    
    # Значения K для исследования
    ks = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
    
    results_linear = []
    results_sort_binary = []
    
    for k in ks:
        # Линейный поиск: каждый раз в неотсортированном массиве
        t_start = time.perf_counter()
        for q in queries[:k]:
            linear_search_sentinel(arr_unsorted.copy(), q)
        t_linear = time.perf_counter() - t_start
        results_linear.append(t_linear)
        
        # Сортировка + бинарный поиск: сортируем один раз
        t_start = time.perf_counter()
        arr_sorted = sorted(arr_unsorted)
        for q in queries[:k]:
            binary_search(arr_sorted, q)
        t_sort_binary = time.perf_counter() - t_start
        results_sort_binary.append(t_sort_binary)
        
        print(f"K={k:<4} | Linear: {t_linear:.4f}с | Sort+Binary: {t_sort_binary:.4f}с")
    
    return ks, results_linear, results_sort_binary


# ==================== ЭКСПЕРИМЕНТ ДЛЯ ЗАДАНИЯ 6 ====================

def experiment_task6():
    """
    Исследование зависимости времени поиска от размера массива N
    """
    print("\n" + "=" * 70)
    print("ЗАДАНИЕ 6: Зависимость от размера массива N")
    print("=" * 70)
    
    sizes = [10**3, 10**4, 10**5]  # 10^6 можно добавить, но линейный поиск будет медленным
    reps = 50  # число повторений для усреднения
    random.seed(42)
    
    results = {
        'linear': [],
        'binary': [],
        'interpolation': [],
        'exponential': []
    }
    
    for N in sizes:
        # Генерация отсортированного массива с равномерным распределением
        arr = sorted([random.randint(0, 10 * N) for _ in range(N)])
        target = random.choice(arr)
        
        # Линейный поиск
        t_start = time.perf_counter()
        for _ in range(reps):
            linear_search_sentinel(arr.copy(), target)
        t_linear = (time.perf_counter() - t_start) / reps * 1000  # в мс
        results['linear'].append(t_linear)
        
        # Бинарный поиск
        t_start = time.perf_counter()
        for _ in range(reps):
            binary_search(arr, target)
        t_binary = (time.perf_counter() - t_start) / reps * 1000
        results['binary'].append(t_binary)
        
        # Интерполяционный поиск
        t_start = time.perf_counter()
        for _ in range(reps):
            interpolation_search(arr, target)
        t_interp = (time.perf_counter() - t_start) / reps * 1000
        results['interpolation'].append(t_interp)
        
        # Экспоненциальный поиск
        t_start = time.perf_counter()
        for _ in range(reps):
            exponential_search(arr, target)
        t_exp = (time.perf_counter() - t_start) / reps * 1000
        results['exponential'].append(t_exp)
        
        print(f"N={N:<6} | Linear: {t_linear:.4f}мс | Binary: {t_binary:.4f}мс | "
              f"Interp: {t_interp:.4f}мс | Exp: {t_exp:.4f}мс")
    
    return sizes, results


# ==================== ПОСТРОЕНИЕ ГРАФИКОВ ====================

def plot_task3(ks, linear_times, sort_binary_times):
    """Построение графика для Задания 3"""
    plt.figure(figsize=(10, 6))
    
    plt.plot(ks, linear_times, 'ro-', label='Linear total (линейный поиск)', 
             linewidth=2, markersize=6, markerfacecolor='red')
    plt.plot(ks, sort_binary_times, 'gs-', label='Sort + Binary total', 
             linewidth=2, markersize=6, markerfacecolor='green')
    
    # Находим порог, где Sort+Binary становится выгоднее
    threshold = None
    for i, (tl, tsb) in enumerate(zip(linear_times, sort_binary_times)):
        if tsb < tl:
            threshold = ks[i]
            break
    
    if threshold:
        plt.axvline(x=threshold, color='blue', linestyle='--', alpha=0.5, 
                   label=f'Порог эффективности K ≈ {threshold}')
        plt.annotate(f'Порог K≈{threshold}', 
                    xy=(threshold, min(linear_times[ks.index(threshold)], 
                                      sort_binary_times[ks.index(threshold)])),
                    xytext=(threshold * 2, max(linear_times)),
                    arrowprops=dict(arrowstyle='->', color='blue'),
                    fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))
    
    plt.xlabel('Число запросов K', fontsize=11)
    plt.ylabel('Время выполнения (с)', fontsize=11)
    plt.title('Зависимость времени выполнения от числа запросов K (N = 100 000)', 
              fontsize=13, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3, linestyle=':')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('task3_graph.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("\n✓ График для Задания 3 сохранён: task3_graph.png")


def plot_task6(sizes, results):
    """Построение графика для Задания 6"""
    plt.figure(figsize=(10, 6))
    
    colors = {
        'linear': 'red',
        'binary': 'green', 
        'interpolation': 'blue',
        'exponential': 'purple'
    }
    markers = {
        'linear': 'o',
        'binary': 's',
        'interpolation': '^',
        'exponential': 'D'
    }
    labels = {
        'linear': 'Линейный поиск',
        'binary': 'Бинарный поиск',
        'interpolation': 'Интерполяционный поиск',
        'exponential': 'Экспоненциальный поиск'
    }
    
    for algo in ['linear', 'binary', 'interpolation', 'exponential']:
        plt.plot(sizes, results[algo], 
                color=colors[algo], 
                marker=markers[algo],
                label=f"{labels[algo]}",
                linewidth=2, markersize=7)
    
    # Добавляем справочные линии сложности
    min_time = min(min(results[algo]) for algo in results if results[algo])
    max_time = max(max(results[algo]) for algo in results if results[algo])
    
    # Линия O(n) для наглядности
    n_ref = [sizes[0], sizes[-1]]
    o_n = [min_time * 0.5, max_time * 2]
    plt.plot(n_ref, o_n, 'r--', alpha=0.2, label='O(n) (справочно)')
    
    # Линия O(log n) для наглядности  
    o_log = [min_time] * 2
    plt.plot(n_ref, o_log, 'g--', alpha=0.2, label='O(log n) (справочно)')
    
    plt.xlabel('Размер массива N', fontsize=11)
    plt.ylabel('Среднее время поиска (мс)', fontsize=11)
    plt.title('Зависимость времени поиска от размера массива N', 
              fontsize=13, fontweight='bold')
    plt.legend(fontsize=9)
    plt.grid(True, alpha=0.3, linestyle=':')
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('task6_graph.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ График для Задания 6 сохранён: task6_graph.png")


# ==================== ОСНОВНАЯ ПРОГРАММА ====================

def main():
    print("🔍 Лабораторная работа №4: Построение графиков")
    print("Запуск экспериментов...\n")
    
    # Эксперимент и график для Задания 3
    ks, linear_times, sort_binary_times = experiment_task3()
    plot_task3(ks, linear_times, sort_binary_times)
    
    # Эксперимент и график для Задания 6
    sizes, results = experiment_task6()
    plot_task6(sizes, results)
    
    print("\n" + "=" * 70)
    print("✅ Все графики успешно построены и сохранены!")
    print("📁 Файлы: task3_graph.png, task6_graph.png")
    print("=" * 70)


if __name__ == "__main__":
    main()