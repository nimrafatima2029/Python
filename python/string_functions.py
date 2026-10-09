my_text = "i am Nimra Fatima and i am studying python from youtube"

#********function1: my_text.endswith(" ")
print(my_text.endswith("tube"))#returns true bcz my string ends with tube
print(my_text.endswith("er"))#returns false bcz my string does not ends with er, it ends with tube instead

#******function2: my_text.capitalize()
print(my_text.capitalize())#will print the first letter of the string in capitalized form
#this fuction => my_text.capitalize() does not mutate the original string but creates another string and make it capitalize
#we can confirm this by just printing the string, it will give us uncapitalized original string
print(my_text)
#now to do changes in the actual string we will store the changes made by the function in our parent variable
my_text = my_text.capitalize()
print(my_text)#now changes occur in the original string as well

#********function3: my_text.replace("old" , "new") 
print(my_text.replace("o" , "a"))
my_text = my_text.replace("I am nimra fatima", "I am student of Artificial Intelligence")#if i write the first letters of my name in
#capitalized form then it will not replace the old with new bcz of the use of capitalize function which tends to 
#capitalize the first letter of the sentence while keeps all the letters in lower case. this unexpected result is 
#due to the reason that we have mutate the original string by using code in the line 13 which says what changes this function 
#brings will be considered as the original string so it capitalize the first letter and made rest in lower caset of the letter
#so "i am nimra fatima" is my old sentence and will replace this with new one
print(my_text)

#*******function4: str1.find("")
str1 = "my name is nimra"
print(str1.find("n")) #it will print the index of first occurrer
print(str1.find("nimra"))#my word start from index 11
print(str1.find("N"))#as capital N does not exist it will return -1. anything that does not exist in that case it will return -1



#function5: str2.count("")
str2 = "i am nimra fatima studing ai in university of malakand, hello nimra! "
print(str2.count("i"))
print(str2.count("nimra"))