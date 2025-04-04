def generate_permutations(elements):
    def backtrack(path, remaining):
        if len(path) == len(elements):
            # Добавляем уникальную перестановку в результат
            result.add(tuple(path))
            return

        for i in range(len(remaining)):
            # Выбираем текущий элемент
            next_path = path + [remaining[i]]
            next_remaining = remaining[:i] + remaining[i+1:]
            backtrack(next_path, next_remaining)

    result = set()
    backtrack([], elements)
    return list(result)

# Пример использования
elements = [1, 2, 2]
unique_permutations = generate_permutations(elements)
for perm in unique_permutations:
    print(perm)


"""
    Функция generate_permutations(elements): Это основная функция, 
    которая принимает список элементов и инициализирует множество для хранения уникальных перестановок.

    Вложенная функция backtrack(path, remaining): Это рекурсивная функция, которая генерирует перестановки.
        path — текущая перестановка, которую мы строим.
        remaining — оставшиеся элементы, которые еще не были добавлены в path.

    Базовый случай: Когда длина path равна длине исходного списка elements, мы добавляем текущую перестановку в результат.

    Цикл for: Мы перебираем все оставшиеся элементы и добавляем каждый из них в path, создавая новую комбинацию. 
    Затем рекурсивно вызываем backtrack для оставшихся элементов.

    Использование множества: Мы используем set для хранения перестановок, чтобы избежать дублирования.
"""