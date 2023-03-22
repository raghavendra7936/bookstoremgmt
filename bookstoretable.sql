CREATE TABLE 'bookstore' (
  'Book_name' varchar(50) DEFAULT NULL,
  'Author' varchar(50) DEFAULT NULL,
  'Genre' varchar(15) DEFAULT NULL,
  'ISBN' int(10) DEFAULT NULL,
  'BorrowedStatus' char(5) DEFAULT NULL,
  'BorrowedDate' date DEFAULT NULL,
  'ReturnDate' date DEFAULT NULL,
  'ReturnStatus' char(5) DEFAULT NULL
)