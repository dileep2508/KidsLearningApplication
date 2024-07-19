from tkinter import *
from PIL import Image , ImageTk


def refresh():
    global count
    if count==0:
        label.configure(image=photo5)
        label1.configure(image=photo6)
        label2.configure(image=photo7)
        label3.configure(image=photo8)
        label4.configure(image=photo9)
        check1.configure(text="Ant")
        check3.configure(text="Books")
        check5.configure(text="Butterflies")
        check7.configure(text="Drums")
        check9.configure(text="Football")
        count=+1
    elif count==1:
        label.configure(image=photo10)
        label1.configure(image=photo11)
        label2.configure(image=photo12)
        label3.configure(image=photo13)
        label4.configure(image=photo14)
        check.configure(text="House")
        check2.configure(text="Balloons")
        check4.configure(text="Ladybug")
        check6.configure(text="Orange")
        check8.configure(text="Laptops")
        count+=1
    elif count==2:
        label.configure(image=photo15)
        label1.configure(image=photo16)
        label2.configure(image=photo17)
        label3.configure(image=photo18)
        label4.configure(image=photo19)
        check1.configure(text="Lions whiskers")
        check3.configure(text="mobiles")
        check5.configure(text="shoes")
        check7.configure(text="clouds")
        check9.configure(text="strawberry")
        count+=1
    elif count==3:
        label.configure(image=photo)
        label1.configure(image=photo1)
        label2.configure(image=photo2)
        label3.configure(image=photo3)
        label4.configure(image=photo4)
        check.configure(text=t1)
        check1.configure(text=t2)
        check2.configure(text=t3)
        check3.configure(text=t4)
        check4.configure(text=t5)
        check5.configure(text=t6)
        check6.configure(text=t7)
        check7.configure(text=t8)
        check8.configure(text=t9)
        check9.configure(text=t10)
        count=0

def OK():
    new_window=Toplevel(root)
    new_window.geometry("300x300")
    new_window.title("Options are:")
    new_window.resizable(False,False)
    lbl=Label(new_window,text="Correct options selected:")
    lbl.pack()
    global count
    pcount=0
    if count==0:
        if var3.get()==1:
            pcount+=1
            print(pcount)
        if var6.get()==1:
            pcount+=1
        if var7.get()==1:
            pcount+=1
        if var8.get()==1:
            pcount+=1
        if var9.get()==1:
            pcount+=1


    elif count==1:

        if var1.get()==1:
            pcount+=1
            print(pcount)
        if var3.get()==1:
            pcount+=1
        if var5.get()==1:
            pcount+=1
        if var7.get()==1:
            pcount+=1
        if var9.get()==1:
            pcount+=1

    elif count==2:
        if var.get() == 1:
            pcount += 1
        if var2.get() == 1:
            pcount += 1
        if var4.get() == 1:
            pcount += 1
        if var6.get() == 1:
            pcount += 1
        if var8.get() == 1:
            pcount += 1
    elif count==3:
        if var1.get() == 1:
            pcount += 1
            print(pcount)
        if var3.get() == 1:
            pcount += 1
        if var5.get() == 1:
            pcount += 1
        if var7.get() == 1:
            pcount += 1
        if var9.get() == 1:
            pcount += 1
    lab=Label(new_window,text=str(pcount))
    lab.pack()





root=Tk()
root.geometry("1200x800")

#========================FRAME1=======================================================
f1=Frame(root,bg="grey",bd=3,relief=RIDGE)
f1.place(x=50, y=130,width=300,height=250)
#========================FRAME2=======================================================
f2=Frame(root,bg="grey",bd=3,relief=RIDGE)
f2.place(x=360, y=130,width=300,height=250)
#========================FRAME3=======================================================
f3=Frame(root,bg="grey",bd=3,relief=RIDGE)
f3.place(x=670, y=130,width=300,height=250)
#========================FRAME4=======================================================
f4=Frame(root,bg="grey",bd=3,relief=RIDGE)
f4.place(x=50, y=390,width=300,height=250)
#========================FRAME5=======================================================
f5=Frame(root,bg="grey",bd=3,relief=RIDGE)
f5.place(x=360, y=390,width=300,height=250)

