list1=[1,2,2,3,4,4,5]
print(list1)
for i in range(len(list1)-1, -1, -1):#range(start, stop, step)
    if list1[i] in list1[0:i]:
        list1.remove(list1[i])
print(list1)