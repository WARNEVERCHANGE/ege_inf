f = open('text.txt')

n = int(f.readline())


min_sum = 0
diff = 0
for i in range(n):
    p1, p2 = map(int, f.readline().split())
    if p1 > p2:
        p1, p2 = p2, p1
    if (p2 - p1) % 3 != 0 and (p2 - p1) < diff:
        diff = (p2 - p1)
    min_sum += p1

if min_sum % 3 != 0:
    print(min_sum)
else:
    print(min_sum + diff)

