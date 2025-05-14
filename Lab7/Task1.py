def min_orders(orders:list):
    orders.sort(key=lambda x: x[1])
    groups = 0
    i = 0
    n = len(orders)

    while i < n:
        groups += 1
        time_limit = orders[i][1] + 2
        while i < n and orders[i][1] <= time_limit:
            i += 1

    return groups

n = int(input("Введите количество заказов: "))
children = [tuple(map(int, input("Введите номер заказа и день: ").split())) for _ in range(n)]
print(min_orders(children))
