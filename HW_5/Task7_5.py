"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)


a = int(input(f'Введите любое натуральное число '))
print(f'Для множества натуральных чисел выполняется равенство: 1+2+...+n = '
      f'n(n+1)/2 = {(sum_n(a) == (a * (a + 1) / 2))} ')
