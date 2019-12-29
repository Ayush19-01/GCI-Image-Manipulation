import PIL.Image
import os
from resizeimage import resizeimage
from tkinter import filedialog
import tinify
from tkinter import *
tinify.key="scp7tv5trlLwgDKVPvCLcYS6Pzdv2njN"
def selectfile(event):
    global ffs
    global z
    global button1
    global var
    global label_1
    global label_2
    global entry1
    global button2
    global label3

    var=StringVar()
    ffs = filedialog.askopenfilename(initialdir =  "/", title = "Select an image", filetypes =(("Image File","*.png"),))
    print(ffs)
    label_1.place_forget()
    label_2.place_forget()
    button1.place_forget()
    l = len(ffs)
    strg=""
    for i in range(-1, -l - 1, -1):
        strg += ffs[i]

    x = strg.find("/")
    l -= x
    z = ffs[:l]
    z += "newimages"
    try:
        os.mkdir(z)
        os.chdir(z)
    except:
        print("Directory already present!")
        os.chdir(z)
    label3 = Label(root1, text="Enter the name of the output file", font=("roboto", 20), bg="#220047", fg="#CE9141")
    label3.place(x=60, y=10)
    entry1 = Entry(root1, textvar=var, width=50)
    entry1.place(x=100, y=60)
    button2= Button(root1, text="Compress", font=("roboto", 20), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button2.bind("<Button-1>", convert)
    button2.place(x=180, y=90)
def convert2():
    global xinp
    global label4
    source = tinify.from_file(xinp)
    source.to_file(xinp)
    label4.place_forget()
    label5 = Label(root1, text="Conversion done succesfully", font=("roboto", 25), bg="#220047", fg="#CE9141")
    label5.place(x=50, y=10)
    button3 = Button(root1, text="Quit", font=("roboto", 20), bg="#CE9141", fg="#220047",
                     activeforeground="#CE9141",
                     activebackground="#220047")
    button3.bind("<Button-1>", destruct)
    button3.place(x=210, y=80)
    print("Finished")
def convert(event):
    global xinp
    global label4
    global label3
    global entry1
    global button2
    global var
    global ffs
    entry1.place_forget()
    button2.place_forget()
    label3.place_forget()
    label4 =Label(root1, text="Please wait...\nManipulating the file...", font=("roboto", 30), bg="#220047", fg="#CE9141")
    label4.place(x=60, y=10)
    print(ffs)
    front = open(ffs, "rb+")
    img = PIL.Image.open(front)
    cover = resizeimage.resize_contain(img,[300,300])
    xinp = var.get()
    xinp+=".png"
    cover.save(xinp,img.format)
    convert2()
def body1():
    global root1
    global Username
    global button1
    global label_1
    global label_2
    root1 = Tk()
    root1.resizable(0, 0)
    Username = StringVar()
    root1.geometry("500x150")
    root1.config(bg="#220047")
    root1.title("Welcome")
    label_1 = Label(root1, text="Image Manipulator", font=("roboto", 30), bg="#220047", fg="#CE9141")
    label_1.place(x=76, y=10)
    label_2 = Label(root1, text="Select a file to manipulate", font=("roboto", 19), bg="#220047", fg="#CE9141")
    label_2.place(x=40, y=90)
    button1 = Button(root1, text="Select", font=("roboto", 20), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button1.bind("<Button-1>",selectfile)
    button1.place(x=350, y=80)
    root1.mainloop()
def destruct(event):
    root1.destroy()
body1()