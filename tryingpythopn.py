n = list(map(int,input().split()))
val = int(input())
M = []
#max element of list ee list lo una edho oka index ki less than or equal to avali
#so index check cheyali ante while loop chedam
index = len(n)
for I in range(0,index):
     if n[I] <= val:
          M.append(n[I])
print(max(M))