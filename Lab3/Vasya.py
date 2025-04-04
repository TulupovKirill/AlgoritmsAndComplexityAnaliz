class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class RequiredItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

def calculate_purchases(budget, required_items, price_list):
    # Фильтруем доступные товары
    available_items = {item.name: item.price for item in price_list if item.name in [req.name for req in required_items]}
    
    # Сортируем товары по цене
    sorted_items = sorted(available_items.items(), key=lambda x: x[1])
    
    purchased_items = {}
    
    for name, price in sorted_items:
        for req in required_items:
            if req.name == name and req.quantity > 0:
                if budget >= price:  # Проверяем, позволяет ли бюджет
                    purchased_items[name] = purchased_items.get(name, 0) + 1
                    req.quantity -= 1
                    budget -= price
                else:
                    break  # Бюджет исчерпан

    return purchased_items, budget

# Пример данных
budget = 100
required_items = [RequiredItem("Ручка", 2), RequiredItem("Тетрадь", 3), RequiredItem("Линейка", 1)]
price_list = [Item("Ручка", 10), Item("Тетрадь", 30), Item("Линейка", 5)]

purchased, remaining_budget = calculate_purchases(budget, required_items, price_list)

print("Купленные товары:", purchased)
print("Оставшийся бюджет:", remaining_budget)
