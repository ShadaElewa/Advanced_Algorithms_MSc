import time
import tracemalloc
import csv
import sys
import copy
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from algorithms.count_sort import count_sort
from algorithms.radix_sort import radix_sort
from algorithms.bucket_sort import bucket_sort
from data_generator import DataGenerator

# CONFIGURATION

TEST_SIZES = [10000, 50000, 100000, 200000 , 500000]
RUNS_PER_ALGO = 5

def measure_performance(sort_func, data):
    """
    Runs a sorting function and measures Time (ms) and Peak Memory (KB).
    """
    tracemalloc.start()

    data_copy = data[:]
    
    # Start Timer
    start_time = time.perf_counter()
    # Run Algo
    sort_func(data_copy)
    # Stop Timer
    end_time = time.perf_counter()
    

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    

    time_ms = (end_time - start_time) * 1000
    memory_kb = peak_memory / 1024
    
    return time_ms, memory_kb

def run_benchmarks():
    print("🚀 Starting Benchmark Suite...")
    print(f"Sizes to test: {TEST_SIZES}")
    print(f"Runs per size: {RUNS_PER_ALGO} (taking average)")
    print("-" * 60)
    
    # CSV Setup
    csv_file = "analysis_results.csv"
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Algorithm", "Input_Size", "Time_ms", "Memory_KB"])
        
       
        for N in TEST_SIZES:
            print(f"\n[Testing Input Size: {N}]")
            
            # Generate Datasets
            int_data = DataGenerator.get_uniform_integers(N)
            float_data = DataGenerator.get_uniform_floats(N)
            
            
            tasks = [
                ("Quick Sort", quick_sort, int_data),
                ("Heap Sort", heap_sort, int_data),
                ("Count Sort", count_sort, int_data),
                ("Radix Sort", radix_sort, int_data),
                ("Bucket Sort", bucket_sort, float_data) # Uses float data
            ]
            
            for name, func, dataset in tasks:
                total_time = 0
                total_mem = 0
                
                
                for i in range(RUNS_PER_ALGO):
                    t, m = measure_performance(func, dataset)
                    total_time += t
                    total_mem += m
                
            
                avg_time = total_time / RUNS_PER_ALGO
                avg_mem = total_mem / RUNS_PER_ALGO
                
                
                writer.writerow([name, N, f"{avg_time:.4f}", f"{avg_mem:.4f}"])
                print(f"  -> {name}: {avg_time:.2f} ms | {avg_mem:.2f} KB")

    print("\n✅ Benchmarking Complete!")
    print(f"📊 Results saved to: {csv_file}")

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    run_benchmarks()