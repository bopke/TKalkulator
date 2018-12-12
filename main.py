from math import sqrt
import tkinter as tk


class Calculator:

    def __init__(self, master):
        # config
        buttonfont = ("monospaced", 20)

        # window
        master.geometry()
        master.title("TKalculator")
        master.config(bg='black')

        # display management
        label_display = tk.Label(master, fg='white', bg='black', text="Calculatoroinator",
                                 font=("monospaced", 24, "bold"))
        label_display.grid(row=0, column=0, columnspan=4)
        self.display = tk.Entry(master, fg='white', width=10, bd=4, bg='gray', justify=tk.RIGHT,
                                font=("monospaced", 40))
        self.display.grid(row=1, column=0, columnspan=4)
        #        self.display.insert(0, '0') # więcej z tego problemu niż pożytku
        self.display.focus_set()

        # buttons
        tk.Button(master, text="%", command=lambda: self.display.insert(tk.END, "%"), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=3, column=0)
        tk.Button(master, text="sqrt", command=lambda: self.sqrt(), bg='gray', fg='white', font=buttonfont,
                  width=4).grid(row=3, column=1)
        tk.Button(master, text="x^2", command=lambda: self.square(), bg='gray', fg='white', font=buttonfont,
                  width=4).grid(row=3, column=2)
        tk.Button(master, text="1/x", command=lambda: self.inverse_number(), bg='gray', fg='white', font=buttonfont,
                  width=4).grid(row=3, column=3)
        tk.Button(master, text="CE", command=lambda: self.display.delete(0, tk.END), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=4, column=0)
        tk.Button(master, text="C", command=lambda: self.display.delete(0, tk.END), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=4, column=1)
        tk.Button(master, text="del", command=lambda: self.display.delete(len(self.display.get()) - 1, tk.END),
                  bg='gray', fg='white', font=buttonfont, width=4).grid(row=4, column=2)
        tk.Button(master, text="/", command=lambda: self.display.insert(tk.END, "/"), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=4, column=3)
        tk.Button(master, text="7", command=lambda: self.display.insert(tk.END, 7), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=5, column=0)
        tk.Button(master, text="8", command=lambda: self.display.insert(tk.END, 8), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=5, column=1)
        tk.Button(master, text="9", command=lambda: self.display.insert(tk.END, 9), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=5, column=2)
        tk.Button(master, text="*", command=lambda: self.display.insert(tk.END, "*"), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=5, column=3)
        tk.Button(master, text="4", command=lambda: self.display.insert(tk.END, 4), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=6, column=0)
        tk.Button(master, text="5", command=lambda: self.display.insert(tk.END, 5), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=6, column=1)
        tk.Button(master, text="6", command=lambda: self.display.insert(tk.END, 6), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=6, column=2)
        tk.Button(master, text="-", command=lambda: self.display.insert(tk.END, "-"), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=6, column=3)
        tk.Button(master, text="1", command=lambda: self.display.insert(tk.END, 1), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=7, column=0)
        tk.Button(master, text="2", command=lambda: self.display.insert(tk.END, 2), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=7, column=1)
        tk.Button(master, text="3", command=lambda: self.display.insert(tk.END, 3), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=7, column=2)
        tk.Button(master, text="+", command=lambda: self.display.insert(tk.END, "+"), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=7, column=3)
        tk.Button(master, text="±", command=lambda: self.opposite_number(), bg='gray', fg='white', font=buttonfont,
                  width=4).grid(row=8, column=0)
        tk.Button(master, text="0", command=lambda: self.display.insert(tk.END, 0), bg='gray80', fg='white',
                  font=buttonfont, width=4).grid(row=8, column=1)
        tk.Button(master, text=".", command=lambda: self.display.insert(tk.END, "."), bg='gray', fg='white',
                  font=buttonfont, width=4).grid(row=8, column=2)
        tk.Button(master, text="=", command=lambda: self.calculate(), bg='gray', fg='white', font=buttonfont,
                  width=4).grid(row=8, column=3)

    def set_text(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(0, text)

    def get_text(self):
        t = self.display.get()
        if len(t) == 0:
            return '0'
        return t

    def opposite_number(self):
        try:
            self.calculate()
        except:
            self.set_text("error")
            return
        if self.get_text()[0] == '-':
            self.display.delete(0, 1)
        else:
            self.display.insert(0, '-')

    def calculate(self):
        try:
            v = eval(self.get_text())
        except:
            self.set_text("Error")
            raise ArithmeticError
        else:
            self.set_text(v)

    def square(self):
        try:
            v = eval(self.get_text())
        except:
            self.set_text("Error")
        else:
            self.set_text(v ** 2)

    def sqrt(self):
        try:
            self.calculate()
            v = sqrt(self.get_text())
        except:
            self.set_text("Error")
        else:
            self.set_text(v)

    def inverse_number(self):
        try:
            self.calculate()
            v = 1 / float(self.get_text())
        except:
            self.set_text("Error")
        else:

            self.set_text(v)


init = tk.Tk()
calculatorApp = Calculator(init)
init.mainloop()
