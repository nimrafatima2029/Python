marks = int(input("Enter your marks to check your grade: "))
if(marks >= 90):
    print("congratulations! your grade is A🎉")
elif(marks >= 80 and marks < 90):
    print("great job! your grade is B ")
elif(marks >= 50 and marks < 80):
    print("keep it up! your grade is C")

else:
    print("you have failed😥")



    #now next practice question
light = input("enter the colour of light traffic signal is displaying now: ")
if(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
elif(light == "red"):
    print("stop")
else:
    print("traffic light is out of order")    
