from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Error Handling")
window.geometry("300x155")
window.resizable(0, 0)
window.config(bg="pink")

amountlabel = Label(window, text="Please enter amount in your account:")
amountlabel.place(x=15, y=30)
amountfield = Entry(window)
amountfield.place(x=15, y=60)


def checkqualification():
    try:
        money = float(amountfield.get())
        if money < 3000:
            messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
            amountfield.delete(0, END)
        else:
            messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
            amountfield.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please put in an amount in numbers.")
        amountfield.delete(0, END)


enterbutton = Button(window, text="Check qualification", command=checkqualification)
enterbutton.place(x=15, y=120)


def clearfunc():
    amountfield.delete(0, END)


clearbutton = Button(window, text="Clear", command=clearfunc, bg="lime", borderwidth="5")
clearbutton.place(x=15, y=180)


def exitfunc():
    window.destroy()


exitbutton = Button(window, text="Exit", command=exitfunc, bg="lime", borderwidth="5")
exitbutton.place(x=230, y=180)
window.mainloop()
