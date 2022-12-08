#ExampleQuest v2
#Simulates a simple text-based RPG battle
#2-14-22
#CSI 106.01

import random
import jvf
import displayArt

#======= STAT VALUES ====================
high = 100
medium = 75
low = 50
atkMod = 5
healCost = 10
healPercent = .15
border = "==================================================================="
#========================================
#========================================
#Introduce game
#-- Print some ASCII art:  ExampleQuest
#========================================
def intro():

   title = '''
     ______                           _       ____                  _
    |  ____|                         | |     / __ \                | |
    | |__  __  ____ _ _ __ ___  _ __ | | ___| |  | |_   _  ___  ___| |_
    |  __| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ |  | | | | |/ _ \/ __| __|
    | |____ >  < (_| | | | | | | |_) | |  __/ |__| | |_| |  __/\__ \ |_
    |______/_/\_\__,_|_| |_| |_| .__/|_|\___|\___\_\\__,_|\___||___/\__|
                               | |
                               |_|
   '''
   jvf.slowPrint("Welcome to....")
   print(title)
   print(border)

#=============================
#Create character
#=============================
def createCharacter():
   player = {}

   #-- get name from user
   player["name"] = input("Enter a name for your characer: ")
   while(len(player["name"]) == 0):
      player["name"] = input("Enter a name for your characer: ")
   #-- have the user pick a class
   classMenu = '''
   =====================SELECT YOUR CLASS================================
   1) Wizard:  A magical sorcerer, weilding spells but weak of flesh
   2) Warrior:  A fierce competitor, dealing high damage but weak of mind
   3) Rogue:  A 'glass cannon', dealing high damage but low HP
   '''

   classSelected = False
   while(not classSelected):  #begin selection loop
       print(classMenu)
       userClass = input("CHOOSE WISELY:")
       while(userClass not in ("1","2","3")):
          userClass = input("CHOOSE WISELY:")

       if(userClass == "1"):
           player["hp"] = medium
           player["mp"] = high
           player["speed"] = low
           player["attack"] = low
           player["maxHP"] = medium
           player["fled"] = False

           print("Name:", player["name"])
           print("HP:", player["hp"])
           print("MP:", player["mp"])
           print("Speed:", player["speed"])
           print("AttacK", player["attack"])

       elif(userClass == "2"):
           player["hp"] = high
           player["mp"] = low
           player["speed"] = medium
           player["attack"] = high
           player["maxHP"] = high
           player["fled"] = False

           print("Name:", player["name"])
           print("HP:", player["hp"])
           print("MP:", player["mp"])
           print("Speed:", player["speed"])
           print("AttacK", player["attack"])

       elif(userClass == "3"):
           player["hp"] = low
           player["mp"] = medium
           player["speed"] = high
           player["attack"] = high
           player["maxHP"] = low
           player["fled"] = False

           print("Name:", player["name"])
           print("HP:", player["hp"])
           print("MP:", player["mp"])
           print("Speed:", player["speed"])
           print("AttacK", player["attack"])

       else:
           print("Invalid selection: ", userClass)


       classSelected = jvf.confirm("Continue with selection? (y/n):")
       #end selection loop
       return player

def displayStatus(character):
   print(border)
   print(character["name"])
   print("HP: ", character["hp"])
   print("MP: ", character["mp"])

#========================================================
#======================= SETUP ENEMY=====================
#========================================================
def createEnemy():
   enemy = {}
   #Generate random enemy
   #--- roll a random number (random.randint(1, numEnemies))
   numEnemies = 3
   eNum = random.randint(1, numEnemies)

   if(eNum == 1):
       #--- Enemy 1:  The Greed Gobbler
       #---------- HP: low
       #---------- SPD: high
       #---------- ATK: medium
       enemy["name"] = "The Greed Gobbler"
       enemy["art"]= displayArt.displayArt(enemy["name"])
       enemy["hp"] = low
       enemy["attack"] = medium
       enemy["speed"] = high
       enemy["maxHp"] = enemy["hp"]
       enemy["mp"] = medium
       enemy["fled"] = False
       enemy["dialogue"] = ("GG1","GG2","GG3")

   elif(eNum == 2):
       #--- Enemy 2:  Octavius the Ogre
       #---------- HP: high
       #---------- SPD: slow
       #---------- ATK: high
       enemy["name"] = "Octavius the Ogre"
       enemy["art"]= displayArt.displayArt(enemy["name"])
       enemy["hp"] = high
       enemy["attack"] = high
       enemy["speed"] = low
       enemy["mp"] = medium
       enemy["maxHp"] = enemy["hp"]
       enemy["fled"] = False
       enemy["dialogue"] = ("OO1","OO2","OO3")

   elif(eNum == 3):
       enemy["name"] = "Goblin Gregg"
       enemy["art"]= displayArt.displayArt(enemy["name"])
       enemy["hp"] = low
       enemy["attack"] = low
       enemy["speed"] = medium
       enemy["mp"] = medium
       enemy["maxHp"] = enemy["hp"]
       enemy["fled"] = False
       enemy["dialogue"] = ("Gregg1","Gregg2","Gregg3")

   else:
       print("This should not print.", eNum)

   return enemy

