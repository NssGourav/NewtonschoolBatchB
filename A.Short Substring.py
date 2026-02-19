t = int(input())
for i in range(t):
    b = ((input().strip(" ")))
    s=b[0]
    for i in range(1,len(b),2):
        s+=b[i]
    print(s)
