from BackgroundPage import *
from Components.MessageComponent import WhiteMessage
from Components.ButtonComponent import *
from DatabaseHelper import *
from Components.table import SimpleTable
from PIL import Image, ImageTk
from tkinter import messagebox
# from Queries.Customer import *
import datetime


class StudentHomePage(BackgroundPage):
    def __init__(self, root, student_details: dict):
        super().__init__(root)
        # store customer details dictionary here
        self.details = student_details
        self.root.state('zoomed')
        print(self.details)
        # create dictionary for food menu items
        self.dct_IntVar = {}
        self.m = WhiteMessage(self.panel, text=f"Welcome {self.details['StudentName']}")
        self.m.place(x=50, y=20)
        self.add_buttons()
        # Add the menu frame that has an image
        self.add_menu()

    def add_buttons(self):
        # Add 3 buttons- logout, check order status, order history
        self.logout = WhiteButton(self.f, text="Logout", command=self.customer_logout)
        self.logout.place(x=800, y=30)



    def customer_logout(self):
        import MainPage
        self.f.destroy()
        self.redirect = MainPage.MainPage(self.root)


    def add_menu(self):
        #  Add image, add 3 menu buttons
        # Add a button-> place order
        self.menu_frame = Frame(self.panel, height=600, width=600, bg="white")
        self.menu_frame.place(x=650, y=170)
        self.menu_frame.pack_propagate(0)

        self.raw_menu_image = Image.open("images/MainImgClgProj.1.jpg")
        self.raw_menu_image = self.raw_menu_image.resize((600, 600))
        self.menu_img = ImageTk.PhotoImage(self.raw_menu_image)
        self.menu_panel = Label(self.menu_frame, image=self.menu_img)
        self.menu_panel.pack()

        self.available_button = GrayButton(self.menu_frame, text="Available",
                                           command=lambda: self.add_book_items('Available'))
        self.available_button.place(x=30, y=550)

        self.not_available_button = GrayButton(self.menu_frame, text="Available Soon",
                                               command=lambda: self.add_book_items("Not Available"))
        self.not_available_button.place(x=430, y=550)




    def add_book_items(self, type):
        if(type=='Available'):
            query = 'select * from books where bookavailability=1'
            result = DatabaseHelper.get_all_data(query)

            self.menu_items_frame = SimpleTable(self.menu_frame, rows=len(result), columns=len(result[0]), height=500,
                                                width=500)
            self.menu_items_frame.place(x=30, y=30)
            self.menu_items_frame.grid_propagate(0)
            self.text_font = ("MS Serif", 12)



            for r in range(len(result)):
                for c in range(len(result[0])):
                    if (c == 0 and r != 0):
                        self.menu_items_frame.set(row=r, column=c, value=result[r][c])
                    else:
                        self.menu_items_frame.set(row=r, column=c, value=result[r][c], width=25)

        else:
            query = 'select * from books where bookavailability=0'
            result = DatabaseHelper.get_all_data(query)

            self.menu_items_frame = SimpleTable(self.menu_frame, rows=len(result), columns=len(result[0]), height=500,
                                                width=500)
            self.menu_items_frame.place(x=30, y=30)
            self.menu_items_frame.grid_propagate(0)
            self.text_font = ("MS Serif", 12)
            for r in range(len(result)):
                for c in range(len(result[0])):
                    self.menu_items_frame.set(row=r, column=c, value=result[r][c], width=25)



if __name__ == '__main__':
    root = Tk()
    details = {'StudentId': 4, 'StudentName': 'lavina', 'StudentPassword': 'lavina', 'StudentContact': 7507840801, }
    c = StudentHomePage(root, details)
    root.mainloop()
# 1	Naina	naina	7507840801
