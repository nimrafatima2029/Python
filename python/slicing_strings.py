#accessing part of a string
#syntax => [starting index : ending index]
#ending index is not included
str = "Nimra Fatima"
print(str[0 : 2]) #from zero index to index (2-1) printed,i minused 1 because ending index is not included
print(str[5 : 7]) #will print from index 5 i.e empty space to (7-1) i.e index 6 which is charcter 'F'
print(str[0 : 5]) #it will print the first word of the my name i.e 'Nimra'
print(str[6 : 12])#it will print the second word of the my name i.e 'Fatima'

print(str[ : 5])#the python interpretor will assume itself to start from index 0 and will print the first part of my name
print(str[6: ])#the python interpretor will assume itself to print till the end of the string and will print the second part of my name

print(str[6 : len(str)])#Python slicing has a special feature called out-of-bounds slicing =>Python stops at the string boundaries instead of crashing with an error.


#slicing ==> *negative index*
str2 = "Apple"
print(str2[-1]) #prints the final letter of the word
print(str2[-1 : -4])#It prints nothing because Python slices from left to right by default, 
#but here indexes are trying to go from right to left.Since Python defaults to a step of +1, it starts at 'e' and tries
#to move forward to the right. But there is nothing to the right of 'e' before hitting -4.

print(str2[-5 : -1])#appl
print(str2[-5 : ])#now it print whole word i.e apple

#now to print the flipped version of apple
#syntax => print(str[start : stop : step])
print(str2[-1 : -6 ])