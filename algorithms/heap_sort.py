def heapify(arr, n, i):
    """
    Corresponds to the 'Heapify' block in your image.
    n: The size of the heap (elements_in(A) in image)
    i: The index to fix
    """
    largest = i          # In image: max = i
    left = 2 * i + 1     # In image: left = 2i (adjusted for 0-index)
    right = 2 * i + 2    # In image: right = 2i+1 (adjusted for 0-index)
 
    # Logic: if (left <= n) and (A[left] > A[i])
    if left < n and arr[left] > arr[largest]:
        largest = left
 
    # Logic: if (right <= n) and (A[right] > A[max])
    if right < n and arr[right] > arr[largest]:
        largest = right
 
    # Logic: if (max != i)
    if largest != i:
        # swap (A[i], A[max])
        arr[i], arr[largest] = arr[largest], arr[i] 
        
        # Heapify (A, max)
        heapify(arr, n, largest)
 
def build_max_heap(arr):
    """
    Corresponds to 'BuildMaxHeap' in your image.
    """
    n = len(arr)
    # In image: for i = floor(n/2) to 1
    # Python range is exclusive, so we go down to -1 to include index 0
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    """
    Corresponds to 'Heapsort' in your image.
    """
    n = len(arr)
    
    # Step 1: Build the heap
    build_max_heap(arr)
 
    # Step 2: Extraction Loop
    # In image: for i = n to 1 (swapping with root)
    for i in range(n - 1, 0, -1):
        # swap (A[1], A[i]) -> In Python A[0] is root
        arr[i], arr[0] = arr[0], arr[i]
        
        # n = n - 1 (handled by passing 'i' as the new size)
        # Heapify(A, 1) -> In Python index 0
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