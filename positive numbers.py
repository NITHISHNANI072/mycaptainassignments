#list 1
n= int(input("enter the number of items in the list 1:"))
list=[]
j=0
for i in range(0,n):
    m=input()
    list.append(m)
print(list)
for x in list:
    if x>="0":
        continue
    else:
        list.remove(x) 
print(list)





#list 2
a= int(input("enter the number of items in the list 2:"))
list1=[]
for i in range(0,a):
    h=input()
    list1.append(h)
print(list1)
for x in list1:
    if x>="0":
        continue
    else:
        list1.remove(x) 
print(list1)
