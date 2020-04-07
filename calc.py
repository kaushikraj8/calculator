import sys
from tkinter import *
import tkinter
import tkinter.messagebox
import math


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False
        
        


    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "power":
            v = math.pow(self.total,self.current)
            self.total = v
        if self.op == "log":
            v = math.log(self.total,self.current)
            self.total = v
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
        
    def const_e(self):
        self.eq = False
        self.current = math.e
        self.display(self.current)

    def Scientfic(self):

        bttn_sin = Button(calc,bd=8, text = " sin ",fg="blue")
        bttn_sin["command"] = sum1.sin
        bttn_sin.grid(row = 1, column = 5,padx=16, pady=16)

        bttn_cos = Button(calc,bd=8, text = " cos ",fg="blue")
        bttn_cos["command"] = sum1.cos
        bttn_cos.grid(row = 2, column = 5,padx=16, pady=16)

        bttn_tan = Button(calc, bd=8,text = " tan ",fg="blue")
        bttn_tan["command"] = sum1.tan
        bttn_tan.grid(row = 3, column = 5,padx=16, pady=16)

        bttn_sin = Button(calc,bd=8, text = " sin' ",fg="orange")
        bttn_sin["command"] = sum1.sin1
        bttn_sin.grid(row = 1, column = 6,padx=16, pady=16)

        bttn_cos = Button(calc,bd=8, text = " cos' ",fg="orange")
        bttn_cos["command"] = sum1.cos1
        bttn_cos.grid(row = 2, column = 6,padx=16, pady=16)

        bttn_tan = Button(calc, bd=8,text = " tan' ",fg="orange")
        bttn_tan["command"] = sum1.tan1
        bttn_tan.grid(row = 3, column = 6,padx=16, pady=16)

        bttn_sin = Button(calc,bd=8, text = " sinh ",fg="blue")
        bttn_sin["command"] = sum1.sinh
        bttn_sin.grid(row = 1, column = 7,padx=16, pady=16)

        bttn_cos = Button(calc,bd=8, text = " cosh ",fg="blue")
        bttn_cos["command"] = sum1.cosh
        bttn_cos.grid(row = 2, column = 7,padx=16, pady=16)

        bttn_tan = Button(calc, bd=8,text = " tanh ",fg="blue")
        bttn_tan["command"] = sum1.tanh
        bttn_tan.grid(row = 3, column = 7,padx=16, pady=16)

        bttn_sin = Button(calc,bd=8, text = " sinh' ",fg="orange")
        bttn_sin["command"] = sum1.sinh1
        bttn_sin.grid(row = 1, column = 8,padx=16, pady=16)

        bttn_cos = Button(calc,bd=8, text = " cosh' ",fg="orange")
        bttn_cos["command"] = sum1.cosh1
        bttn_cos.grid(row = 2, column = 8,padx=16, pady=16)

        bttn_tan = Button(calc, bd=8,text = " tanh' ",fg="orange")
        bttn_tan["command"] = sum1.tanh1
        bttn_tan.grid(row = 3, column = 8,padx=16, pady=16)

        bttn_0 = Button(calc,bd=8, text = "  √x  ",fg="black")
        bttn_0["command"] = sum1.sqrt
        bttn_0.grid(row = 4, column = 6,padx=16, pady=16)

        bttn_0 = Button(calc,bd=8, text = "  x!  ",fg="black")
        bttn_0["command"] = sum1.fact
        bttn_0.grid(row = 5, column = 6,padx=16, pady=16)

        bttn_0 = Button(calc, bd=8,text = " ln  ",fg="black")
        bttn_0["command"] = sum1.ln
        bttn_0.grid(row = 4, column = 5,padx=16, pady=16)

        bttn_0 = Button(calc,bd=8, text = " log ",fg="black")
        bttn_0["command"] = sum1.log
        bttn_0.grid(row = 5, column = 5,padx=16, pady=16)

        bttn_pi = Button(calc,bd=8, text = " π ",fg="green")
        bttn_pi["command"] = sum1.const_pi
        bttn_pi.grid(row = 5, column = 4,padx=16, pady=16)

        bttn_pi = Button(calc,bd=8, text = " x ̂ y ",fg="black")
        bttn_pi["command"] = lambda: sum1.operation("power")
        bttn_pi.grid(row = 4, column = 7,padx=16, pady=16)

        bttn_pi = Button(calc,bd=8, text = " e ̂ x ",fg="black")
        bttn_pi["command"] = sum1.expo
        bttn_pi.grid(row = 4, column = 8,padx=16, pady=16)

        bttn_pi = Button(calc,bd=8, text = " x ̂ 2 ",fg="black")
        bttn_pi["command"] = sum1.x2
        bttn_pi.grid(row = 5, column = 8,padx=16, pady=16)

        bttn_pi = Button(calc,bd=8, text = "log(x[base])",fg="black")
        bttn_pi["command"] = lambda: sum1.operation("log")
        bttn_pi.grid(row = 5, column = 7,padx=16, pady=16)

    def const_pi(self):
        self.eq = False
        self.current = math.pi
        self.display(self.current)
    def sin(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.sin(v)
        self.display(self.current)

    def cos(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.cos(v)
        self.display(self.current)

    def tan(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.tan(v)
        self.display(self.current)

    def sin1(self):
        v = float(text_box.get())
        self.current = math.asin(v)
        self.current = math.degrees(self.current)
        self.display(self.current)

    def cos1(self):
        v = float(text_box.get())
        self.current = math.acos(v)
        self.current = math.degrees(self.current)
        self.display(self.current)
        
    def tan1(self):
        v = float(text_box.get())
        self.current = math.atan(v)
        self.current = math.degrees(self.current)
        self.display(self.current)

    def sinh(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.sinh(v)
        self.display(self.current)

    def cosh(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.cosh(v)
        self.display(self.current)

    def tanh(self):
        v = float(text_box.get())
        v*=(math.pi/180)
        self.current = math.tanh(v)
        self.display(self.current)

    def sinh1(self):
        v = float(text_box.get())
        self.current = math.asinh(v)
        self.current = math.degrees(self.current)
        self.display(self.current)

    def cosh1(self):
        v = float(text_box.get())
        self.current = math.acosh(v)
        self.current = math.degrees(self.current)
        self.display(self.current)

    def tanh1(self):
        v = float(text_box.get())
        self.current = math.atanh(v)
        self.current = math.degrees(self.current)
        self.display(self.current)
    
    def fact(self):
        f = float(text_box.get())
        self.current = math.factorial(f)
        self.display(self.current)
       
    def sqrt(self):
        f = float(text_box.get())
        self.current = math.sqrt(f)
        self.display(self.current)

    def ln(self):
        f = float(text_box.get())
        self.current = math.log(f)
        self.display(self.current)

    def log(self):
        f = float(text_box.get())
        self.current = math.log10(f)
        self.display(self.current)

    def expo(self):
        f = float(text_box.get())
        self.current = math.exp(f)
        self.display(self.current)

    def x2(self):
        f = float(text_box.get())
        self.current = f**2
        self.display(self.current)

    def about(self):
        tkinter.messagebox.showinfo('About',"Calculating Machine\n\nCoded By:\n\tPHILSON K PHILIP\nSupported By:\n\tJOVIAL J\n\tTINI THOMAS\n\tJUSTINE SAJI\nGuided By:\n\tMs.Dhanyamol Antony\n\nA Micro Project Group Work")
        
        
    def exit1(self):
        answer = tkinter.messagebox.askquestion('Calculating Machine','Are you sure to Quit')
        if answer == "yes":
            exit(code=None)
        

           
sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Scientific Calculator",command=sum1.Scientfic )
subMenu.add_separator()
subMenu.add_command(label="Exit" ,command =sum1.exit1 )

abtMenu = Menu(menu)
menu.add_cascade(label="About",menu=abtMenu)
abtMenu.add_command(label="Credits",command = sum1.about)



root.title("Calculating Machine")

text_box = Entry(calc,bd=20, insertwidth=1,font=30 , justify=RIGHT,relief=RIDGE,bg="powder blue")
text_box.grid(row = 0, column = 0, columnspan = 8, pady = 20)
text_box.insert(0, "0")


numbers = "123456789"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,bd=8,fg="green", text = numbers[ i ]))
        bttn[i].grid(row = j, column = k,padx=16, pady=16 )
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc,bd=8,fg="green", text = " 0 ")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1,padx=16, pady=16)

bttn_div = Button(calc,bd=8, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3,padx=16, pady=16)

bttn_mult = Button(calc, bd=8,text = " x ")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3,padx=16, pady=16)

minus = Button(calc,bd=8, text = " - ")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3,padx=16, pady=16)

point = Button(calc,bd=8, text = " . ")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0,padx=16, pady=16)

add = Button(calc, bd=8,text = " + ")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,padx=16, pady=16)

bttn_e = Button(calc,bd=8, text = " e ",fg="blue")
bttn_e["command"] = sum1.const_e
bttn_e.grid(row = 5, column = 3,padx=16, pady=16)

bttn_0 = Button(calc,bd=8, text = "-(x)",fg="red")
bttn_0["command"] = sum1.sign
bttn_0.grid(row = 4, column = 2,padx=16, pady=16)

clear = Button(calc, bd=8,text = "  C  ",fg="red")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 0,padx=16, pady=16)

all_clear = Button(calc,bd=8, text = "  AC ",fg="orange")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 1,padx=16, pady=16)

equals = Button(calc,bd=8, text = " = ")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 2,padx=16, pady=16)



root.mainloop()