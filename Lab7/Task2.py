def min_groups(children:list[tuple]):
    children.sort(key=lambda x: x[1])
    groups = 0
    n = len(children)
    i = 0
    while i < n:
        groups += 1
        age_limit = children[i][1] + 2
        while i < n and children[i][1] <= age_limit:
            print(f"Номер группы: {groups}, ребенок: {children[i]}")
            i += 1
    return groups
children = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)]
count = min_groups(children)
print(f"Оптимальное количестов групп: {count}")
