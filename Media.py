# Author: Savva Petrov, Robert Plastina
# Date: 4/29/2003
# Description: The media class

class Media:
    def __init__(self, id, title, avgp):
        self._id = id
        self._title = title
        self._avgp = avgp

    #getters and setters
    def get_id(self):
        return self._id
    def get_title(self):
        return self._title
    def get_avgp(self):
        return self._avgp

    def set_id(self, id):   #just in case
        self._id = id
    def set_title(self, title):
        self._title = title
    def set_avgp(self, avgp):
        self._avgp = avgp