# Python has tkinter as a built in library

from tkinter import *


def km_to_miles():
    """
    Function to convert km to miles
    1 mile = 1.6 km
    :return:
    """
    # print("Calling function")
    # print the result of the entry widget
    # print(entry_value.get())

    miles = float(entry_value.get()) / 1.6
    # Now this entry_value should be inserted into the text box
    t1.insert(END, str(miles) + " miles")


# Creating a window object
window = Tk()

# Creating a button
# A button is a widget
# The first parameter should be the window
# Whatever is passed to the command argument will be executed
# Calling the km_to_mile function on press of this button

b1 = Button(window, text="Execute", command=km_to_miles)

# Call the pack method
# b1.pack()

# A widget can be displayed using the grid method as well
# The grid method allows us to specify where the widget should
# be placed.

b1.grid(row=0, column=0)


# An entry is another widget
# An entry is like an are where you can enter a value
# Whatever is entered in the Entry widget can be got
# from the StringVar object


entry_value = StringVar()
e1 = Entry(window, textvariable=entry_value)
e1.grid(row=0, column=1)

# Text Widget
# The text box has to have some height and width
# Height and width represent the number of cells this
# text widget will span
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


# Start the window loop
window.mainloop()