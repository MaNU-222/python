
from cgitb import text
import tkinter as tk
import number_entry as nent


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Set the configuration of GUI window
    root.geometry("500x300")

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Compound Interest Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):


    def calculate_ci():
        # get a content from entry box
        principle = int(principle_field.get())
     
        rate = float(rate_field.get())
 
        time = int(time_field.get())
     
        # Calculates compound interest 
        CI = principle * (pow((1 + rate / 100), time))
 
        # insert method inserting the 
        # value in the text entry box.
        compound_field.insert(10, CI)
        
        button1.config(command=calculate_ci)
        
        

        


    def clear_all():
        
        # whole content of entry boxes is deleted
        principle_field.delete(0, tk.END)  
        rate_field.delete(0, tk.END)
        time_field.delete(0, tk.END)
        compound_field.delete(0, tk.END)
    
   
        # set focus on the principle_field entry box 
        principle_field.bind("<KeyRelease>", calculate_ci)

        # Give the keyboard focus to the age entry box.
        principle_field.focus_set()


        # Bind the clear function to the clear button so
        # that the clear function will be called when the
        # user clicks the clear button.
        button2.config(Command=clear_all)



    # Create a Principle Amount : label
    lab_pa1 = tk.Label(frm_main, text="Principle Amount(Rs): ")

    # Create a Rate : label
    lab_rate2 = tk.Label(frm_main, text="Rate(%): ")

    # Create a Time : label
    lab_time3 = tk.Label(frm_main,text="Time(years): " )


    # Create a Compound Interest : label
    lab_ci4  = tk.Label(frm_main, text="Compound Interest : ")

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    lab_pa1.grid(row = 1, column = 0, padx = 10, pady = 10) 
    lab_rate2.grid(row = 2, column = 0, padx = 10, pady = 10) 
    lab_time3.grid(row = 3, column = 0, padx = 10, pady = 10)
    lab_ci4.grid(row = 5, column = 0, padx = 10, pady = 10)

    principle_field = nent.IntEntry(frm_main, 1, 10000000000000, width=30)
    rate_field =  nent.IntEntry(frm_main, 1, 1000, width=30)
    time_field =  nent.IntEntry(frm_main, 1, 1000, width=30)
    compound_field = nent.IntEntry(frm_main, 1, 100000000000000000000, width=30)

    principle_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
    rate_field.grid(row = 2, column = 1, padx = 10, pady = 10) 
    time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
    compound_field.grid(row = 5, column = 1, padx = 10, pady = 10)

    # Create a Submit Button and attached 
    # to calculate_ci function
    button1 = tk.Button(frm_main, text = "Submit", command=calculate_ci)

    # Create a Clear Button and attached 
    # to clear_all function
    button2 = tk.Button(frm_main, text = "Clear", command=clear_all)
    
   
    button1.grid(row = 4, column = 1, pady = 10)
    button2.grid(row = 6, column = 1, pady = 10)



if __name__ == "__main__":
    main()