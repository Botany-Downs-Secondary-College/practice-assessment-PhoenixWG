
from Tkinter import *

root = Tk()
root.title("Screen1")
root.geometry("400x300+850+850")

label1 = Label(root, bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
               text = "Welcome to Math Quiz", font=("Times", "24", "bold italic"))
label1.pack() #pack method packs the widget into GUI

label2 = Label(root, text = "Name", width = 20, font=("Times", "14", "bold italic"))
label2.pack()

textbox1 = Entry(root, width = 20)
textbox1.pack()

label3 = Label(root, text= "Age", width = 20, font=("Times", "14", "bold italic"))
label3.pack()

textbox2 = Entry(root, width = 20)
textbox2.pack()

rb1 = Radiobutton(root, width = 20, value = 1, text = "Easy", anchor = W)
rb1.pack()
rb2 = Radiobutton(root, width = 20, value = 2, text = "Medium", anchor = W)
rb2.pack() 
rb3 = Radiobutton(root, width = 20, value = 3, text= "Hard", anchor = W)
rb3.pack()

button1 = Button(root, text = "Next")
button1.pack()

root.mainloop()