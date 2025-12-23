import time
import sys

# Algorithms
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from algorithms.count_sort import count_sort
from algorithms.radix_sort import radix_sort
from algorithms.bucket_sort import bucket_sort 

# Data Factory
from data_generator import DataGenerator

def test_algorithm(name, sort_function, original_data):
    """
    Standard test function for any algorithm
    """
    
    arr_copy = original_data[:] 
    
    start_time = time.perf_counter()
    sorted_data = sort_function(arr_copy)
    end_time = time.perf_counter()
    
    # Handles both integers and floats correctly
    is_sorted = True
    for i in range(len(sorted_data)-1):
        if sorted_data[i] > sorted_data[i+1]:
            is_sorted = False
            break
            
    if is_sorted:
        print(f"✅ {name}: Success in {(end_time - start_time):.6f} seconds.")
    else:
        print(f"❌ {name}: Failed.")

def run_test():
    print("========================================")
    print("   ADVANCED ALGORITHMS INTEGRATION TEST   ")
    print("========================================")
    
    N = 50000 
    
    
    print(f"\n[PART 1] Testing Integer Sorts (N={N})")
    print("Generating random integers...")
    int_data = DataGenerator.get_uniform_integers(N)
    
    test_algorithm("Quick Sort", quick_sort, int_data)
    test_algorithm("Heap Sort ", heap_sort, int_data)
    test_algorithm("Count Sort", count_sort, int_data)
    test_algorithm("Radix Sort", radix_sort, int_data)
    
    
    print(f"\n[PART 2] Testing Float Sorts (N={N})")
    print("Generating random floats [0, 1)...")
    float_data = DataGenerator.get_uniform_floats(N)
    
    
    test_algorithm("Bucket Sort", bucket_sort, float_data)
    
    
    test_algorithm("Quick Sort", quick_sort, float_data) 
    
    print("\n========================================")

if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    run_test()