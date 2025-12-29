def heapify(arr, n, i):
    """
    Corresponds to the 'Heapify' block in your image.
    n: The size of the heap (elements_in(A) in image)
    i: The index to fix
    """
    largest = i          
    left = 2 * i + 1     
    right = 2 * i + 2    
 
    # Logic: if (left <= n) and (A[left] > A[i])
    if left < n and arr[left] > arr[largest]:
        largest = left
 
    # Logic: if (right <= n) and (A[right] > A[max])
    if right < n and arr[right] > arr[largest]:
        largest = right
 
    # Logic: if (max != i)
    if largest != i:
        
        arr[i], arr[largest] = arr[largest], arr[i] 
        
        heapify(arr, n, largest)
 
def build_max_heap(arr):
    """
    Corresponds to 'BuildMaxHeap' in your image.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    maintains the Max-Heap property by sinking smaller nodes down the tree.
    """
    n = len(arr)
    
    # Step 1: Build the heap
    build_max_heap(arr)
 
    # Step 2: Extraction Loop
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    return arr

# --- Test Block ---
if __name__ == "__main__":
    print("--- Testing Heap Sort (Image Logic) ---")
    test_arr = [4, 10, 3, 5, 1]
    print(f"Original: {test_arr}")
    sorted_arr = heap_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")
    
    if sorted_arr == sorted([4, 10, 3, 5, 1]):
        print("✅ Correctness Check Passed!")
    else:
        print("❌ Algorithm Failed!")