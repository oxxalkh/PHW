"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы
множеств.

"""
import timeit

code_to_test = """
n = (int(input("Введите число N элементов: ")))
num_list_1 = []
for i in range(n):
    num = int(input("Введите num "))
    num_list_1.append(num)
print(num_list_1)

m = (int(input("Введите число M элементов: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Введите num "))
    num_list_2.append(num)
print(num_list_2)

num_list_3 = num_list_1 + num_list_2
print(num_list_3)
sorted(num_list_3)
for i in set(num_list_3):
    if num_list_3.count(i) <= 1:
        continue
    print(i, end=' ')
"""
elapsed_time = timeit.timeit(code_to_test, number=3)/3
print(elapsed_time)
