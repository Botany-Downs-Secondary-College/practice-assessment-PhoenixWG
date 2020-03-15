from Tkinter import *

from random import *


def next_problem():
    
    
    global x
    global y
    
    x = randrange(20)
    y = randrange(20)    
    
    problem_text = str(x) + "  +  " + str(y) + "  =  "
    problem_label.configure(text = problem_text)
    answer_entry.focus()
    
def check_answer():
    
    
    answer = x + y
    
    try:
        
        user_answer = int(answer_entry.get())
        
        if user_answer == answer:
            
            feedback.configure(text = "Correct!")
            
        else:
            feedback.configure(text = "Wrong!")

    except ValueError:
        feedback.configure(text = "That is not a number")
        answer_entry.delete(0, END)
        answer_entry.focus()
        
root = Tk()
root.title("Math Question")

x = randrange(20)
y = randrange(20)


problem_label = Label(root, text = "", width = 18, height = 3)
problem_label.grid(row = 0, column = 0, sticky = W)

answer_entry = Entry(root, width = 7)
answer_entry.grid(row = 0, column = 1, sticky = W)

check_btn = Button(root, text = "Check Answer", command = check_answer, relief = RIDGE)
check_btn.grid(row = 1, column = 0)

next_btn = Button(root, text = "Next", width = 5, command = next_problem, relief = RIDGE)
next_btn.grid(row = 1, column = 1)

feedback = Label(root, text = "", height = 3,)
feedback.grid(row = 2, column = 0)


next_problem()
root.geometry("300x200+500+200")
root.mainloop()
    
    
    