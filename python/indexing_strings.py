#indexing ++> how to access individual items iside a sequence__like string, tuple and list
#Python uses 0-indexed positions, meaning the very first item is always at index 0.



#1. Positive Indexing (Left to Right)
#Positive indexing starts at 0 from the beginning of the sequence and goes up.
str = "Nimra Fatima"
a = str[6] #want to access element at position 6
print(a)


#2. Negative Indexing (Right to Left)
#Negative indexing starts at -1 from the very end of the sequence and moves backward.
# This is useful when you want to get the last items without knowing the total length.
str = "Nimra Fatima"
a = str[-1]#what it does it took the whole length of the string and then minus 1 from it as
#... as the indexing starts from 0 in the python in this way it gives u the last 
#...element of the string
print(a)





#The Underlying Math
#Python actually converts negative indexes into positive ones behind the scenes using a
#simple formula:
#Index = Length + Negative Index
#If you have the 6-character string "PYTHON" (length = 6):
#To get the last item: 6 + (-1) = 5 (which is index 5, or 'N').
#If you used -0: 6 + (-0) = 6 (index 6 is out of bounds and doesn't exist)







#Important Rules to Remember
#IndexError: If you try to access an index that
#...doesn't exist (e.g., text[18]), Python will throw an IndexError: string index out of range.

#Immutability: Strings and tuples are immutable. You can read a character using indexing,
#...but you cannot change it directly (e.g., text[0] = "X" will cause a TypeError).
#... Lists, however, are mutable, so my_list[0] = "X" works perfectly.