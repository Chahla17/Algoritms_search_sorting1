import time
start = time.time()
import random
def interpolationSearch(A, target):
    if not A:
        return -1
    (left, right) = (0, len(A) - 1)
    while A[right] != A[left] and A[left] <= target <= A[right]:
        mid = left + (target - A[left]) * (right - left) // (A[right] - A[left])
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if target == A[left]:
        return left
    return -1
if __name__ == '__main__':
    A = [random.randint(0, 10) for i in range(10000)]
    key = 5
    index = interpolationSearch(A, key)
    if index != -1:
        print('Элемент имеет индекс', index)
    else:
        print('Элемента нет в списке')
end = time.time()
print("Время выполнения:", end - start)