# Use the QuickSelect Algorithm to find the k-th largest element of an array
import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def kthlargest(arr, k):
    n = len(arr)
    def partition(start, end, ind):
        """ Rearranges arr[start:end] so that everything to
        the left of arr[pivot] is smaller than it and likewise
        for the right of arr[pivot] """
        # ind = random.randrange(start, end)
        swap(arr, start, ind)
        pivot = arr[start]
        divider = start+1
        explorer = start+1
        while explorer <= end:
            if arr[explorer] < pivot:
                swap(arr, explorer, divider)
                divider += 1
                if explorer < divider:
                    explorer += 1
            else:
                explorer += 1
        divider -= 1
        swap(arr, start, divider)
        return divider
    
    start, end = 0, n-1
    divider = partition(start, end, random.randint(start, end))
    while divider != n-k:
        if divider < n-k:
            start = divider
        else:
            end = divider
        divider = partition(start, end, random.randint(start, end))
    return arr[divider]

#print(kthlargest([3, 4, 1, 5, 7,8 , 0, 0], 4))

def sortByResidueClass(arr, n):
    dividers = [0]*(n-1)
    explorer = 0
    # everything before arr[dividers[i]] will be of residue class i or smaller
    while explorer < len(arr):
        if arr[explorer] % n < n-1:
            swap(arr, dividers[arr[explorer] % n], explorer) 
            for i in range(arr[explorer] % n, n-1):
                dividers[i] += 1
            if max(dividers) > explorer:
                explorer += 1
        else:
            explorer += 1
        print(dividers)
        print(arr)
    return arr

#print(sortByResidueClass(arr = [3, 0, 4, 1, 5, 2], n = 4))

import heapq

def kthlargestheap(arr, k):
    heap = arr[:k]
    heapq.heapify(heap) #min heap
    for i in range(k, len(arr)):
        if arr[k] > heap[0]:
            heapq.heappush(heap, arr[k])
            heapq.heappop(heap)
    return heapq.heappop(heap)

#print(kthlargest([3, 4, 1, 5, 7,8 , 0, 0], 4))


def hoare(arr):
    """ Partitions array using Hoare's scheme, wrt last element """
    l, r = 0, len(arr)-2
    while l < r:
        if arr[l] > arr[r]:
            swap(arr, l, r)
        else:
            pass
            
        



