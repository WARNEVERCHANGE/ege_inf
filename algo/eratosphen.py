N = int(input())
a = [True] * (N + 2)
k = 2
while k ** 2 <= N:
    if a[k]:
        i = k ** 2
        while i <= N:
            a[i] = False
            i = i + k
    k += 1
for i in range(2, N):
    if a[i]:
        print(i)


