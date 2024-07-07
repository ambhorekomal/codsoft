from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title('To Do List')
root.geometry("500x500")
root.config(bg='PowderBlue')

my_font = tkFont.Font(family="DejaVu Serif", size=30, weight="bold")
myLabel = Label(root, text="TO-DO List", bg='PowderBlue', font=my_font)
myLabel.pack(pady=20)

my_entry = Entry(root, font=("DejaVu Serif", 24), width=26)
my_entry.pack(pady=20)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
    
def delete_item():
    my_list.delete(ANCHOR)
    
def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#dedede'
    )
    my_list.selection_clear(0, END)
    
def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#464646'
    )
    my_list.selection_clear(0, END)
    
def delete_cross_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(count)
        else:
            count += 1

button_frame = Frame(root)
button_frame.pack(pady=20)
add_button = Button(button_frame, text="Add Task", command=add_item)
delete_button = Button(button_frame, text="Delete Task", command=delete_item)
cross_button = Button(button_frame, text="Mark Task Done", command=cross_item)
uncross_button = Button(button_frame, text="Mark Task Not Done", command=uncross_item)
delete_cross_button = Button(button_frame, text="Delete Completed Task", command=delete_cross_item)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3)
delete_cross_button.grid(row=0, column=4)

my_frame = Frame(root)
my_frame.pack(pady=10)
my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg="SystemButtonFace",
                  bd=0, highlightthickness=0, fg="#464646", selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

root.mainloop()
