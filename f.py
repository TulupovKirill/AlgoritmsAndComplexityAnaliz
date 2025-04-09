string = 'чтобы, расшифровать закодированную строку необходимо идти по дереву, сворачивая в соотвуствующую каждому биту сторону до тех пор, пока не будет достигнут лист.'

code = {}
lenght = len(string)

for i in string:
    if i not in code.keys():
        code[i] = 1
    else:
        code[i] += 1

# print(code)
code = sorted(code.items(), key=lambda x: x[1], reverse=True)
print(code)

class Tree:
    def __init__(self):
        self.right = None
        self.left = None
        self.name = None
        self.data = None
