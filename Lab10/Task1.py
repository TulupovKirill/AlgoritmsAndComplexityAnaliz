import numpy as np
import time
import matplotlib.pyplot as plt
class Node:
    def __init__(self, data):
        self.right: Node = None
        self.left: Node = None
        self.data = data
        self.name: str = None
class Algorithm:
    def __init__(self, data: str):
        self.data: str = data
        self.freq: dict[str, int] = {}
        self.root: Node = None
        self.encoding: dict[str, str] = {}
        self.decoding: dict[str, str] = {}
    def encode(self, message):
        encode_message = ''
        for item in message:
            encode_message += self.encoding[item]
        return encode_message
    def decode(self, message):
        decode_message, temp = '', ''
        for i in range(len(message)):
            temp += message[i]
            try:
                decode_message += self.decoding[temp]
                temp = ''
            except:
                continue
        return decode_message
    def _frequence(self):
        for i in self.data:
            if i not in self.freq.keys():
                self.freq[i] = 1
            else:
                self.freq[i] += 1
    def build(self) -> dict[str, str]:
        self._search(self.root, '0')
    def _search(self, node: Node, result: str) -> None:
        self.encoding[node.name] = result
        self.decoding[result] = node.name
        if node.left is not None:
            self._search(node.left, result + "0")
        if node.right is not None:
            self._search(node.right, result + "1")
        return
    def run(self):
        self._frequence()
        sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)
        nodes: list[Node] = []
        for item in sort_freq:
            node = Node(item[1])
            node.name = item[0]
            nodes.append(node)
        while len(nodes) > 1:
            left = nodes[-1]
            right = nodes[-2]
            nodes = nodes[:-2]
            new = Node(left.data + right.data)
            new.left = left
            new.right = right
            nodes.append(new)
            nodes = sorted(nodes, key=lambda x: x.data, reverse=True)
        self.root = nodes[0]
def main(string):
    alg = Algorithm(string)
    alg.run()
    alg.build()
    encode = alg.encode(string)
    decode = alg.decode(encode)
def result_plot(n):
    result = []
    alf = {1: "А", 2: "Б", 3: "В", 4: "Г", 5: "Д", 6: "Е", 7: "Ё", 8: "Ж", 9: "З", 10: "И",
           11: "Й", 12: "К", 13: "Л", 14: "М", 15: "Н", 16: "О", 17: "П", 18: "Р", 19: "С", 20: "Т",
           21: "У", 22: "Ф", 23: "Х", 24: "Ц", 25: "Ч", 26: "Ш", 27: "Щ", 28: "Ъ", 29: "Ы", 30: "Ь", 
           31: "Э", 32: "Ю", 33: "Я"}
    for i in range(1, n):
        numbers = np.random.randint(1, 33, i)
        string  = "".join([alf[j] for j in numbers])
        start = time.time()
        main(string)
        end = time.time()
        result.append(end - start)
    
    plt.title("Анализ сложности Хоффмана")
    plt.ylabel("Время, сек")
    plt.xlabel("Длина строки")
    plt.plot(result)
    plt.savefig("Lab10/time.jpg")

result_plot(300)
