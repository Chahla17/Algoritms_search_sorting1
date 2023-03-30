import random
import time
start = time.time()

def binarySearch(A, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return binarySearch(A, left, mid - 1, x)
    else:
        return binarySearch(A, mid + 1, right, x)
def exponentialSearch(A, x):
    if not A:
        return -1
    bound = 1
    while bound < len(A) and A[bound] < x:
        bound *= 2      
    return binarySearch(A, bound // 2, min(bound, len(A) - 1), x)
if __name__ == '__main__':
    A = [random.randint(0, 10) for i in range(10000)]
    key = 6
    index = exponentialSearch(A, key)
    if index != -1:
        print('Элемент имеет индекс:', index)
    else:
        print('Элемента нет в списке')
end = time.time()
print("Время выполнения:", end - start)
