from tkinter import *
from tkinter import ttk

#print("Select an operation to Perform:")
#print("1. ADD ")
#print("2. SUBTRACT ")
#print("3. MULTIPLY ")
#print("4. DIVIDE ")

root = Tk()
root.title("Python Calculator")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


display_entry= ttk.Entry(mainframe, width=9, textvariable= )
display_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=sum).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="1", command=1).grid(column=0, row=2,)
ttk.Button(mainframe, text="2", command=2).grid(column=1, row=2,)
ttk.Button(mainframe, text="3", command=3).grid(column=2, row=2,)
ttk.Button(mainframe, text="4", command=4).grid(column=0, row=3,)
ttk.Button(mainframe, text="5", command=5).grid(column=1, row=3,)
ttk.Button(mainframe, text="6", command=6).grid(column=2, row=3,)
ttk.Button(mainframe, text="7", command=7).grid(column=0, row=4,)
ttk.Button(mainframe, text="8", command=8).grid(column=1, row=4,)
ttk.Button(mainframe, text="9", command=9).grid(column=2, row=4,)
ttk.Button(mainframe, text="0", command=0).grid(column=1, row=5,)
ttk.Button(mainframe, text="-", command="calculate").grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="*", command="calculate").grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="/", command="calculate").grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="+", command="calculate").grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="=", command="calculate").grid(column=3, row=5, sticky=W)

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) + int(num2) 
    print("The sum is ", sum)
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) - int(num2)
    print("The sum is ", sum)
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) * int(num2)
    print("The sum is ", sum)
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    sum = int(num1) / int(num2)
    print("The sum is ", sum)
else: 
    print("Invalid Entry")

    print("Done")