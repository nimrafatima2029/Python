#1: these are three ways in which you can write the strings 
str1 = "my brother is good, he is so handsome, he is so talented he is studying for his paper"
str2 = 'it is 7 october 2026'
str3 = """tomorrow is his islamiat paper"""
print(str1, str2, str3)

#2: escape sequences => \n, \t
# \n --> used to move to next line
# \t --> used to give a space exactly of 1 tab

str1 = "my brother is good, he is so handsome,\n he is so talented he is studying for his paper"
str2 = "my brother is good, he is so handsome,\t he is so talented he is studying for his paper"
print(str1, str2)


#3: concatenation
str1 = "Nimra"
str2 = "-Fatima"

final_str = str1 + str2
print(final_str)



#4: length of the string ==> len(str)
str1 = "Nimra"
str2 = "Fatima"
length_str1 = len(str1)
length_str2 = len(str2)
print(length_str1)
print(length_str2)


#5: in measuring the length of the string even the empty space is calculated 
#while measuring the length everything is calculated e.g special characters, numbers etc
# *** \n and \t *** are considered as single character in measuring length
str1 = "Nimra"
str2 = "Fatima"
final_str = str1 + " " + str2 #it will calculate the empty space as well while measuring length 
print(len(final_str))
print(final_str)

