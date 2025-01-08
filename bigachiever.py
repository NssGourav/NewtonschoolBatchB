def bigachiever(t):
    for _ in range(t):
        Number0fstudents = int(input())
        scores = list(map(int, input().split()))
        result = []

        for i in range(Number0fstudents):
            happy = 1  
            
            for j in range(i):
                if scores[j] > scores[i]:
                    happy = 0  
                    break
            result.append(happy)
        print(" ".join(map(str, result)))

t = int(input())
bigachiever(t)
