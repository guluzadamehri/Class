n = int(input())
elek = [True] * (n + 1)
for p in range(2, n + 1):
    if elek[p]:
        print(p, end=" ")
        for i in range(p * p, n + 1, p):
            elek[i] = False
