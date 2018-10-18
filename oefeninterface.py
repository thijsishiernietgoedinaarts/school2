from tkinter import *
root = Tk()

label = Label(master=root,
              text='Hello World',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'),
              width=14,
              height=3)
label.pack()
button = Button(master=root, text='Druk hier')
button.pack(pady=10, fill=X)
entry = Entry(master=root)
entry.pack(padx=10, pady=10)
root.mainloop()