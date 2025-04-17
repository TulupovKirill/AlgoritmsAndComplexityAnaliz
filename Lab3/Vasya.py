def calculate_purchases(budget, price_list: dict):
    # Сортируем товары по цене
    sorted_items = sorted(price_list.items(), key=lambda x: x[1])
    
    purchased_items = {}
    
    # максимальная мощность корзины
    for name, price in sorted_items:
        if budget >= price:  # Проверяем, позволяет ли бюджет
            purchased_items[name] = purchased_items.get(name, 0) + 1
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

budget = 90
price_list = {"Ручка": 10, "Тетрадь": 30, "Линейка": 5}

purchased = calculate_purchases(budget, price_list)

for items in purchased:
    print(items)
