from tkinter import *
from tkinter.font import Font
import qrcode  

root=Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#00BFFF")
root.resizable(False,False)

#icon image
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)
  

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")
    
    global Image
    Image=PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)
    
    
Image_view=Label(root,bg="#00BFFF")
Image_view.pack(padx=50,pady=10,side=RIGHT)

myfont =Font(
    family = 'Times',
    size = 35,
    weight = 'bold',
    slant = 'roman',
    underline = 0,
    overstrike = 0
)

Label(root,text="Generate the required \n QR !!",fg="#483D8B",bg="#00BFFF",font=myfont).place(x=30,y=30)
title = Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)

Button(root,text ="Generate",width=20,height=2,bg="black",fg="#00BFFF",command=generate).place(x=50,y=300)


root.mainloop()

