# def izi(n):
#     count = 0
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             count += 1
#     return count == 0


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

# st = 4986
# fn = 32599
# s = 0
# for i in range(st, fn + 1):
#     count = 0
#     if int(i ** 0.5) ** 2 != i:
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 count += 1
#     if count == 1:
#         s += i

# print(s)


# Доделать(поиск чисел которые являются произведением двух простых, вывести их количество и число близкое к среднему значению)
# st = 412567
# fn = 473265
# rez = []
# for i in range(st, fn + 1):
#     count = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0 and izi(j) and izi(i // j):
#             count += 1
#     if count == 1:
#         rez.append(i)
    
# rez.sort()
# sr_znach = sum(rez) / len(rez)
# print(len(rez))



# task 1
# st = 25317
# fn = 51237
# for i in range(st, fn+1):
#     count = 0
#     if int(i ** 0.5) ** 2 != i:
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 count += 1
#                 dv = j
#     if count == 3:
#         print(i, dv)


# task 2 : ans: 388 318449

# def izi(x):
#     count = 0
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             count += 1
#     return count == 0


# st = 318216
# fn = 369453
# d1 = 0
# d2 = 0
# count = 0
# mn = 369454
# for i in range(st, fn + 1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             d1 = d2 
#             d2 = j
#             if d1 != 0 and d2 != 0 and int(i / (d1 * d2)) == i / (d1 * d2) \
#                  and d1 % 10 == d2 % 10 == int(i / (d1 * d2)) % 10 \
#                      and izi(d1) and izi(d2) and izi(int(i / (d1 * d2))):
#                 count += 1
#                 if i < mn:
#                     mn = i
# print(count)
# print(mn)


# task 3: неполное решение
# st = 326359
# fn = 421986
# diff = 0
# mx_diff = 0
# d = set()
# flag = True

# for i in range(st, fn + 1):
#     temp = set()
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0 and flag:
#             diff = (i // j) - j
#             flag = False
#             temp.add(j); temp.add(i // j)
#         else:
#             if i % j == 0:
#                 temp.add(j); temp.add(i // j)

#     if diff > mx_diff:
#         mx_diff = diff
#         d = temp.copy()
#     flag = True

# print(diff)
# for i in sorted(d):
#     print(i, end = ' ')



# task 4: 101889375
# st = 2945
# fn = 18294
# res = 0
# for i in range(st, fn + 1):
#     count = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if int(j ** 0.5) ** 2 == j and i % j == 0:
#             count += 1
#     if count == 0:
#         res += i

# print(res) 

# res = 0
# for i in range(st, fn + 1):
#     res += i

# print(res)




# task 5 ans:   1 2532007
                # 4 2532083
                # 7 2532113
                # 10 2532157
# def izi(n):
#     count = 0
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             count += 1
#     return count == 0
# st = 2532000
# fn = 2532160
# num = 1
# for i in range(st, fn + 1):
#     if izi(i):
#         if num % 3 == 1:
#             print(num, i)
#         num +=1 



