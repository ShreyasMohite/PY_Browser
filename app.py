from tkinter import *
from PIL import ImageTk
from PIL import *
from tkinter import ttk
import tkinter
import webbrowser

class Browser:
    def __init__(self,root):
        self.root=root
        self.root.title("Web Browser")
        self.root.geometry("820x455")
        self.root.iconbitmap("logo990.ico")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_google['background']="black"
            but_google['foreground']="cyan"
        def on_leave1(e):
            but_google['background']="SystemButtonFace"
            but_google['foreground']="SystemButtonText"


        def on_enter2(e):
            but_youtube['background']="black"
            but_youtube['foreground']="cyan"
        def on_leave2(e):
            but_youtube['background']="SystemButtonFace"
            but_youtube['foreground']="SystemButtonText"

        def on_enter3(e):
            but_github['background']="black"
            but_github['foreground']="cyan"
        def on_leave3(e):
            but_github['background']="SystemButtonFace"
            but_github['foreground']="SystemButtonText"

        def on_enter4(e):
            but_stackoverflow['background']="black"
            but_stackoverflow['foreground']="cyan"
        def on_leave4(e):
            but_stackoverflow['background']="SystemButtonFace"
            but_stackoverflow['foreground']="SystemButtonText"

        def on_enter5(e):
            but_instagram['background']="black"
            but_instagram['foreground']="cyan"
        def on_leave5(e):
            but_instagram['background']="SystemButtonFace"
            but_instagram['foreground']="SystemButtonText"

        
        def on_enter6(e):
            but_facebook['background']="black"
            but_facebook['foreground']="cyan"
        def on_leave6(e):
            but_facebook['background']="SystemButtonFace"
            but_facebook['foreground']="SystemButtonText"

        
        def on_enter7(e):
            but_snapchat['background']="black"
            but_snapchat['foreground']="cyan"
        def on_leave7(e):
            but_snapchat['background']="SystemButtonFace"
            but_snapchat['foreground']="SystemButtonText"

        
        def on_enter8(e):
            but_twitter['background']="black"
            but_twitter['foreground']="cyan"
        def on_leave8(e):
            but_twitter['background']="SystemButtonFace"
            but_twitter['foreground']="SystemButtonText"

        def on_enter9(e):
            but_whatsapp['background']="black"
            but_whatsapp['foreground']="cyan"
        def on_leave9(e):
            but_whatsapp['background']="SystemButtonFace"
            but_whatsapp['foreground']="SystemButtonText"

        def on_enter10(e):
            but_wikipedia['background']="black"
            but_wikipedia['foreground']="cyan"
        def on_leave10(e):
            but_wikipedia['background']="SystemButtonFace"
            but_wikipedia['foreground']="SystemButtonText"

        def on_enter11(e):
            but_gmail['background']="black"
            but_gmail['foreground']="cyan"
        def on_leave11(e):
            but_gmail['background']="SystemButtonFace"
            but_gmail['foreground']="SystemButtonText"

        def on_enter12(e):
            but_w3school['background']="black"
            but_w3school['foreground']="cyan"
        def on_leave12(e):
            but_w3school['background']="SystemButtonFace"
            but_w3school['foreground']="SystemButtonText"

        def on_enter13(e):
            but_geeksforgeeks['background']="black"
            but_geeksforgeeks['foreground']="cyan"
        def on_leave13(e):
            but_geeksforgeeks['background']="SystemButtonFace"
            but_geeksforgeeks['foreground']="SystemButtonText"

        def on_enter14(e):
            but_quora['background']="black"
            but_quora['foreground']="cyan"
        def on_leave14(e):
            but_quora['background']="SystemButtonFace"
            but_quora['foreground']="SystemButtonText"

        def on_enter15(e):
            but_slack['background']="black"
            but_slack['foreground']="cyan"
        def on_leave15(e):
            but_slack['background']="SystemButtonFace"
            but_slack['foreground']="SystemButtonText"



        def hello():
            print("hello")

        def google():
            webbrowser.open('https://www.google.com/')


        def youtube():
            webbrowser.open('https://youtube.com/')

        def github():
            webbrowser.open('https://github.com/')

        def stackoverflow():
            webbrowser.open('https://stackoverflow.com/')

        def instagram():
            webbrowser.open('https://www.instagram.com/')

        def facebook():
            webbrowser.open('https://www.facebook.com/')

        def twitter():
            webbrowser.open('https://twitter.com/login?lang=en')

        def whatsapp():
            webbrowser.open('https://web.whatsapp.com/')

        def wikipedia():
            webbrowser.open('https://en.wikipedia.org/wiki/Wikipedia')

        def gmail():
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')

        def snapchat():
            webbrowser.open('https://www.snapchat.com/')

        def w3schools():
            webbrowser.open('https://www.w3schools.com/')

        def gfg():
            webbrowser.open('https://www.geeksforgeeks.org/')

        def quora():
            webbrowser.open('https://www.quora.com/')
        
        def slack():
            webbrowser.open('https://slack.com/intl/en-in/')



