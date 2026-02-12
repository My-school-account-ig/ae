import sys
import time
import logging
import warnings
import random
sys.stderr.write("err: import logging is unused\n")
sys.stderr.write("THERE IS AN ERROR ON LINE 55\n")
sys.stderr.write("there is no number c on line 38\n")

x = int(random.randint(1, 3))

knife = 0

inventory = []

def holyhead():
    print("holyhead() subroutine has been activated")
    choice = 0
    print("you have arrived at holyhead and got some supplies")
    time.sleep(5)
    print("""what do you want to do?
1. look for more supplies
2. go back to llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
3. check inventory""")
    choice = input(int())
    if choice == "1":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("you look for more supplies")
        holyhead()
    elif choice == "2":
        llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        holyhead()
    else:
        warnings.warn("this will loop the subroutine", stacklevel=2)
        warnings.warn("please input a valid integer", stacklevel=2)
        holyhead()
        
def llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch():
    print("llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch() subroutine has been activated")
    choice = 0
    print("you have reached llanfairpwllgwyngyllgogerychrywndrobwllllantysiliogogogoch after hours of driving")
    time.sleep(5)
    print("""what do you want to do?
1) get some rest
2) go get some more supplies from holyhead
3) check inventory""")
    choice = input(int())
    if choice == "1":
        print("you have completed the game")
        print("theres nothing else to do now")
    elif choice == "2":
        warnings.warn("this subroutine doesn't exist", stacklevel=2)
        sys.stderr.write("program has been terminated")
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    else:
        warnings.warn("this will loop the subroutine", stacklevel=2)
        warnings.warn("please input a valid integer", stacklevel=2)
        llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()

def road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch():
    print("road_to_llanfairpwlldwyngyllgogerychwyrndrobwllllantysiliogogogoch() subroutine has been activated")
    choice = 0
    print("holy thats a long subroutine name")
    print("you are on the road to llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")
    print("""where do you want to go?
    1) keep going
    2) loot services
    3) check inventory""")
    choice = input(int())
    if choice == "1":
        warnings.warn("this subroutine doesn't exist", stacklevel=2)
        sys.stderr.write("program has been terminated")
    elif choice == "2":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("you loot the services and got supplies")
        road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    else:
        warnings.warn("this will loop the subroutine", stacklevel=2)
        warnings.warn("please input a valid integer", stacklevel=2)
        road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()

def m4_b():
    print("m4_b() subroutine has been activated")
    choice = 0
    print("a")
    time.sleep(5)
    print("""where do you want to go?
    1) back to newport
    2) go to llanfairpwllgwyngyllgogerychwryndrobwllllantysiliogogogoch
    3) check inventory""")
    choice = input(int())
    if choice == "1":
        newport()
    elif choice == "2":
        road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        m4_b()
    else:
        warnings.warn("this will loop the subroutine", stacklevel=2)
        warnings.warn("please input a valid integer", stacklevel=2)
        m4_b()

def cardiff():
    print("cardiff() subroutine has been activated")
    choice = 0
    print("you have arrived at cardiff")
    time.sleep(5)
    print("""what do you want to do?
    1) get supplies
    2) go back on the m4
    3) check inventory""")
    choice = input(int())
    if choice == "1":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("you got some supplies")
        cardiff()
    elif choice == "2":
        m4_b()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        cardiff()
    else:
        warnings.warn("this will loop the subroutine", stacklevel=2)
        warnings.warn("please input a valid integer", stacklevel=2)
        cardiff()

def m4_a():
    print("m4_a() subroutine has been activated")
    choice = 0
    print("you are on the m4")
    time.sleep(5)
    print("""where do you want to go?
1) go to cardiff
2) go to Llanfairpwllgwyngyllgogerychrwyndrobwllllantysiliogogoch
3) check inventory""")
    choice = input(int())
    if choice == "1":
        cardiff()
    elif choice == "2":
        road_to_llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        m4_a()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        m4_a()

def newport():
    print("newport() subroutine has been activated")
    choice = 0
    print("you can skip this if you want lol")
    time.sleep(5)
    print("""what do you want to do?
1) go get supplies
2) go on the M4
3) check inventory""")
    choice = input(int())
    if choice == "1":
        print("you go get supplies and got food")
        warnings.warn("this will loop the subroutine", stacklevel=2)
        newport()
    elif choice =="2":
        m4_a()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        newport()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        newport()

