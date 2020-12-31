def izi(n):
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
    return count == 0


# st = 11275
# fn = 16328
# count = 5
# for i in range(st, fn + 1):
#     if int(int(i ** 0.5) ** 0.5) ** 4 == i and izi(int(int(i ** 0.5) ** 0.5)):
#         d = [0] * count
#         d[0] = 1
#         d[1] = int(int(i ** 0.5) ** 0.5)
#         d[2] = int(i ** 0.5)
#         d[3] = d[1] * d[2]
#         d[4] = i
#         print(*d)

# st = 248015
# fn = 251575
# num = 0
# for i in range(st, fn + 1):
#     count = 1
#     if i % 2 == 1:
#         count += 1
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             if j % 2 == 1:
#                 count += 1
#             if (i // j) % 2 == 1:
#                 count += 1
#     if int(i ** 0.5) ** 2 == i:
#         count -= 1
#     if count % 2 == 1:
#         num += 1
#         print(num, i, count, int(i ** 0.5))

# num = 0
# st = 2943444
# fn =2943529
# for i in range(st, fn+1):
#     count = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         num += 1
#         print(num, i)


# st = 33333
# fn = 55555
# mx = 33332
# mn = 55556
# counter = 0
# for i in range(st, fn+1):
#     if (i // 10000) % 2 != 0 and ((i % 10000) // 1000 ) % 2 != 0 and ((i % 1000) // 100) % 2 == 0 and ((i % 100) // 10) % 2 != 0 and (i % 10 ) % 2 == 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0:
#         counter += 1
#         if i > mx:
#             mx = i
#         if i < mn:
#             mn = i

# print(counter, mx - mn)

st = 4986
fn = 32599
s = 0
for i in range(st, fn + 1):
    count = 0
    if int(i ** 0.5) ** 2 != i:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
    if count == 1:
        s += i

print(s)


