
n = int(input())
arr = list(map(int, input().split()))

pre_count=[0]*n
pre_count[0]=(1 if arr[0]%5==0 else 0)

for i in range(1,n):
    pre_count[i]=pre_count[i-1] + (1 if arr[i]%5==0 else 0)

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    if l==0:
        print(pre_count[r]) 
    else:
        print(pre_count[r]-pre_count[l-1])
