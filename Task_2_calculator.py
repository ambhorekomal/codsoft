from tkinter import*
root = Tk()
root.title("Simple Calculator")
e= Entry(root,width=50,borderwidth = 5,fg= "white",bg="black")
e.grid(row=0,column=0 , columnspan = 4, padx = 10, pady = 10)
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_no = e.get()
    global f_num 
    global operation_to_be_performed
    operation_to_be_performed = "Addition of numbers"
    f_num = int(first_no)
    e.delete(0,END)

def button_sub():
    first_no = e.get()
    global f_num 
    global operation_to_be_performed
    operation_to_be_performed = "Subtraction of numbers"
    f_num = int(first_no)
    e.delete(0,END)

def button_mul():
    first_no = e.get()
    global f_num 
    global operation_to_be_performed
    operation_to_be_performed = "Multiplication of numbers"
    f_num = int(first_no)
    e.delete(0,END)

def button_div():
    first_no = e.get()
    global f_num 
    global operation_to_be_performed
    operation_to_be_performed = "Division of numbers"
    f_num = int(first_no)
    e.delete(0,END)

def button_equal():
    second_no = e.get()
    e.delete(0,END)
    if  (operation_to_be_performed == "Addition of numbers"):
        e.insert(0,f_num + int(second_no))
    if  (operation_to_be_performed == "Subtraction of numbers"):
        e.insert(0,f_num - int(second_no))
    if  (operation_to_be_performed == "Multiplication of numbers"):
        e.insert(0,f_num * int(second_no))
    if  (operation_to_be_performed == "Division of numbers"):
        e.insert(0,f_num / int(second_no))
        
        
#define all the buttons
Button_1 = Button(root, text= "1", padx= 40 , pady =15, command=lambda:button_click(1),fg= "white",bg="black")
Button_2 = Button(root, text= "2", padx= 40 , pady =15, command=lambda:button_click(2),fg= "white",bg="black")
Button_3 = Button(root, text= "3", padx= 40 , pady =15, command=lambda:button_click(3),fg= "white",bg="black")
Button_4 = Button(root, text= "4", padx= 40 , pady =15, command=lambda:button_click(4),fg= "white",bg="black")
Button_5 = Button(root, text= "5", padx= 40 , pady =15, command=lambda:button_click(5),fg= "white",bg="black")
Button_6 = Button(root, text= "6", padx= 40 , pady =15, command=lambda:button_click(6),fg= "white",bg="black")
Button_7 = Button(root, text= "7", padx= 40 , pady =15, command=lambda:button_click(7),fg= "white",bg="black")
Button_8 = Button(root, text= "8", padx= 40 , pady =15, command=lambda:button_click(8),fg= "white",bg="black")
Button_9 = Button(root, text= "9", padx= 40 , pady =15, command=lambda:button_click(9),fg= "white",bg="black")
Button_0 = Button(root, text= "0", padx= 40 , pady =15, command=lambda:button_click(0),fg= "white",bg="black")
Button_add = Button(root, text= "+", padx= 40 , pady =15, command=button_add,fg= "white",bg="black")
Button_sub = Button(root, text= "-", padx= 40 , pady =15, command=button_sub,fg= "white",bg="black")
Button_mul = Button(root, text= "*", padx= 40 , pady =15, command=button_mul,fg= "white",bg="black")
Button_div = Button(root, text= "/", padx= 40 , pady =15, command=button_div,fg= "white",bg="black")
Button_clear = Button(root, text= "C", padx= 40 , pady =15, command=button_clear,fg= "white",bg="black")
Button_equal = Button(root, text= "=", padx= 40 , pady =15, command=button_equal,fg= "white",bg="black")
#define the grid for the buttons
Button_1.grid(row =  3, column =  0)
Button_2.grid(row = 3 , column =1 )
Button_3.grid(row = 3 , column =2 )
Button_4.grid(row = 2 , column = 0 )
Button_5.grid(row = 2 , column = 1 )
Button_6.grid(row = 2 , column = 2 )
Button_7.grid(row = 1, column = 0 )
Button_8.grid(row = 1 , column = 1 )
Button_9.grid(row = 1 , column = 2 )
Button_0.grid(row = 4 , column = 0 )
Button_add.grid(row = 2, column = 3 )
Button_sub.grid(row = 3 , column =  3)
Button_mul.grid(row = 4 , column = 1 )
Button_div.grid(row =  4 , column = 2 )
Button_clear.grid(row = 1 , column = 3 )
Button_equal.grid(row =  4 , column = 3 )
root.mainloop()