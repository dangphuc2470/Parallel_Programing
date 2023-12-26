import multiprocessing

# Hàm để thực hiện công việc cập nhật mảng
def append(index, value, result_array):
    result_array[index] = value

if __name__ == "__main__":
    # Khởi tạo mảng multiprocessing
    result = multiprocessing.Array('i', [0] * 10)  # Mảng số nguyên với độ dài 10, giá trị ban đầu là 0

    # List các công việc cần thực hiện
    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=append, args=(i, i+1, result))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    # In ra kết quả
    print(list(result))
