print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input("You're at a cross road.Where do you want to go?\n       Type \"Left\" or \"Right\"").lower()
if road == "right":
    print("You fall into s hole! GAME OVER!")
elif road == "left":
    print("You've come to a lake. You look and see there is a island in the middle of the lake! you have 2 options")
    wait = input("Type \"wait\" to wait for a boat or type \"swim\" to swin across").lower()
    if wait == "swim":
        print("You tried to swim across but were attacked and eaten by trouts! GAME OVER!")
    elif wait == "wait":
        print("You waited for a boat and once it arrived you got on and made it to the island! GREAT JOB!")
        print("You arrive on the island and discover a passage way that splits into four doors!")
        door = input("Type \"Yellow\", \"Red\" or \"Blue\" or \"Black\" \"Leave\"").lower()
        if door == "blue":
            print("You were attacked by Gobind Sarvar Gr8A wannabe daku's! GAME OVER!")
        elif door == "red":
            print("you were double teamed by Dr Chahal and ms Rekhi.GAME OVER!")
        elif door == "yellow":
            print("Congrats you have survived 24hours in Gobind Sarvar! Your reward is becoming the GURDWARA PARDHAN! GREAT JOB!")
        elif door == "black":
            print("Congrats! you have unlocked prime Mr Joshi! He kills everyone by maintaining the decorum of the island and gets you the Dub! YES BOSS!")
        elif door == "leave":
            print("Why are You running? WHY ARE YOU RUNNING!!! GAME OVER!")
        else:
            print("You loose! Maybe listen to instructions")

print("Are you ready for the ultimate challenge? Get Ready For Survive GOBIND SARVAR PART 2!")