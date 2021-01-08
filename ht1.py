# a = [15, 1, 64, 23, 10, 55, 3, 10, 20, 32]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = len(a)
# for i in range(n - 1):
#     for j in range(n-i-1):
#         if b[j] % 2 == 0 and b[j+1] % 2 == 1:
#             a[j], a[j+1] = a[j+1], a[j]
#             b[j], b[j+1] = b[j+1], b[j]
#         elif (b[j] % 2 == b[j+1] % 2) and (a[j] > a[j+1]):
#             a[j], a[j+1] = a[j+1], a[j]
#             b[j], b[j+1] = b[j+1], b[j]
# print(a)
# print(b)


#
#a = [10, 11, 6, 4, 22, 8, 13, 8, 9, 11]
#
#min_sum = int(input())
#
#a.sort()
#s = 0
#i = len(a) - 1
#
#
#while i >= 0 and s + a[i] <= min_sum:
#    s += a[i]
#    i -= 1
#
#print(len(a) - i)
#
#if s + a[i] <= min_sum or i == -1 and s < min_sum:
#    print('ne hvataet')
#
#j = 0
#while j < len(a)  and s + a[j] < min_sum:
#    j += 1
#
#
#
#if j == len(a):
#    print(a[0])
#else:
#    print(a[j])



# f = open('./26/26-10.txt')

# size, n = map(int, f.readline().split())
# a = [0] * n


# for i in range(n):
#     a[i] = int(f.readline())

# a.sort()
# s = 0
# last = 0
# for i in range(n):
#     if s + a[i] <= size:
#         s += a[i]
#         last = i
# print(last + 1)

# s -= a[last]
# for i in range(last + 1, n):
#     if s + a[i] <= size:
#         last = i
# print(a[last])



# f = open('./26/26-k3.txt')
# n, k, m = map(int, f.readline().split())
# a = [0] * n

# for i in range(n):
#     a[i] = int(f.readline())

# a.sort()

# print(a[len(a) - k], a[len(a)-m-k])

# f = open('./27/27-7a.txt')
# n = int(f.readline())

# m_prod = 0
# mk7 = 0
# mn7 = 0

# for i in range(n):
#     x = int(f.readline())
#     # обработка введенного значения
#     # если х - кратен 7 и не кратен 49 -> max(m_prod, mn7 * x)
#     # если х - не кратен 7 -> max(m_prod, mk7 * x)
#     if x % 7 == 0 and x % 49!= 0:
#         if m_prod < mn7 * x:
#             m_prod = mn7 * x
#         if mk7 < x:
#             mk7 = x
#     if x % 7 != 0:
#         if m_prod < mk7 * x:
#             m_prod = mk7 * x
#         if mn7 < x:
#             mn7 = x
#         # подготовка следующей итерации
#         # узнать есть ли новый максимум для кратного 7
#         # узнать, есть ли новый максимум для некратного 7

# print(m_prod)



# f = open('./27/27-2a.txt')

# n = int(f.readline())
# m_s = 0
# a = [10001] * 3
# a[0] = 0

# for i in range(n):
#     p1, p2 = map(int, f.readline().split())
#     if p1 > p2: 
#         p1, p2 = p2, p1
#     m_s += p2
#     ta = a.copy()
#     r = (p2 - p1) % 3
#     if r > 0:
#         for j in range(3):
#             if a[j] + (p2 - p1) < ta[(j + r) % 3]:
#                 ta[(j + r) % 3] = a[j] + (p2 - p1)
#         a = ta.copy()
# if m_s % 3 != 0:
#     m_s -= a[m_s % 3]
#     r = (p2 - p1) % 3


# print(m_s)



f = open('./27/27-7a.txt')

k2 = -1; k13 = -1; nk1 = -1; nk2 = -1;

n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    if x % 26 != 0:
        if x % 2 == 0 and x > k2:
            k2 = x
        elif x % 13 == 0 and x > k13:
            k13 = x
        else:
            if x > nk:
                nk = x  
print(max(k2*nk, k13*nk))