from Insersion_vector import permutation, gereration_with_vector
from Jonson_Trottet import Jonson_Trottet
from Narayna import next_permutation

import time
import matplotlib.pyplot as plt


disriptions = None
result = {0: [], 1: [], 2: []}
n = 10
for i in range(2, n):

    vector = {i: 0 for i in range(1, i)}
    flag = False
    time1 = time.time()
    while not flag:
        flag = permutation(vector)
        gereration_with_vector(vector)
    time2 = time.time()

    sequence = list(range(1, i))
    disriptions = [-1] * len(sequence)
    flag = True
    time3 = time.time()
    while flag:
        flag = Jonson_Trottet(sequence, disriptions)
    time4 = time.time()

    seq = list(reversed(range(1, i)))
    permutation_found = True
    time5 = time.time()
    while permutation_found:
        permutation_found = next_permutation(seq)
    time6 = time.time()

    result[0].append(time2 - time1)
    result[1].append(time4 - time3)
    result[2].append(time6 - time5)


plt.title("Временной анализ")
plt.plot(range(2, n), result[0], color="red")
plt.plot(range(2, n), result[1], color="black")
plt.plot(range(2, n), result[2], color="blue")
plt.xlabel("Лексико-графический порядок")
plt.ylabel("Время, мсек")
plt.legend(["Вектор инверсий", "Джонсон-Троттета", "Нарайна"])
plt.savefig("time1.png")