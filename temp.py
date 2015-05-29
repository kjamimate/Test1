from Tkinter import *
import ttk

root =Tk()
root.title("System One")
frame = ttk.Frame(root)
frame.pack()
frame.configure(height = 100, width = 200)
frame.configure( relief = SOLID)

tools_run =StringVar()

c1 = ttk.Combobox(root, textvariable= tools_run, width =35)
c1.configure(values = ('0032B + 9622 + 9013A + 9074 + 9013C', 'Just inrod (9013C)', 'All tools + Gyro'))
c1.pack()


root.mainloop()