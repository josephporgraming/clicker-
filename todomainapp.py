import tkinter as tk
from tkinter import messagebox

class myGUI:
    i = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root['background'] = 'black'
        self.root.overrideredirect(False)

        self.var = tk.StringVar()
        self.var.set("click the button to start")
        self.menue_bar = tk.Menu (self.root)

        self.filemenue = tk.Menu(self.menue_bar, tearoff=0)
        self.filemenue.add_command(label="Close", command=self.on_closeing)
        self.filemenue.add_command(label="Close without qestion", command=quit)

        self.menue_bar.add_cascade(menu=self.filemenue, label= "stuff")

        self.root.config(menu=self.menue_bar)

        self.timesuserclicked = tk.Label(self.root, textvariable=self.var, font=('Arial', 18),
                                         bg = "black",fg="white")
        self.timesuserclicked.pack()

        self.button = tk.Button(self.root,text='Click Me!!' , font=('Arial', 18), command= self.showmeage,
                                bg = "black",fg="white")
        self.button.pack()
        


        self.root.mainloop()
    def showmeage(self):
        self.i += 1
        self.var.set(f"you clicked me {self.i} times.")
        self.timesuserclicked = self.timesuserclicked = tk.Label(self.root, text=f'times you click {self.i}', font=('Arial', 18))
    def on_closeing(self):
        if messagebox.askyesno(title="Quit?", message="do you realy whant to quit??") == 1:
            self.root.destroy()
    
myGUI()    