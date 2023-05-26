#PR 3: Min, Max, Sum and Average operations

import numpy as np
import openmp

# Parallel Reduction - Min
def parallel_min(arr):
    min_value = np.inf

    with openmp.parallel:
        for i in range(len(arr)):
            if arr[i] < min_value:
                min_value = arr[i]
    return min_value

def parallel_max(arr):
    max_value = -np.inf

    with openmp.parallel:
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
    return max_value

def parallel_sum(arr):
    total = 0

    with openmp.parallel:
        for i in range(len(arr)):
            total += arr[i]
    return total


def parallel_average(arr):
    total = parallel_sum(arr)
    num_elements = len(arr)
    return total / num_elements


# Example usage
if __name__ == '__main__':
    arr = np.array([5, 8, 2, 10, 3, 6, 1, 9, 4, 7])
    min_value = parallel_min(arr)
    print("Min:", min_value)
    max_value = parallel_max(arr)
    print("Max:", max_value)
    sum_value = parallel_sum(arr)
    print("Sum:", sum_value)
    avg_value = parallel_average(arr)
    print("Average:", avg_value)
