import time
import matplotlib.pyplot as plt

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


seq = list(reversed(range(1, 10)))
permutation_found = True
while permutation_found:
	permutation_found = next_permutation(seq)
	print(seq)

"""
    Функция generate_permutations(n): Эта функция инициализирует вектор инверсий и массив для хранения перестановок. 
	Она запускает рекурсивную функцию backtrack.

    Функция backtrack(current_permutation): Эта рекурсивная функция генерирует перестановки. 
	Если длина текущей перестановки равна n, она добавляет её в список результатов. 
	В противном случае, она перебирает все возможные элементы, которые могут быть добавлены.

    Обновление вектора инверсий: При добавлении нового элемента мы обновляем вектор инверсий, проверяя, 
	сколько элементов в текущей перестановке больше нового элемента.

    Рекурсия и возврат: После добавления элемента вызывается рекурсивный вызов. 
	После завершения мы удаляем последний элемент и восстанавливаем вектор инверсий.

"""