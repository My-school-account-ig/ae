import sys
import time
import logging
import warnings
sys.stderr.write("err: import time is unused\n")
sys.stderr.write("THERE IS AN ERROR ON LINE 55\n")
sys.stderr.write("there is no number c on line 38\n")

print("This part of the game is old and outdated, it won't be updated and debug mode is always on. soz! - the creator :3")
time.sleep(1)
print("If you want the updated version of the game, please download the latest version of the game on github (look at releases, it should be at the top, this will be at the bottom) - the (femboy) creator :3")
time.sleep(1)

inventory = []

def house_bedroom():
    print("house_bedroom() subroutine is activated")
    print("You need to leave and escape.")
    print("""What do you want to do?
1) leave the bedroom
2) grab your phone
3) inventory (does not progress the game)""")
    choice = input(int())
    if choice == "1":
        warnings.warn("no subroutine", stacklevel=2)
        sys.stderr.write("program has terminated")
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
