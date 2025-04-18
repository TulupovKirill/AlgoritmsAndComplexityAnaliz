disriptions = None

def Jonson_Trottet(sequence: list, disriptions):
    lenght = len(sequence)

    id_max_value = sequence.index(min(sequence))
    disription = 0

    arr_idx_value_greater_max_value = []

    for i in range(lenght):
        if disriptions[i] > 0 and i < lenght - 1:
            if sequence[i] > sequence[i + 1] and sequence[i] >= sequence[id_max_value]:
                id_max_value = i
                disription = disriptions[i]
        
        if disriptions[i] < 0 and i > 0:
            if sequence[i] > sequence[i - 1] and sequence[i] >= sequence[id_max_value]:
                id_max_value = i
                disription = disriptions[i]
    
    if disription == 0:
        return False
    
    for i in range(lenght):
        if sequence[i] > sequence[id_max_value]:
            arr_idx_value_greater_max_value.append(i)

    if disription > 0:
        sequence[id_max_value], sequence[id_max_value + 1] = sequence[id_max_value + 1], sequence[id_max_value]
        disriptions[id_max_value], disriptions[id_max_value + 1] = disriptions[id_max_value + 1], disriptions[id_max_value]
    else:
        sequence[id_max_value], sequence[id_max_value - 1] = sequence[id_max_value - 1], sequence[id_max_value]
        disriptions[id_max_value], disriptions[id_max_value - 1] = disriptions[id_max_value - 1], disriptions[id_max_value]

    for i in arr_idx_value_greater_max_value:
        disriptions[i] *= -1
    return True


sequence = list(range(1, 10))
disriptions = [-1] * len(sequence)
flag = True
while flag:
    flag = Jonson_Trottet(sequence, disriptions)