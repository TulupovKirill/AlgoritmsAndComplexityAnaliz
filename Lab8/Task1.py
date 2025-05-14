import numpy as np
import matplotlib.pyplot as plt
import time
def knapsack_full_brute_force(weights, values, W):
    n = len(weights)
    max_value = 0
    best_combination = []
    for i in range(1 << n):
        total_weight = 0
        total_value = 0
        current_combination = []
        for j in range(n):
            if i & (1 << j):
                total_weight += weights[j]
                total_value += values[j]
                current_combination.append(j)
        if total_weight <= W and total_value > max_value:
            max_value = total_value
            best_combination = current_combination
    return best_combination, max_value
def knapsack_greedy(weights, values, W):
    n = len(weights)
    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_weight = 0
    total_value = 0
    best_combination = []
    for i in range(n):
        weight, value = items[i]
        if total_weight + weight <= W:
            total_weight += weight
            total_value += value
            best_combination.append(items[i])
    return best_combination, total_value
result = []
for i in range(20):
    weights = np.random.randint(1, 100, i)
    values = np.random.randint(1, 100, i)
    W = np.random.randint(1, 100)
    time1 = time.time()
    best_combination_brute, max_value_brute = knapsack_full_brute_force(weights, values, W)
    time2 = time.time()
    best_combination_greedy, max_value_greedy = knapsack_greedy(weights, values, W)
    time3 = time.time()
    result.append([time2 - time1, time3 - time2])
result = np.array(result)
plt.title("Анализ сложности")
plt.plot(result[:, 0], label="Полный перебор")
plt.plot(result[:, 1], label="Жадный алгоритм")
plt.xlabel("Размер данных")
plt.ylabel("Время, сек")
plt.legend()
plt.savefig("Lab8/result.jpg")

