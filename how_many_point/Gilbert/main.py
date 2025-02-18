# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

story = 500
challenge = 200
love_battle = 40

multiplicateur_story = 3
multiplicateur_love = 3

tab = [story, story + challenge, story, story + challenge, story, story, story + challenge, story, story,  # 9
       story + challenge, story, story + challenge, story, story + challenge, story, story, story + challenge, story,
       # 9
       story + challenge, story, story, story + challenge, story, story + challenge, story]

# compte principal
# story_ticket = 94 + 6
# cake_100 = 68
# cake_50 = 85

# compte secondaire
story_ticket = 345 + 6
cake_100 = 25
cake_50 = 132


def total_story():
    # Use a breakpoint in the code line below to debug your script.

    complete_story = int((story_ticket / 5) / 25)
    extra_story_ticket = story_ticket % 5
    global_story = int((story_ticket - extra_story_ticket + complete_story * 5) / 5)
    total = 0
    i = 1
    p = 1

    while i != global_story:
        p = 1
        for x in tab:
            # print(p, x)
            total += x * multiplicateur_story
            if i == global_story:
                break
            i += 1
            p += 1
        total += story * multiplicateur_story
    # print(total)
    return total


def total_cake():
    cake = (cake_100 + (cake_50 - (cake_50 % 2))) * 5
    tot = cake * (love_battle * multiplicateur_love)
    # print(tot)
    return tot


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("total of point")
    print((total_story() + total_cake()) / 100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
