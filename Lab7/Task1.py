class Order:
    def __init__(self, id, price, date):
        self.id = id
        self.price = price
        self.date = date
def min_orders(orders:list[Order]) -> list[Order]:
    orders.sort(key=lambda x: x.price, reverse=True)
    groups = []
    free_day = 1
    n = len(orders)
    for i in range(n):
        order = orders[i]
        if len(groups) < order.date:
            if free_day <= order.date:
                free_day = order.date - free_day
            groups.append(order)
    return groups
n = 5
orders_string = ''
orders = [Order("A", 40, 2), Order("B", 25, 1), Order("C", 30, 2), Order("D", 15, 1), Order("E", 20, 3)]
print("Номер", "Дедлайн", "Стоимость",  sep="\t")
for order in orders:
    print(order.id, order.date, order.price, sep="\t")
result = min_orders(orders)
print("Решение")
for order in result:
    print(order.id, order.date, order.price, sep="\t")
