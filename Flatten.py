import multiprocessing
import concurrent.futures
import time
import random


def append(position1, arr, result):
    pos = position1
    for j in range(len(arr)):
        result[pos] = arr[j]
        pos = pos + 1
    return result


# def flatten_2d_array(array_2d):
#     flattened_array = []
#     for row in array_2d:
#         for element in row:
#             flattened_array.append(element)
#     return flattened_array
#

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # arr = [
        #     [1, 5],
        #     [4],
        #     [7, 10, 13],
        #     [2]
        # ]

        # arr = [
        #     [1, 5, 9, 12, 22, 34, 19, 8],
        #     [4, 6, 11, 23, 14, 18, 31, 21, 35],
        #     [7, 10, 13, 20, 29, 32, 25, 30, 33, 36],
        #     [2, 3, 15, 37, 38, 39, 40]
        # ]
        arr = []

        counter = 1

        for i in range(1000):
            col_length = random.randint(1, 1000)
            row = [counter + j for j in range(col_length)]
            arr.append(row)
            counter += col_length
        print(arr)

        prefixSum = 0
        position = [0]
        for a in arr:
            prefixSum += len(a)
            position.append(prefixSum)
        print(position)

        result = manager.list([-1] * position[len(arr)])
        print(result)
        start = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for i in range(len(position) - 1):
                future = executor.submit(append, position[i], arr[i], result)  # Bỏ qua phần tử đầu
                futures.append(future)
            concurrent.futures.wait(futures)
        print(result)
        print(time.time() - start)

        # Tóm tắt thuật toán: Tìm độ dài của từng dòng trong mảng,
        # thêm vào mảng position, mảng này chứa vị trí bắt đầu của từng dòng mới
        # Tiến hành thêm các phần tử của mỗi dòng song song với nhau
        # Phần dưới là dùng multiprocessing nhưng em thấy thời gian chạy nó lâu hơn dùng concurrent.futures

        # result = multiprocessing.Array('i', [-1] * position[len(arr)])
        #
        # start = time.time()
        # processes = []
        # for i in range(len(position) - 1):
        #     p = multiprocessing.Process(target=append, args=(position[i], arr[i], result))
        #     processes.append(p)
        #     p.start()
        #
        # for p in processes:
        #     p.join()
        #
        # print(list(result))
        # print(time.time() - start)
