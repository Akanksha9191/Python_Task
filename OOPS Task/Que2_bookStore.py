# 2)Write a program which contains one class named as BookStore.
# Bookstore class contains two instance variables as Name , Author.
# That class contains one class variable as NoofBooks which is initialize to 0
# There is one instanace methods of class as Display which displays name, author and number of books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1=Bookstore(“Linux System Programming”,”Robert Love”)
# Obj1.Display()  # Linux System Programming. No of books : 1

# Obj2=Bookstore(“C Programming”,”Robert Love”)
# Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2

class BookStore:
    noOfBook = 0
    
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.noOfBook += 1
        
    def Display(self):
        print('Book Name:', self.Name)
        print('Book Author : ', self.Author)
        print('No. of book : ', BookStore.noOfBook)
        


Obj1=BookStore('Linux System Programming','Robert Love')
Obj1.Display()  # Linux System Programming. No of books : 1
print()
Obj2=BookStore('C Programming' , 'Robert Love')
Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2