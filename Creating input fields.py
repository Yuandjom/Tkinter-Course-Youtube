from tkinter import * #remember dont save file as tkinter 

#first thing to create is the root widget , Must go first
root = Tk()

e = Entry(root, width = 50) #allow you to type stiff , got borderwidth also
e.pack()
e.insert(0, "Enter your name: ") #add default text in the text box
def myClick(): #command no need () when calling the function in command 
    hello = "Hello " + e.get() #e.get() get the 
    myLabel = Label(root, text=hello)
    myLabel.pack()
#two step . 1st create the button widge , next shove in screen
myButton = Button(root, text='Enter Your Name!' , command = myClick , fg= "blue" , bg = "white") #state= DISABLED
#Shoving it onto the screen 
myButton.pack() 
#continuous display 
root.mainloop() 