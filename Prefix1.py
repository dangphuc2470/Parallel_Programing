from concurrent.futures import ThreadPoolExecutor, wait
import multiprocessing


def calculate_prefix_sum(arr, result_arr, start, end):
    prefix_sum = 0
    for a in range(start, end):
        prefix_sum += arr[a]
        result_arr[a] = prefix_sum
    return result_arr


if __name__ == '__main__':

    with multiprocessing.Manager() as manager:
        arr = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        print(arr)
        result = manager.list([-1] * len(arr))  # Giá trị ban đầu của các phần tử là -1, tương đương việc chươ tính
        print(calculate_prefix_sum(arr, result, 0, len(arr)))

        result2 = manager.list([-1] * len(arr))  # Giá trị ban đầu của các phần tử là -1, tương đương việc chươ tính

        n = 4  # Số phần muốn chia mảng

        chunk_size = len(arr) // n  # Kích thước của mỗi phần
        futures = []
        endIndex = []
        endIndexValue = []
        with ThreadPoolExecutor() as executor:
            start = 0
            for i in range(n):
                if i < n - 1:
                    end = start + chunk_size
                else:
                    end = len(arr)  # Tính toán end cho từng phần
                #calculate_prefix_sum(arr, result2, start, end)
                future = executor.submit(calculate_prefix_sum, arr, result2, start, end)
                futures.append(future)
                endIndex.append(end-1)
                start = end  # Cập nhật start cho phần tiếp theo
            wait(futures)
            for i in endIndex:
                print(result2[i])
            print(result2)

            # for i in range(len(arr)):
            #     if i <= 3:
            #         result2[i] += endIndex[0]
            #     else:
            #         if i <= 7:
            #             result2[i] += endIndex[1]
            #         else:
            #             result2[i] += endIndex[2]

            # start = 0
            # for i in range(n):
            #     if i < n - 1:
            #         end = start + chunk_size - 1
            #     else:
            #         end = len(arr) - 1  # Tính toán end cho từng phần
            # addEndIndex(arr, result, start, end, endIndex[i])
            # future = executor.submit(addEndIndex, arr, result, start, end, endIndex[i])

        # print(result2)
        # print(endIndex)
        # print(calculate_prefix_sum(arr, result, 0, 4))
