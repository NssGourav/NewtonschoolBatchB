#F. Divisible Pairs
def pairs():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    dict = {}
    result = 0
    
    for i in range(n):
        t = a[i] % x
        o = a[i] % y
        
        rem1 = (x - t) % x
        rem2 = o
        
        if (rem1, rem2) in dict:
            result += dict[(rem1, rem2)]
        
        if (t, o) in dict:
            dict[(t, o)] += 1
        else:
            dict[(t, o)] = 1
    
    print(result)
 
t = int(input())
for _ in range(t):
    pairs()
