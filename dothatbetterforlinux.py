import os
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import tinify
from tkinter import *
tinify.key="scp7tv5trlLwgDKVPvCLcYS6Pzdv2njN"
def directory(event):
    global drt1
    global drt2
    global label1
    global label2
    global button1
    global label4
    label1.place_forget()
    button1.place_forget()
    label2.place_forget()
    label4 = Label(root1, text="Manipulating the images\nPlease wait...", font=("roboto", 30), bg="#220047",
                   fg="#CE9141")
    label4.place(x=45, y=25)
    drt1 = askdirectory()
    os.chdir(drt1)
    for j in os.listdir(drt1):
        if j.endswith(".jpg"):
            list1.append(j)
    print(list1)
    drt2="newphotos"

    try:
        os.mkdir(drt2)
        convert2()
    except:
        print("Directory already present!")
        convert2()
def convert2():
    global list1
    global label4
    global drt1
    global drt2
    for j in list1:
        img = PIL.Image.open(j)
        width, height = img.size
        if width>height:
            source = tinify.from_file(j)
            resized = source.resize(method="scale",width=400)
            os.chdir(drt2)
            resized.to_file(j)
            os.chdir(drt1)
        if width<height:
            source = tinify.from_file(j)
            resized = source.resize(method="scale", height=400)
            os.chdir(drt2)
            resized.to_file(j)
            os.chdir(drt1)
        if width==height:
            source = tinify.from_file(j)
            resized = source.resize(method="scale", height=400,width=400)
            os.chdir(drt2)
            resized.to_file(j)
            os.chdir(drt1)
    label4.place_forget()
    label5 = Label(root1, text="Conversion done succesfully", font=("roboto", 25), bg="#220047", fg="#CE9141")
    label5.place(x=65, y=10)
    button3 = Button(root1, text="Quit", font=("roboto", 20), bg="#CE9141", fg="#220047",
                     activeforeground="#CE9141",
                     activebackground="#220047")
    button3.bind("<Button-1>", destruct)
    button3.place(x=250, y=80)
    print("Finished")
def body1():
    global root1
    global Username
    global button1
    global label1
    global label2
    root1 = Tk()
    root1.resizable(0, 0)
    Username = StringVar()
    root1.geometry("600x150")
    root1.config(bg="#220047")
    root1.title("Image Manipulator")
    label1 = Label(root1, text="Image Manipulator", font=("roboto", 37), bg="#220047", fg="#CE9141")
    label1.place(x=70, y=1)
    label2 = Label(root1, text="Select the directory ", font=("roboto", 23), bg="#220047", fg="#CE9141")
    label2.place(x=60, y=90)
    button1 = Button(root1, text="Select", font=("roboto", 20), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button1.bind("<Button-1>",directory)
    button1.place(x=390, y=85)
    root1.mainloop()
def destruct(event):
    root1.destroy()
list1=[]
list2=[]
body1()
