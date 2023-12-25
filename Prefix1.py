from concurrent.futures import ThreadPoolExecutor, wait
import multiprocessing


def calculate_prefix_sum(arr, result_arr, start, end, arrIndexValue, i):
    prefix_sum = 0
    for a in range(start, end):
        prefix_sum += arr[a]
        result_arr[a] = prefix_sum
    arrIndexValue[i] = result_arr[end - 1]
    return result_arr


def calculate_prefix_sum2(arr):
    prefix_sum = 0
    result_arr = [0] * len(arr)
    for a in range(len(arr)):
        prefix_sum += arr[a]
        result_arr[a] = prefix_sum
    return result_arr


def add(result, i, endIndexValue, endI):
    result[i] += endIndexValue[endI]


if __name__ == '__main__':

    with multiprocessing.Manager() as manager:
        arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        print("Input array: ", arr)
        result = manager.list([-1] * len(arr))  # Giá trị ban đầu của các phần tử là -1, tương đương việc chươ tính

        n = 4  # Số phần muốn chia mảng

        numPerChunk = len(arr) // n  # Kích thước của mỗi phần
        futures = []
        endIndex = []
        endIndexValue = [0] * (n + 1)
        with ThreadPoolExecutor() as executor:
            start = 0
            for i in range(n):
                if i < n - 1:
                    end = start + numPerChunk
                else:
                    end = len(arr)  # Tính toán end cho từng phần
                future = executor.submit(calculate_prefix_sum, arr, result, start, end, endIndexValue,
                                         i + 1)  # Bỏ qua phần tử đầu
                futures.append(future)
                endIndex.append(end - 1)
                start = end  # Cập nhật start cho phần tiếp theo
            wait(futures)
            print("End indexes: ", endIndex)
            print("End indexes value: ", endIndexValue)
            endIndexValue = calculate_prefix_sum2(endIndexValue)
            print("End indexes value sum: ", endIndexValue)
            print("Normal Prefix Sum: ", calculate_prefix_sum2(arr))
            print("Before Prefix Sum: ", result)

            print("Value to Add: ", endIndexValue)
            endI = 0
            i = 0
            while i < len(result):
                future = executor.submit(add, result, i, endIndexValue, endI)
                futures.append(future)
                i = i + 1
                if i % numPerChunk == 0:
                    endI += 1

            wait(futures)
            print("After Prefix Sum: ", result)

