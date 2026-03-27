from tkinter import*

def plus():
    f=float(entr1.get())
    s=float(entr2.get())
    p=f+s
    txt1.delete(0.0,END)
    txt1.insert(END,round(p,1))
def mini():
    f=float(entr1.get())
    s=float(entr2.get())
    p=f-s
    txt1.delete(0.0,END)
    txt1.insert(END,round(p,1))  
def div():
    f=float(entr1.get())
    s=float(entr2.get())
    p=f/s
    txt1.delete(0.0,END)
    txt1.insert(END,round(p,1))
def mul():
    f=float(entr1.get())
    s=float(entr2.get())
    p=f*s
    txt1.delete(0.0,END)
    txt1.insert(END,round(p,1))
def clear():
    entr1.delete(0,END)
    entr2.delete(0,END)
    txt1.delete(0.0,END)

win=Tk()
win.title("Simple Calculator")
win.geometry("600x545+400+200")
win.resizable(0,0)
win.configure(bg="#708090")
win.columnconfigure(0,weight=2)
win.columnconfigure(1,weight=2)
Label(win,text="     Calculator     ",font="none 30",fg="black",bg="#95B9C7")\
        .grid(row=0,column=0,columnspan=2,padx=10,pady=10)

lbl1=Label(win,text="Enter First Number:",font="none 20",fg="black",bg="light blue")
lbl1.grid(row=1,column=0,padx=10,pady=10,sticky=W)
lbl2=Label(win,text="Enter Second Number:",font="none 20",fg="black",bg="light blue")
lbl2.grid(row=2,column=0,padx=10,pady=10,sticky=W)
lbl3=Label(win,text="     Answer:     ",font="none 20",fg="black",bg="light blue")
lbl3.grid(row=4,column=0,padx=10,pady=10,sticky=W)

entr1=Entry(win,font="none 25",fg="black",bg="white",width="10")
entr1.grid(row=1,column=1,padx=10,pady=20,sticky=W)
entr2=Entry(win,font="none 25",fg="black",bg="white",width="10")
entr2.grid(row=2,column=1,padx=10,pady=20,sticky=W)

txt1=Text(win,font="none 40",fg="black",bg="white",width="10",height="1")
txt1.grid(row=4,column=1,padx=10,pady=20,sticky=W)

btn1=Button(win,text="÷",font="none 20",height=2,width="4",bg="#95B9C7",command=div)
btn1.grid(row=3,column=1,sticky=W,padx=35)
btn2=Button(win,text="x",font="none 20",height=2,width="4",bg="#95B9C7",command=mul)
btn2.grid(row=3,column=0,sticky=E)
btn3=Button(win,text="+",font="none 20",height=2,width="4",bg="#95B9C7",command=plus)
btn3.grid(row=3,column=0,sticky=W,padx=10)
btn4=Button(win,text="-",font="none 20",height=2,width="4",bg="#95B9C7",command=mini)
btn4.grid(row=3,column=0,sticky=S)

btncl=Button(win,text="Clear",font="none 20",bg="#95B9C7",height=2,command=clear)
btncl.grid(row=5,column=1,padx=10,pady=20,sticky=E)

win.mainloop()
