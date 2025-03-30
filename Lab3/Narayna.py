def next_permutation(sequence) -> bool:
	count = len(sequence)
	i = count
	# Этап № 1
	while True:
		if i < 2:
			return False # Перебор закончен
		i -= 1
		if sequence[i - 1] > sequence[i]:
			break
	# Этап № 2
	j = count
	while j > i and not sequence[i - 1] > sequence[j - 1]:
		j -= 1
	sequence[i - 1], sequence[j - 1] = sequence[j - 1], sequence[i - 1]
	# Этап № 3
	j = count
	while i < j - 1:
		j -= 1
		sequence[i], sequence[j] = sequence[j], sequence[i]
		i += 1
	return True


def greater(value_0, value_1) -> bool:
	return value_0 > value_1


def main():
    sequence = list(map(lambda x: int(x), input().split(' ')))
    permutation_found = True
    while permutation_found:
        print(sequence)
        permutation_found = next_permutation(sequence)
		
if __name__ == '__main__':
    main()