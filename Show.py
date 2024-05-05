# Author: Savva Petrov, Robert Plastina
# Date: 4/29/2003
# Description: Show class


from Media import Media

class Show(Media):      #same as book should now work in loadshows func
    def __init__(self, show_id,type,title,director,cast,average_rating,country,date_added,release_year,rating,duration,listed_in,description):
        super().__init__(show_id, title, average_rating)
        self._show_type = type
        self._directors = director
        self._actors = cast
        self._country_code = country
        self._addition_date = date_added
        self._release_year = release_year
        self._mpaa_rating = rating
        self._show_duration = duration
        self._categories = listed_in
        self._synopsis = description
        #getters setter like before
    def get_show_type(self):
            return self._show_type

    def set_show_type(self, type):
            self._show_type = type

    def get_directors(self):
            return self._directors

    def set_directors(self, directors):
            self._directors = directors

    def get_actors(self):
            return self._actors

    def set_actors(self, actors):
            self._actors = actors

    def get_country_code(self):
            return self._country_code

    def set_country_code(self, country_code):
            self._country_code = country_code

    def get_addition_date(self):
            return self._addition_date

    def set_addition_date(self, addition_date):
            self._addition_date = addition_date

    def get_release_year(self):
            return self._release_year

    def set_release_year(self, release_year):
            self._release_year = release_year

    def get_mpaa_rating(self):
            return self._mpaa_rating

    def set_mpaa_rating(self, mpaa_rating):
            self._mpaa_rating = mpaa_rating

    def get_show_duration(self):
            return self._show_duration

    def set_show_duration(self, show_duration):
            self._show_duration = show_duration

    def get_categories(self):
            return self._categories

    def set_categories(self, categories):
            self._categories = categories

    def get_synopsis(self):
            return self._synopsis

    def set_synopsis(self, synopsis):
            self._synopsis = synopsis

