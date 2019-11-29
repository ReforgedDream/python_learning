# coding=utf-8

import time
import numpy as np

# Всё, что у нас есть на входе - длина последовательности.
sequence_length = 100_000_000

# Используя данную длину, сделаем список-арифметическую прогрессию.
sequence = list(range(1, sequence_length + 1))
# То же самое, но используя numpy
array = np.arange(1, sequence_length + 1)


def calculate_avg_simple(input_sequence):
    """Вычислить среднее арифметическое входной последовательности.
    Используются простые функции, предоставляемые python.
    :param input_sequence: входной массив данных.
    :return: среднее арифметическое всех членов массива.
    """
    total = 0
    for x in input_sequence:
        total += x
    total /= len(input_sequence)
    return total


def calculate_avg_science(input_sequence):
    """Тоже вычислить среднее арифметическое, но с помощью numpy.
    :param input_sequence: входной массив данных.
    :return: среднее арифметическое всех членов массива.
    """
    return np.average(input_sequence)


# Запомнить время начала выполнения
t_start = time.time()
answer_simple = calculate_avg_simple(sequence)
# Зная время начала и текущее время, посчитать длительность
t_execution = round(time.time() - t_start, 2)

print('Average calculation with pure python')
print(answer_simple)
print(t_execution, 'seconds total')

print('\n')

# Запомнить время начала выполнения
t_start = time.time()
answer_scientific = calculate_avg_science(array)
# Зная время начала и текущее время, посчитать длительность
t_execution = round(time.time() - t_start, 2)

print('Average calculation with numpy')
print(answer_scientific)
print(t_execution, 'seconds total')
