list1 = [1,22,333,44,5,6]
#methods of list
#append, len,insert,index,remove,sort,reverse,pop,slices,extend

# print("lenght of list == > ", len(list1))
list1.append("po ")
# print("after appeanding ==> ",list1)
list1.insert(2,"priti")
# print("aftr inserting at index 2 ==> ",list1)
#.index will return place where passed charater is placed in list
# print(list1.index("priti"))
list1.remove("priti")
# print(list1)
list1.remove("po ")
# print("after removing po from list == > ",list1)
list1.pop()
# print("list after popping last charater ==> ",list1)
list1.sort()
# print("List after sorting ==> " ,list1)
# print("slicing the list ==> ",list1[2:4])
list2 = ["bhavika","pratap"]
list2.extend(list1)
print(list2)