from functools import reduce
import operator
import re

# Задача: доделать задачи 41 и 43, причем с применением функций ускоренной обработки данных.
# в 41 задаче можно решить вариант без использования скобок.
# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

def my_evel(string):
    if "(" in string:
        numbers = re.findall(r"\((.+)\)", string)[0]
        exp = re.findall(r"\(.+\)", string)[0]
        return my_evel(string.replace(exp, str(my_evel(numbers))))
    elif "+" in string:
        numbers = re.split(r"\+", string, 1)
        return operator.add(my_evel(numbers[0]), my_evel(numbers[1]))
    elif "-" in string:
        numbers = re.split(r"\-", string, 1)
        return operator.sub(my_evel(numbers[0]), my_evel(numbers[1]))
    elif "*" in string:
        numbers = re.split(r"\*", string, 1)
        return operator.mul(my_evel(numbers[0]), my_evel(numbers[1]))
    elif "/" in string:
        numbers = re.split(r"\/", string, 1)
        return operator.floordiv(my_evel(numbers[0]), my_evel(numbers[1]))
    else:
        return int(string)

exp = "3*((10-2*3)+3)"
print("Задача 41")
print(f"{exp}={my_evel(exp)}")

# Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
num_list = [1, 2, 3, 5, 1, 5, 3, 10]
print("Задача 43")
un_elements = [i for i in num_list if reduce(lambda count, item: count + (item == i), num_list, 0) == 1]
print(un_elements)