#==========================frame=========================#
        
        mainframe=Frame(self.root,width=820,height=455,relief="ridge",bd=3,bg="gray77")
        mainframe.place(x=0,y=0)


        

        self.original_google=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\google.jpg")
        self.resized_goolge=self.original_google.resize((150, 110),Image.ANTIALIAS)
        self.image_google=ImageTk.PhotoImage(self.resized_goolge)
        but_google=Button(mainframe,image=self.image_google,text="GOOGLE",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=google)
        but_google.place(x=0,y=0)
        but_google.bind("<Enter>",on_enter1)
        but_google.bind("<Leave>",on_leave1)


        self.original_youtube=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\youtubes.png")
        self.original_youtube=self.original_youtube.resize((150, 110),Image.ANTIALIAS)
        self.original_youtube=ImageTk.PhotoImage(self.original_youtube)
        but_youtube=Button(mainframe,image=self.original_youtube,text="YOUTUBE",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=youtube)
        but_youtube.place(x=163,y=0)
        but_youtube.bind("<Enter>",on_enter2)
        but_youtube.bind("<Leave>",on_leave2)

        self.original_github=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\github.png")
        self.original_github=self.original_github.resize((150, 110),Image.ANTIALIAS)
        self.original_github=ImageTk.PhotoImage(self.original_github)
        but_github=Button(mainframe,image=self.original_github,text="GITHUB",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=github)
        but_github.place(x=325,y=0)
        but_github.bind("<Enter>",on_enter3)
        but_github.bind("<Leave>",on_leave3)

        self.original_stackoverflow=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\stackoverflow.png")
        self.original_stackoverflow=self.original_stackoverflow.resize((150, 110),Image.ANTIALIAS)
        self.original_stackoverflow=ImageTk.PhotoImage(self.original_stackoverflow)
        but_stackoverflow=Button(mainframe,image=self.original_stackoverflow,text="STACKOVERFLOW",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=stackoverflow)
        but_stackoverflow.place(x=487,y=0)
        but_stackoverflow.bind("<Enter>",on_enter4)
        but_stackoverflow.bind("<Leave>",on_leave4)

        self.original_instagram=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\instagram.jpg")
        self.original_instagram=self.original_instagram.resize((150, 110),Image.ANTIALIAS)
        self.original_instagram=ImageTk.PhotoImage(self.original_instagram)
        but_instagram=Button(mainframe,image=self.original_instagram,text="INSTAGRAM",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=instagram)
        but_instagram.place(x=651,y=0)
        but_instagram.bind("<Enter>",on_enter5)
        but_instagram.bind("<Leave>",on_leave5)

        self.original_facebook=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\facebook.jpg")
        self.original_facebook=self.original_facebook.resize((150, 110),Image.ANTIALIAS)
        self.original_facebook=ImageTk.PhotoImage(self.original_facebook)
        but_facebook=Button(mainframe,image=self.original_facebook,text="FACEBOOK",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=facebook)
        but_facebook.place(x=0,y=150)
        but_facebook.bind("<Enter>",on_enter6)
        but_facebook.bind("<Leave>",on_leave6)

        self.original_twitter=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\twitter.jpg")
        self.original_twitter=self.original_twitter.resize((150, 110),Image.ANTIALIAS)
        self.original_twitter=ImageTk.PhotoImage(self.original_twitter)
        but_twitter=Button(mainframe,image=self.original_twitter,text="TWITTER",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=twitter)
        but_twitter.place(x=163,y=150)
        but_twitter.bind("<Enter>",on_enter8)
        but_twitter.bind("<Leave>",on_leave8)


        self.original_whatsapp=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\whatsapp.png")
        self.original_whatsapp=self.original_whatsapp.resize((150, 110),Image.ANTIALIAS)
        self.original_whatsapp=ImageTk.PhotoImage(self.original_whatsapp)
        but_whatsapp=Button(mainframe,image=self.original_whatsapp,text="WHATSAPP",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=whatsapp)
        but_whatsapp.place(x=325,y=150)
        but_whatsapp.bind("<Enter>",on_enter9)
        but_whatsapp.bind("<Leave>",on_leave9)


        self.original_wikipedia=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\wikipedia.png")
        self.original_wikipedia=self.original_wikipedia.resize((150, 110),Image.ANTIALIAS)
        self.original_wikipedia=ImageTk.PhotoImage(self.original_wikipedia)
        but_wikipedia=Button(mainframe,image=self.original_wikipedia,text="WIKIPEDIA",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=wikipedia)
        but_wikipedia.place(x=487,y=150)
        but_wikipedia.bind("<Enter>",on_enter10)
        but_wikipedia.bind("<Leave>",on_leave10)


        self.original_gmail=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\gmail.jpg")
        self.original_gmail=self.original_gmail.resize((150, 110),Image.ANTIALIAS)
        self.original_gmail=ImageTk.PhotoImage(self.original_gmail)
        but_gmail=Button(mainframe,image=self.original_gmail,text="GMAIL",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=gmail)
        but_gmail.place(x=651,y=150)    
        but_gmail.bind("<Enter>",on_enter11)
        but_gmail.bind("<Leave>",on_leave11)

        




        self.original_snapchat=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\snapchat.jpg")
        self.original_snapchat=self.original_snapchat.resize((150, 110),Image.ANTIALIAS)
        self.original_snapchat=ImageTk.PhotoImage(self.original_snapchat)
        but_snapchat=Button(mainframe,image=self.original_snapchat,text="SNAPCHAT",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=snapchat)
        but_snapchat.place(x=0,y=300)
        but_snapchat.bind("<Enter>",on_enter7)
        but_snapchat.bind("<Leave>",on_leave7)

        self.original_w3school=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\W3Schools.png")
        self.original_w3school=self.original_w3school.resize((150, 110),Image.ANTIALIAS)
        self.original_w3school=ImageTk.PhotoImage(self.original_w3school)
        but_w3school=Button(mainframe,image=self.original_w3school,text="W3SCHOOLS",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=w3schools)
        but_w3school.place(x=163,y=300)
        but_w3school.bind("<Enter>",on_enter12)
        but_w3school.bind("<Leave>",on_leave12)


        self.original_gfg=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\gfg.png")
        self.original_gfg=self.original_gfg.resize((150, 110),Image.ANTIALIAS)
        self.original_gfg=ImageTk.PhotoImage(self.original_gfg)
        but_geeksforgeeks=Button(mainframe,image=self.original_gfg,text="GEEKS FOR GEEKS",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=gfg)
        but_geeksforgeeks.place(x=325,y=300)
        but_geeksforgeeks.bind("<Enter>",on_enter13)
        but_geeksforgeeks.bind("<Leave>",on_leave13)


        self.original_quora=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\quora.png")
        self.original_quora=self.original_quora.resize((150, 110),Image.ANTIALIAS)
        self.original_quora=ImageTk.PhotoImage(self.original_quora)
        but_quora=Button(mainframe,image=self.original_quora,text="QUORA",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=quora)
        but_quora.place(x=487,y=300)
        but_quora.bind("<Enter>",on_enter14)
        but_quora.bind("<Leave>",on_leave14)

        self.original_slack=Image.open(r"C:\Users\SHREYAS\Desktop\shreyas python\Py_browser\image\slack.jpg")
        self.original_slack=self.original_slack.resize((150, 110),Image.ANTIALIAS)
        self.original_slack=ImageTk.PhotoImage(self.original_slack)
        but_slack=Button(mainframe,image=self.original_slack,text="SLACK",font=('times new roman',12),fg="black",bd=4,cursor="hand2",compound=TOP,command=slack)
        but_slack.place(x=651,y=300)
        but_slack.bind("<Enter>",on_enter15)
        but_slack.bind("<Leave>",on_leave15)

        




if __name__ == "__main__":
    root=Tk()
    app=Browser(root)
    root.mainloop()