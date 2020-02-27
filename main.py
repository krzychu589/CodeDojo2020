import csv
from bs4 import BeautifulSoup
from datetime import datetime,date
from friend import Friend
from urllib.request import urlopen


class InputHandler():
    def __init__(self):
        pass

    def readFromCSV(self,path):
        friends =[]
        with open(path , newline='') as csvfile:
            csv_data = csv.reader(csvfile,delimiter=',')

            for i,row  in enumerate(csv_data):
                if i ==0:
                    continue
                first_name,last_name,email =row[0].strip(), row[1].strip(), row[3].strip()
                birth_date = datetime.strptime(row[2].strip(),"%Y-%m-%d")
                new_friend = Friend(first_name,last_name,email,birth_date)
                friends.append(new_friend)
        return friends

    def readFromWeb(self,link):
        friends =[]
        with urlopen(link) as response:
            soup = BeautifulSoup(response.read(),"html.parser")
            for row in soup.select("tr"):
                person = [x.get_text() for x in row.select("td")]
                if not person:
                    continue
                first_name = person[0].strip()
                last_name = person[1].strip()
                birth_date = datetime.strptime(person[2].strip(),"%Y-%m-%d")
                email = person[3].strip()
                new_friend = Friend(first_name, last_name, email, birth_date)
                friends.append(new_friend)
        return friends


def select_friends(friends):
    for friend in friends:
        if not friend.birth_date == date.today():
            friends.remove(friend)
    return friends


def send_greetings(friends):
    for friend in friends:
        print(f"Dear {friend.first_name},\n"
              f"Today is your Birthday,\n"
              f"so we wish you that your code will always work!\n"
              f"Kind Regards\n"
              f"Sonia & Krzysiek\n")


birthday = InputHandler()
friends =birthday.readFromWeb(r'http://212.47.253.227/')
# friends =birthday.readFromCSV('input.csv')
friends= select_friends(friends)
send_greetings(friends)

