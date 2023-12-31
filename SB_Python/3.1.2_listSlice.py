#Зрізи списків. Оператори порівняння списків

l = ["dnepr", "kiev", "harkov", "summu"]

k = l[-2:-4:-1]
m = l[-3:-1]

m[0] = "vinnica"

print(l, k, m)

#Задачі
#Є список переглядів відео по днях:
#v = [1205, 1101, 1434, 1320, 923, 874]
#Необхідно вибрати з нього перші три значення (використовуючи зрізи) та вивести результат на екран.

v = [1205, 1101, 1434, 1320, 923, 874]
print(v[0:3])

#Є список переглядів відео по днях:
#v = [1205, 1101, 1434, 1320, 923, 874]
#Необхідно вибрати з нього останні чотири значення (використовуючи зрізи) та вивести результат на екран.

v = [1205, 1101, 1434, 1320, 923, 874]
print(v[len(v) - 4:])

#Є перелік міст:
#c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
#Необхідно за допомогою зрізів вибрати з міста через один (починаючи з першого) і результат вивести на екран.

c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[::2])

#Є перелік міст:
#c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
#Необхідно за допомогою зрізів вибрати з міста через один (починаючи з другого) і результат вивести на екран.

c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
print(c[1::2])

#Є список із оцінками студента:
#m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
#Необхідно за допомогою зрізів вибрати елементи з 3 по 7 (включно) і вивести їх на екран у зворотному порядку.

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[2:7][::-1])

#Є список із оцінками студента:
#m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
#Необхідно за допомогою зрізів вибрати елементи через один, починаючи з останнього, та вивести результат на екран.

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-2])