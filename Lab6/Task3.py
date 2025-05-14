class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.lenght = right - left
def Algorithm(data: list[Interval]) -> tuple[list[Interval], Interval]:
    sort_data = list(sorted(data, key=lambda x: x.left, reverse=False))
    result = [sort_data[0]]
    interval = sort_data[0]
    for item in sort_data[1:]:
        if item.left < interval.left:
            result.append(item)
            interval.left = item.left
        if item.right > interval.right:
            result.append(item)
            interval.right = item.right   
    return result
def demo():
    data_string = ""
    data = [Interval(0, 30), Interval(10, 40), Interval(20, 70), Interval(50, 60), Interval(40, 90), Interval(10, 20), Interval(50, 70)]
    for item in data:
        data_string += f"[{item.left}, {item.right}], "
    print("Отрезки")
    print(data_string[:-2])
    result = Algorithm(data)
    result_string = ''
    for item in result[1:]:
        result_string += f"[{item.left}, {item.right}], "
    print("Решение")
    print(result_string[:-2])