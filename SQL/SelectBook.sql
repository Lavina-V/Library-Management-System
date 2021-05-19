Create Table SelectBook
(
	SelectId int auto_increment key,
	BookId int,
    StudentId int,
    BookDetails varchar(1000),
    BookGenre varchar(1000),
    IsGranted int default 0
    
)