def street():
    print("street() subroutine has been activated")
    choice = 0
    print("you are now outside")
    print("""what do you want to do?
1) get in the car
2) check inventory""")
    choice = input(int())
    if choice == "1":
        newport()
    elif choice =="2":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        street()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        street()

def house_kitchen_cupboards():
    print("house_kitchen_cupboards() subroutine has been activated")
    choice = 0
    print("you go to check the cupboards")
    time.sleep(5)
    print("""check cupboard:
1) cupboard 1
2) cupboard 2
3) cupboard 3
4) go back
5) check inventory""")
    choice = input(int())
    if choice == "1":
        print("you check the cupboard")
        if x == "1":
            print("you found a knife")
            inventory.append("knife")
            knife = 1
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "2":
        print("you check the cupboard")
        if x == "2":
            print("you found a knife")
            inventory.append("knife")
            knife = 1
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "3":
        print("you check the cupboard")
        if x == "3":
            print("you found a knife")
            inventory.append("knife")
            knife = 1
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "4":
        house_kitchen()
    elif choice == "5":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_kitchen_cupboards()
    else:
        warnings.warn("please input a vaild integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        house_kitchen_cupboards()

def house_kitchen():
    print("house_kitchen() subroutine has been activated")
    choice = 0
    print("you went into the kitchen")
    time.sleep(5)
    print("""what do you want to do?
1) fight zombie
2) look in the cupboards
3) check inventory""")
    choice = input(int())
    if choice == "1":
        print("you go to fight the zombie")
        if knife == 1:
            print("you fight the zombie")
            print("you win")
            house_hallway()
        else:
            print("you can't fight the zombie yet")
            warnings.warn("this will repeat the subroutine", stacklevel=2)
            house_kitchen()
    elif choice == "2":
        house_kitchen_cupboards()
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_kitchen()
    else:
        warnings.warn("please input a vaild integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_kitchen()

def house_hallway():
    print("house_hallway() subroutine has been activated")
    choice = 0
    print("you entered the hallway")
    time.sleep(1)
    print("""what do you want to do?
1) go to the kitchen
2) go outside
3) go to the living room
4) go to the dining room
5) check inventory""")
    choice = input(int())
    if choice == "1":
        house_kitchen()
    if choice =="2":
        street()
    if choice == "3":
        print("You have died, please restart the game (there is no saving lol)")
    if choice == "4":
        print("You have died, please restart the game (there is no saving lol)")
    if choice == "5":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_hallway()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_landing()

def house_landing():
    print("house_landing() subroutine has been activated")
    choice = 0
    print("you have entered the landing")
    time.sleep(5)
    print("""only 1 of 4 rooms will help you escape
1) turn back
2) bedroom 2
3) bedroom 3
4) bathroom
5) go downstairs
6) inventory (does not progress the game)""")
    choice = input(int())
    if choice == "1":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "2":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "3":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "4":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "5":
        house_hallway()
    elif choice == "6":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_landing()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_landing()

def house_bedroom():
    print("house_bedroom() subroutine is activated")
    print("You need to leave and escape.")
    time.sleep(5)
    print("""What do you want to do?
1) leave the bedroom
2) grab your phone
3) inventory (does not progress the game)""")
    choice = input(int())
    if choice == "1":
        house_landing()
    elif choice == "2":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        inventory.append("phone")
        house_bedroom()
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_bedroom()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_bedroom()
    
def house():
    print("house() subroutine is activated")
    print("this is the house where your're lives")
    time.sleep(5)
    print("tiem to leave teh hose :3")
    house_bedroom()

name = print("What's your're name?")
time.sleep(5)
sys.stderr.write("err: unused variable name\n")
print("sike your're name is caine >:3")
time.sleep(1)
print(";w;")
time.sleep(5)
print("ono zombie caine aaaaaaa zombie aaaaaaaaaaaaaaaa - said co-caine")
time.sleep(1)
print("dgsafagrwigfrwuvfebvgiubjsbvv\bxzbv - says the zombie")
time.sleep(1)
print("ono the zombie has zombied the zombie and is going to zombie our zombie runnn! - said co-caine")
house()

