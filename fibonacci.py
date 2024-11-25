limit=int(input("Enter a limit: "))
a,b=0,1
list=[a,b]
count=2
# print(a)
# print(b)
while count<limit:
    c=a+b
    a=b
    b=c
    list.append(c)
    count+=1
print(list)


