import random
import time
import matplotlib.pyplot as plt
import numpy as np


def random_permutation(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a

def fisher_yates_shuffle(arr: list):
    a = arr[:]
    n = len(arr)
    result = []
    for i in range(n):
        j = random.randint(0, len(a) - 1)
        result.append(a[j])
        a.pop(j)
    return result

def demo():
    elements = [1, 2, 3, 4]
    print(random_permutation(elements))
    print(fisher_yates_shuffle(elements))

def t(n):
    result = {0: [], 1 : []}
    for i in range(2, n):
        elements = np.random.randint(0, 10, i).tolist()
        time1 = time.time()
        random_permutation(elements)
        time2 = time.time()
        fisher_yates_shuffle(elements)
        time3 = time.time()

        result[0].append(time2-time1)
        result[1].append(time3-time2)
    
    plt.title("Временной анализ алгоритмов слечайных генераций")
    plt.plot(range(2, n), result[0], color="blue", label="Вывернутый алгоритм")
    plt.plot(range(2, n), result[1], color = "black", label="Алгоритм Фишера-Йетеса")
    plt.xlabel("Мощность множества")
    plt.ylabel("Время, мсек")
    plt.legend()
    plt.savefig("Lab4/Task2/time.png")

demo()