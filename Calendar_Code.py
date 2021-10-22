from tkinter import *
import calendar

text=calendar.calendar(2022)

root=Tk()
root.geometry("550x600")
root.title("CALENDAR")

label1=Label(root, text="CALENDAR", background='green', font=("times",25,'bold'))
label1.grid(row=1, column=1)

root.config(background="light green")

label1=Label(root, text=text, font="consolas 10 bold")
label1.grid(row=2, column=1, padx=20)

root.mainloop()