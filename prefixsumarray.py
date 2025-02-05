# def solve(arr,target):
#     prefix_summ_map = {}
#     current_sum = 0
#     for i in range(len(arr)):
#         current_sum += arr[i]
#         if current_sum == target:
#             return(0,i)
#         if (current_sum - target) in prefix_summ_map:
#             return (prefix_summ_map[current_sum-target]+1,i)
#         prefix_summ_map[current_sum] = i
#         print(prefix_summ_map)
#     return -1
# arr = list(map(int,input().split()))
# target = int(input())
# print(solve(arr,target))

def find_pair(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return True
    return False
target = 5
arr = [1,2,3,4,4,4,4,4,6,2,1]
print(find_pair(arr,target))
