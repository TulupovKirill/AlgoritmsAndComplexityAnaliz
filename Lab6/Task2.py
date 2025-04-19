import numpy as np
import datetime

class Interval:
    def __init__(self, start: datetime.time, end: datetime.time):
        self.start = start
        self.end = end


def Algorithm(data: list[Interval]) -> list[Interval]:
    sort_data = list(sorted(data, key=lambda x: x.end, reverse=False))

    result = [sort_data[0]]
    max_right = sort_data[0].end
    for item in sort_data:
        if item.start > max_right:
            result.append(item)
            max_right = item.end
    
    return result


def demo():
    data = [
        Interval(datetime.time(10, 0, 0),datetime.time(11, 30, 0)),
        Interval(datetime.time(11, 0, 0),datetime.time(12, 30, 0)),
        Interval(datetime.time(13, 0, 0),datetime.time(14, 30, 0)),
        Interval(datetime.time(14, 0, 0),datetime.time(15, 30, 0)),
        Interval(datetime.time(15, 0, 0),datetime.time(16, 30, 0))
        ]
    result = Algorithm(data)
    for item in result:
        print(item.start, item.end)

demo()
