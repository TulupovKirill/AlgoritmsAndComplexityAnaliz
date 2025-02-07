import time
import matplotlib.pyplot as plt
import numpy as np


def GenerationData(n):
    file = open("Lab2/data.txt", 'w+', encoding='utf-8')
    for i in range(1, n + 1):
        data = np.random.randint(1, 100000, i)
        line = " ".join([str(i) for i in data])[:-1]
        file.write(line + "\n")
    file.close()


def BubbleSort(data: list[int]):
    t = 1
    N = len(data)
    t += 1
    for i in range(N-1):
        t += 1
        for j in range(N-1-i):
            if data[j] > data[j+1]:
                t += 4
                data[j], data[j+1] = data[j+1], data[j]
    return data, t + 1


def InsertSort(data: list[int]):
    n = len(data)
    t = 2
    for i in range(1, n):
        x = data[i]
        j = i
        t += 3
        while j > 0 and data[j - 1] > x:
            data[j] = data[j - 1]
            j -= 1
            t += 2
        data[j] = x
        t += 1

    return data, t + 1


def GnomeSort(data: list[int]):
    n, i = len(data) - 1, 0
    t = 3
    while i < n:
        if data[i] <= data[i + 1]:
            i += 1
            t += 2
        else:
            data[i], data[i + 1] = data[i + 1], data[i]
            t += 3
            if i > 0:
                i -= 1
                t += 2
    
    return data, t + 1


def main():
    # GenerationData(50)
    data = list(map(lambda x: x.split(' '), open("Lab2/data.txt").readlines()))
    lens = []
    for i in range(len(data)):
        lens.append(len(data[i]))
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

    result_time = {1: [], 2: [], 3: []}
    result_operation = {1: [], 2: [], 3: []}

    for array in data:
        time1 = time.time()
        _, t1 = BubbleSort(array)
        time2 = time.time()
        _, t2 = InsertSort(array)
        time3 = time.time()
        _, t3 = GnomeSort(array)
        time4 = time.time()

        result_time[1].append((time2 - time1) * 1000)
        result_time[2].append((time3 - time2) * 1000)
        result_time[3].append((time4 - time3) * 1000)

        result_operation[1].append(t1)
        result_operation[2].append(t2)
        result_operation[3].append(t3)

    print(len(result_time[1]), len(result_operation[2]), len(lens))
    plt.title("Временный анализ")
    plt.plot(lens, result_time[1], color="red")
    plt.plot(lens, result_time[2], color="black")
    plt.plot(lens, result_time[3], color="blue")
    plt.xticks(lens)
    plt.xlabel("Сортировка")
    plt.ylabel("Время, мсек")
    plt.legend(["Пузырьковая", "Вставками", "Гномья"])
    plt.savefig("Lab2/time.png")

    plt.clf()

    plt.title("Анализ сложности")
    plt.plot(lens, result_operation[1], color="red")
    plt.plot(lens, result_operation[2], color="black")
    plt.plot(lens, result_operation[3], color="blue")
    plt.xticks(lens)
    plt.xlabel("Сортировка")
    plt.ylabel("Количество операций")
    plt.legend(["Пузырьковая", "Вставками", "Гномья"])
    plt.savefig("Lab2/iteration.png")


def example(line: str):
    data = list(map(lambda x: int(x), line.split(' ')))
    res1, _ = BubbleSort(data)
    res2, _ = InsertSort(data)
    res3, _ = GnomeSort(data)
    print(f'Bubble: {res1}\nInsert: {res2}\nGnome: {res3}')

if __name__ == "__main__":
    line = input()
    example(line)