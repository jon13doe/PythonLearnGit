a = [1, 23, 121, -31, 12.5, -76.5]
print(a)

a.append(121)
print(a)

a.append(True)
print(a)

a.insert(2, 777)
print(a)

a.remove(True)
print(a)

b = a.pop(5)
print(a, b)

z = a.copy()

z.clear()
print(z)

c = a.copy()
d = a[:]
e = list(a)
print(a, c, d, e, sep="\n")

a.append(777)
b = a.count(777)
print(a, b, sep="\n")

c = a.index(777)
d = a.index(777, 2)
print(c, d, sep="\n")

a.reverse()
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a = str(input())
lst = list(a.strip())

lst.pop(0)
lst.pop(0)
lst.insert(0, '8')
lst.remove('-')
lst.remove('-')

print("".join(lst))

a = list(map(int, input().split()))
a.sort()
b = a[0: 3]
print(b)

#Задачі
#Вводиться рядок з цілих чисел через пропуск. Якщо перше число не дорівнює останньому, потрібно додати значення True, а інакше - значення False. Результуючий список lst вивести команду на екран: print(*lst)
#Реалізувати завдання без використання умовних операторів.

lst = list(map(int, input().split()))
lst.append(lst[0] != lst[-1])
print(*lst)

#Є перелік міст:
#cities = ["Москва", "Казань", "Ярославль"]
#Необхідно вставити в другу позицію цього списку рядок "Ульяновськ" та вивести список командою: print(*cities)

cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, "Ульяновск")
print(*cities)

#Вводиться рядок із номером телефону у форматі: 
#+7(xxx)xxx-xx-xx
#Необхідно перетворити її на список lst (посимвольно, тобто, елементами списку будуть окремі символи рядка). Потім, видалити перший +, число 7 замінити на 8 і прибрати дефіси. Відобразити отриманий список на екрані командою: print("".join(lst))

a = str(input())
lst = list(a.strip())
lst.pop(0)
lst.pop(0)
lst.insert(0, '8')
lst.remove('-')
lst.remove('-')
print("".join(lst))

#В один рядок через пропуск вводяться: ім'я, по батькові та прізвище. Необхідно подати ці дані у вигляді нового рядка у форматі: Прізвище І.О. (Наприклад, Сергій Михайлович Балакірєв -> Балакірєв С.М.).

iof = input().split()
i = list(iof[0]).pop(0)
o = list(iof[1]).pop(0)
print(f"{iof[2]} {i}.{o}.")

#Вводяться цілі числа в один рядок через пропуск (не менше чотирьох). Необхідно знайти три найменші числа в цій послідовності чисел і вивести їх на екран у порядку зростання. Реалізувати програму без умовного оператора.

a = list(map(int, input().split()))
a.sort()
b = a[0: 3]
print(*b)

#Вводяться цілі числа в один рядок через пропуск. Необхідно перетворити їх у список lst , потім видалити останнє значення і якщо воно непарне, то до списку (в кінець) додати True, інакше - False. Відобразити отриманий список на екрані командою: print(*lst)
#Реалізувати програму без умовного оператора.

lst = list(map(int, input().split()))
lst.append(lst.pop() % 2 != 0)
print(*lst)

#Вводяться оцінки студента (числа від 2 до 5) в один рядок через пропуск. Необхідно визначити кількість двійок та вивести це значення на екран.

print(list(map(int, input().split())).count(2))

#Вводятся названия рек в одну строчку через пробел. Необхідно все їх відсортувати за іменами (за віком) і у відсортованому списку видалити перший елемент. Результат відображається на екрані в одну строчку через пробіл.

lst = list(map(str, input().split()))
lst.sort()
lst.pop(0)
print(*lst)