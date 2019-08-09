import random
import time


def print_pause(string):
    print(string)
    time.sleep(2)


def left_right(item, location, enemy1, guard1):
    while True:

        way = input("Which way are you picking?\nleft or right\n")

        if "left" in way:
            print_pause("you chose left")
            house(item, location, enemy1, guard1)
            break

        elif "right" in way:
            print_pause("you chose right")
            cave(item, location, enemy1, guard1)

            if "light" in location:
                light(item, location, enemy1, guard1)
                break

            else:
                break

        else:
            print_pause("try again")


def intro():
    print_pause("You find yourself in a dark dungeon.\n"
                "and are trying to get out.")
    print_pause("In front of you are two passageways")
    print_pause("There is a passage to the left and another to the right")


def house(item, location, enemy1, guard1):
    print_pause("After a long walk you arrived to an old house.")
    print_pause("Would you like to knock and see if someone is inside?\n")
    yes_no = input("yes or no\n")

    if "yes" in yes_no and not("sword" in item):
        print_pause(f"After knocking {enemy1[0]} answers the door.")
        hello = input("Would you like to run or say hello?\n")

        if "run" in hello:
            print("You head back in the direction you came\n"
                  "Now what")
            left_right(item, location, enemy1, guard1)

        elif "hello" in hello:
            print_pause(f"You are greeted by {enemy1[0]} and offered"
                        "a way out of the dungeon.")
            print_pause("However it will cost you gold.")

            if "gold" in item:
                give = input("Pay the gold you found?\n yes or no\n")

                if "yes" in give:
                    print_pause("You give the gold and are lead to a "
                                "secret passage.")
                    print_pause("It turns out it was a lie, and your "
                                "gold was stolen.")
                    print_pause("Fortunately for you thats all that happened.")
                    print_pause("As you make your way back you discover a "
                                "golden sword.\n"
                                "Light yet sharp and capable of breaking any "
                                "other metal it slices through.")
                    print_pause("With this you shouldn't fear anything.")
                    item.append("sword")
                    left_right(item, location, enemy1, guard1)

                elif "no" in give:
                    print("You make your way back.\nWhat now?")

            else:
                print_pause("Not having any gold you decide to make"
                            "your way back the way you came from.")
                left_right(item, location, enemy1, guard1)

        else:
            print("Try again")

    elif "yes" in yes_no and "sword" in item:
        print_pause("Seems like no one is home now.")
        print_pause("So you simply head back.")
        left_right(item, location, enemy1, guard1)

    elif "no" in yes_no:
        print_pause("With fear you head back the way you came from.")
        left_right(item, location, enemy1, guard1)

    else:
        print_pause("Try again")
        left_right(item, location, enemy1, guard1)


def cave(item, location, enemy1, guard1):
    print_pause("After a long walk you arrived to a dark cave.")
    print_pause("Would you like to look around\n")
    look = input("yes or no\n")

    while True:

        if "yes" in look and not("gold" in item):
            print_pause("You spot something shimmering on the ground.")
            print_pause("After further analysis you discover some "
                        "gold on the ground.")
            print_pause("As your picking it up you discover light"
                        " coming from an opening up ahead.")
            item.append("gold")
            location.append("light")
            cave2(item, location, enemy1, guard1)
            break

        elif "no" in look:
            print_pause("You simply make your way back the way you came from.")
            left_right(item, location, enemy1, guard1)

        elif "yes" in look and "gold" in item:
            print_pause("After searching you discover the light once more\n"
                        "and make your way towards it.")
            break

        else:
            print("Try again")


def cave2(item, location, enemy1, guard1):
    light = input("Would you like to continue up ahead, yes or no\n")

    if "yes" in light:
        print_pause("You make your way towards the light.")
        return

    elif "no" in light:
        print_pause("You simply make your way back the way you came from.")
        left_right(item, location, enemy1, guard1)

    else:
        print_pause("Try again")
        cave2(item, location, enemy1, guard1)


def light(item, location, enemy1, guard1):
    print_pause("Once you make your way outside, you notice someone.")
    print_pause(f"It's {guard1[0]}")
    light1(item, location, enemy1, guard1)


def light1(item, location, enemy1, guard1):
    approach = input("Would you like to approach or run?:\n")

    if "approach" in approach:
        print_pause("He sees you approaching")
        print_pause("and lets you know not to go any further.")
        print_pause("unless you don't fear losing your life")
        light2(item, location, enemy1, guard1)

    elif "run" in approach:
        print_pause("Running in fear you simply make your way back."
                    "What now?")
        left_right(item, location, enemy1, guard1)

    else:
        print("Try again")
        light1(item, location, enemy1, guard1)


def light2(item, location, enemy1, guard1):

    while True:
        con = input("Continue?\nyes or no\n")

        if "yes" in con:

            if "sword" in item:
                victory(item, location, enemy1, guard1)
                return

            else:
                death(item, location, enemy1, guard1)
                return

        elif "no" in con:
            print_pause("Running in fear you simply make your "
                        "way back to where you started.\n"
                        "What now")
            left_right(item, location, enemy1, guard1)

        else:
            print("Try again")
            light2(item, location, enemy1, guard1)


def death(item, location, enemy1, guard1):
    print_pause("He imediately strikes you from above\n"
                "not having a sword it's instant death.")
    print_pause("Seems like you lost your life and he has "
                "gotten away with your belongings.")
    print_pause("\n\nGame Over\n\n")
    play_again(item, location, enemy1, guard1)


def victory(item, location, enemy1, guard1):
    print_pause("Having no fear because of the sword you approach.\n")
    print_pause("He strikes you from above only to have his "
                "sword snap at the point of contact with yours.")
    print_pause(f"Not wanting to kill {guard1} you let him live\n"
                "and make your way out of the dungeon, never to return again")
    play_again(item, location, enemy1, guard1)


def play_again(item, location, enemy1, guard1):
    item.clear()
    location.clear()
    enemy1.clear()
    guard1.clear()
    play = input("Would you like to play again?\nyes/no\n")

    if "yes" in play:
        print_pause("Let the game begin")
        print_pause("\n\n\n\n")
        adventure()

    elif "no" in play:
        print("Hope you had fun")

    else:
        print("Try again")
        play_again(item, location, enemy1, guard1)


def adventure():
    item = []
    location = []
    enemy = ["A Vampire", " An Ogre", "La llorona",
             "A large man", "El Chupacabra"]
    enemy1 = []
    enemy1.append(random.choice(enemy))
    guard = [" A Knight", "Link", "The tooth fairy"]
    guard1 = []
    guard1.append(random.choice(guard))
    intro()
    left_right(item, location, enemy1, guard1)


adventure()
