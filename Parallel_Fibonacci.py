import concurrent.futures
import multiprocessing
import sys
import time

# Đặt giới hạn cho số chữ số cho 1 số nguyên là 1 tỷ chữ số
sys.set_int_max_str_digits(1000000000)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


def Append(i, mangFibonacci, mangIndexFCanTinh):
    h = int(i)
    if mangFibonacci[h] == -1:  # Chưa được gán
        mangFibonacci[h] = h
        mangIndexFCanTinh.append(h)

    return


def ThemSoFibonacciCanTinh(soBanDau, mangFibonacci, mangIndexFCanTinh):
    '''
        Từ n ban đầu, lần lượt chia đôi ra và tìm các số Fibonacci cần tính, đưa nó vào đúng thứ tự (Index)
        trong mảng Fibonacci, lưu thứ tự đó vào MangIndexFCanTinh
    '''
    # Đối với index từ 0 đến 2, ta gán sẵn giá trị cho nó
    if soBanDau == 2:
        Append(1, mangFibonacci, mangIndexFCanTinh)
        return
    if soBanDau == 0:
        Append(0, mangFibonacci, mangIndexFCanTinh)
        return
    if soBanDau == 1:
        Append(1, mangFibonacci, mangIndexFCanTinh)
        return

    # Kể từ Index thứ 3, thêm số đó vào MangFibonacci và MangIndexFCanTinh,
    # sau đó đệ quy để tìm tiếp tục (Chỉ đệ quy nếu số đó chưa được gán)
    Append(soBanDau, mangFibonacci, mangIndexFCanTinh)
    # Tìm k và N sao cho số lượng số Fibonacci cần có trước để tính 1 số Fibonacci là ít nhất
    if soBanDau % 2 == 0:  # Đối với số chẵn, lấy k = N = soBanDau / 2, cần tìm cả F[k], F[k+1] và F[k-1]
        k = int(soBanDau / 2)
        if mangFibonacci[k] == -1:
            ThemSoFibonacciCanTinh(k, mangFibonacci, mangIndexFCanTinh)
        if mangFibonacci[k + 1] == -1:
            ThemSoFibonacciCanTinh(k + 1, mangFibonacci, mangIndexFCanTinh)
        if mangFibonacci[k - 1] == -1:
            ThemSoFibonacciCanTinh(k - 1, mangFibonacci, mangIndexFCanTinh)
    else:  # Đối với số lẻ, lấy k (soBanDau + 1) / 2), N = (soBanDau - 1) / 2, chỉ cần tìm F[k] và F[N]
        k = int((soBanDau + 1) / 2)
        N = int((soBanDau - 1) / 2)
        if (mangFibonacci[N] == -1):
            ThemSoFibonacciCanTinh(N, mangFibonacci, mangIndexFCanTinh)
        if (mangFibonacci[k] == -1):
            ThemSoFibonacciCanTinh(k, mangFibonacci, mangIndexFCanTinh)

    return


def TinhFibonacciThuN(mangCacMangIndexFCanTinh, F):
    '''
    Tính lần lượt các mảng con để tìm ra được số Fibonacci thứ N
    :param mangCacMangIndexFCanTinh: Mảng các mảng con từ mảng Index đã chia ra
    :param F: Mảng Fibonacci
    :return:
    '''

    F[0] = 0
    F[1] = 1
    F[2] = 1
    F[3] = 2
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for subarray in mangCacMangIndexFCanTinh:
            for element in subarray:
                future = executor.submit(TinhFibonacci, element, F)
                futures.append(future)
            concurrent.futures.wait(futures)

    return


# region Không song song (Không dùng)
def TinhFibonacciThuNKhoongSongSong(MangCacMangIndexFCanTinh):  # Tính không song song
    for subarray in MangCacMangIndexFCanTinh:
        for value in subarray:
            TinhFibonacciKSS(value)
    return


def TinhFibonacciKSS(n):  # Chỉ dùng với hàm tính không song song
    soNaoDo = int(n)
    F[0] = 0
    F[1] = 1
    F[2] = 1
    F[3] = 2
    if soNaoDo <= 3:
        return

    if soNaoDo % 2 == 0:
        k = int(soNaoDo / 2)
        N = int(soNaoDo / 2)
    else:
        k = int((soNaoDo + 1) / 2)
        N = int((soNaoDo - 1) / 2)

    F[soNaoDo] = F[N + 1] * F[k] + F[N] * F[k - 1]
    return


# endregion

