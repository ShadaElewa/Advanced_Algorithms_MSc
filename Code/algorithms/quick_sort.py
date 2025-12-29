import random
import sys

# Increase recursion depth just in case for very large datasets
sys.setrecursionlimit(20000)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _randomized_partition(arr, low, high):
    random_pivot_index = random.randint(low, high)
    
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]
    
    return _partition(arr, low, high)

def quick_sort_recursive(arr, low, high):
    if low < high:
        # pi = partitioning index
        pi = _randomized_partition(arr, low, high)

        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr):
    
    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr



if __name__ == "__main__":
    print("--- Testing Quick Sort Logic ---")
    
    # Test
    test_arr = [10, 7, 8, 9, 1, 5]
    print(f"Original: {test_arr}")
    sorted_arr = quick_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")
    
    # Validation
    if sorted_arr == sorted([10, 7, 8, 9, 1, 5]):
        print("Correctness Check Passed!")
    else:
        print("Algorithm Failed!")