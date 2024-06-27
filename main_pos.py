from tkinter import *
from customtkinter import *

class POS:
    def __init__(self,window):
        self.window = window
        self.window.geometry('1360x720+0+0')
        self.window.title("SERENSMAN")
        
        self.navigationframe = CTkFrame(self.window,width = 1360,height = 60)
        self.navigationframe.pack(pady=0,padx =0)
        self.navigationframe.configure(fg_color = "lightblue")
        # Frame Title
        self.nav_title = CTkLabel(self.navigationframe,text = "Serenity Sales Manager",font = ("Montserrat",20,'bold'),text_color="black")
        self.nav_title.place(relx = 0.02,rely =0.3)

        self.LoginFrame()
        set_appearance_mode('dark')
        set_default_color_theme('dark-blue')
    def LoginFrame(self):
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
        self.entryuserpass.configure(placeholder_text_color = "lightblue",show = '*')

        self.loginButton = CTkButton(self.loginFrame,text = "Login",text_color= "white",border_color='lightblue',corner_radius=20,width =335,height = 32,font = ("Montserrat",15,'bold'),hover_color="green",command = self.main_dashboard)
        self.loginButton.place(relx = 0.15,rely = 0.55)

        self.forgot = CTkLabel(self.loginFrame,text = "Forgot password? Contact System Admin",font = ("Montserrat",14),text_color = "lightblue")
        self.forgot.place(relx = 0.15,rely =0.64)
        
    def main_dashboard(self):
        
        self.navigationframe.configure(fg_color = "lightblue")
        self.dashFrame = CTkFrame(self.window,width =1358,height =660)
        self.dashFrame.place(relx = 0,rely = 0.08)
        self.sideNav = CTkFrame(self.dashFrame,width =230,height=660,corner_radius=0)
        self.sideNav.place(relx =0,rely =0)
        self.sideNav.configure(fg_color = "lightblue")
        self.dashboard()
        # buttons and icons,
        self.dashboard_label =CTkButton(self.sideNav,text = "Dashboard",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command = self.dashboard)
        self.dashboard_label.place(relx = 0.15,rely = 0.05)

        self.new_sale_label =CTkButton(self.sideNav,text = "New Sale",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command = self.NewSale)
        self.new_sale_label.place(relx = 0.15,rely = 0.15)

        self.inventory_label =CTkButton(self.sideNav,text = "Inventory",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command = self.inventory)
        self.inventory_label.place(relx = 0.15,rely = 0.25)

        self.sales_report_label =CTkButton(self.sideNav,text = "Sales Reports",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command = self.SalesReport)
        self.sales_report_label.place(relx = 0.15,rely = 0.35)


        self.user_label =CTkButton(self.sideNav,text = "User",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command = self.user)
        self.user_label.place(relx = 0.15,rely = 0.45)

        self.setting_label =CTkButton(self.sideNav,text = "Settings",font = ("Montserrat",15,"bold"),text_color="black",fg_color="lightblue",hover_color= "white",command =self.settings)
        self.setting_label.place(relx = 0.15,rely = 0.55)
    
    def dashboard(self):
        self.dashboard_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.dashboard_window.place(relx = 0.17,rely =0)

        self.card_frame = CTkFrame(self.dashboard_window,width = 1060, height = 150)
        self.card_frame.place(relx = 0.02,rely = 0.02)
        
        self.total_product = CTkFrame(self.card_frame,width=200,height=100,fg_color="lightblue",corner_radius=10)
        self.total_product.place(relx=0.05,rely=0.1)
        
        self.low_stock = CTkFrame(self.card_frame,width=200,height=100,fg_color="lightblue",corner_radius=10)
        self.low_stock.place(relx=0.3,rely=0.1)
        
        self.out_of_stock = CTkFrame(self.card_frame,width=200,height=100,fg_color="lightblue",corner_radius=10)
        self.out_of_stock.place(relx=0.54,rely=0.1)
        
        self.suppliers = CTkFrame(self.card_frame,width=200,height=100,fg_color="lightblue",corner_radius=10)
        self.suppliers.place(relx=0.78,rely=0.1)

        self.card_frame = CTkFrame(self.dashboard_window,width = 1060, height = 230)
        self.card_frame.place(relx = 0.02,rely = 0.28)

        self.card_frame = CTkFrame(self.dashboard_window,width = 1060, height = 230)
        self.card_frame.place(relx = 0.02,rely = 0.65)
        
         
    def NewSale(self):
        self.sales_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.sales_window.place(relx = 0.17,rely =0)         

         
    def inventory(self):
        self.inventory_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.inventory_window.place(relx = 0.17,rely =0) 


    def SalesReport(self):
        self.report_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.report_window.place(relx = 0.17,rely =0) 
        
    def user(self):
        self.user_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.user_window.place(relx = 0.17,rely =0) 
    
    def settings(self):
        self.setting_window = CTkFrame(self.dashFrame,width = 1150,height =660,bg_color="lightblue")
        self.setting.place(relx = 0.17,rely =0) 
         
         
pos = CTk()
object = POS(pos)
pos.mainloop()