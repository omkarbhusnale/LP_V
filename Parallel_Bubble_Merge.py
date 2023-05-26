#PR 2 : Parallel Bubble Sort and Merge Sort

import random
import time
import openmp


# Sequential Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Parallel Bubble Sort
def parallel_bubble_sort(arr):
    n = len(arr)

    with openmp.parallel(num_threads=4):
        for i in range(n - 1):
            with openmp.parallel:
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Sequential Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Parallel Merge Sort
def parallel_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        with openmp.parallel:
            parallel_merge_sort(left_half)
            parallel_merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Measure performance of sequential and parallel algorithms
def measure_performance(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time


# Generate random array
array_size = 1000
random_array = [random.randint(1, 1000) for _ in range(array_size)]

# Measure performance of sequential bubble sort
seq_bubble_sort_time = measure_performance(bubble_sort, random_array[:])

# Measure performance of parallel bubble sort
par_bubble_sort_time = measure_performance(parallel_bubble_sort, random_array[:])

# Measure performance of sequential merge sort
seq_merge_sort_time = measure_performance(merge_sort, random_array[:])

# Measure performance of parallel merge sort
par_merge_sort_time = measure_performance(parallel_merge_sort, random_array[:])

# Print performance results
print("Sequential Bubble Sort Time:", seq_bubble_sort_time)
print("Parallel Bubble Sort Time:", par_bubble_sort_time)
print("Sequential Merge Sort Time:", seq_merge_sort_time)
print("Parallel Merge Sort Time:", par_merge_sort_time)
