import numpy as np
import time
import matplotlib.pyplot as plt

def generate_subsets(elements):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(elements)):
            backtrack(i + 1, path + [elements[i]])

    result = []
    backtrack(0, [])
    return result


def demo():
    elements = ['стол', 'стул', 'шкаф']
    subsets = generate_subsets(elements)
    for subset in subsets:
        print(subset)


def t(n):
    result = []
    for i in range(3, n):
        elements = [str(i) for i in np.random.randint(0, 10, i).tolist()]
        time1 = time.time()
        for j in range(1, len(elements) + 1):
            generate_subsets(elements[:j])
        time2 = time.time()
        result.append(time2 - time1)

    plt.title("Временной анализ всевозможных выборок из множества")
    plt.plot(range(3, n), result)
    plt.xlabel("Мощность множества")
    plt.ylabel("Время, мсек")
    plt.savefig("time.png")

t(10)