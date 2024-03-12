#Create a banner at the start
def bookreviewer ():
    print ("*************************************************************") 
    print ("*********Welcome to Charlie's Handy Book Reviews!***********")
    print ("************************************************************")

#Checks that user enters something for required text (such as title)
#From the video resource:
    
#Functions go here
def not_blank (question):

    error ="Sorry, responses to this question can't be blank"    

    valid= False
    while not valid:
        response = input (question)

        if response !="":
            return response
        else:
            print (error)
            print("")


#Main Routine goes here
title = not_blank("Please enter the title of the book:")
print ("You will be reviewing {}". format(title))





