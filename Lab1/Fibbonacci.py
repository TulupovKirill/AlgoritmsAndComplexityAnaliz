import time
import matplotlib.pyplot as plt

def RecursionMethod(n : int, t: int):
    if n == 0:
        return 0, t + 2
    if n == 1:
        return 1, t + 2
    t += 1
    a, t1 = RecursionMethod(n - 1, t)
    b, t2 = RecursionMethod(n - 2, t)
    return a + b, t1 + t2 + t


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
    n = 20

    recurrent_result_time = []
    recurrent_result_iteration = []

    recursion_result_time = []
    recursion_result_iteration = []

    for i in range(n):
        t = 0
        start_time = time.time()
        code_to_test, iter_result = ReccurentMethod(i, t)
        stop_time = time.time()
        recurrent_result_time.append((stop_time - start_time) * 1000)
        recurrent_result_iteration.append(iter_result)

        t = 0
        start_time = time.time()
        code_to_test, iter_result = RecursionMethod(i, t)
        stop_time = time.time()
        recursion_result_time.append((stop_time - start_time) * 1000)
        recursion_result_iteration.append(iter_result)

    plt.clf()

    plt.title("Временный анализ")
    plt.plot(range(n), recurrent_result_time, color="red")
    plt.plot(range(n), recursion_result_time, color="black")
    plt.xticks(range(n))
    plt.xlabel("Вычисление номера элемента Фиббоначчи")
    plt.ylabel("Время, мсек")
    plt.legend(["Рекурретность", "Рекурсия"])
    plt.savefig("Lab1/time.png")

    plt.clf()

    plt.title("Анализ сложности")
    plt.plot(range(n), recurrent_result_iteration, color="red")
    plt.plot(range(n), recursion_result_iteration, color="black")
    plt.xticks(range(n))
    plt.xlabel("Вычисление номера элемента Фиббоначчи")
    plt.ylabel("Количество операций")
    plt.legend(["Рекурретность", "Рекурсия"])
    plt.savefig("Lab1/iteration.png")

if __name__ == "__main__":
    main()
