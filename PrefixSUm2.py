def scan_r(Input, Result, start, end, offset):
    if start == end:
        Result[start] = offset + Input[start]
        return
    mid = (start + end) // 2

    left_arr = Input[start: mid + 1]
    leftSum = reduce(left_arr, len(left_arr))
    (parallel)
    scan_r(Input, Result, start, mid, offset)
    scan_r(Input, Result, mid + 1, end, offset + leftSum)

def reduce(A, n):
    if n == 1:
        return A[0]
    else:
        (parallel)
        L = reduce(A[:n // 2], n // 2)
        R = reduce(A[n // 2:], n - n // 2)
        return L + R

if __name__ == '__main__':
    input_array = [0, 1, 2, 3, 4, 5, 6, 7]
    # Tạo mảng kết quả với độ dài bằng với mảng đầu vào, ban đầu các phần tử có thể là None hoặc 0
    result_array = [None] * len(input_array)
    # Gọi hàm scan_r với mảng đầu vào và mảng kết quả
    scan_r(input_array, result_array, 0, len(input_array) - 1, 0)
    print(result_array)