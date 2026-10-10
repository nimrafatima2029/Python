#method1: adding elements

#• list_name.append(element): Adds a single element to the very end of the list.

marks = [96, 93, 47, 80, 87]
marks.append(85)
print(marks)

#list_name.insert(index, element): Inserts a single element at a specified position.

marks.insert(3, 100)
print(marks)

#method2: Removing Elements

#• pop(index=-1): Removes and returns the item at the given index (default last).
b = marks.pop(2)
print(marks)
print(b)#prints the item that is removed

#• remove(element): Removes the first matching value, raising a ValueError if absent.
marks.remove(96)
print(marks)

#clear(): Empties the list completely.
marks.clear()
print(marks)#will print empty list

alphabets = ['a', 'a', 'v', 'y', 'h', 'n','n', 'c', 'c','c']
print(alphabets)

#method3: 🔍 Searching & Counting
#• index(element): Returns the first index of a value, raising a ValueError if not found.
a = alphabets.index("h")
print(a)#as we have used claer fuction above it so that is why it is printig"ValueError: 80 is not in list" because as 
#clear function runs it leaves the list empty therefore we have no value in the list

#count(element): Counts occurrences of a value.
v = alphabets.count("a")
print(v)

#🔄 Ordering & Reversing
d = alphabets.sort()#The sort() method sorts the original list in ascending order but returns None
#Therefore, assigning it to d makes d equal to None, and print(d) displays None.
print(alphabets)#Prints the sorted list

e = alphabets.reverse()
print(alphabets)


h = alphabets.sort(reverse = True)
print(alphabets)

#📋 Copying
f = alphabets.copy()
print(f)

# alphabets.reverse()	        |Reverses the current order of elements.
# alphabets.sort()	            |Sorts elements in ascending order.
# alphabets.sort(reverse=True)	|Sorts elements in descending order.

#One more important point: Both reverse() and sort() modify the original list and return None.
#Therefore, e and h will also contain None if you print them.


