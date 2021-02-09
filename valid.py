import datetime

today = datetime.date.today()
day = today.day
month = today.month
year = today.year

class Valid():

    def remove_space(self, string):
        if '　' in string:
            string = string.replace('　', ' ')
            string = " ".join(string.split())
        return string



class Date(Valid):

    def date_replacer(self, date_text):
        
        pass