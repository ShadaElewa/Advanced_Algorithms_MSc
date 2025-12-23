def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    """
    Sorts an array of floats uniformly distributed in [0, 1).
    Time Complexity: O(N + K) on average.
    Space Complexity: O(N).
    """
    if not arr:
        return arr

    n = len(arr)
    # 1. Create n empty buckets
    buckets = [[] for _ in range(n)]

    # 2. Put array elements in different buckets
    for x in arr:
        # Index = floor(n * value). 
        # Example: 0.76 * 10 = 7.6 -> Index 7.
        index = int(n * x)
        # Safety check: if x is exactly 1.0 (rare), put in last bucket
        if index == n:
            index = n - 1
        buckets[index].append(x)

    # 3. Sort individual buckets
    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    # 4. Concatenate all buckets into arr[]
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
            
    return arr

if __name__ == "__main__":
    print("--- Testing Bucket Sort ---")
    test_arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Original: {test_arr}")
    sorted_arr = bucket_sort(test_arr)
    print(f"Sorted:   {sorted_arr}")
    
    # Check correctness
    if sorted_arr == sorted([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]):
        print("✅ Correctness Check Passed!")
    else:
        print("❌ Algorithm Failed!")