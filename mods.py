# array[0 .. n -1, 0, 1]
# int[n][2]


# Не Кратность для двоек
# f = open('text.txt')

# n = int(f.readline())
# diff = 10001
# min_s = 0 
# for i in range(n):
#     p1, p2 = map(int, f.readline().split())
#     if p1 > p2:
#         p1, p2 = p2, p1
#     min_s += p1
#     if (p2 - p1) % 3 != 0 and p2 - p1 < diff:
#         diff = p2 - p1


# if min_s % 3 == 0:
#     min_s = min_s + diff

# print(min_s)


# Не Кратность для троек
# f = open('text.txt')

# n = int(f.readline())

# min_diff = 10001
# max_s = 0
# for i in range(n):
#     p = list(map(int, f.readline().split()))
#     p.sort()
#     max_s += p[2] + p[1]
#     if p[2] - p[0] < min_diff and (p[2] - p[0]) % 5 != 0:
#         min_diff = p[2] - p[0]
#     if p[1] - p[0] < min_diff and (p[1] - p[0]) % 5 != 0:
#         min_diff = p[1] - p[0]

# if max_s % 5 == 0:
#     max_s = max_s - min_diff

# print(max_s) 

# f = open('text.txt')

# n = int(f.readline())
# max_s = 0
# ost = [10001] * 5
# ost[0] = 0

# for i in range(n):
#     a = list(map(int, f.readline().split()))
#     a.sort()
#     # OBRABOTKA NOVIH ZNACHENIY
#     max_s += a[1]
#     # PODGOTOVKA SLEDUISHIH ITERACIY
#     diff = a[1] - a[0]
#     temp = ost.copy()
#     for j in range(5):
#         if j + diff % 5 < 5:
#             next_j = j + diff % 5
#         else:
#             next_j = j + diff % 5 - 5


#         if ost[j] != 10001 and temp[next_j] > ost[j] + diff:
#             temp[next_j] = temp[j] + diff
    
#     if temp[diff % 5] > diff:
#         temp[diff % 5] = diff

#     ost = temp.copy()

# # vichislenie resultata
# if max_s % 5 != 0:
#     max_s -= ost[max_s % 5]

# print(max_s)


'''
1.Прочитать условие
2.Разобраться почему пример выводит такие значения
3.Придумать алгоритм для примера
4.Придумать, какие случаи необходимо обработать
5.Придумать алгоритм, который решает задачу с учетом п.4
6.Понять сколько нужно переменных и каких
7.Начать писать код(ввод данных и обработка конечная)
8.Подумать как обрабатываются данные на итерации
9.Что нужно на следующей
10.Написать код

'''


# Task 1
# f = open('./mods/27-26a.txt')
# n = int(f.readline())

# min_s = 0
# ost = [10001] * 16
# ost[0] = 0
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     if a > b:
#         a, b = b, a
#     min_s += a
#     diff = b - a
#     temp = ost.copy()
#     for j in range(16):
#         if ost[j] != 10001 and temp[(j + diff % 16) % 16] > ost[j] + diff:
#             temp[(j + diff % 16) % 16] = ost[j] + diff
#     if temp[diff % 16] > diff:
#         temp[diff % 16] = diff

#     ost = temp.copy()
# if min_s % 16 != 15:
#     min_s += ost[15 - (min_s % 16)]


# print(min_s)


# Task 2
# f = open('./mods/27-32b.txt')

# n = int(f.readline())

# ost = [10001] * 12
# ost[0] = 0
# min_s = 0

# for i in range(n):
#     a = list(map(int, f.readline().split()))
#     a.sort()
#     min_s += a[0]
#     diff = a[2] - a[0]
#     temp = ost.copy()
#     for j in range(12):
#         if ost[j] != 10001 and temp[(j + diff % 11) % 11] > ost[j] + diff:
#             temp[(j + diff % 11) % 11] = ost[j] + diff
#     if temp[diff % 5] > diff:
#         temp[diff % 5] = diff
#     ost = temp.copy()
#     diff = a[1] - a[0]
#     for j in range(12):
#         if ost[j] != 10001 and temp[(j + diff % 11) % 11] > ost[j] + diff:
#             temp[(j + diff % 11) % 11] = ost[j] + diff
#     if temp[diff % 5] > diff:
#         temp[diff % 5] = diff
#     ost = temp.copy()

# if min_s % 11 != 0:
#     min_s += ost[11 - (min_s % 11)]

# print(min_s)


# Task 3 
# f = open('./mods/27-23b.txt')

# n = int(f.readline())

# max_s = 0
# diff = 10001

# for i in range(n):
#     a, b = map(int, f.readline().split())
#     if a > b:
#         a, b = b, a
#     max_s += b
#     if (b - a) % 5 != 0 and b - a < diff:
#         diff = b - a

# print(max_s)
# print(diff)
# if max_s % 5 == 0 and max_s % 2 != 0:
#     max_s -= diff
# print(max_s)