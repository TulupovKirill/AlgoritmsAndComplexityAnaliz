import numpy as np
import time
import matplotlib.pyplot as plt

def generate_permutations(elements):
    def backtrack(path, remaining):
        if len(path) == len(elements):
            result.add(tuple(path))
            return

        for i in range(len(remaining)):
            next_path = path + [remaining[i]]
            next_remaining = remaining[:i] + remaining[i+1:]
            backtrack(next_path, next_remaining)

    result = set()
    backtrack([], elements)
    return list(result)


def t(n):
    result = []
    for i in range(3, n):
        elements = np.random.randint(0, 10, i).tolist()
        time1 = time.time()
        generate_permutations(elements)
        time2 = time.time()

        result.append(time2 - time1)

    plt.title("Временной анализ перестановок с повторениями")
    plt.plot(range(3, n), result)
    plt.xlabel("Мощность множества")
    plt.ylabel("Время, мсек")
    plt.savefig("time.png")


def demo():
    elements = [1, 2, 2]
    unique_permutations = generate_permutations(elements)
    for perm in unique_permutations:
        print(perm)
