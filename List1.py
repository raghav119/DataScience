list1 = [10,20,30,40]
print(list1)
type(list1)
list1[0]
list1[-2]
list1[0:2]
list1[:3]
list1[0::-1]


#create a list with elements in the range of 1 to 10 with step size of 1 
list2 = range(1,10,1) 
type(list2)
print (list2) 
for x in list2:
    print (x)
    
    list1[0] = 100
         
list3 = []
list3.append(1)
list3.append(2)
list3.append(3)
list3.insert(8,6)   
print(list3)    

len(list3)    

list3.sort()
print(list3)
list3.sort(reverse=True)
for x in list3:
    print (x)



