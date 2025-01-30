TARGET = "ADVITIYA"

def min_steps(s):
    steps = 0
    for i in range(8):
        current = ord(s[i]) - ord('A')
        target = ord(TARGET[i]) - ord('A')
        diff = (target - current + 26) % 26
        steps += diff
    return steps

T = int(input())
for _ in range(T):
    S = input().strip()
    print(min_steps(S))
