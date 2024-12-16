t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != a[1] and a[0] != a[2]:
        freqmax = 1
    elif a[1] != a[0] and a[1] != a[2]:
        freqmax = 2
    else:
        for i in range(2, n):
            if a[i] != a[0]:
                freqmax = i + 1
                break

    print(freqmax)
