"""
Задание 1.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

"""

a = float(input("Ведите начальную дистанцию: "))
b = float(input("Введите дистанцию, которую нужно достигнуть: "))
day = 1
while a < b:
    a = a + a / 10
    day += 1
print(f"На {day} день спортсмен достиг результата — не менее {b} км.")
