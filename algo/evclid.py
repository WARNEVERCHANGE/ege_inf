def evclid(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(evclid(12, 36))