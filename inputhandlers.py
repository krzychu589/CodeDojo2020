from datetime import datetime
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from friend import Friend


class BaseInputHandler:
    def __init__(self):
        pass

    def make_person_from_list(self, raw_list):
        """Get a raw list of person attributes in the order: first_name, last_name, birth_date, email"""
        clean_list = [x.strip() for x in raw_list]
        first_name, last_name = clean_list[:2]
        birth_date = datetime.strptime(clean_list[2].strip(), "%Y-%m-%d")
        email = clean_list[3]
        return Friend(first_name=first_name, last_name=last_name, email=email, birth_date=birth_date)

    def read(self, source):
        pass


class CsvInputHandler(BaseInputHandler):

    def read(self,path):
        friends =[]
        with open(path , newline='') as csvfile:
            csv_data = csv.reader(csvfile,delimiter=',')
            for i, row in enumerate(csv_data):
                if i == 0:
                    continue
                new_friend = self.make_person_from_list(row)
                friends.append(new_friend)
        return friends


class WebInputHandler(BaseInputHandler):

    def read(self,link):
        friends =[]
        with urlopen(link) as response:
            soup = BeautifulSoup(response.read(),"html.parser")
            for row in soup.select("tr"):
                person = [x.get_text() for x in row.select("td")]
                if not person:
                    continue
                new_friend = self.make_person_from_list(person)
                friends.append(new_friend)
        return friends