size=int(input("size: "))
# print(size)
# dic={
#     0:"ab", #0
#     5:"cd", #0
#     7:"ef", #2
#     9:"gh", #4
#     14:"ij" #4
# }
n = int(input("N: "))
dic= {input("Key: "): input("Value: ") for _ in range(n)}

print(dic)

h_v=[[] for i in range(size)] 
# print(h_v)
for key,value in dic.items():
    key=int(key)
    # print(f"{key}: {value}")
    h=key%size
    # print(h)
    h_v[h].append(value)

print(h_v)








