# Вводится список городов в одну строчку через пробел.
# Необходимо создать итератор для этого списка и с
# помощью итератора вывести на экран в столбик первые
# два значения (названия городов).

c = list(input().split())
t = iter(c)
for i in range(2):
    print(next(t))

# Вводится строка. Нужно создать итератор для перебора символов
# этой строки. Затем, перебрать через созданный итератор все
# символы до первого пробела. В процессе перебора символы
# выводить на экран в одну строчку друг за другом (без пробелов).
# Гарантируется, что во введенной строке имеется хотя бы один пробел.

s = str(input())
t = iter(s)
n = ''
for i in range(s.find(' ')):
    n += next(t)
print(n)

# Вводится четырехзначное целое положительное число.
# Подумайте, как можно определить итератор для перебора
# его цифр. Выведите цифры этого введенного числа
# (с помощью итератора) в одну строчку через пробел.

s = str(input())
t = iter(s)
n = ''
fl = True
for i in range(len(s)):
    n += ("" if fl else " ") + next(t)
    fl = False
print(n)