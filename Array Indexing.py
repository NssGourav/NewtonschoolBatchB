def Function(N, A):
    total_sum = sum(A)
    left_sum = 0
    count = 0
    for i in range(N):
        right_sum = total_sum - left_sum - A[i]
        if left_sum >= right_sum:
            count += 1
        left_sum += A[i]

    return count

N = int(input())
A = list(map(int, input().split()))
print(Function(N, A))
