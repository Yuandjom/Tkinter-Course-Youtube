from tkinter import * #remember dont save file as tkinter 

#first thing to create is the root widget , Must go first
root = Tk()

#Creating a Label Widget 
myLabel1 = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = 'My Name Is John Elder')
#Shoving it onto the screen 
myLabel1.grid(row=0 , column = 0) #doesnt resize 
myLabel2.grid(row=1 , column = 0) #relative to each other 

#continuous display 
root.mainloop() 