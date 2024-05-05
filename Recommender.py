# Author: Savva Petrov, Robert Plastina
# Date: 4/29/2003
# Description: Recommender class


from tkinter import filedialog, messagebox
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self._books = {}
        self._shows = {}
        self._associations = {}

    def loadBooks(self):
            #
            while True:
                path = filedialog.askopenfilename(title="Select book file", filetypes=[("CSV Files", "*.csv")])
                if path:
                    break
                messagebox.showerror("Error", "Please select a valid file.")
            
            with open(path, 'r') as file:
                headers = file.readline().strip().split(',')  # get headers
                print(headers)
                for line in file:
                    book_data = line.strip().split(',')
                    print(book_data)
                    book_info = dict(zip(headers, book_data))
                    print(book_info)    
                    book_id = book_info['bookID']
                    book = Book(**book_info)  # allegedly this turns dict stuff into vars
                    self._books[book_id] = book
            file.close()

    def printBooks(self):
        #just for debugging
 
            print(self._books)


def main():
    rec = Recommender()
    rec.loadBooks()
    rec.printBooks()

if __name__ == "__main__":
    main()

