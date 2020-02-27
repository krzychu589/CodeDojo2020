from friend import Friend
from datetime import datetime,date
from main import select_friends
from freezegun import freeze_time


def get_friends():
    friends = [Friend("Turner", "Charles", "uwright@hotmail.com",datetime(1989, 10, 12)),
               Friend("Turner", "Charles", "uwright@hotmail.com",datetime(2004, 2, 29)),
               Friend("Turner", "Charles", "uwright@hotmail.com",datetime(1997, 2, 28))]
    return friends


@freeze_time("2020-02-28")
def test_select_when_29feb_is_in_the_year():
    expected = [Friend("Turner", "Charles", "uwright@hotmail.com",datetime(1997, 2, 28))]

    friends = get_friends()
    actual = select_friends(friends)
    assert actual == expected


@freeze_time("2019-02-28")
def test_select_when_no_29feb_in_the_year():
    expected = [Friend("Turner", "Charles", "uwright@hotmail.com",datetime(2004, 2, 29)),
                Friend("Turner", "Charles", "uwright@hotmail.com",datetime(1997, 2, 28))]
    friends = get_friends()
    actual = select_friends(friends)
    assert actual == expected
