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
        decode_message = ''
        temp = ''
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
            # print('--------1---------')
            # print('\n'.join([f"{node.data}, {node.name}" for node in nodes]))
            left = nodes[-1]
            right = nodes[-2]
            nodes = nodes[:-2]

            new = Node(left.data + right.data)
            new.left = left
            new.right = right

            nodes.append(new)
            nodes = sorted(nodes, key=lambda x: x.data, reverse=True)
            # print('--------2---------')
            # print('\n'.join([f"{node.data}, {node.name}" for node in nodes]))

        self.root = nodes[0]


def main():
    string = "hello"
    alg = Algorithm(string)
    alg.run()
    alg.build()

    print(alg.encoding)
    print(alg.decoding)

    encode = alg.encode(string)
    decode = alg.decode(encode)

    print(f"{string}\n{encode}")
    print(f"{encode}\n{decode}")

if __name__ == "__main__":
    main()