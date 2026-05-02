import time
import random
from dynamic_array import DynamicArray
from singly_linked_list import SinglyLinkedList

def benchmark_operation(name, func, n_runs=1):
    start_time = time.perf_counter()
    for _ in range(n_runs):
        func()
    end_time = time.perf_counter()
    return end_time - start_time

def run_comparison():
    sizes = [100, 1000, 10000]
    
    print(f"{'N':<6} | {'Arr Append':<12} | {'List Append':<12} | {'Arr Del Front':<13} | {'List Del Front':<13} | {'Arr Get Idx':<11} | {'List Get Idx':<11}")
    print("-" * 85)

    for N in sizes:
        # 1. Добавление в конец (N раз)
        def test_arr_append():
            arr = DynamicArray()
            for _ in range(N): arr.append(1)
        
        def test_lst_append():
            lst = SinglyLinkedList()
            for _ in range(N): lst.add_back(1)

        t_arr_app = benchmark_operation("Arr Append", test_arr_append)
        t_lst_app = benchmark_operation("List Append", test_lst_append)

        # 2. Удаление из начала (N раз)
        # Сначала нужно наполнить структуры
        def test_arr_del_front():
            arr = DynamicArray()
            for _ in range(N): arr.append(1)
            for _ in range(N): arr.delete(0)

        def test_lst_del_front():
            lst = SinglyLinkedList()
            for _ in range(N): lst.add_back(1)
            for _ in range(N): lst.remove_front()

        t_arr_del = benchmark_operation("Arr Del", test_arr_del_front)
        t_lst_del = benchmark_operation("List Del", test_lst_del_front)

        # 3. Получение по случайному индексу (N раз)
        # Генерируем индексы заранее, чтобы не замерять их генерацию
        indices = [random.randint(0, N-1) for _ in range(N)]

        def test_arr_get():
            arr = DynamicArray()
            for _ in range(N): arr.append(1)
            for idx in indices: arr.get(idx)

        def test_lst_get():
            lst = SinglyLinkedList()
            for _ in range(N): lst.add_back(1)
            for idx in indices: lst.get(idx)

        t_arr_get = benchmark_operation("Arr Get", test_arr_get)
        t_lst_get = benchmark_operation("List Get", test_lst_get)

        print(f"{N:<6} | {t_arr_app:<12.6f} | {t_lst_app:<12.6f} | {t_arr_del:<13.6f} | {t_lst_del:<13.6f} | {t_arr_get:<11.6f} | {t_lst_get:<11.6f}")

if __name__ == "__main__":
    run_comparison()