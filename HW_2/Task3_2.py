"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в
программе.
"""
my_list = [456, 55.78, {'shop': 'AVdaily', 'home': 'lomonosovskii'}, -45,
           ('dtxyst', 'wtyyjcnb'), None, 'True', True, ['4', 'grrr'], ]


def type_list(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


type_list(my_list)
