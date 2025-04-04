def generate_permutations(n: int):
    # Инициализация вектора инверсий
    inversions = [0] * n
    # Инициализация массива для хранения перестановок
    permutations = []
    
    def backtrack(current_permutation: list):
        if len(current_permutation) == n:
            permutations.append(current_permutation[:])
            return
        
        for i in range(n):
            if i not in current_permutation:
                current_permutation.append(i)
                # Обновляем вектор инверсий
                new_inversions = inversions[:]
                for j in current_permutation[:-1]:
                    if j > i:
                        new_inversions[j] += 1
                inversions[:] = new_inversions
                backtrack(current_permutation)
                current_permutation.pop()
                # Восстанавливаем вектор инверсий
                inversions[:] = [0] * n

    backtrack([])
    return permutations

# Пример использования
n = 3
perms = generate_permutations(n)
for perm in perms:
    print(perm)
