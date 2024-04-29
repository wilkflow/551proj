# Author: Savva Petrov, Robert Plastina
# Date: 4/29/2003
# Description: Book class

from Media import Media

class Book(Media):
    def __init__(self, id, title, avgr, auth, isbn, isbn13, lang, np, nr, pubdate, pub):
        super().__init__(id, title, avgr)   #inherit
        self._auth = auth
        self._isbn = isbn
        self._isbn13 = isbn13
        self._lang = lang
        self._np = np
        self._nr = nr
        self._pubdate = pubdate
        self._pub = pub


    #getters setters
    def get_auth(self):
        return self._auth

    def set_auth(self, auth):
        self._auth = auth

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_isbn13(self):
        return self._isbn13

    def set_isbn13(self, isbn13):
        self._isbn13 = isbn13

    def get_lang(self):
        return self._lang

    def set_lang(self, lang):
        self._lang = lang

    def get_np(self):
        return self._np

    def set_np(self, np):
        self._np = np

    def get_nr(self):
        return self._nr

    def set_nr(self, nr):
        self._nr = nr

    def get_pubdate(self):
        return self._pubdate

    def set_pubdate(self, pubdate):
        self._pubdate = pubdate

    def get_pub(self):
        return self._pub

    def set_pub(self, pub):
        self._pub = pub

