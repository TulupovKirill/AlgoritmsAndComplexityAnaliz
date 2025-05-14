def min_groups(children):
    children.sort(key=lambda x: x[1])
    groups = 0
    i = 0
    n = len(children)

    while i < n:
        groups += 1
        age_limit = children[i][1] + 2
        while i < n and children[i][1] <= age_limit:
            i += 1

    return groups

# Пример использования
n = int(input("Введите количество детей: "))
children = [tuple(map(int, input("Введите номер и возраст ребенка: ").split())) for _ in range(n)]
print(min_groups(children))
