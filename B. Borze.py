a = list(input().strip())
result = ""
i = 0

while i < len(a):
    if a[i] == '.':
        result += '0'
        i += 1
    elif a[i] == '-':
        if a[i + 1] == '.':
            result += '1'
        else:
            result += '2'
        i =i+ 2

print(result)
