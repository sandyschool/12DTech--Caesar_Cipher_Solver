#Asking for the title, make sure it can't be blank.

title= ""

title = input  ("Please enter the title of the book:")
while title== "":
    print ("")
    print("Sorry your response cannot be blank")
    print ("")
    title = input  ("Please enter the title of the book:")
print("")
print ("You will be reviewing", title )

#Ask for author's name- if response is blank set it to 'Anonymous' 
author_name =""
