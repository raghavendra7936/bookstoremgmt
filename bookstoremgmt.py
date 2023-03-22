from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import bookstoredb as bookdb


root =Tk()
root.title("Computer Mini-Project")
root.geometry("1200x600")

def showAllBooks():
    books = bookdb.allbooks()
    tree.delete(*tree.get_children())
    for i in books:
        tree.insert('', END, values=i)

def searchBooks():
    searchByOption = clicked2.get()
    searchText = e1.get()
    match searchByOption:
        case "Title":
           searchResults = bookdb.searchbookname(searchText)
        case "Author":
           searchResults = bookdb.searchauthor(searchText)
        case "Genre":
           searchResults = bookdb.searchgenre(searchText)
        case "ISBN":
           searchResults = bookdb.searchisbn(searchText)
    if (not searchResults):
        messagebox.showinfo("Search Results", "No matching books found!")
    else:
        tree.delete(*tree.get_children())
        for i in searchResults:
            tree.insert('', END, values=i)
#def show():
#    textbox.delete(0,"end")
#    textbox.insert(0,clicked.get() )
# def temp_text(e):
#     textbox.delete(0,"end")

# def leave(*args):
#     textbox.delete(0, 'end')
#     textbox.insert(0, ' ')
#     root.focus()
def displaySelectedItem(a):
    entry_id.delete(0,END)
    borrowed_status.delete(0,END)
    borrowed_on.delete(0,END)
    selectedItem = tree.selection()[0]
    entry_id.insert(0, tree.item(selectedItem)['values'][1])
    borrowed_status.insert(0, tree.item(selectedItem)['values'][4])
    borrowed_on.insert(0, tree.item(selectedItem)['values'][5])

#LABELS DEFINITION    
Label(root, text='BOOK STORE MANAGEMENT', font=("Arial,45")).grid(row=0,column=1)
#Label(root, text='What are you looking for: ', font=("Arial,45")).grid(row=2,column=0,padx=0)
Label(root, text=' ', font=("Arial,45")).grid(row=1,column=0)
Label(root, text=' ', font=("Arial,45")).grid(row=3,column=0)
Label(root,text='Book chosen:').grid(row=6)
entry_id= Entry(root, bg="white", width=50, borderwidth=2)  
entry_id.insert(0,"None selected")
entry_id.grid(row=6,column=1)
Label(root,text='').grid(row=7)
Label(root,text=" ").grid(row=10)
Label(root,text=" ").grid(row=11)
Label(root,text=" ").grid(row=12)

#DROPDOWN PROGRAM
# options = [
#     "Book name",
#     "Author name",
#     "Genre",
#     "ISBN Number"
# ]
# clicked = StringVar()
  
# clicked.set( "Book Name" )
# drop = OptionMenu( root , clicked , *options )
# drop.grid(row=2,column=1)

button = Button( root , text = "Fetch All Books" , command = showAllBooks ).grid(row=2,column=2)
lblGrid = Label(root, text='Book Listing', font=("Arial,45"))
lblGrid.grid(row=4,column=0)

#TEXTBOX OPERATION
# textbox = Entry(root, bg="white", width=50, borderwidth=2)
# textbox.insert(0,"None selected")
# textbox.grid(row=4,column=1)
# textbox.bind("<FocusIn>", temp_text)
# textbox.bind("<Leave>", leave)


#LISTBOX DATABASE
#columns = ('ISPN number', 'Book name', 'Author','Genre', 'Borrowed Status')
columns = ('ISBN number', 'Book name', 'Author','Genre', 'Borrowed Status', 'Borrowed Date')
displayCols = ('ISBN number', 'Book name', 'Author','Genre')
tree =ttk.Treeview(root, columns=columns, displaycolumns=displayCols, show='headings')

tree.heading('ISBN number', text='ISBN number')
tree.heading('Book name', text='Book name')
tree.heading('Author', text='Author')
tree.heading('Genre', text='Genre')
#tree.heading('Borrowed Status', text='Borrowed Status')
#tree.heading('Borrowed Date', text='Borrowed Date')


showAllBooks()
tree.grid(row=5, column=0, sticky='nsew')


#SCROLLBAR FOR LISTBOX
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=5, column=1, sticky='ns')
tree.bind("<<TreeviewSelect>>", displaySelectedItem)

#BOOK INFORMATION IMPORTED FROM SQL
Label(root,text="Borrowed: ").grid(row=8)
Label(root,text="Borrowed on: ").grid(row=9)
#Label(root,text="Number of Books available").grid(row=10)


borrowed_status = Entry(root, bg="white", width=50, borderwidth=2)
borrowed_status.grid(row=8,column=1)
borrowed_status.insert(0,"None selected")

borrowed_on = Entry(root, bg="white", width=50, borderwidth=2)
borrowed_on.grid(row=9,column=1)
borrowed_on.insert(0,"None selected")

#Entry(root).grid(row=8,column=1)
#Entry(root).grid(row=9,column=1)
#Entry(root).grid(row=10,column=1)


#OPERATIONS ON DATABASE

Label(root,text="Search for books").grid(row=13,column=0)
options2=[
    'Title',
    'Author',
    'Genre',
    'ISBN'
    ]
clicked2=StringVar()
clicked2.set("Title")
drop2=OptionMenu(root,clicked2,*options2)
drop2.grid(row=15,column=0)

#OPERATIONS ON ADD AND DELETE BOOKS FROM DATABASE
# l1 = Label(root, text="Title")
# l1.grid(row=15,column=0,ipadx=100)

# l2 = Label(root, text="Author")
# l2.grid(row=15,column=2)

# l3 = Label(root, text="Genre")
# l3.grid(row=16,column=0)

# l4 = Label(root, text="ISBN")
# l4.grid(row=16,column=2)

title_text = StringVar()
e1 = Entry(root, textvariable= title_text)
e1.grid(row=15, column=1)

# author_text = StringVar()
# e2 = Entry(root, textvariable= author_text)
# e2.grid(row=15, column=3)

# year_text = StringVar()
# e3 = Entry(root, textvariable= year_text)
# e3.grid(row=16, column=1)

# ispn_text = StringVar()
# e4 = Entry(root, textvariable= ispn_text)
# e4.grid(row=16, column=3)

srchButton = Button( root , text = "Search", command=searchBooks)
srchButton.grid(row=17,column=1)

root.mainloop()
