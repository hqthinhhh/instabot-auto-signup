list = []
with open("girlname.txt","r") as f:
    
    for i in f.readlines():
        for y in i.split():
            list.append(y)
    print(list)