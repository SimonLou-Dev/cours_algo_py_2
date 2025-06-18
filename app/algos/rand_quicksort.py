"""
Exercice 5 : Tri Rapide Randomisé
"""

import random

def quicksort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort_deterministic(left) + [pivot] + quicksort_deterministic(right)

def quicksort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    arr.remove(pivot)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]
    return quicksort_randomized(left) + [pivot] + quicksort_randomized(right)

def compare_sorts(arr):
    import time
    from copy import deepcopy

    start = time.time()
    quicksort_deterministic(deepcopy(arr))
    det_time = time.time() - start

    start = time.time()
    quicksort_randomized(deepcopy(arr))
    rand_time = time.time() - start

    return det_time, rand_time