def TinhFibonacci(soCanTinh, mangF):
    '''
    Tính từng số Fibonacci dựa trên các số Fibonacci đã có, áp dụng công thức
    F[N + k] = F[N + 1] * F[k] + F[N] * F[k - 1]
    :param soCanTinh: Số thứ tự của số Fibonacci
    :param mangF: Mảng Fibonacci
    :return:
    '''
    if soCanTinh % 2 == 0:
        k = int(soCanTinh / 2)
        N = int(soCanTinh / 2)
    else:
        k = int((soCanTinh + 1) / 2)
        N = int((soCanTinh - 1) / 2)
    mangF[soCanTinh] = mangF[N + 1] * mangF[k] + mangF[N] * mangF[k - 1]
    return


def splitNext(mangIndexFCanTinh):
    '''
    Tách mảng Index ra để chạy song song nhiều lần,
    vì cần phải có kết quả ở trước mới chạy ở mảng sau được
    :param mangIndexFCanTinh:
    :return: MangIndexFCanTinh
    '''
    mangCacMangIndexFCanTinh = []
    temp = []
    count = 0
    limit = 4
    for i in range(len(mangIndexFCanTinh)):
        if mangIndexFCanTinh[i] > 3:
            if count < limit and (len(temp) == 0 or mangIndexFCanTinh[i] - temp[-1] == 1):
                temp.append(mangIndexFCanTinh[i])
                count += 1
            else:
                mangCacMangIndexFCanTinh.append(temp)
                temp = [mangIndexFCanTinh[i]]
                count = 1

    # Thêm mảng con cuối cùng vào kết quả
    mangCacMangIndexFCanTinh.append(temp)
    return mangCacMangIndexFCanTinh

def main():
    n = 100000
    full_time_start = start_time = time.time()
    MangIndexFCanTinh = []

    with multiprocessing.Manager() as manager:
        F = manager.list([-1] * (n + 1))  # Giá trị ban đầu của các phần tử là -1, tương đương việc chươ tính
        print("Thời gian tạo mảng:", time.time() - start_time)

        start_time = time.time()
        # Từ n ban đầu, lần lượt chia đôi ra và tìm các số Fibonacci cần tính,
        # đưa nó vào đúng thứ tự (Index) trong mảng Fibonacci, lưu thứ tự đó vào MangIndexFCanTinh
        ThemSoFibonacciCanTinh(n, F, MangIndexFCanTinh)
        print("Thời gian thêm số F cần tính:", time.time() - start_time)

        start_time = time.time()
        # Sắp xếp index theo thứ tự để tính từ bé đến lớn
        MangIndexFCanTinh = quick_sort(MangIndexFCanTinh)
        end_time = time.time()
        print("Thời gian sort:", time.time() - start_time)
        print("Các số Fibonacci cần tính là:\n", MangIndexFCanTinh)

        start_time = time.time()
        # Tách mảng Index ra để chạy song song nhiều lần,
        # vì cần phải có kết quả ở trước mới chạy ở mảng sau được
        MangCacMangIndexFCanTinh = splitNext(MangIndexFCanTinh)
        print("Mảng đã chia ra để tính song song mỗi phần tử trong mảng con:\n", MangCacMangIndexFCanTinh)
        print("Thời gian split:", time.time() - start_time)

        # TinhFibonacciThuNKhoongSongSong(MangCacMangIndexFCanTinh)   Khi tính tuần tự nó vẫn nhanh hơn tính song song, Em chưa biết do phần nào làm cho nó chạy chậm

        start_time = time.time()
        # Tính lần lượt các mảng con để tìm ra được số Fibonacci thứ N
        TinhFibonacciThuN(MangCacMangIndexFCanTinh, F)
        print("Thời gian tính F cuối cùng:", time.time() - start_time)
        print("Tổng thời gian thực thi:", time.time() - full_time_start)
        print(f"Số Fibonacci thứ {n} là: ", F[n])

        # Ghi chú: Trong quá trình thực thi bằng hàm tính Fibonacci song song bên trên,
        # nếu chạy chương trình 2 lần gần nhau có thể cho ra kết quả sai,
        # VD: F[10] lần đầu bằng 55, khi chạy lần nữa sẽ ra 65
        # Khi dùng hàm không song song thì không xảy ra hiện tượng này,
        # em đã thử tạo hàm reset cache nhưng vẫn không thể khắc phục được hiện tượng này.

    return 0

if __name__ == "__main__":
    main()