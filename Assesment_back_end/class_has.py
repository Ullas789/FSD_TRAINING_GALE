def hasmap(dic,size):
    h_v=[[] for i in range(size)] 
    for key,value in dic.items():
        key=int(key)
        # print(f"{key}: {value}")
        h=key%size
        # print(h)
        h_v[h].append(value)
    print(f"dic{dic}")
    print(f"hash:{h_v}")


size=int(input("size: "))

n = int(input("N: "))
dic= {input("Key: "): input("Value: ") for _ in range(n)}
hasmap(dic,size)