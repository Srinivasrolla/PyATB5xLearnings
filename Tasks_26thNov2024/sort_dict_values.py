my_dict = {"a": 3, "b": 1, "c": 2, "d":1}
value=[]
d={}
for i in my_dict.values():
    value.append(i)
value.sort()
for i in value:
    for j,k in my_dict.items():
        if (k==i) and (j not in d):
            d[j]=i
print(d)