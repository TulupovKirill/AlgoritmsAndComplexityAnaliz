def generate_subsets(elements):
    def backtrack(start, path):
        # Добавляем текущее подмножество в результаты
        result.append(path)
        # Перебираем элементы, начиная с текущего индекса
        for i in range(start, len(elements)):
            # Рекурсивный вызов с добавлением текущего элемента в путь
            backtrack(i + 1, path + [elements[i]])

    result = []
    backtrack(0, [])
    return result

# Пример использования
elements = ['стол', 'стул', 'шкаф']
subsets = generate_subsets(elements)

# Выводим все подмножества
for subset in subsets:
    print(subset)
