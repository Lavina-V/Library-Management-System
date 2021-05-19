from BackgroundPage import *
from tkinter import messagebox
from Components.ButtonComponent import GrayButton
from DatabaseHelper import *
from Components.MessageComponent import WhiteMessage
from LoginWindowPage import *
from SignUpWindowPage import *


class MainPage(BackgroundPage):
    def __init__(self, root):
        super().__init__(root)
        self.root.geometry('900x600')
        self.root.state('normal')
        self.add_widgets()

    def add_widgets(self):
        self.admin_button = GrayButton(self.panel, "Librarian login", lambda: Login("Librarian", self))
        self.admin_button.place(x=450, y=150)
        self.user_button = GrayButton(self.panel, "Student login", lambda: Login("Student", self))
        self.user_button.place(x=620, y=150)
        self.new_user_button = GrayButton(self.panel, "New Student? Sign up here", SignUp, borderwidth=2, relief=RIDGE)
        self.new_user_button.place(x=550, y=220)

        self.contact = WhiteMessage(self.f, text="Contact Details Here!")
        self.contact_detail = WhiteMessage(self.f,
                                           text=" City Library,\n 221B Baker Street\n London\n +44 20 7234 3456",
                                           font=("Times New Roman", 15, "bold", "italic"))
        self.contact.place(x=500, y=320)
        self.contact.bind("<Button-1>", self.show_contact_details)

    def show_contact_details(self, event):
        self.contact_detail.place(x=500, y=400)

    def redirect_to_page(self, result, login_type):
        self.f.destroy()
        if login_type == "Librarian":
            import LibrarianHomePage as librarian
            librarian.LibrarianHomePage(self.root,result)
        elif login_type == "Student":
            import StudentHomePage
            print(result)
            StudentHomePage.StudentHomePage(self.root, result)


if (__name__ == "__main__"):
    root = Tk()
    m = MainPage(root)
    root.mainloop()
