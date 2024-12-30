
n = int(input())
numbers = list(map(int, input().split()))
even = []
odd = []
index = 1  
for num in numbers:
    if num % 2 == 0:
        even.append(index)
    else:
        odd.append(index)
    index += 1 
if len(even) == 1:
    print(even[0])
else:
    print(odd[0])
