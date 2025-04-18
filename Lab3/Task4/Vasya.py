def calculate_purchases(budget, price_list: dict, required_item: dict):
    # Сортируем товары по цене
    sorted_items = sorted(price_list.items(), key=lambda x: x[1])
    
    purchased_items = {}
    
    # максимальная мощность корзины
    for name, price in sorted_items:
        if budget >= price and name in required_item:  # Проверяем, позволяет ли бюджет
            purchased_items[name] = purchased_items.get(name, 0) + required_item[name]
            budget -= price
        else:
            break  # Бюджет исчерпан

    # осталось добить бюджет или в ноль
    def backtrack(budget, elements:dict):
        for name, price in sorted_items:
            if budget >= price:
                elements[name] += 1
                budget -= price
                el = elements.copy()
                b = budget
                backtrack(b, el)
            else:
                break

        if elements not in result:
            result.append(elements)

    result = []
    backtrack(budget, purchased_items)
    return result


def demo():
    budget = 100
    required_item = {"Ручка": 2, "Тетрадь": 2, "Линейка": 2}
    price_list = {"Ручка": 10, "Тетрадь": 30, "Линейка": 5}

    purchased = calculate_purchases(budget, price_list, required_item)

    for items in purchased:
        print(items)