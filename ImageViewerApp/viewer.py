from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title("Image View App")
root.geometry("420x450")

my_image1 = ImageTk.PhotoImage(Image.open("background1.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("background2.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("background3.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("background4.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("background5.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("background6.jpg"))
my_image7 = ImageTk.PhotoImage(Image.open("background7.jpg"))
my_image8 = ImageTk.PhotoImage(Image.open("background8.jpg"))
my_image9 = ImageTk.PhotoImage(Image.open("background9.jpg"))


imageList = [my_image1,my_image2,my_image3,my_image4,my_image5,my_image6,my_image7,my_image8,my_image9]

status = Label(root,text="Image 1 of " + str(len(imageList))+" " ,bd=5,anchor=CENTER,relief=SUNKEN)

my_label = Label(image=my_image1)
my_label.grid(row=0,column=0,columnspan=3)


def forward(imageNumber):
    global my_label
    global buttonBack
    global buttonForward

    my_label.grid_forget()
    my_label = Label(image=imageList[imageNumber - 1])

    buttonForward = Button(root,text="Next",command = lambda:forward(imageNumber + 1),fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))

    buttonBack = Button(root,text="Previos",command = lambda:back(imageNumber - 1),fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))

    if imageNumber == len(imageList):
        buttonForward = Button(root,text="Next",state=DISABLED,fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))
        

    my_label.grid(row=0,column=0,columnspan=3)
    buttonBack.grid(row=1,column=0)
    buttonForward.grid(row=1,column=2)

    status = Label(root,text="Image " + str(imageNumber) + " of " + str(len(imageList)) + " " ,bd=5,relief=SUNKEN,anchor=CENTER)
    status.grid(row=2,column=1,columnspan=3,sticky= W)

def back(imageNumber):

    global my_label
    global buttonBack
    global buttonForward

    my_label.grid_forget()
    my_label = Label(image=imageList[imageNumber - 1])

    buttonForward = Button(root,text="Next",command = lambda:forward(imageNumber + 1),fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))

    buttonBack = Button(root,text="Previos",command = lambda:back(imageNumber - 1),fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))

    if imageNumber == 1:
        buttonBack = Button(root,text="Previos",state=DISABLED,fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'))

    my_label.grid(row=0,column=0,columnspan=3)
    buttonBack.grid(row=1,column=0)
    buttonForward.grid(row=1,column=2)

    status = Label(root,text="Image " + str(imageNumber) + " of " +str(len(imageList))+" ",bd=5,anchor=CENTER,relief=SUNKEN)
    status.grid(row=2,column=1,columnspan=3,sticky = W)

def infomessage():
    messagebox.showinfo("App", '''This Is Picture App.

    Click Next for the next picture.
    Click Back for the back picture.
    You can browse picture from your computer but this 
    isn't save.
    ''')

def exit():
    response = messagebox.askquestion("Exit","Are you Sure ?")
    if response == "yes":
        root.destroy()
    else:
        pass

def showYourImage():

    lbl=Label(my_label)
    filenameShow =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    imageShow = Image.open(filenameShow)
    imageShow = imageShow.resize((400, 350), Image.ANTIALIAS)
    imageShow = ImageTk.PhotoImage(imageShow)
    lbl.configure(image=imageShow)
    lbl.image = imageShow  
    lbl.pack()
    
     

myMenu = Menu(root)
root.config(menu=myMenu)
fileMenu = Menu(myMenu)

myMenu.add_cascade(label="Settings",menu=fileMenu)
fileMenu.add_command(label = "Information", command = infomessage)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exit)
myMenu.add_cascade(label="Browse Image",command=showYourImage)


buttonBack = Button(root,text="Previos",fg="darkgreen",bg="lightgrey",font=('Sans','10','bold'),state = DISABLED)
buttonForward = Button(root,text="Next",fg="darkgreen",font=('Sans','10','bold'),bg="lightgrey",command = lambda:forward(2))


buttonBack.grid(row=1,column=0)
buttonForward.grid(row=1,column=2)
status.grid(row=2,column=1,columnspan=3,sticky = W)

root.mainloop()
