import time
import sys

# 1. Import your logic
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
# 2. Import your data factory
from data_generator import DataGenerator

def test_algorithm(name, sort_function, original_data):
    """
    Helper function to time and validate a sorting algorithm.
    """
    # CRITICAL: Create a copy of the data. 
    # If we don't, the first algorithm sorts the list, and the second 
    # gets an already sorted list!
    arr_copy = original_data[:] 
    
    start_time = time.perf_counter()
    sorted_data = sort_function(arr_copy)
    end_time = time.perf_counter()
    
    # Validation check
    is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
    
    if is_sorted:
        print(f"✅ {name}: Success in {(end_time - start_time):.6f} seconds.")
    else:
        print(f"❌ {name}: Failed (Data not sorted).")

def run_test():
    print("--- Integration Test Started ---")
    
    # Define size
    N = 20000 
    
    # 1. Generate Data ONCE
    print(f"[1] Generating {N} random integers...")
    master_data = DataGenerator.get_uniform_integers(N)
    
    print("-" * 40)
    
    # 2. Test Quick Sort
    test_algorithm("Quick Sort", quick_sort, master_data)
    
    # 3. Test Heap Sort
    test_algorithm("Heap Sort ", heap_sort, master_data)
    
    print("-" * 40)

if __name__ == "__main__":
    # Increase recursion limit just in case
    sys.setrecursionlimit(20000)
    run_test()