# f = open('./24data/24.txt')
# a = list(f.read().strip())
# count = 0
# max_count = 0
# for i in range(1, len(a)):
#     if a[i-1] != a[i]:
#         count += 1
#     else:
#         if count + 1 > max_count:
#             max_count = count + 1
#         count = 0
# print(max_count)

# task 1
f = open('./24data/k7-20.txt')
count = 0
max_len = 0
a = list(f.read().strip())
print(a)
for i in range(len(a)):
    if a[i] == 'C':
        count += 1
    else:
        if count > max_len:
            max_len = count
        count = 0
print(count)

# task 2