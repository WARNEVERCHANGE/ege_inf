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

f = open('text.txt')

n = int(f.readline())
max_s = 0
ost = [10001] * 5


for i in range(n):
    a = list(map(int, f.readline().split()))
    a.sort()
    # OBRABOTKA NOVIH ZNACHENIY
    max_s += a[1]
    # PODGOTOVKA SLEDUISHIH ITERACIY
    diff = a[1] - a[0]
    temp = ost.copy()
    for j in range(5):
        if temp[j] != 10001 and temp[(j + diff % 5) % 5] > temp[j] + diff:
            temp[(j + diff % 5) % 5] = temp[j] + diff
# vichislenie resultata
if max_s % 5 != 0:
    max_s -= ost[max_s % 5]

print(max_s)