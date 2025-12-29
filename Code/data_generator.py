import random

class DataGenerator:
    @staticmethod
    def get_uniform_integers(size, min_val=0, max_val=100000):
        ##Will be used for: Quick Sort, Merge Sort, Heap Sort (integers between min_val and max_val)
        return [random.randint(min_val, max_val) for _ in range(size)]

    @staticmethod
    def get_uniform_floats(size):
        ##Will be used for: Bucket Sort (floats between 0 and 1)
        return [random.random() for _ in range(size)]

    @staticmethod
    def get_sorted_integers(size, reverse=False):
        ##Will be used for: Testing the worst case scenario for Quick Sort
        data = list(range(size))
        if reverse:
            return data[::-1]
        return data
    