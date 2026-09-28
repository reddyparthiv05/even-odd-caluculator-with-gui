import tkinter as tk 
def even_odd():
    number=int(Entry1.get())
    if number%2==0:
        label2.config(text='the number is even')  
    else:
        label2.config(text='the number is odd')  
root=tk.Tk()
root.title('even odd caluculator')
root.geometry('500x500')
label1=tk.Label(root,text='enter the number')
label1.place(x=100,y=100)
Entry1=tk.Entry(root)
Entry1.place(x=150,y=150)
button=tk.Button(root,text='caluculate',command=even_odd)
button.place(x=200,y=200)
label2=tk.Label(root,text='')
label2.place(x=300,y=300)
root.mainloop()