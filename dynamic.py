# f = open('text.txt')
# n = int(f.readline())
#
# count = [0] * 13
# for i in range(n):
#     x = int(f.readline())
#     count[x] += 1
#
#
# num = [0] * 13
# for i in range(1, 13):
#     num[i] = i
#
#
# for j in range(11):
#     for i in range(12 - j):
#         if count[i] > count[i+1]:
#             count[i], count[i+1] = count[i+1], count[i]
#             num[i], num[i+1] = num[i+1], num[i]
#
#
# for i in range(13):
#     if count[i] != 0:
#         print(num[i], count[i])


# !!!!!!!!!!!!!!!Не выдает верное значение посмотреть обработку для 60 в конце(не ищется 60 * 60 из-за недостаточности условия
# d6 * any or  d3 * d2
# f = open('text.txt')
# x = int(f.readline())
# m = -1
# count = 0
# d6, d2, d3, d1 = 0, 0, 0, 0
# while x != 0:
#     count += 1
#     # 1) Находим значения для текущего считанного (все обработанные до
#     #     текущего значения + само значение)
#     # 2)подготавливаем данные для следующей итерации, вносим
#     #     текущее значение в обработанный набор
#     if x % 6 == 0:
#         if m < x * d1:
#             m = x * d1
#         if x > d6:
#             d6 = x
#     elif x % 3 == 0:
#         if m < x * d2:
#             m = x * d2
#         if x > d3:
#             d3 = x
#     elif x % 2 == 0:
#         if m < x * d3:
#             m = x * d3
#         if x > d2:
#             d2 = x
#     else:
#         if m < d6 * x:
#             m = x * d6
#         if x > d1:
#             d1 = x
#     x = int(f.readline())
# control = int(f.readline())
# print(count)
# print(control)
# print(m)
# if m == control:
#     print('ok')
# else:
#     print('not ok')


# f = open('text.txt')
# n = int(f.readline())
# m_ar = [30001, 30001]
# m = 60001
# for i in range(n):
#     x = int(f.readline())
#     ind = x % 2
#     if m_ar[ind] != 30001 and x + m_ar[ind] < m:
#         m = x + m_ar[ind]
#     if x < m_ar[ind]:
#         m_ar[ind] = x
# if m == 60001:
#     print(m_ar[0]+m_ar[1])
# else:
#     print(m)

# f = open('text.txt')
# n = int(f.readline())
# t = int(f.readline())
# A = 0; B = t
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     A = A + a
#     B = min(B + b, A + t)
# print(B)
#
# f = open('text.txt')
# n = int(f.readline())
# digits = [0] * 10
# for i in range(n):
#     x = int(f.readline())
#     while x > 9:
#         x = x // 10
#     digits[x] += 1
#
# min_ind = 0
# for i in range(1, 10):
#     if digits[i] > 0 and (min_ind == 0 or digits[i] < digits[min_ind]):
#         min_ind = i
#
# min_value = 1001
# for i in range(1, 10):
#     if digits[i] > 0 and min_value > digits[i]:
#         min_value = digits[i]
# print(min_ind)


# Задача № 1
# f = open('./27/27-7b.txt')
# n = int(f.readline())
# max_p = -1
# d1, d7 = 0, 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 7 == 0 and x % 49 != 0:
#         if d1 != 0 and d1 * x > max_p:
#             max_p = d1 * x
#         if d7 < x:
#             d7 = x
#     if x % 49 != 0 and x % 7 != 0:
#         if d7 != 0 and d7 * x > max_p:
#             max_p = d7 * x
#         if d1 < x:
#             d1 = x
#
#
# print(abs(max_p))


# Задача №2
# f = open('./27/27-2a.txt')
# n = int(f.readline())
# d = [10001, 10001, 10001]
# max_s = 0
# for i in range(n):
#     a, b = map(int, f.readline().split())
#     if a > b:
#         a, b = b, a
#     max_s += b
#     if a != b and b - a < d[(b - a) % 3]:
#         d[(b - a) % 3] = b - a
#
# print(max_s)
# if max_s % 3 != 0:
#     max_s -= d[max_s % 3]
# print(max_s)


# Задача №3
# f = open('text.txt')
# n = int(f.readline())
# max_p = 0
# d1, d2, d13 = 0, 0, 0
# for i in range(n):
#     x = int(f.readline())
#     if x % 2 == 0 and x % 13 != 0:
#         if max(d1 * x, x * d2) > max_p:
#             max_p = max(d1 * x, d2 * x)
#         if x > d2:
#             d2 = x
#     elif x % 13 == 0 and x % 2 != 0:
#         if max(d1 * x, d13 * x) > max_p:
#             max_p = max(d1 * x, d13 * x)
#         if x > d13:
#             d13 = x
#     else:
#         if x % 13 != 0 and x % 2 != 0:
#             if max(x * d1, x * d2, x * d13) > max_p:
#                 max_p = max(x * d1, x * d2, x * d13)
#             if x > d1:
#                 d1 = x
#
# cntrl = int(f.readline())
# print(max_p)
# if max_p == cntrl:
#     print("YES")
# else:
#     print("NO")

