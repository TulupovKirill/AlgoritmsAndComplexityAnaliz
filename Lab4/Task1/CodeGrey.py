def gray_code(n):
    return [i ^ (i >> 1) for i in range(1 << n)]

def generate_permutations(n):
    gray_codes = gray_code(n)
    permutations = []
    
    for code in gray_codes:
        permutation = []
        for i in range(n):
            # Получаем i-ый бит кода Грэя и добавляем соответствующее значение
            if (code >> i) & 1:
                permutation.append(i + 1)
        permutations.append(permutation)
    
    return permutations

# Пример использования
n = 3
permutations = generate_permutations(n)
print("Перестановки с использованием кода Грэя:")
for perm in permutations:
    print(perm)