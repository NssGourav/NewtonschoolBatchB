def functionn(a):
    results = []
    for i in range(a):
        k = input().strip()  
        if k.lower() == "yes":  
            results.append("YES")
        else:
            results.append("NO")
    return ('\n'.join(results))
 
a = int(input())
print(functionn(a))
