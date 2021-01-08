# n = 10
#
# max_value = 30
# counter = 0
# a = [4, 6, 7, 8, 7, 9, 16, 7, 14, 2, 14]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
#
# for j in range(len(a)):
#     for i in range(len(a) - 1 - j):
#         if a[i] > a[i+1] or a[i] == a[i+1] and b[i] < b[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#             b[i], b[i+1] = b[i+1], b[i]
#
# s = 0
# for i in range(n):
#     if s + a[i] <= max_value:
#         s += a[i]
#         counter += 1
#     else:
#         break
#
# print(s, counter)
#
# print(a)
# print(b)


# Задача №2
# a = [15, 1, 64, 23, 10, 55, 3, 10, 20, 32]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# n = len(a)
# for j in range(n - 1):
#     for i in range(n - j - 1):
#         if b[i] % 2 == 0:
#             b[i], b[i+1] = b[i+1], b[i]
#             a[i], a[i+1] = a[i+1], a[i]
# for i in range(n):
#     if b[i] % 2 == 0:
#         border = i
#         break
# print(border)
# for j in range(border - 1):
#     for i in range(border - j - 1):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#             b[i], b[i+1] = b[i+1], b[i]
# j = border
# while j <= len(a):
#     for i in range(border, n - 1 + border - j):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#             b[i], b[i+1] = b[i+1], b[i]
#     j += 1
# print(a)
# print(b)

# Задача №3
# f = open('./26/26-10.txt')
# s, n = map(int, f.readline().split())
# a = []
# for i in range(n):
#     a.append(int(f.readline()))
# for j in range(n - 1):
#     for i in range(n - j - 1):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
# count = 0
# for i in range(n):
#     if s - a[i] > 0:
#         s -= a[i]
#         count += 1
#     else:
#         max_el = a[i-1]
#         break
# s += a[i]
# for i in range(count, n):
#     if s - a[i] > 0 and a[i] > max_el:
#         max_el = a[i]
#     else:
#         break
# print(count, max_el)

# Задача №4
# f = open('./26/26-k3.txt')
# n, k, m = map(int, f.readline().split())
# a = []
# for i in range(n):
#     a.append(int(f.readline()))
# for j in range(n - 1):
#     for i in range(n - 1 - j):
#         if a[i] < a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
# print(a[k - 1], a[m + k - 1])

