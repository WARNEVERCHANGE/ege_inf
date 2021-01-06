# not effective
# f = open('text.txt')
# n = int(f.readline())
# a = [0] * 10000

# for i in range(n):
#     a[i] = int(f.readline())

# max_sum = 0

# for i in range(n - 7):
#     for j in range(i + 7, n):
#         if a[i] + a[j] > max_sum:
#             max_sum = a[i] + a[j]
# print(max_sum)




# more effective algorithm
# f = open("text.txt")
# n = int(f.readline())
# a = [0] * 10000

# max_sum = 0

# for i in range(7):
#     a[i] = int(f.readline())


# for i in range(7, n):
#     a[i] = int(f.readline())
#     if a[i] + max(a[0:i - 6]) > max_sum:
#         max_sum = a[i] + max(a[0: i - 6])

# print(max_sum)



# Очередь !!!!!
# f = open("text.txt")
# a = [0] * 7



# n = int(f.readline())
# for i in range(7):
#     a[i] = int(f.readline())

# max_sum = 0
# max_i = 0
# head = 0

# for i in range(7, n):
#     head = i % 7 #(3)
#     if max_i < a[head]: #i % 7 
#         max_i = a[head]
    
#     x = int(f.readline())

#     if max_i + x > max_sum:
#         max_sum = max_i + x
#     a[head] = x 
#     # head += 1 head == 7 : head = 0 (1)
#     # head = (head + 1) % 7 (2)

# print(max_sum)


# Мое кривое решение задачи
# f = open('text.txt')

# n = int(f.readline())

# a = [0] * 4

# counter = 0
# for i in range(4):
#     a[i] = int(f.readline())

# for i in range(4, n):
#     x = int(f.readline())
#     for j in range(4):
#         if (x * a[j]) % 13 == 0 and (x + a[j]) % 2 == 1:
#             counter += 1
#     for j in range(3):
#         a[j] = a[j+1]
#     a[3] = x
# print(counter)


# Аналогичное решение
# f = open('text.txt')

# a = [0] * 4

# n = int(f.readline())

# for i in range(4):
#     a[i]  = int(f.readline())

# count = 0

# for i in range(4, n):
#     x = int(f.readline())
#     for j in range(4):
#         if (a[j] * x) % 13 == 0 and (a[j] + x ) % 2 == 1: 
#             count += 1
    
#     a[i % 4] = x
#     # for j in range(3):
#     #     a[j] = a[j+1]
#     # a[3] = x

# print(count)

# f = open('text.txt')
# n = int(f.readline())
# a = [0] * 6
# for i in range(6):
#     a[i] = int(f.readline())

# min_nch = 1001
# min_m = 1002001

# for i in range(6, n):
#     if a[i % 6] % 2 == 1 and a[i % 6] < min_nch:
#         min_nch = a[i % 6]
#     x = int(f.readline())
#     if x % 2 == 1 and x * min_nch < min_m and min_nch != 1001:
#         min_m = x * min_nch
#     a[i % 6] = x

# if min_m != 1002001:
#     print(min_m)
# else:
#     print(-1)


# task 1 not effective
# f = open('text.txt')

# n = int(f.readline())

# a = []

# for i in range(4):
#     a.append(int(f.readline()))
# counter = 0
# for i in range(4, n):
#     x = int(f.readline())
#     for j in range(i - 3):
#         if (a[j] * x ) % 10 == 1:
#             counter += 1
#     a.append(x)

# print(counter)

# task 2
f = open('text.txt')

n = int(f.readline())

d3 = 10001
nd3 = 10001



#task 3 недорешенная задача
# f = open('text.txt')

# n = int(f.readline())

# a = [0] * 7

# for i in range(7):
#     a[i] = int(f.readline())
# count = 0
# for i in range(7, n):
#     x = int(f.readline())
#     for j in range(7):
#         if (x + a[j]) % 8 != 0:
#             count += 1
#     for j in range(6):
#         a[j] = a[j+1]
#     a[6] = x

# print(count) 


# task 4
d = [0, 0, 0]
f = open('text.txt')

n = int(f.readline())

a = [0] * 5

for i in range(5):
    a[i] = int(f.readline())

for i in range(5, n):
    if d[a[0] % 3] != 0 and d[a[0] % 3]