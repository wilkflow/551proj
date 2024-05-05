# Author: Savva Petrov(wilkflow), Robert Plastina(m-456)
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

    def getTVList(self):
        """
        function to get all TV shows' title and number of seasons
        :return: list of TV shows with their titles and number of seasons, formatted in neat columns.
        """
        max_title_length = 0
        max_seasons_length = 0
        tv_shows = []
        for show in self._shows.values():
            if show.get_show_type() == 'TV Show':
                tv_shows.append((show.get_title(), show.get_show_duration()))
                if len(show.get_title()) > max_title_length:
                    max_title_length = len(show.get_title())
                if len(show.get_show_duration()) > max_seasons_length:
                    max_seasons_length = len(show.get_show_duration())

        res = []
        header = f"{'Title'.ljust(max_title_length)} {'Seasons'.ljust(max_seasons_length)}"
        res.append(header)
        #print(header)
        for title, seasons in tv_shows:
            #print(f"{title.ljust(max_title_length)} {seasons.ljust(max_seasons_length)}")
            res.append(f"{title.ljust(max_title_length)} {seasons.ljust(max_seasons_length)}")
        return res

    def getBookList(self):
        """
        get book title and auth
        :return: list of books with their titles and authors, formatted in neat columns.
        """
        max_title_length = 0
        max_authors_length = 0
        books = []
        for book in self._books.values():
            auth = book.get_authors().replace('\\', ', ')
            books.append((book.get_title(), auth))
            if len(book.get_title()) > max_title_length:
                max_title_length = len(book.get_title())
            if len(auth) > max_authors_length:
                max_authors_length = len(auth)

        res = []
        header = f"{'Title'.ljust(max_title_length)} {'Author(s)'.ljust(max_authors_length)}"
        print(header)
        res.append(header)
        for title, authors in books:
            print(f"{title.ljust(max_title_length)} {authors.ljust(max_authors_length)}")
            res.append(f"{title.ljust(max_title_length)} {authors.ljust(max_authors_length)}")
        return res


    def getMovieStats(self):
        """
        Get statistics about movies
        :return: dict containing the statistics.
        """
        stats = {}
        ratings = {}
        duration = 0
        directors = {}
        actors = {}
        genres = {}
        mcount = 0
        for show in self._shows.values():
            if show.get_show_type() == 'Movie':
                if show.get_rating() in ratings:
                    ratings[show.get_rating()] += 1
                else:
                    ratings[show.get_rating()] = 1
                
                duration += int(show.get_show_duration().replace(' min', ''))
                dirs = show.get_directors().split('\\')
                for dir in dirs:
                    if dir in directors:
                        directors[dir] += 1
                    else:
                        directors[dir] = 1
                
                acts = show.get_actors().split('\\')
                for act in acts:
                    if act in actors:
                        actors[act] += 1
                    else:
                        actors[act] = 1

                cats = show.get_categories().split('\\')
                for cat in cats:
                    if cat in genres:
                        genres[cat] += 1
                    else:
                        genres[cat] = 1
 
                mcount += 1
        stats['Average Movie Duration: '] = f'{duration/mcount} minutes'
        hgcount = 0
        hg = ''
        notacount = 0
        nota = ''
        notdcount = 0
        notd = ''
        for d in directors:
            if directors[d] > notdcount:
                notd = d
        stats['Most Prolific Director: '] = notd
        for a in actors:
            if actors[a] > notacount:
                nota = a
        stats['Most Prolific Actor: '] = nota
        for g in genres:
            if genres[g] > hgcount:
                hg = g
        stats['Most Frequent Genre: '] = hg
        rdict = {}
        for r in ratings:
            rdict[r] = f'{ratings[r]/mcount:.2f}'
        stats['rstat'] = rdict
 
        return stats

    def getShowStats(self):
        """
        Get statistics about shows
        :return: dict containing the statistics.
        """
        stats = {}
        ratings = {}
        duration = 0

        actors = {}
        genres = {}
        scount = 0
        for show in self._shows.values():
            if show.get_show_type() == 'TV Show':
                if show.get_rating() in ratings:
                    ratings[show.get_rating()] += 1
                else:
                    ratings[show.get_rating()] = 1
                
                duration += int(show.get_show_duration().replace(' Seasons', ''))
                
                
                acts = show.get_actors().split('\\')
                for act in acts:
                    if act in actors:
                        actors[act] += 1
                    else:
                        actors[act] = 1

                cats = show.get_categories().split('\\')
                for cat in cats:
                    if cat in genres:
                        genres[cat] += 1
                    else:
                        genres[cat] = 1
 
                scount += 1
        stats['Average Movie Duration: '] = f'{duration/scount:.2f} Seasons'
        hgcount = 0
        hg = ''
        notacount = 0
        nota = ''
       
        
        for a in actors:
            if actors[a] > notacount:
                nota = a
        stats['Most Prolific Actor: '] = nota
        for g in genres:
            if genres[g] > hgcount:
                hg = g
        stats['Most Frequent Genre: '] = hg
        rdict = {}
        for r in ratings:
            rdict[r] = f'{ratings[r]/scount:.2f}'
        stats['rstat'] = rdict
 
        return stats


    def getBookStats(self):
        """
        Get statistics about books
        :return: dict containing the statistics.
        """
        stats = {}

        pcount = 0

        authors = {}
        pubs = {}
        bcount = 0
        for book in self._books.values():

            pcount += int(book.get_num_pages())

            auth = book.get_authors().split('\\')
            for au in auth:
                if au in authors:
                    authors[au] += 1
                else:
                    authors[au] = 1

            if book.get_publisher() in pubs:
                pubs[book.get_publisher()] += 1
            else:
                pubs[book.get_publisher()] = 1
 
            bcount += 1
        stats['Average Page Count: '] = f'{pcount/bcount:.2f} Seasons'
        hpc = 0
        hp = ''
        notacount = 0
        nota = ''
       
        
        for a in authors:
            if authors[a] > notacount:
                nota = a
        stats['Most Prolific Author: '] = nota
        for p in pubs:
            if pubs[p] > hpc:
                hp = p
        stats['Most Prolific Publisher: '] = hp

        print(stats)
        return stats


def main():
    rec = Recommender()
    rec.loadBooks()
    rec.getBookStats()

if __name__ == "__main__":
    main()

