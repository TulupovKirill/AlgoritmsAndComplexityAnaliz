import time
import matplotlib.pyplot as plt

def RecursionMethod(n : int, t: int):
    if n == 0:
        t += 2
        return 0
    if n == 1:
        t += 2
        return 1
    t += 1
    return RecursionMethod(n - 1, t) + RecursionMethod(n - 2, t), t


def ReccurentMethod(n : int, t: int):
    t += 1
    fibbonacci_num = [1, 1]
    t += 1
    for i in range(2, n):
        t += 2
        fibbonacci_num.append(fibbonacci_num[i - 1] + fibbonacci_num[i - 2])
    t += 1
    return fibbonacci_num[n - 1], t


def main():
    n = 200

    recurrent_result_time = []
    recurrent_result_iteration = []

    recursion_result_time = []
    recursion_result_iteration = []

    for i in range(n):
        t = 0
        start_time = time.time()
        code_to_test, time_result = ReccurentMethod(i, t)
        stop_time = time.time()
        recurrent_result_time.append((stop_time - start_time) * 1000)
        recurrent_result_iteration.append(time_result)

        t = 0
        start_time = time.time()
        code_to_test, time_result = ReccurentMethod(i, t)
        stop_time = time.time()
        recursion_result_time.append((stop_time - start_time) * 1000)
        recursion_result_iteration.append(time_result)

    plt.clf()

    plt.title("Временный анализ")
    plt.xlabel("Вычисление номера элемента Фиббоначчи")
    plt.ylabel("Время, мсек")
    plt.plot(range(n), recurrent_result_time, color="red", label="Рекурсия")
    plt.plot(range(n), recursion_result_time, color="black", label="Рекурретность")
    plt.savefig("time.png")

    plt.clf()

    plt.title("Анализ сложности")
    plt.xlabel("Вычисление номера элемента Фиббоначчи")
    plt.ylabel("Количество операций")
    plt.plot(range(n), recurrent_result_iteration, color="red", label="Рекурсия")
    plt.plot(range(n), recursion_result_iteration, color="black", label="Рекурретность")
    plt.savefig("iteration.png")

if __name__ == "__main__":
    main()
