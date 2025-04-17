def generate_permutations(elements):
    def backtrack(path, remaining):
        if len(path) == len(elements):
            result.add(tuple(path))
            return

        for i in range(len(remaining)):
            next_path = path + [remaining[i]]
            next_remaining = remaining[:i] + remaining[i+1:]
            backtrack(next_path, next_remaining)

    result = set()
    backtrack([], elements)
    return list(result)

elements = [1, 2, 2]
unique_permutations = generate_permutations(elements)
for perm in unique_permutations:
    print(perm)