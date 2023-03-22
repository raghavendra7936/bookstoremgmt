import mysql.connector as mycon
con = mycon.connect(host = 'localhost', database = 'mysql', user = 'root', password = '')
mycursor = con.cursor()

def allbooks():
    with con.cursor() as cursor:
        cursor.execute("select ISBN, Book_name, Author, Genre, BorrowedStatus, BorrowedDate from bookstore;")
        result = [
           row
           for row in cursor.fetchall()
        ]
    return result    

def searchbookname(name):
    with con.cursor() as cursor:
        cursor.execute("select ISBN, Book_name, Author, Genre, BorrowedStatus, BorrowedDate from bookstore where book_name like '%%%s%%'" %(name,))
        result = [
           row
           for row in cursor.fetchall()
        ]
    return result        

def searchauthor(author):
    with con.cursor() as cursor:
        cursor.execute("select ISBN, Book_name, Author, Genre, BorrowedStatus, BorrowedDate from bookstore where author like '%%%s%%'" %(author,))
        result = [
           row
           for row in cursor.fetchall()
        ]
    return result

def searchgenre(genre):
    with con.cursor() as cursor:
        cursor.execute("select ISBN, Book_name, Author, Genre, BorrowedStatus, BorrowedDate from bookstore where genre = '%s'" %(genre,))
        result = [
           row
           for row in cursor.fetchall()
        ]
    return result    

def searchisbn(ISBN):
    with con.cursor() as cursor:
        cursor.execute("select ISBN, Book_name, Author, Genre, BorrowedStatus, BorrowedDate from bookstore where ISBN = '%s'" %(ISBN,))
        result = [
           row
           for row in cursor.fetchall()
        ]
    return result