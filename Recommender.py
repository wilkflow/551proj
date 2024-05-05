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
            """
                load books from file anbd put into _books
                :return: None
            """
            while True:
                path = filedialog.askopenfilename(title="Select book file", filetypes=[("CSV Files", "*.csv")])
                if path:
                    break
                messagebox.showerror("Error", "Please select a valid file.")
            
            with open(path, 'r') as file:
                headers = file.readline().strip().split(',')  # get headers
                #print(headers)
                for line in file:
                    book_data = line.strip().split(',')
                    #print(book_data)
                    book_info = dict(zip(headers, book_data))
                    #print(book_info)    
                    book_id = book_info['bookID']
                    book = Book(**book_info)  # allegedly this turns dict stuff into vars
                    self._books[book_id] = book
            file.close()
    
    def loadShows(self):
        """
        load shows from file and put into _shows
        :return: None
        """
        while True:
            path = filedialog.askopenfilename(title="Select show file", filetypes=[("CSV Files", "*.csv")])
            if path:
                break
            messagebox.showerror("Error", "Please select a valid file.")

        with open(path, 'r') as file:
                headers = file.readline().strip().split(',')  # get headers
                #print(headers)
                for line in file:
                    show_data = line.strip().split(',')
                    show_info = dict(zip(headers, show_data))
                    show_id = show_info['show_id']
                    show = Show(**show_info)  # allegedly this turns dict stuff into vars
                    self._shows[show_id] = show
        file.close()
    

    def loadAssociations(self):
        """
        Load associations and put into _associations
        :return: None
        """
        while True:
            path = filedialog.askopenfilename(title="Select association file", filetypes=[("CSV Files", "*.csv")])
            if path:
                break
            messagebox.showerror("Error", "Please select a valid file.")

        with open(path, 'r') as file:
            for line in file:
                ids = line.strip().split(',')
                show_id, book_id = ids[0], ids[1]

                #show
                if show_id not in self._associations:
                    self._associations[show_id] = {}
                if book_id in self._associations[show_id]:
                    self._associations[show_id][book_id] += 1
                else:
                    self._associations[show_id][book_id] = 1
                #book
                if book_id not in self._associations:
                    self._associations[book_id] = {}
                if show_id in self._associations[book_id]:
                    self._associations[book_id][show_id] += 1
                else:
                    self._associations[book_id][show_id] = 1
        file.close()

    def getMovieList(self):
        """
            function to get all movies' title and duration
        :return: list of movies with their titles and runtimes, formatted in neat columns.
        """
        max_title_length = 0
        max_runtime_length = 0
        movies = []
        for show in self._shows.values():
            if show._show_type == 'Movie':
                movies.append((show.get_title(), show.get_show_duration()))
                if len(show.get_title()) > max_title_length:
                    max_title_length = len(show.get_title())
                if len(show.get_show_duration()) > max_runtime_length:
                    max_runtime_length = len(show.get_show_duration())

        res = []
        header = f"{'Title'.ljust(max_title_length)} {'Runtime'.ljust(max_runtime_length)}" #this should hopefully work?
        res.append(header)
        for title, runtime in movies:
            res.append(f"{title.ljust(max_title_length)} {runtime.ljust(max_runtime_length)}")
        return res



    def printBooks(self):
        #just for debugging
 
            print(self._books)


def main():
    rec = Recommender()
    rec.loadShows()
    rec.getMovieList()

if __name__ == "__main__":
    main()

