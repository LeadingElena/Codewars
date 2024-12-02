from itertools import groupby


def unique_in_order(sequence):
    list_sequence = list(sequence)
    list_unique_value = []
    if len(list_sequence) != 0:
        list_unique_value = [list_sequence[0]]
        x = 1
        for value in list_sequence[1:]:
            if value != list_unique_value[x - 1]:
                list_unique_value.append(value)
                x += 1

    return list_unique_value


def unique_in_order_1(sequence):
    if not sequence:
        return []

    return [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i - 1]]

def unique_in_order_2(sequence):
    return [k for k, g in groupby(sequence)]

sequence = 'AFRDS'
print(unique_in_order(sequence))

