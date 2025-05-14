import numpy as np

def add(vector:dict):
    i = len(vector)
    flag = True
    while i > 0:
        if flag and i > vector[i]:
            vector[i] += 1
            flag = False
        if i == vector[i]:
            vector[i] = 0
            if i > 1:
                vector[i - 1] += 1
        i -= 1
    flag = True
    for i in vector.keys():
        if vector[i] != 0:
            flag = False
            break
    return flag

def gereration_with_vector(vector:dict):
    L = list(range(len(vector)))
    result = []
    for i in range(len(vector), 0, -1):
        index = vector[i] + 1
        a = L[-index]
        result.append(a)
        L.remove(a)
    result = list(reversed(result))
    return result

def permutation(vector):
    return add(vector)

def demo():
    vector = {i: 0 for i in range(1, 4)}
    flag = False
    while not flag:
        flag = permutation(vector)
        print(gereration_with_vector(vector))
