import numpy as np

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.lenght = right - left


def Algorithm(data: list[Interval]) -> tuple[list[Interval], Interval]:
    sort_data = list(sorted(data, key=lambda x: x.lenght, reverse=True))

    result = [sort_data[0]]
    print(f"result: {result[0].left, result[0].right}")
    print("------------")
    interval = sort_data[0]
    for item in sort_data:
        if item.left < interval.left:
            result.append(item)
            interval.left = item.left

        if item.right > interval.right:
            result.append(item)
            interval.right = item.right

        print(item.left, item.right)
    
    return result, interval


def demo():
    main_interval = Interval(0, 100)
    data = [Interval(0, 30), Interval(10, 40), Interval(20, 70), Interval(50, 60),
            Interval(40, 90), Interval(10, 20), Interval(50, 70)]
    
    result, interval = Algorithm(data)

    print('----------------------------')
    for item in result:
        print(item.left, item.right)
    
    print('----------------------------')
    print(interval.left, interval.right)

demo()
