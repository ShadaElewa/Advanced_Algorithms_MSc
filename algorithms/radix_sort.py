def counting_sort_for_radix(arr, exp):
    """
    A specific version of Count Sort used by Radix Sort.
    It sorts elements based on the significant digit represented by 'exp'.
    exp = 1 (Units), 10 (Tens), 100 (Hundreds), etc.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits are always 0-9
 
    # 1. Store count of occurrences in count[]
    # We look at (arr[i] // exp) % 10 to get the specific digit
    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1
 
    # 2. Change count[i] so that count[i] now contains actual
    #    position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # 3. Build the output array
    # Must traverse in REVERSE to ensure STABILITY
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
 
    # 4. Copy the output array to arr[], so that arr now
    #    contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]
 
def radix_sort(arr):
    """
    Sorts an array of integers using Radix Sort (LSD).
    Time Complexity: O(d * (N + b)) where d is digits, b is base (10).
    """
    if not arr:
        return arr

    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # current digit number
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