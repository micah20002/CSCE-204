FILE_NAME = "excercises/nov-10/books.txt"

def write_books(books):
    with open (FILE_NAME, "w") as file:
        for book in books:
            file.write(book + "\n")

def read_books():
   books = []
   with open(FILE_NAME) as file:
       for line in file:
           line = line.replace("\n","").strip()
           books.append(line)
           return books

def list_books(books):
    for i in range(len(books)):
        print()
