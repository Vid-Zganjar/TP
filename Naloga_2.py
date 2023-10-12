list1=[0,1,2,3,4,5,6,7,8,9]
list2=[9,8,7,6,5,4,3,2,1,0]

print(list1)
print(list2)
list3=[]
for i in range(0,10):
    list3.append(list1[i]+list2[i])
print(list3)
