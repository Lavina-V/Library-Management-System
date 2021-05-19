from BackgroundPage import *
from Components.ButtonComponent import WhiteButton
from DatabaseHelper import *
from Components.table import SimpleTable
from Components.MessageComponent import WhiteMessage
from tkinter import messagebox

class LibrarianHomePage(BackgroundPage):
    def __init__(self, root, details):
        self.details=details
        print("Librarian home page called")
        super().__init__(root)
        self.root.state('zoomed')  # Maximize the screen
        self.admin_page = WhiteMessage(self.f, text="Librarian Page")
        self.admin_page.place(x=320, y=20)
        self.admin_name = WhiteMessage(self.f, text="Welcome " + self.details["LibrarianName"], width=200)
        self.admin_name.place(x=40, y=300)
        # message that displays admin's email address
        self.admin_email = WhiteMessage(self.f, text="Email " + self.details["LibrarianEmail"], width=300)
        self.admin_email.place(x=40, y=350)

        self.dct_IntVar={}
        # self.add_admin_details()
        self.add_buttons()

    def addbooks(self, ):
        self.addbtn_window = Toplevel()
        self.addbtn_window.title('Add Books')
        # self.main_page = main_page
        f = Frame(self.addbtn_window, height=200, width=400)
        l1 = Label(f, width=20, text="Enter bookname ")
        # storing this inside self because we need this later to get data
        self.bookname = Entry(f, width=30, fg='black', bg='white')
        # activative the cursor here
        self.bookname.focus_set()
        self.genre = Entry(f, width=30, fg='black', bg='white')
        l2 = Label(f, width=20, text="Enter genre ")
        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        self.bookname.grid(row=1, column=4, padx=10, pady=10)
        self.genre.grid(row=2, column=4, padx=10, pady=10)
        b1 = Button(f, text="Submit", height=2, width=10, command=self.execute)
        # # Whenever enter is pressed anywhere on this temporary root, call my validate function.
        # self.login_window.bind('<Return>', lambda event: self.validate())
        b1.grid(row=3, column=1, padx=10, sticky='e')
        b2 = Button(f, text="Reset", height=2, width=10, command=self.reset)
        b2.grid(row=3, column=4, padx=10, sticky='w')
        f.pack()
        f.grid_propagate(0)

    def reset(self):
        self.bookname.delete(0, END)
        self.genre.delete(0, END)

    def execute(self):
        bkName = self.bookname.get()
        bkGenre = self.genre.get()
        query = 'insert into books(BookName , BookGenre , BookAvailability) values(%s,%s,1)'
        parameters = (bkName, bkGenre)
        DatabaseHelper.execute_query(query,parameters)
        self.addbtn_window.destroy()
        #execute_query(query, parameters)

    def deletebooks(self):
        self.menu_frame = Frame(self.panel, height=600, width=600, bg="white")
        self.menu_frame.place(x=650, y=170)
        self.menu_frame.pack_propagate(0)

        self.raw_menu_image = Image.open("images/MainImgClgProj.1.jpg")
        self.raw_menu_image = self.raw_menu_image.resize((600, 600))
        self.menu_img = ImageTk.PhotoImage(self.raw_menu_image)
        self.menu_panel = Label(self.menu_frame, image=self.menu_img)
        self.menu_panel.pack()


        query = 'select * from books'
        result = DatabaseHelper.get_all_data(query)

        self.menu_items_frame = SimpleTable(self.menu_frame, rows=len(result), columns=len(result[0]), height=500,
                                            width=500)
        self.menu_items_frame.place(x=30, y=30)
        self.menu_items_frame.grid_propagate(0)



        self.text_font = ("MS Serif", 12)

        for i in range(1, len(result)):
            # Storing foodname as the key of dictionary
            self.dct_IntVar[result[i][0]] = IntVar()

        for r in range(len(result)):
            for c in range(len(result[0])):
                if (c == 0 and r != 0):
                    check_b = Checkbutton(self.menu_items_frame, text=result[r][c], font=self.text_font,
                                          variable=self.dct_IntVar.get(result[r][0]))  # to get FoodName
                    self.menu_items_frame.set(row=r, column=c, value=result[r][c], widget=check_b)
                else:
                    self.menu_items_frame.set(row=r, column=c, value=result[r][c], width=25)

        deleteme=WhiteButton(self.menu_frame, "Delete now", self.deleteme)
        deleteme.place(x=200,y=550)

    def deleteme(self):
        selected_items = []
        for key, value in self.dct_IntVar.items():
            if (value.get() == 1):
                selected_items.append(key)
                value.set(0)
        print(selected_items)
        if (len(selected_items) == 0):
            messagebox.showwarning("No order", "Please select atleast one food order to execute")

        else:
            query = 'DELETE FROM books WHERE bookid IN (%s)'
            result = DatabaseHelper.execute_all_data_multiple_input(query, selected_items)
            messagebox.showwarning('','Selected books are deleted')
            self.deletebooks()


    def showbooks(self):
        self.show_frame = Frame(self.panel, height=600, width=600, bg="white")
        self.show_frame.place(x=650, y=170)
        self.show_frame.pack_propagate(0)

        self.raw_show_image = Image.open("images/MainImgClgProj.1.jpg")
        self.raw_show_image = self.raw_show_image.resize((600, 600))
        self.show_img = ImageTk.PhotoImage(self.raw_show_image)
        self.show_panel = Label(self.show_frame, image=self.show_img)
        self.show_panel.pack()

        query = 'select * from books'
        result = DatabaseHelper.get_all_data(query)
        print(len(result[0]))
        self.show_items_frame = SimpleTable(self.show_frame, rows=len(result), columns=len(result[0]), height=500,
                                            width=500)
        self.show_items_frame.place(x=30, y=30)
        self.show_items_frame.grid_propagate(0)

        self.text_font = ("MS Serif", 12)


        for r in range(len(result)):
            for c in range(len(result[0])):
                if (c == 1 and r != 0):
                    self.show_items_frame.set(row=r, column=c, value=result[r][c], width=25)
                else:
                    self.show_items_frame.set(row=r, column=c, value=result[r][c],width=15)


    def librarian_logout(self):
        import MainPage
        self.f.destroy()
        self.redirect = MainPage.MainPage(self.root)

    def add_buttons(self):

        addbooks_button = WhiteButton(self.f, "Add books", self.addbooks)
        addbooks_button.place(x=400, y=90)
        deletebooks_button = WhiteButton(self.f, "Delete books", self.deletebooks)
        deletebooks_button.place(x=600, y=90)
        showbooks_button = WhiteButton(self.f, "Show books", self.showbooks)
        showbooks_button.place(x=800, y=90)

        self.logout = WhiteButton(self.f, "Logout", self.librarian_logout, width=10)
        self.logout.place(x=800, y=20)


if (__name__ == "__main__"):
    root = Tk()
    details = {'LibrarianId': 1, 'LibrarianName': 'harsha', 'LibrarianPassword': 'harshi',
                     'LibrarianEmail': 'harshadubey@gmail.com'
                     }
    a = LibrarianHomePage(root, details)
    root.mainloop()