#========================HEADING OF PROJECT=======================================================
title=Label(root,text="KID'S LEARNING PROJECT",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
f6=Frame(root,bg="grey",bd=3,relief=RIDGE)
f6.place(x=50,y=650)
f7=Frame(root,bg="grey",bd=3,relief=RIDGE)
f7.place(x=920,y=650)
f8=Frame(root,bg="grey",bd=3,relief=RIDGE)
f8.place(x=50,y=680)
f9=Frame(root,bg="grey",bd=3,relief=RIDGE)
f9.place(x=180,y=680)

#========================image jpg open1========================================================
image=Image.open("pictures/1.jpeg")
photo=ImageTk.PhotoImage(image)

#========================image jpg open2========================================================
image1=Image.open("pictures/4.jpeg")
photo1=ImageTk.PhotoImage(image1)

#========================image jpg open3========================================================
image2=Image.open("pictures/3.jpeg")
photo2=ImageTk.PhotoImage(image2)


#========================image jpg open4========================================================
image3=Image.open("pictures/5.jpeg")
photo3=ImageTk.PhotoImage(image3)

#========================image jpg open5========================================================
image4=Image.open("pictures/6.jpeg")
photo4=ImageTk.PhotoImage(image4)
#========================image jpg open6========================================================
image5=Image.open("pictures/7.jpg")
photo5=ImageTk.PhotoImage(image5)
#========================image jpg open7========================================================
image6=Image.open("pictures/8.jpg")
photo6=ImageTk.PhotoImage(image6)
#========================image jpg open8========================================================
image7=Image.open("pictures/9.jpg")
photo7=ImageTk.PhotoImage(image7)
#========================image jpg open9========================================================
image8=Image.open("pictures/10.jpg")
photo8=ImageTk.PhotoImage(image8)
#========================image jpg open10========================================================
image9=Image.open("pictures/11.jpg")
photo9=ImageTk.PhotoImage(image9)
#========================image jpg open11========================================================
image10=Image.open("pictures/12.jpg")
photo10=ImageTk.PhotoImage(image10)
#========================image jpg open13========================================================
image11=Image.open("pictures/13.jpg")
photo11=ImageTk.PhotoImage(image11)
#========================image jpg open14========================================================
image12=Image.open("pictures/14.jpg")
photo12=ImageTk.PhotoImage(image12)
#========================image jpg open15========================================================
image13=Image.open("pictures/15.jpg")
photo13=ImageTk.PhotoImage(image13)
#========================image jpg open16========================================================
image14=Image.open("pictures/16.jpg")
photo14=ImageTk.PhotoImage(image14)
#========================image jpg open17========================================================
image15=Image.open("pictures/17.jpg")
photo15=ImageTk.PhotoImage(image15)
#========================image jpg open18========================================================
image16=Image.open("pictures/18.jpg")
photo16=ImageTk.PhotoImage(image16)
#========================image jpg open19========================================================
image17=Image.open("pictures/19.jpg")
photo17=ImageTk.PhotoImage(image17)
#========================image jpg open20========================================================
image18=Image.open("pictures/20.jpg")
photo18=ImageTk.PhotoImage(image18)
#========================image jpg open21========================================================
image19=Image.open("pictures/21.jpg")
photo19=ImageTk.PhotoImage(image19)
#========================image jpg open22========================================================
image20=Image.open("pictures/22.jpg")
photo20=ImageTk.PhotoImage(image20)



#========================labels========================================================
label=Label(f1,image=photo)
label1=Label(f2,image=photo1)
label2=Label(f3,image=photo2)
label3=Label(f4,image=photo3)
label4=Label(f5,image=photo4)
count=0

var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
t1="Princess"
t2="Doraemon"
t3="pitch"
t4="Penguin"
t5="Hello"
t6="Pony tail"
t7="monkey"
t8="Snake"
t9="Boom"
t10="lion"
check=Checkbutton(f8,text=t1,variable=var)
check.pack()
check1 = Checkbutton(f8, text=t2, variable=var1)
check1.pack()
check2 = Checkbutton(f8, text=t3, variable=var2)
check2.pack()
check3 = Checkbutton(f8, text=t4, variable=var3)
check3.pack()
check4 = Checkbutton(f8, text=t5, variable=var4)
check4.pack()
check5 = Checkbutton(f9, text=t6, variable=var5)
check5.pack()
check6 = Checkbutton(f9, text=t7, variable=var6)
check6.pack()
check7 = Checkbutton(f9, text=t8, variable=var7)
check7.pack()
check8 = Checkbutton(f9, text=t9, variable=var8)
check8.pack()
check9 = Checkbutton(f9, text=t10, variable=var9)
check9.pack()

#========================BUTTON========================================================
refresh=Button(f6,text="Refresh",command=refresh)
next=Button(f7,text="OK",command=OK)

#========================Packing everything========================================================
label.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
refresh.pack()
next.pack()




root.mainloop()
