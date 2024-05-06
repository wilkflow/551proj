# Author: Savva Petrov(wilkflow), Robert Plastina(m-456)
# Date: 5/5/2024
# Description: GUI for the program, written in tkinter

import tkinter as tk
from tkinter import ttk, messagebox
import Recommender as rec

class RecommenderGUI:
    def __init__(self):
        self.new_rec = rec.Recommender()

        self.Toplevel = tk.Tk()
        self.Toplevel.title("Media 4 U")
        self.Toplevel.geometry("1200x800")

        self.selection = ttk.Notebook(self.Toplevel)
        self.selection.pack(side=tk.TOP, fill='both', expand=True)

        self.movie_tab = ttk.Frame(self.selection)  # The movie tab.
        self.selection.add(self.movie_tab, text="Movies")
        self.movie_list = tk.Text(self.movie_tab, padx=10, pady=10, wrap=tk.WORD)
        self.movie_stats = tk.Text(self.movie_tab, padx=10, pady=10, wrap=tk.WORD)
        self.movie_list.insert(tk.END, "No data loaded.")
        self.movie_stats.insert(tk.END, "No data loaded.")
        self.movie_list.config(state=tk.DISABLED)
        self.movie_stats.config(state=tk.DISABLED)
        self.movie_list_scroll = tk.Scrollbar(self.movie_tab, command=self.movie_list.yview)
        self.movie_tab.grid_columnconfigure(0, weight=1)
        self.movie_tab.grid_rowconfigure(0, weight=1)
        self.movie_tab.grid_rowconfigure(1, weight=1)
        self.movie_list.grid(row=0, column=0, sticky='nsew')
        self.movie_list_scroll.grid(row=0, column=1, sticky='ns')
        self.movie_stats.grid(row=1, column=0, sticky='nsew')

        self.book_tab = ttk.Frame(self.selection)  # The book tab.
        self.selection.add(self.book_tab, text="Books")
        self.book_list = tk.Text(self.book_tab, padx=10, pady=10, wrap=tk.WORD)
        self.book_stats = tk.Text(self.book_tab, padx=10, pady=10, wrap=tk.WORD)
        self.book_list.insert(tk.END, "No data loaded.")
        self.book_stats.insert(tk.END, "No data loaded.")
        #self.book_list.config(state=tk.DISABLED) why on gods green earth did you disable books as well
        #self.book_stats.config(state=tk.DISABLED)
        self.book_list_scroll = tk.Scrollbar(self.book_tab, command=self.book_list.yview)
        self.book_tab.grid_columnconfigure(0, weight=1)
        self.book_tab.grid_rowconfigure(0, weight=1)
        self.book_tab.grid_rowconfigure(1, weight=1)
        self.book_list.grid(row=0, column=0, sticky='nsew')
        self.book_list_scroll.grid(row=0, column=1, sticky='ns')
        self.book_stats.grid(row=1, column=0, sticky='nsew')

        self.tv_tab = ttk.Frame(self.selection)  # The TV shows tab.
        self.selection.add(self.tv_tab, text="TV Shows")
        self.tv_list = tk.Text(self.tv_tab, padx=10, pady=10, wrap=tk.WORD)
        self.tv_stats = tk.Text(self.tv_tab, padx=10, pady=10, wrap=tk.WORD)
        self.tv_list.insert(tk.END, "No data loaded.")
        self.tv_stats.insert(tk.END, "No data loaded.")
        self.tv_list.config(state=tk.DISABLED)
        self.tv_stats.config(state=tk.DISABLED)
        self.tv_list_scroll = tk.Scrollbar(self.tv_tab, command=self.tv_list.yview)
        self.tv_tab.grid_columnconfigure(0, weight=1)
        self.tv_tab.grid_rowconfigure(0, weight=1)
        self.tv_tab.grid_rowconfigure(1, weight=1)
        self.tv_list.grid(row=0, column=0, sticky='nsew')
        self.tv_list_scroll.grid(row=0, column=1, sticky='ns')
        self.tv_stats.grid(row=1, column=0, sticky='nsew')

        self.ms_search = ttk.Frame(self.selection)  # The movie/show search tab.
        self.selection.add(self.ms_search, text="Search Movies/Shows")
        self.ms_choice = ttk.Combobox(self.ms_search)
        self.ms_choice['values'] = ('Movie', 'TV Show')
        self.ms_cl = tk.Label(self.ms_search, text="Type:")
        self.mst_l = tk.Label(self.ms_search, text="Title:")
        self.mst_e = tk.Entry(self.ms_search, width=20)
        self.msd_l = tk.Label(self.ms_search, text="Director:")
        self.msd_e = tk.Entry(self.ms_search, width=20)
        self.msa_l = tk.Label(self.ms_search, text="Actor:")
        self.msa_e = tk.Entry(self.ms_search, width=20)
        self.msg_l = tk.Label(self.ms_search, text="Genre:")
        self.msg_e = tk.Entry(self.ms_search, width=20)
        self.ms_sb = tk.Button(self.ms_search, text="Search", command=self.searchShows)
        self.ms_info = tk.Text(self.ms_search, padx=10, pady=10, wrap=tk.WORD)
        self.ms_info.insert(tk.END, "No data loaded.")
        self.ms_info_scroll = tk.Scrollbar(self.ms_search, command=self.ms_info.yview)
        self.ms_info.config(state=tk.DISABLED)
        self.ms_cl.grid(row=0, column=0, padx=10, sticky='w')
        self.ms_choice.grid(row=0, column=1, padx=10, pady=5, sticky='we')
        self.ms_choice.state(['readonly'])
        self.mst_l.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.mst_e.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.msd_l.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.msd_e.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        self.msa_l.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.msa_e.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        self.msg_l.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.msg_e.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
        self.ms_sb.grid(row=5, column=0, sticky='w', pady=10, padx=10)
        self.ms_info.grid(row=6, column=0, sticky='nsew')
        self.ms_info_scroll.grid(row=6, column=2, sticky='ns')

        self.bk_search = ttk.Frame(self.selection)  # The book search tab.
        self.selection.add(self.bk_search, text="Search Books")
        self.bkt_l = tk.Label(self.bk_search, text="Title:")
        self.bkt_e = tk.Entry(self.bk_search, width=20)
        self.bka_l = tk.Label(self.bk_search, text="Author:")
        self.bka_e = tk.Entry(self.bk_search, width=20)
        self.bkp_l = tk.Label(self.bk_search, text="Publisher:")
        self.bkp_e = tk.Entry(self.bk_search, width=20)
        self.bk_sb = tk.Button(self.bk_search, text="Search", command=self.searchBooks)
        self.bk_info = tk.Text(self.bk_search, padx=10, pady=10, wrap=tk.WORD)
        self.bk_info.insert(tk.END, "No data loaded.")
        self.bk_info_scroll = tk.Scrollbar(self.bk_search, command=self.bk_info.yview)
        self.bk_info.config(state=tk.DISABLED)
        self.bkt_l.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.bkt_e.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.bka_l.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.bka_e.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.bkp_l.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.bkp_e.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
        self.bk_sb.grid(row=3, column=0, sticky='w', pady=10, padx=10)
        self.bk_info.grid(row=4, column=0, sticky='nsew')
        self.bk_info_scroll.grid(row=4, column=2, sticky='ns')

        self.rec_tab = ttk.Frame(self.selection)  # The recommendation tab.
        self.selection.add(self.rec_tab, text="Recommendations")
        self.rec_choice = ttk.Combobox(self.rec_tab)
        self.rec_choice['values'] = ('Movie', 'TV Show', 'Book')
        self.rect_l = tk.Label(self.rec_tab, text="Title:")
        self.rect_e = tk.Entry(self.rec_tab, width=20)
        self.rec_sb = tk.Button(self.rec_tab, text="Get Recommendation", command=self.getRecommendations)
        self.rec_info = tk.Text(self.rec_tab, padx=10, pady=10, wrap=tk.WORD)
        self.rec_info.insert(tk.END, "No data loaded.")
        self.rec_info_scroll = tk.Scrollbar(self.rec_tab, command=self.rec_info.yview)
        self.rec_info.config(state=tk.DISABLED)
        self.rec_choice.grid(row=0, column=0, padx=10, pady=5, sticky='we')
        self.rec_choice.state(['readonly'])
        self.rect_l.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.rect_e.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.rec_sb.grid(row=2, column=0, sticky='w', pady=10, padx=10)
        self.rec_info.grid(row=3, column=0, sticky='nsew')
        self.rec_info_scroll.grid(row=3, column=2, sticky='ns')

        # Bonus Begins
        # self.rating_tab = ttk.Frame(self.selection)  # The rating tab.
        # self.selection.add(self.rating_tab, text="Ratings")
        # Bonus Ends

        self.sl_button = ttk.Button(self.Toplevel, text="Load Shows", command=self.loadShows)
        self.sl_button.pack(side=tk.LEFT, padx=10, pady=2)

        self.bl_button = ttk.Button(self.Toplevel, text="Load Books", command=self.loadBooks)
        self.bl_button.pack(side=tk.LEFT, padx=10, pady=2)

        self.br_button = ttk.Button(self.Toplevel, text="Load Recommendations", command=self.loadAssociations)
        self.br_button.pack(side=tk.LEFT, padx=10, pady=2)

        self.in_button = ttk.Button(self.Toplevel, text="Information", command=self.creditInfoBox)
        self.in_button.pack(side=tk.LEFT, padx=10, pady=2)

        self.quit_button = ttk.Button(self.Toplevel, text="Quit", command=self.Toplevel.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=10, pady=2)

        self.Toplevel.mainloop()

    def loadShows(self):
        self.movie_list.config(state=tk.NORMAL)
        self.movie_stats.config(state=tk.NORMAL)
        self.tv_list.config(state=tk.NORMAL)
        self.tv_stats.config(state=tk.NORMAL)
        self.new_rec.loadShows()
        self.movie_list.delete('1.0', tk.END)
        self.tv_list.delete('1.0', tk.END)
        self.movie_list.insert(tk.END, self.new_rec.getMovieList())
        self.tv_list.insert(tk.END, self.new_rec.getTVList())
        self.movie_stats.delete('1.0', tk.END)
        self.movie_stats.insert(tk.END, 'Ratings:\n')
        self.tv_stats.insert(tk.END, 'Ratings:\n')
        for k,v in self.new_rec.getMovieStats().items(): 
            self.movie_stats.insert(tk.END, k+v+'\n')
        for k,v in self.new_rec.getShowStats().items():
            self.tv_stats.insert(tk.END, k+v+'\n')


    def loadBooks(self):
        self.book_list.config(state=tk.NORMAL)
        self.book_stats.config(state=tk.NORMAL)
        self.new_rec.loadBooks()
        self.book_list.delete('1.0', tk.END)
        for b in self.new_rec.getBookList():
            self.book_list.insert(tk.END, b+'\n')
        self.book_stats.delete('1.0', tk.END)
        for k,v in self.new_rec.getBookStats().items(): 
            self.book_stats.insert(tk.END, k+v+'\n\n')

    def loadAssociations(self):
        self.new_rec.loadAssociations()

    def creditInfoBox(self):
        message = "Created by Savva Petrov (wilkflow) and Robert Plastina (m-456) on May 5, 2024"
        messagebox.showinfo("Information", message)
    def searchShows(self):
        self.ms_info.config(state=tk.NORMAL)
        ms_type = self.ms_choice.get()
        ms_title = self.mst_e.get()
        ms_director = self.msd_e.get()
        ms_actor = self.msa_e.get()
        ms_genre = self.msg_e.get()
        self.ms_info.delete('1.0', tk.END)
        self.ms_info.insert(tk.END, self.new_rec.searchTVMovies(ms_type, ms_title, ms_director, ms_actor, ms_genre))
        self.ms_info.config(state=tk.DISABLED)

    def searchBooks(self):
        self.bk_info.config(state=tk.NORMAL)
        bk_title = self.bkt_e.get()
        bk_author = self.bka_e.get()
        bk_publisher = self.bkp_e.get()
        self.bk_info.delete('1.0', tk.END)
        self.bk_info.insert(tk.END, self.new_rec.searchBooks(bk_title, bk_author, bk_publisher))
        self.bk_info.config(state=tk.DISABLED)

    def getRecommendations(self):
        self.rec_info.config(state=tk.NORMAL)
        rec_type = self.rec_choice.get()
        rec_title = self.rect_e.get()
        self.rec_info.delete('1.0', tk.END)
        self.rec_info.insert(tk.END, self.new_rec.getRecommendations(rec_type, rec_title))
        self.rec_info.config(state=tk.DISABLED)

def main():
    app = RecommenderGUI()

main()