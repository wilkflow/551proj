# Author: Savva Petrov, Robert Plastina
# Date: 4/29/2003
# Description: Show class


from Media import Media

class Show(Media):
    def __init__(self, id, title, avgr, type, dirs, act, cc, date, ry, rate, dur, genres, desc):
        super().__init__(id, title, avgr)
        self._type = type
        self._dirs = dirs
        self._act = act
        self._cc = cc
        self._date = date
        self._ry = ry
        self._rate = rate
        self._dur = dur
        self._genres = genres
        self._desc = desc
    #getters setter like before
    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_dirs(self):
        return self._dirs

    def set_dirs(self, dirs):
        self._dirs = dirs

    def get_act(self):
        return self._act

    def set_act(self, act):
        self._act = act

    def get_cc(self):
        return self._cc

    def set_country_code(self, cc):
        self._cc = cc

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_ry(self):
        return self._ry

    def set_ry(self, ry):
        self._ry = ry

    def get_rate(self):
        return self._rate

    def set_rate(self, rate):
        self._rate = rate

    def get_dur(self):
        return self._dur

    def set_duration(self, dur):
        self._dur = dur

    def get_genres(self):
        return self._genres

    def set_genres(self, genres):
        self._genres = genres

    def get_desc(self):
        return self._desc

    def set_description(self, desc):
        self._desc = desc
