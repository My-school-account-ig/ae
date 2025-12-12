import sys
import time
sys.stderr.write("err: import time is unused\n")
sys.stderr.write("THERE IS AN ERROR ON LINE 55\n")
sys.stderr.write("there is no number c on line 38\n")

print("This part of the game is old and outdated, it won't be updated and debug mode is always on. soz! - the creator :3")
print("If you want the updated version of the game, please download the latest version of the game on github (look at releases, it should be at the top, this will be at the bottom) - the (femboy) creator :3")

def house():
    print("house() subroutine is activated")
    print("this is the house where your're lives")
    print("tiem to leave teh hose :3")
    house_bedroom()

name = print("What's your're name?")
sys.stderr.write("err: unused variable name\n")
print("sike your're name is caine >:3")
print(";w;")
print("ono zombie caine aaaaaaa zombie aaaaaaaaaaaaaaaa - said co-caine")
print("dgsafagrwigfrwuvfebvgiubjsbvv\bxzbv - says the zombie")
print("ono the zombie has zombied the zombie and is going to zombie our zombie runnn! - said co-caine")
house()

inventory = []

def house_bedroom():
    print("house_bedroom() subroutine has been activated")
    print("You phone grab the phone")
    inventory.append("phone")
    choice = input("""What to are the want you to do?
a) check inventory
b) go to the landing
""")
    if choice == "check inventory":
        print("inventory: ", inventory)
        house_bedroom()
    elif choice == "hallway":
        house_hallway()
    elif choice == "landing":
        house_hallway()
    else:
        print("yoy're have been of the dead")
        
def street():
    print("street() subroutine is activated")
    print("its car time")
    choice = input("""What do you want to do?
a) check inventory
b) get in the car""")
    if choice == "check inventory":
        print("inventory:", inventory)
        street()
    elif choice == "get in the car":
        car_newport()

def m4_to_cardiff():
    print("m4_to_cardiff() subroutine is activated")
    print("gotta go fast - some wise person")
    cardiff()
    
def cardiff():
    print("cardiff() subroutine is activated")
    print("caerdydd is reiiiiiiiiiiiiiiiiiiiiglkvq")
    choice = input("""what do you want to do?
a) check inventory
b) go get supplies
c) go back to newport""")
    if choice == "check inventory":
        print("inventory:", inventory)
        cardiff()
    elif choice == "go get supplies":
        supplies_cardiff()
    elif choice == "go back to newport":
        m4_to_newport()
    else:
        sys.stderr.out("illegal instruction")
        cardiff()
    
def supplies_area():
    print("supplies_area() subroutine is activated")
    print("nyeh heh heh heh heh supplies for the us >:3")
    inventory.append("supplies")

def house_hallway():
    print("house_hallway() subroutine is activated")
    print("hellway >:3")
    choice = input("""what do you want to do?
a) check inventory
b) go to the kitchen
c) go outside""")
    if choice == "go into the kitchen":
        house_kitchen()
    elif choice == "go outside":
        street()
    elif choice == "check inventory":
        print("inventory:", inventory)
        house_hallway()
    else:
        print("your're have been of the dead, please restat >:3")
    
def house_kitchen():
    print("house_kitchen() subroutine is activated")
    print("suplieries >:3")
    print("ded end")
    zombie = True
    choice = input("""what do you want to do?
a) check inventory
b) check cupboard
c) fight zombie
d) leave kitchen""")
    if choice == "check cupboard":
        which = int(input("""which cupboard?
a) cupboard a
b) cupboard b"""))
        if which == "a":
            kitchen_cupboard_thing_a()
        elif which == "b":
            kitchen_cupboard_thing_b()
        else:
            kitchen_cupboard_thing_c()
    elif choice == "fight":
        fight = input("""do the fight you zombie?
a) fight
b) don't fight""")
        if fight == "fight":
            if gotknife == True:
                print("you stab zombie")
                inventory.remove("knife")
                gotknife = False
                zombie = False
            elif fight == "don't fight":
                print("You get away from the zombie")
                house_kitchen()
            else:
               print("deaded")
    elif choice == "check inventory":
        print("inventory:", inventory)
        house_kitchen()
    elif choice == "leave kitchen":
        if zombie == True:
            print("You can't get past the zombie")
            house_kitchen()
        else:
            house_hallway()
    else:
        print("you didn't know what to do and ded :3")
    
def kitchen_cupboard_thing_a():
    print("kitchen_cupboard_thing_a() subroutine has been activated")
    if len(inventory) >= 3:
        print("you can't not not carry anymore not items")
    else:
        print("You have collected a of the knife :3")
        inventory.append("knife")
        gotknife = True
    house_kitchen()

def kitchen_cupboard_thing_b():
    print("kitchen_cupboard_thing_b() subroutine has been activated")
    if len(inventory) >= 3:
        print("no")
    else:
        print("you collected some supplies")
        inventory.append("supplies")
    house_kitchen()

def kitchen_cupboard_thing_c():
    print("kitchen_cupboard_thing_c() subroutine has been activated")
    print("this cupboard does not exist :3")
    print("you just wasted your're time >:3")
    house_kitchen()
    
def newport():
    print("newport() subroutine has been activated")
    choice = input("""Choose the choose
a) check inventory
b) go get supplies
c) go back""")
    if choice == "check inventory":
        print("inventory: ", inventory)
        newport()
    elif choice == "go get supplies":
        supplies_area()
    elif choice == "go back":
        car_newport()
        
def car_newport():
    print("car_newport() subroutine has been activated")
    choice = input("""where do you want to go?
a) check inventory
b) go into town
c) go to sainsburys
d) go to the M4
e) go up malpas road""")
    if choice == "check inventory":
        print("inventory:", inventory)
        car_newport()
    elif choice == "go into town":
        newport()
    elif choice == "go to sainsburys":
        supplies_sainsburys()
    elif choice == "go to the M4":
        m4_to_cardiff()
    elif choice == "go up malpas road":
        print("you go up malpas road, which it feels like a M6.5 earthquake")
        malpas_road()
    else:
        print("place not found, please try again")
        car_newport()
        
def supplies_newport():
    print("supplies_newport() subroutine has been activated")
    inventory.append("supplies")
    newport()
    
def supplies_sainsburys():
    print("supplies_sainsburys() subroutine has been activated")
    inventory.append("supplies")
    car_newport()

def supplies_cardiff():
    print("supplies_cardiff() subroutine has been activated")
    inventory.append("supplies")

def malpas_road():
    print("malpas_road() subroutine has been activated")
    print("you are now on the way to Llanfairpwllgwyngyllgogerychrywndrobwllllantysiliogogogoch")

def m4_to_newport():
    print("m4_to_newport() subroutine has been activated")
    car_newport()
    
def road_to_Llanfairpwllgwyngyllgogerychrwyn():
    print("??")

def devmode():
    print("devmode() subroutine has been activated")
    if devmode == 1:
        print("wow")

print("")

def yesnt():
    print("ono zombie caine aaaaaaa zombie aaaaaaaaaaaaaaaa - said co-caine")
    print("dgsafagrwigfrwuvfebvgiubjsbvv\bxzbv - says the zombie")
    print("ono the zombie has zombied the zombie and is going to zombie our zombie runnn! - said co-caine")
    #leave_house_quest(this no longer exists :3)
    house()

if 1 == 4:
    print("how") #prints if you somehow make 1 equals 4
