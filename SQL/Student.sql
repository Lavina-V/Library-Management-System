Create table Student
(StudentId 		int 	auto_increment key,
 StudentName 		varchar(200),
 StudentPassword 	varchar(200),
 StudentContact 	bigint
)

Insert into Student(StudentName,StudentPassword,
StudentContact)
Values('Naina','naina',7507840801)