from Tkinter import *

def Screen1():
    global frame1
    global frame2
    
    frame2.grid_remove()
    frame1 = LabelFrame(root, height = "450", width = "400", bg = "light blue")
    frame1.grid(row = 0, column = 0)
    
    TitleLabel = Label(frame1, bg = "black", fg = "white", width = 32, padx = 30, pady = 20, text = "Welcome to Math Quiz", font=("Times", "14", "bold italic"))
    TitleLabel.grid(columnspan = 2) 
    
    button1 = Button(frame1, text = "Next", anchor = W, command = Screen2)
    button1.grid(columnspan = 2)
    
def Screen2():
    global frame1
    global frame2
    frame1.grid_remove()
    
    frame2 = LabelFrame(root, height = "450", width = "400", bg = "red")
    frame2.grid(row = 0, column = 1)
    
    questions = Label(frame2, bg = "black", fg = "white", width = 32, padx = 30, pady= 20,
                      text = "Answer the Questions", font=("Times", "14", "bold italic"))
    questions.grid(columnspan = 2)
    
    home = Button(frame2, text = "Home", anchor = W, command = Screen1)
    home.grid(row = 1, column = 0)
    
    home = Button(frame2, text = "Report", anchor = W, command = Screen1)
    home.grid(row = 1, column = 1)
    
root = Tk()
root.title("Frames")
root.geometry("600x300+850+0")
frame1 = Frame(root)
frame2 = Frame(root)
    
Screen2()
Screen1() 
root.mainloop()





