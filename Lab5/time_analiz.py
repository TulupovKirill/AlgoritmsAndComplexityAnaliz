import time
import numpy as np
import matplotlib.pyplot as plt
def test_search_algorithms(text: str, pattern: str) -> dict:
    algorithms = {
        "Naive": naive_search,
        "Boyer-Moore": boyer_moore_search,
        "Rabin-Karp": rabin_karp_search,
        "KMP": kmp_search,
    }
    result = {
        "Naive": 0,
        "Boyer-Moore": 0,
        "Rabin-Karp": 0,
        "KMP": 0,
    }
    for name, algorithm in algorithms.items():
        start_time = time.time()
        algorithm(text, pattern)
        end_time = time.time()
        result[name] = end_time - start_time  
    return result
def generation_test():
    alf = {1: "А", 2: "Б", 3: "В", 4: "Г", 5: "Д", 6: "Е", 7: "Ё", 8: "Ж", 9: "З", 10: "И",
           11: "Й", 12: "К", 13: "Л", 14: "М", 15: "Н", 16: "О", 17: "П", 18: "Р", 19: "С", 20: "Т",
           21: "У", 22: "Ф", 23: "Х", 24: "Ц", 25: "Ч", 26: "Ш", 27: "Щ", 28: "Ъ", 29: "Ы", 30: "Ь", 
           31: "Э", 32: "Ю", 33: "Я"}
    file = open("Lab5/test.txt", "w")
    for i in range(10, 100):
        test = np.random.randint(1, 33, i)
        string  = "".join([alf[j] for j in test])
        file.write(string + '\n')
    file.close()
def test():
    text = open("Lab5/test.txt").readlines()
    pattern = "МАМА"
    result_test = {
        "Naive": [],
        "Boyer-Moore": [],
        "Rabin-Karp": [],
        "KMP": [],
    }
    for line in text:
        res = test_search_algorithms(line, pattern)
        for name in res.keys():
            result_test[name].append(res[name])
    plt.title("Временной анализ алгоритмов поиска подстроки в строке")
    for name in result_test:
        plt.plot(range(10, 100), result_test[name], label=name)
    plt.xlabel("Мощность множества строки")
    plt.ylabel("Время, мсек")
    plt.legend()
    plt.savefig("Lab5/time.png")

test()
