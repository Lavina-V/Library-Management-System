CREATE TABLE Librarian
(
	LibrarianId int auto_increment key,
	LibrarianName varchar(200),
	LibrarianPassword varchar(200),
    LibrarianEmail varchar(200)
   
)

Insert into Librarian(LibrarianName,LibrarianPassword,LibrarianEmail)
Values('Harsha','harshi','harshadubey@gmail.com')