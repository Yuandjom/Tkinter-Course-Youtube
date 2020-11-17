from tkinter import * #remember dont save file as tkinter 

#first thing to create is the root widget , Must go first
root = Tk()
def myClick(): #command no need () when calling the function in command 
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()
#two step . 1st create the button widge , next shove in screen
myButton = Button(root, text='Click Me!', padx=50 , pady=50 , command = myClick , fg= "blue" , bg = "white") #state= DISABLED
#Shoving it onto the screen 
myButton.pack() 
#continuous display 
root.mainloop() 