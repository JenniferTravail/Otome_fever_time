import datetime as dt
import calendar

from Lucky_time import Luck

from Type_Lucky import Typelucky

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


STORY = 500
CHALLENGE = 200
LOVE_CHALLENGE = 40

chapter = [STORY, STORY + CHALLENGE, STORY, STORY + CHALLENGE, STORY, STORY, STORY + CHALLENGE, STORY, STORY,  # 9
           STORY + CHALLENGE, STORY, STORY + CHALLENGE, STORY, STORY + CHALLENGE, STORY, STORY, STORY + CHALLENGE,  # 8
           STORY, STORY + CHALLENGE, STORY, STORY, STORY + CHALLENGE, STORY, STORY + CHALLENGE, STORY]  # 8

HOUR = 24
NUMBER = 5  # nb story of a chapter

FRIEND = 50
GOLD = 1000
LOGIN = 200

END = 3  # hour
JET = 7


def start(mois, jour, heure, heart: int, gold: bool, lucky_schedule):
    try:
        end_date = dt.datetime(2023, mois, jour, heure)
    except ValueError as e:
        print(str(e))
        exit(1)
    today = dt.datetime.now()
    if heart == 0:
        heart = 1700
    if gold:
        total_gold = 0
        if today.hour > 17:
            print("YEAH")
        else:
            print("More coins")
    if end_date.hour < today.day:
        print("yeah")
        days = calendar.monthrange(today.year, today.month)[1] - today.day + end_date.hour
    else:
        days = calendar.monthrange(today.year, today.month)[1] - today.day
    last_hour = HOUR - today.hour + (days - 1) * 24 + END
    print(days, last_hour)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #objectif = int(input("Entréz votre objectif: "))
   # possession = int(input("Entrez combien vous avez: "))

    lucky_schedule = [Luck(dt.datetime(2023, 12, 21, 10), dt.datetime(2023, 12, 21, 23), Typelucky.STORY, 3)]

    end_date = dt.datetime(2023, 12, 28, 10)
    start_date = dt.datetime(2023, 12, 21, 10)
    print("HEllo")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
