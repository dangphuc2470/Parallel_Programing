import multiprocessing


def calculate_prefix_sum(arr):
    prefix_sum = 0
    result_arr = [0] * len(arr)
    for a in range(len(arr)):
        prefix_sum += arr[a]
        result_arr[a] = prefix_sum
    return result_arr


def append(position1, arr, result):
    pos = position1
    for j in range(len(arr)):
        result[pos] = arr[j]
        pos = pos + 1
    return result


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # arr = [
        #     [1, 5],
        #     [4],
        #     [7, 10, 13],
        #     [2]
        # ]

        arr = [
            [1, 5, 9, 12, 22, 34, 19, 8],
            [4, 6, 11, 23, 14, 18, 31, 21, 35],
            [7, 10, 13, 20, 29, 32, 25, 30, 33, 36],
            [2, 3, 15, 37, 38, 39, 40]
        ]

        arrLen = [0]
        for a in arr:
            arrLen.append(len(a))
        position = calculate_prefix_sum(arrLen)
        print(position)

        result = manager.list([-1] * position[len(arr)])
        print(result)

        for i in range(len(position)-1):
            append(position[i], arr[i], result)
        print(result)

        # for a in arr:
        #     append(a, position[i], result)
        #     i = i + 1