#========================================================
#======================== FIGHT!!! ======================
#========================================================
def fight(player, enemy):

   #While no-one has lost - player HP and enemy HP are > 0:

   print(border)
   jvf.slowPrint(enemy["name"] +" appears! Defend yourself!")
   print(border)

   actionMenu = '''
   =========
   1) Attack:    Try to deal some damage based on ATK
   2) Cast:
   3) Heal:      10 MP
   4) Run:       Chance to flee based on SPD
   5) Talk:      Try to avoid violence
   =========
   '''
   while(player["hp"] > 0 and enemy["hp"] > 0 and not player["fled"] and not enemy["fled"]):
       displayStatus(player)
       displayStatus(enemy)

       #========================
       #=== PLAYER TURN ========
       #========================

       #display option menu
       print(actionMenu)
       #select an option
       #--- ATTACK: roll how much damage, random.randint(1?, ATK?)
       #--- CAST:  if we have enough MP, does set damage, reduces MP
       #--- HEAL: add to your HP a set amount
       #--- RUN: some chance to escape, generate a random number based on our and enemies speed
       #--- TALK: see what it has to say - prints random battle dialogue

       userInput = input("--> ")
       if(userInput == "1"): #attack
           jvf.slowPrint("You swing at the " + enemy["name"] + "...")
           damage = random.randint(1, player["attack"] // atkMod)
           jvf.slowPrint("...dealing " + str(damage) + " damage!")
           enemy["hp"] -= damage
       elif (userInput == "5"):
          print("You attempt to communicate with", enemy["name"])
          print(random.choice(enemy["dialogue"]))
       elif(userInput == "4"): #run
           jvf.slowPrint("You attempt to flee....")
           runVal = player["speed"] - enemy["speed"]
           if(runVal >= 0): #we are faster
               escapeRoll = random.randint(1,3)
               if(escapeRoll == 1): #we succeed (33% chance)
                   jvf.slowPrint("...and managed to escape!")
                   player["fled"] = True
               else:
                   jvf.slowPrint("...but failed miserably!")
           else: #enemy is faster
               escapeRoll = random.randint(1,5)
               if(escapeRoll == 1): #we succeed (20% chance)
                   jvf.slowPrint("...and managed to escape!")
                   player["fled"] = True
               else:
                   jvf.slowPrint("...but failed miserably!")
       elif(userInput == "3"): #heal
           if(player["mp"] >= healCost):
               player["mp"] -= healCost
               healVal = player["maxHP"] * healPercent
               jvf.slowPrint("You heal for", healVal)
               player["hp"] += healVal
           else:
               jvf.slowPrint("You don't have the required" + str(healCost) + "MP!")
       else:
           print("Not yet implemented.")

       #====================
       #=== ENEMY TURN =====
       #====================
       #enemy attacks
       #--- SAME AS PLAYER
       #--- random selection
       eMove = random.randint(1,3) #CHANGE ONCE PLAYER MOVES IMPLEMENTED!!!!!!!!!!
       if eMove == 1: #ATTACK
           jvf.slowPrint(enemy["name"] + " swings at you...")
           damage = random.randint(1, enemy["attack"] // atkMod)
           jvf.slowPrint("...dealing " + str(damage) + " damage!")
           player["hp"] -= damage
       elif eMove == 2: #HEAL
           healVal = enemy["maxHp"] * healPercent
           jvf.slowPrint(enemy["name"] + "heals for " + str(healVal))
           enemy["hp"] += healVal
       elif eMove == 3: #RUN
           jvf.slowPrint(enemy["name"] + " attempts to flee....")
           runVal = enemy["speed"] - player["speed"]
           if(runVal >= 0): #they are faster
               escapeRoll = random.randint(1,5)
               if(escapeRoll == 1): #they succeed (20% chance)
                   jvf.slowPrint("...and managed to escape!")
                   enemy["fled"] = True
               else:
                   jvf.slowPrint("...but failed miserably!")
           else: #player is faster
               escapeRoll = random.randint(1,10)
               if(escapeRoll == 1): #they succeed (10% chance)
                   jvf.slowPrint("...and managed to escape!")
                   enemy["fled"] = True
               else:
                   jvf.slowPrint("...but failed miserably!")
       else:
           print("This shouldn't print.")

#======================================================
#----------------    ENDING  --------------------------
#======================================================='''
def ending(p,e):
   if(p["hp"] <= 0):
      jvf.slowPrint("You are dead. The " + e["name"] + "stands victorious!", .06)
   elif(e["hp"] <= 0):
      jvf.slowPrint("Sweet victory! The " + e["name"] + " lies slain at your feet!", .06)
   elif(p["fled"]):
      jvf.slowPrint("You manage to escape with your life....if not your honor.", .06)
   elif(e["fled"]):
      jvf.slowPrint("The " + e["name"] + " scurries away, wounded but alive.", .06)
   else:
      print("Should not print")

def main():
   intro()
   player = createCharacter()
   enemy = createEnemy()
   displayStatus(player)
   displayStatus(enemy)
   displayArt.displayArt(enemy)
   fight(player, enemy)
   ending(player, enemy)

main() #call main
