from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.configure(bg="#17161b")
root.resizable(False,False)

label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

equation=""

def button_click(number):
    global equation
    equation+=number
    label_result.config(text=equation)


def calc():
    global equation
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)


def clear():
    global equation
    equation=""
    label_result.config(text=equation)






#Defining Button

button_1=Button(root,text="1",width=5,height=1,command=lambda:button_click("1"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_2=Button(root,text="2",width=5,height=1,command=lambda:button_click("2"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_3=Button(root,text="3",width=5,height=1,command=lambda:button_click("3"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_4=Button(root,text="4",width=5,height=1,command=lambda:button_click("4"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_5=Button(root,text="5",width=5,height=1,command=lambda:button_click("5"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_6=Button(root,text="6",width=5,height=1,command=lambda:button_click("6"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_7=Button(root,text="7",width=5,height=1,command=lambda:button_click("7"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_8=Button(root,text="8",width=5,height=1,command=lambda:button_click("8"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_9=Button(root,text="9",width=5,height=1,command=lambda:button_click("9"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_0=Button(root,text="0",width=5,height=1,command=lambda:button_click("0"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_add=Button(root,text="+",width=5,height=1,command=lambda:button_click("+"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_equal=Button(root,text="=",width=5,height=3,command=lambda:calc(),bg="#fe9037",fg="#fff",font=("arial",30,"bold"))
button_clear=Button(root,text="C",width=16,height=1,command=lambda:clear(),bg="#3697f5",fg="#fff",font=("arial",30,"bold"))

button_sub=Button(root,text="-",width=5,height=1,command=lambda:button_click("-"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_mult=Button(root,text="X",width=5,height=1,command=lambda:button_click("*"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_div=Button(root,text="÷",width=5,height=1,command=lambda:button_click("/"),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
button_decimal=Button(root,text=".",width=5,height=1,command=lambda:button_click("."),bg="#2a2d36",fg="#fff",font=("arial",30,"bold"))
#putting buttons on the screen

button_7.place(x=10,y=100)
button_8.place(x=150,y=100)
button_9.place(x=290,y=100)
button_mult.place(x=430,y=100)

button_4.place(x=10,y=200)
button_5.place(x=150,y=200)
button_6.place(x=290,y=200)
button_sub.place(x=430,y=200)

button_1.place(x=10,y=300)
button_2.place(x=150,y=300)
button_3.place(x=290,y=300)
button_add.place(x=430,y=300)

button_0.place(x=10,y=400)
button_clear.place(x=10,y=500)
button_div.place(x=290,y=400)
button_equal.place(x=430,y=400)
button_decimal.place(x=150,y=400)

root.mainloop()