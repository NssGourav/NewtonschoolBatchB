def water():
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = input().strip()
        result = 0
        i = 0
        while i < n:
            if k[i] == '.':
                count = 0
                while i < n and k[i] == '.':
                    count += 1
                    i += 1
                if count > 2:
                    result = 2
                    break
                else:
                    result += count
            else:
                i += 1
        print(result)
 
water()
