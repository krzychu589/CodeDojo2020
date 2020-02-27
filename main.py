
from datetime import datetime,date
from friend import Friend
import inputhandlers



def select_friends(friends):
    print(len(friends))
    selected = []
    curr_y, curr_m, curr_d = date.today().year, date.today().month, date.today().day

    for friend in friends:
        if friend.birth_date.month == curr_m and friend.birth_date.day == curr_d:
            selected.append(friend)
        elif friend.birth_date.month == 2 and friend.birth_date.day == 29 and curr_m == 2 and curr_d == 28:
            try:
                check_date = datetime(curr_y, 2, 29)
            except ValueError:
                selected.append(friend)

    print(len(selected))
    return selected



def send_greetings(friends):
    for friend in friends:
        print(f"Dear {friend.birth_date},\n"
              f"Today is your Birthday,\n"
              f"so we wish you that your code will always work!\n"
              f"Kind Regards\n"
              f"Sonia & Krzysiek\n")


birthday = inputhandlers.CsvInputHandler()
friends =birthday.read('input.csv')

# birthday = inputhandlers.WebInputHandler()
# friends =birthday.read(r'http://212.47.253.227/')

friends = select_friends(friends)
send_greetings(friends)

