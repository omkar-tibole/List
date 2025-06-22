List=[1,2,3,4,5,6,7]



# List slicing
print("List slicing: ")
print(List[1:3])



# insert is used to insert an element at a specific index.
List.insert(1,3)
print("\ninserting data at index 1: ")
print(List)


# extend is used to extend the list with another list.
List.extend([1,2,3,4])
print("\nextending the list with another list: ")
print(List)



# append is used to add an element at the end of the list.
List.append(3)
print("\nappending data at the end of the list: ")
print(List)



#  pop is used to remove the last element of the list.
List.pop(3)
print("\npopping data at index 3: ")
print(List)


# append is used to add an element at the end of the list.
List.append(3)
print("\nappending data at the end of the list: ")
print(List)



# count is used to count the number of occurrences of an element in the list.
print("\ncounting the number of occurrences of 3 in the list: ")
print(List.count(3))



# index is used to find the index of the first occurrence of an element in the list.
print("\nfinding the index of the first occurrence of 5 in the list: ")
print(List.index(5))



# sort is used to sort the list in ascending order.
List.sort()
print("\nsorting the list in ascending order: ")
print(List)



# reverse is used to reverse the order of the elements in the list.
List.reverse()
print("\nreversing the order of the elements in the list: ")
print(List)



# del is used to delete an element at a specific index.
del List[2]
print("\ndeleting the element at index 2: ")
print(List)



# copy is used to create a shallow copy of the list.
List_copy = List.copy()
print("\ncreating a shallow copy of the list: ")
print(List_copy)



# clear is used to remove all elements from the list.
List.clear()
print("\nclearing the list: ")
print(List)




List=[1,2,4,3,4]
# List is a mutable data type in Python, meaning it can be modified after creation.
print(type(List))
print(List)
# Modifying elements in the list
List[0]=33

