def count_sort(arr):
    """
    Sorts an array of integers using Counting Sort.
    Time Complexity: O(N + K) where K is the range of elements.
    Space Complexity: O(K) for the count array.
    """
    if not arr:
        return arr
    
    # 1. Find Range
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    # 2. Create Count Array
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)
    
    # 3. Store counts
    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1
    
    # 4. Cumulative Count (Positioning)
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    
    # 5. Build Output (Reverse traversal for Stability)
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
    
    # 6. Copy back to original array
    for i in range(len(arr)):
        arr[i] = output_arr[i]
        
    return arr

if __name__ == "__main__":
    print("--- Testing Count Sort ---")
    test_arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {test_arr}")
    sorted_arr = count_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")
    
    if sorted_arr == sorted([4, 2, 2, 8, 3, 3, 1]):
        print("✅ Correctness Check Passed!")
    else:
        print("❌ Algorithm Failed!")