import time
print("You're approaching a mountain, do you want to climb the mountain or setup camp?")
print("(Make your answers lowercase! ♥)")
opt1=input("climb, or setup camp?: ")
inventory = ["Shortsword", "3x Apple", "Foldable crossbow", "3x Rope Coil", "Bottle of Soapy Water"]



if opt1=="climb":
    print("You begin to sacle to mountain.")
    print("You come across a rabid overwatch player.")
    Mtn1=input("What do you want to do? check inventory, or run away?")
    print("(inventory or run)")
    if Mtn1=="inventory":
            print("You open your backpack")
            print(inventory)
    elif Mtn1=="run":
        print("Another rabid overwatch player comes out of nowhere and hacks you.")
        time.sleep(2) 
        print("Your legs no longer work.")
        time.sleep(2) 
        print("You met your demise by roadhog thug shake..")
        time.sleep(2) 
    

elif opt1=="setup camp":
    print("You begin to setup camp.")



else:
    print("You sat there and drooled to death. ):")
    print("Are you happy with youself you indecisive sort?")

