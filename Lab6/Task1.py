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
    data_string = ""
    data = [Interval(0, 30), Interval(10, 40), Interval(20, 70), Interval(50, 60)]
    for item in data:
        data_string += f"[{item.left}, {item.right}], "
    print("Интервалы")
    print(data_string[:-2])
    result = Algorithm(data)
    result_string = ''
    for item in result:
        result_string += f"[{item.left}, {item.right}], "
    print("Решение")
    print(result_string[:-2])

demo()