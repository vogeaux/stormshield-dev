from tkinter import *
from tkinter import filedialog, messagebox
from pythonping import ping
import os
from shutil import copyfile
import datetime

#i love my code


def text ():
    global filesavefile
    x = datetime.datetime.now()
    getFuture=mentFuture.get()
    getGW=mentGW.get()
    getNom_Du_Client=ment_Nom_Du_Client.get()
    savefile=getNom_Du_Client+x.strftime("-%d-%m-%Y")
    filesavefile="./"+savefile+".cli"
    #copyfile(myOpen_myOpenserver,"./"+savefile+".cli")
    with open(myOpen_myOpenserver, "r+") as f:
        old = f.read()# read everything in the file
        print(old,filesavefile)
        old = old.replace("{GETIPFUTURE}", getFuture)
        old = old.replace("{GETGW}", getGW)
        #f.seek(0)  # rewind
        print(old)
        f.close()
    with open(filesavefile, "w") as f:
        f.write(old)
        f.close()


def co():
    try:
        IP = mentIP.get()
        IPs = ping(IP, count=1)
        print(IPs)
        if "Request timed out" in str(IPs):
            print(IP, 'is down!')
            valide_connect.configure(text="X", background="red")
            entry_2.configure(background="red")

        if "Reply" in str(IPs):
            print(IP, 'is up!')
            valide_connect.configure(text="V",background= "green")
            entry_2.configure(background="green")
    except:
        print("erreur")
        valide_connect.configure(text="X", background="red")
        entry_2.configure(background="red")


def myOpenclient():
    global myOpen_myOpenserver
    global myOpen_myOpenserverfile
    myOpen_myOpenserver =(filedialog.askopenfilename())
    mlabel2_myOpenserver.configure(text=myOpen_myOpenserver,background="green")

def transf_file():
    getFuture = mentFuture.get()
    getGW = mentGW.get()
    getmentIP=mentIP.get()
    getmenpassword=mentpassword.get()
    getmentuser=mentuser.get()
    print(f'nsrpc.exe -c "{filesavefile}" "{getmentuser}:{getmenpassword}@{getmentIP}')
    os.system(f'nsrpc.exe -c "{filesavefile}" "{getmentuser}:{getmenpassword}@{getmentIP}')
    #print(f'nsrpc.exe -c "{myOpen_myOpenserver}" "{getmentuser}:{getmenpassword}@{getmentIP}')
    #os.system(f'nsrpc.exe -c "{myOpen_myOpenserver}" "{getmentuser}:{getmenpassword}@{getmentIP}')

def mAbout():
    messagebox.showinfo(title="About",message="The app is open source / Support app  :  kevin.hamon1998@gmail.com")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        myApp.destroy()

## fonction par touche ---- fin



## cadre de l'application ---- début

myApp = Tk()
myApp.geometry('500x500')
myApp.title("stormshield transfert")
myApp.resizable(width=False, height=False)

## cadre de l'application ---- fin

##variable ecriture ---- début
mentIP = StringVar()
ment_Nom_Du_Client = StringVar()
mentuser = StringVar()
mentpassword = StringVar()
mentfile_linux = StringVar()
mentFuture = StringVar()
mentGW = StringVar()

##variable ecriture ---- fin

## titre de pague



label_0 = Label(myApp, text="stormshield transfert",width=20,font=("bold", 20),background=None)
label_0.place(x=90,y=20)


label_2 = Label(myApp, text="IP Du Storm Actuel: ",width=20,font=("bold", 10))
label_2.place(x=5,y=60)
entry_2 = Entry(myApp,textvariable=mentIP)
entry_2.place(x=150,y=60)

label_21 = Label(myApp, text="nom du client: ",width=20,font=("bold", 10))
label_21.place(x=240,y=60)
entry_21 = Entry(myApp,textvariable=ment_Nom_Du_Client)
entry_21.place(x=370,y=60)

label_3 = Label(myApp, text="Nom d'utilisateur : ",width=20,font=("bold", 10))
label_3.place(x=15,y=90)
entry_3 = Entry(myApp,textvariable=mentuser)
entry_3.place(x=150,y=90)

label_1 = Label(myApp, text="Mots de passe : ",width=20,font=("bold", 10))
label_1.place(x=15,y=110)
entry_1 = Entry(myApp,textvariable=mentpassword)
entry_1.place(x=150,y=110)


label_5 = Label(myApp, text="IP Du Storm Future : ",width=20,font=("bold", 10))
label_5.place(x=2,y=150)
entry_5 = Entry(myApp,textvariable=mentFuture)
entry_5.place(x=160,y=150)

label_5 = Label(myApp, text="IP GW Du Storm Future : ",width=20,font=("bold", 10))
label_5.place(x=2,y=190)
entry_5 = Entry(myApp,textvariable=mentGW)
entry_5.place(x=160,y=190)

mButton_valide = Button(myApp,text="test de ping", command = co).place(x=300,y=100)
valide_connect = Label(myApp, text="-",background= "yellow")
valide_connect.place(x=450,y=100)






app_apache_button8 = Button(myApp, text="open conf", command=myOpenclient).place(x=340, y=300)

app_apache_button9 = Button(myApp, text="test conf", command=text).place(x=340, y=350)

mButton_connection = Button(myApp,text="TRANSFERT GO", command =transf_file).place(x=200,y=450)


label_0 = Label(myApp, text="répertoire dans le pc:")
label_0.place(x=1,y=300)
mlabel2_myOpenserver = Label(myApp, text="")
mlabel2_myOpenserver.place(x=1, y=320)


#app_apache1_text = Entry(myApp)
#app_apache1_text.place(x=120, y=330,width=180)


##log = Entry(myApp,text="log",background= "black")
##log.place(x=150,y=250,width=300,height=200)




menubar = Menu(myApp)

#create the file component of that menubar
filemenu = Menu(menubar, tearoff=0)

#Add the sub headings to the file menu
filemenu.add_command(label="Close", command=mQuit)
menubar.add_cascade(label="File",menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help docs",command=None)
helpmenu.add_command(label="About",command=mAbout)


menubar.add_cascade(label="Help",menu=helpmenu)






#add menubar to the window
myApp.config(menu=menubar)

myApp.mainloop()