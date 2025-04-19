import numpy as np

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def Algorithm(data: list[Interval]) -> list[Interval]:
    sort_data = list(sorted(data, key=lambda x: x.right, reverse=False))

    result = [sort_data[0]]
    max_right = sort_data[0].right
    for item in sort_data:
        if item.left > max_right:
            result.append(item)
            max_right = item.right
    
    return result


def demo():
    data = [Interval(0, 30), Interval(10, 40), Interval(20, 70), Interval(50, 60)]
    result = Algorithm(data)
    for item in result:
        print(item.left, item.right)

demo()
