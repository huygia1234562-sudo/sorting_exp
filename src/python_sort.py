import numpy as np
import time
import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]: largest = l
    if r < n and arr[largest] < arr[r]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def generate_data():
    datasets = []
    size = 1000000
    
    datasets.append(np.sort(np.random.rand(size)))
    datasets.append(np.sort(np.random.rand(size))[::-1])
    for i in range(3, 8): datasets.append(np.random.rand(size))
    for i in range(8, 11): datasets.append(np.random.randint(0, 1000000, size))
    
    return datasets

import pandas as pd

results = []

def benchmark():
    datasets = generate_data() 
    
    for i, data in enumerate(datasets):
        row = {'Dữ liệu': i + 1}
        
        methods = {
            'Quicksort': quick_sort,
            'Heapsort': heap_sort,
            'Mergesort': merge_sort,
            'sort (numpy)': np.sort
        }
        
        for name, func in methods.items():
            temp_data = data.copy()
            
            start_time = time.time()
            func(temp_data)
            end_time = time.time()
            
            duration = (end_time - start_time) * 1000
            row[name] = round(duration, 2)
            
        results.append(row)

    df = pd.DataFrame(results)
    df.loc['Trung bình'] = df.mean(numeric_only=True)
    df.to_csv('ket_qua_sorting.csv', index=False, encoding='utf-8-sig')

benchmark()