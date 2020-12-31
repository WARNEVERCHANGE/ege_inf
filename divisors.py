def izi(n):
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
    return count == 0


st = 11275
fn = 16328
count = 5
for i in range(st, fn + 1):
    d = [0] * (count + 1)
    d[0] = 1
    d[count] = i
    c = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if c < (count + 1) // 2:
                d[c] = j
                d[count - c] = i // j
            c += 1 

    if c == (count + 1) // 2 and d[2] == d[3]:
        print(*d)