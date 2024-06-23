from tkinter import *
from customtkinter import *

class POS:
    def __init__(self,window):
        self.window = window
        self.window.geometry('1360x720+0+0')
        self.window.title("SERENPOS")

        set_appearance_mode('dark')
        set_default_color_theme('dark-blue')
        self.navigationframe = CTkFrame(self.window,width = 1360,height = 60)
        self.navigationframe.pack(pady=0,padx =0)
        self.navigationframe.configure(fg_color = "lightblue")
        
    #   Frame Title
        self.nav_title = CTkLabel(self.navigationframe,text = "Serenity Point-Of-Sales System",font = ("Montserrat",20,'bold'),text_color="black")
        self.nav_title.place(relx = 0.02,rely =0.3)

        self.loginFrame=CTkFrame(self.window,width  = 500,height = 700,corner_radius=15)
        self.loginFrame.pack(padx = 200,pady = 50)

        # frame contents
        self.loginLabel = CTkLabel(self.loginFrame,text = "Login",font =("Montserrat",25,"bold"),text_color = "lightblue")
        self.loginLabel.place(relx = 0.42,rely = 0.1)

        self.entryuserID = CTkEntry(self.loginFrame,placeholder_text= "Username",font = ("Montserrat",15),width = 335,height=32,corner_radius=20)
        self.entryuserID.place(relx = 0.15,rely = 0.25)
        self.entryuserID.configure(placeholder_text_color = "lightblue")

        self.entryuserpass = CTkEntry(self.loginFrame,placeholder_text= "Password",font = ("Montserrat",15),width = 335,height=32,corner_radius=20)
        self.entryuserpass.place(relx = 0.15,rely = 0.4)
        self.entryuserpass.configure(placeholder_text_color = "lightblue")

        self.loginButton = CTkButton(self.loginFrame,text = "Login",text_color= "white",border_color='lightblue',corner_radius=20,width =335,height = 32,font = ("Montserrat",15,'bold'),hover_color="green")
        self.loginButton.place(relx = 0.15,rely = 0.55)

pos = CTk()
object = POS(pos)
pos.mainloop()