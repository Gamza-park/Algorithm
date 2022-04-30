def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A, last:int) -> int:
    largest = 0
    for i in range(last + 1):
        if A[i] > A[largest]:
            largest = i

    return largest

A = [1,3,4,5,2]
print(A)
# selectionSort(A)
# print(A)

def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        for i in range(numElements - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

# bubbleSort(A)
# print(A)

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i - 1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc+1] = newItem

# insertionSort(A)
# print(A)

def mergeSort(A, p:int, r:int):
    if p < r:
        q = (p + r)
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p:int, q:int, r:int):
    i = p; j = q+1; t = 0
    tmp = [0 for i in range(len(A))]
    while i <= q and j <= r:
        if A[i]<= A[j]:
            tmp[t] = A[i]; t += 1; i += 1
        else:
            tmp[t] = A[j]; t += 1; j += 1
    while i <= q:
        tmp[t] = A[j]; t += 1; j += 1
    while j <= r:
        tmp[t] = A[j]; t += 1; j += 1
    i = p; t = 0
    while i <= r:
        A[i] = tmp[t]; t += 1; i += 1

def quickSort(A, p:int, r:int):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p:int, r:int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def heapSort(A):
    buildHeap(A)
    for last in range(len(A)-1, 0, -1):
        A[last], A[0] = A[0], A[last]
        percolateDown(A, 0, last-1)

def buildHeap(A):
    for i in range(len(A)-1, 0, -1):
        percolateDown(A,i, len(A)-1)

def percolateDown(A, k:int, end:int):
    child = 2*k+1
    right = 2*k+2
    if child <= end:
        if right <= end and A[child] < A[right]:
            child = right
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, end)

def shellSort(A):
    H = gapSequence(len(A))
    for h in H:
        for k in range(h):
            stepInsertionSort(A, k, h)

def stepInsertionSort(A, k:int, h:int):
    for i in range(k + h, len(A), h):
        j = i - h
        newItem = A[i]
        while 0 <= j and newItem < A[j]:
            A[j + h] = A[j]
            j -= h
        A[j + h] = newItem

def gapSequence(n:int) -> list:
    H = [1]; gap = 1
    while gap < n/5:
        gap = 3 * gap + 1
        H.append(gap)
    H.reverse()
    return H

def countingSort(A):
    k = max(A)
    C = [0 for _ in range(k+1)]
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    B = [0 for _ in range(len(A))]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

import math

def radixSort(A):
    maxValue = max(A)
    numDigits = math.ceil(math.log10(maxValue)) # 자릿수 계산
    bucket = [[] for _ in range(10)] # 0, 1, ..., 9 에 대한 10개의 리스트
    for i in range(numDigits):
        for x in A:
            y = (x // 10 ** i) % 10
            bucket[y].append(x)
        A.clear()
        for j in range(10):
            A.extend(bucket[j])
            bucket[j].clear()

def bucketSort(A):
    n = len(A)
    B = [[]for _ in range(n)]
    for i in range(n):
        B[math.floor(n*A[i])].append(A[i])
    A.clear()
    for i in range(n):
        insertionSort(B[i])
        A.extend(B[i])
