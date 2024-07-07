from tkinter import*
import tkinter.font as tkFont
import random
root= Tk()
root.title("Password Generator")
root.config(bg= "Thistle")
my_font = tkFont.Font(family="DejaVu Serif", size=30, weight="bold")
my_label= Label(root, text= "WELCOME TO PASSWORD GENERATOR!", bg="Thistle",width= 60 ,font= my_font)
my_label.pack(pady=20)
my_frame= Frame(root,bg="Thistle")
my_frame.pack(pady=20)
label1=Label(my_frame,text="Enter the required length of password : ",bg="Thistle",font=("Ariel",14))
label1.grid(row=0,column=0,padx=10,pady=10)
my_entry = Entry(my_frame, width=50, highlightbackground="Thistle")

my_entry.grid(row=0 ,column = 1,padx=10,pady=10)
output_entry= Entry(my_frame,width=50, highlightbackground="Thistle")
output_entry.grid(row=3,column=0, columnspan=2,pady=20)

def create_password():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_chars = "!@#$%^&*(){}"
    
    len_password = my_entry.get()
    
    # Ensure the input length is a valid integer
    try:
        len_password = int(len_password)
        if len_password < 4:
            raise ValueError("Length must be at least 4")

        # Ensure at least one of each required character type is included
        password = [
            random.choice(lower_case),
            random.choice(upper_case),
            random.choice(numbers),
            random.choice(special_chars)
        ]

        # Fill the remaining length of the password with a random selection of all characters
        if len_password > 4:
            all_chars = lower_case + upper_case + numbers + special_chars
            password += random.sample(all_chars, len_password - 4)
        
        # Shuffle the password to mix the characters well
        random.shuffle(password)
        final_password = "".join(password)

        # Clear the output entry before inserting the new password
        output_entry.delete(0, END)
        output_entry.insert(0, final_password)
    except ValueError:
        output_entry.delete(0, END)
        output_entry.insert(0, "Please enter a valid number")
    
button1= Button(my_frame,text="Generate Password",pady=10,padx=20,command= create_password)
button1.grid(row=1,column=0,columnspan=2,pady=20)
root.mainloop()