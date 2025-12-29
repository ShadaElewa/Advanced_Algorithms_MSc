def counting_sort_for_radix(arr, exp):
    """
    A specific version of Count Sort used by Radix Sort.
    It sorts elements based on the significant digit represented by 'exp'.
    exp = 1 (Units), 10 (Tens), 100 (Hundreds), etc.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  
 
    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
 
    
    for i in range(n):
        arr[i] = output[i]
 
def radix_sort(arr):
    """
    Sorts an array of integers using Radix Sort (LSD).
    Time Complexity: O(d * (N + b)) where d is digits, b is base (10).
    """
    if not arr:
        return arr

    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
        
    return arr

# --- Test Block ---
if __name__ == "__main__":
    print("--- Testing Radix Sort ---")
    test_arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original: {test_arr}")
    sorted_arr = radix_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")
    
    if sorted_arr == sorted([170, 45, 75, 90, 802, 24, 2, 66]):
        print("✅ Correctness Check Passed!")
    else:
        print("❌ Algorithm Failed!")