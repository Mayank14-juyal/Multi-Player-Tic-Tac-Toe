from tkinter import *
r=Tk()
bclick=True
a=0
r.title("Tic-Tac-Toe")
label=Label(r,text="Welcome to Tic-Tac-Toe",font="Times 20 italic",bg="grey",fg="red",height=2,width=20)
label.grid(row=0)
label1=Label(r,text="player 1: ",bg="black",fg="white",height=2,width=6)
label1.grid(row=1,column=0,sticky=S+N+E+W)
entry1=Entry(r,width=20)
entry1.grid(row=1,column=1)
label2=Label(r,text="player 2: ",bg="black",fg="white",height=2,width=6)
label2.grid(row=2,column=0,sticky=S+N+E+W)
entry2=Entry(r,width=20)
entry2.grid(row=2,column=1)
def enter():
    root = Toplevel(r)
    def x():
        return 0
    def game(buttons):
        global bclick,e,a
        if buttons["text"]==" " and bclick==True:
            buttons["text"]="X"
            bclick=False
        elif buttons["text"]==" " and bclick==False:
                buttons["text"]="O"
                bclick=True
        if ((button1["text"]==button2["text"]==button3["text"] and button1["text"]!=" ")  or (button4["text"]==button5["text"]==button6["text"] and button4["text"]!=" ")  or (button7["text"]==button8["text"]==button9["text"] and button7["text"]!=" ") or (button1["text"]==button4["text"]==button7["text"] and button1["text"]!=" ") or (button2["text"]==button5["text"]==button8["text"] and button2["text"]!=" ") or (button3["text"]==button6["text"]==button9["text"] and button3["text"]!=" ") or (button1["text"]==button5["text"]==button9["text"] and button1["text"]!=" ") or (button3["text"]==button5["text"]==button7["text"] and button3["text"]!=" ")):
            e=buttons["text"]
            button1.configure(command=x)
            button2.configure(command=x)
            button3.configure(command=x)
            button4.configure(command=x)
            button5.configure(command=x)
            button6.configure(command=x)
            button7.configure(command=x)
            button8.configure(command=x)
            button9.configure(command=x)
            file1 = Toplevel(root)
            if e=="X":
                s=entry1.get()+" won"
            elif e=="O":
                s=entry2.get()+" won"
            l1=Label(file1,text=s,font="Times 20 bold",bg="red",fg="white",height=5,width=20)
            l1.pack(fill=X)
            l2=Label(file1,text="Developed by Mayank Juyal",bg="green",fg="cyan",height=2)
            l2.pack(fill=X)
            a=0
        else:
            a=a+1;
            if a==9:
                file1=Toplevel(root)
                l1=Label(file1,text="game ended in a draw",font="Times 20 bold",bg="red",fg="white",height=5,width=20)
                l1.pack(fill=X)
                l2=Label(file1,text="Developed by Mayank Juyal",bg="green",fg="cyan",height=2)
                l2.pack(fill=X)
                a=0
    button1=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button1))
    button1.grid(row=1,column=0,sticky=S+N+E+W)

    button2=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button2))
    button2.grid(row=1,column=1,sticky=S+N+E+W)

    button3=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button3))
    button3.grid(row=1,column=2,sticky=S+N+E+W)

    button4=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button4))
    button4.grid(row=2,column=0,sticky=S+N+E+W)

    button5=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button5))
    button5.grid(row=2,column=1,sticky=S+N+E+W)

    button6=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button6))
    button6.grid(row=2,column=2,sticky=S+N+E+W)

    button7=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button7))
    button7.grid(row=3,column=0,sticky=S+N+E+W)

    button8=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button8))
    button8.grid(row=3,column=1,sticky=S+N+E+W)

    button9=Button(root,text=" ",font=("Times 20 bold"),bg="grey",fg="white",width=8,height=4,command=lambda:game(button9))
    button9.grid(row=3,column=2,sticky=S+N+E+W)

entbutton=Button(r,text="start",bg="black",fg="white",command=enter)
entbutton.grid(row=3,column=1,columnspan=2)
r.mainloop()
