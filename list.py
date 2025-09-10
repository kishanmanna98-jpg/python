
a=[]
n=int(input("enter a number"))
for i in range(0,n):
    m=int(input("enter a element"))
    a.append(m)
print(a)

k=[1,2,3]
a.extend(k)
print(a)

k.insert(0,2)
print(k)
