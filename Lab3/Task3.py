def generate_subsets(elements):
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(elements)):
            backtrack(i + 1, path + [elements[i]])

    result = []
    backtrack(0, [])
    return result

elements = ['стол', 'стул', 'шкаф']
subsets = generate_subsets(elements)

for subset in subsets:
    print(subset)
