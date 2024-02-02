def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_flag = findFlag(arr, False, pivot)
        greater_flag = findFlag(arr, True, pivot)
        # less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # greater_than_pivot = [x for x in arr[1:] if x > pivot]
        less_than_pivot = filter(arr, less_flag, len(arr))
        greater_than_pivot = filter(arr, greater_flag, len(arr))
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


def findFlag(A, greater, pivot):
    B = [0] * len(A)
    if greater:
        for i in range(len(A)):
            if A[i] > pivot:
                B[i] = 1
    else:
        for i in range(len(A)):
            if A[i] <= pivot:
                B[i] = 1
    return B


def filter(A, ps, n):
    #B = [0] * len(set(ps))  # Tạo mảng B với kích thước bằng số phần tử duy nhất của ps
    B = []
    ps = prefix_sum(ps)
    for i in range(1, n):
        if ps[i] != ps[i - 1]:
           # B[ps[i]] = A[i]
            B.append(A[i])
    return B

def prefix_sum(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])
    return result

# Example usage:
my_array = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_array = quicksort(my_array)
print(sorted_array)
