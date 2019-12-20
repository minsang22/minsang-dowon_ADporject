import json, requests
import unicodedata
from pyparsing import unicode
from datetime import datetime


class haksick:

    def __init__(self):
        now = datetime.now()
        date = ('%s-%s-%s' %(now.year, now.month, now.day))
        url = "https://kmucoop.kookmin.ac.kr/menu/menujson.php?callback=jQuery172002718234401576014_1575532723347&sdate={date}&edate={date}&today={date}".format(
            date=date)
        response = requests.get(url)
        data = response.text
        data = unicode(data[42:-2])
        data = data.encode('utf-8')
        data = data.decode('unicode_escape')
        self.today_menu = data
        print(data)