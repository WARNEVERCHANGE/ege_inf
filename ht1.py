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



a = [10, 11, 6, 4, 22, 8, 13, 8, 9, 11]

min_sum = int(input())

a.sort()
s = 0
i = len(a) - 1
while s + a[i] <= min_sum:
    s += a[i]
    i -= 1

print(len(a) - i - 1)