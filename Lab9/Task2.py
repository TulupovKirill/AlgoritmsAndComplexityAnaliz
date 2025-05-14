def can_place(container, item, incompatible_pairs):
    for other_item in container:
        if (item, other_item) in incompatible_pairs or (other_item, item) in incompatible_pairs:
            return False
    return True

def place_items_in_containers(items, incompatible_pairs):
    containers = []
    
    for item in items:
        placed = False
        for container in containers:
            if can_place(container, item, incompatible_pairs):
                container.append(item)
                placed = True
                break
        if not placed:
            containers.append([item])
    
    return containers

# Пример использования
items = ['A', 'B', 'C', 'D', 'E']
incompatible_pairs = {('A', 'B'), ('C', 'D')}

result = place_items_in_containers(items, incompatible_pairs)
print("Количество контейнеров:", len(result))
print("Компоновка грузов по контейнерам:", result)
