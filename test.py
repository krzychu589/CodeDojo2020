from friend import Friend
from datetime import datetime,date
from main import select_friends

def get_friends():
    friends = [Friend("Turner", "Charles", "uwright@hotmail.com",datetime(1989, 10, 12)),
               Friend("Turner", "Charles", "uwright@hotmail.com",datetime.strptime("2020-02-27","%Y-%m-%d")),
               Friend("Turner", "Charles", "uwright@hotmail.com",datetime.strptime("1997-02-28","%Y-%m-%d"))]
    return friends

def test_selector():
    expected = [Friend("Turner", "Charles", "uwright@hotmail.com",datetime.strptime("2020-02-27","%Y-%m-%d"))]

    friends = get_friends()
    actual = select_friends(friends)
    assert actual == expected


def test_select29Feb():
    pass
