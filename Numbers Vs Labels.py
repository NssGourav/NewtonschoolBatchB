a = input().split(" ") 
k = ["NA", "n/a", "None"]
p = []
q = []
filtered_list = [item for item in a if item not in k]
for i in range(len(filtered_list)):
    if filtered_list[i].isdigit():
        p.append(filtered_list[i])
    if filtered_list[i].isalpha():
         q.append(filtered_list[i])
print(p)
print(q)
