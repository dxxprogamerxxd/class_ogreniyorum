import csv
import os
from inputimeout import inputimeout
import time
riddle_tries = 0 #riddle trial counter

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #This command clears all the unnecessary things on the terminal 



class Riddles:
    all = []
    def __init__(self, question: str, answer: str,hint: str):
        self.question = question
        self.answer = answer
        self.hint = hint

        Riddles.all.append(self)

    def __str__(self):
        return f"{self.question}"
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('/Users/kaankartal/Desktop/proje/source.csv','r') as f: #Place path if python code can not find the .csv folder
            reader = csv.DictReader(f)
            riddles = list(reader)
        for riddle in riddles:
            Riddles(
                question =riddle.get('question'),
                answer = riddle.get('answer'),
                hint = riddle.get('hint')
            )
Riddles.instantiate_from_csv() #Riddles and answer are taken from .csv file provided with the code

class Items:
    def __init__(self, name:str):
        self.name = name
        

class Swords(Items):
    def __init__(self, name:str ,damage:int):
        super().__init__(name)
        self.damage = damage
        
    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"

class Shields(Items):
    def __init__(self,name:str,armor:int):
        super().__init__(name)
        self.armor = armor
    
    def __str__(self):
        return f"[{self.name} (Armor: {self.armor})"
class Character:
    def __init__(self, name: str, damage: int=10, health: int=100, max_health: int=100,lowest_health: int=0,alive:bool = True):
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = max_health
        self.lowest_health = lowest_health
        self.alive = alive
    
    def add_hp(self,health): #working for every character
        if (self.health + health) > self.max_health:
            self.health = self.max_health
        else:
            self.health += health

enemy = Character("Monster",20)


class Main_Player(Character):
    sword = []
    shield = []
    mis_items =[]
    armor = 0
    def add_sword(self, item):
        if len(main_character.sword) >=1:
            while True:
                try:
                    ask_user = int(input(f"Do you want to unequip your current weapon {main_character.sword[0]} for  weapon {item} ? \n 1-> Yes \n 2-> No \n"))
                    if ask_user == 1:
                        
                        main_character.unequip_items_sword(main_character.sword[0])
                        self.sword.append(item)
                        self.damage += item.damage
                        break
                
                    elif ask_user ==2:
                        return None
                except ValueError:
                        print("Please input accordingly.")
                        os.system('cls' if os.name ==  'nt' else 'clear')
        else:
            self.sword.append(item)
            self.damage += item.damage
        

    def add_shield(self, item):
        if len(main_character.shield) >=1:
            while True:
                try:
                    ask_user = int(input(f"Do you want to unequip your current shield {main_character.shield[0]} for  shield {item} ? \n 1-> Yes \n 2-> No \n"))
                    if ask_user == 1:
                            
                        main_character.unequip_items_shield(main_character.shield[0])
                        self.shield.append(item)
                        self.armor += item.armor
                        break
                    
                    elif ask_user ==2:
                        return None
                except ValueError:
                        print("Please input accordingly.")
                        os.system('cls' if os.name ==  'nt' else 'clear')
        else:
            self.shield.append(item)
            self.armor += item.armor

    def add_item(self, item):
        self.mis_items.append(item)



    def unequip_items_sword(self, item): 
        self.sword.remove(item)
        self.damage -= item.damage
    
    def unequip_items_shield(self, item): 
        self.shield.remove(item)
        self.armor -= item.armor


    def show_items(self):
        while True:
            clear()
            try:
                usr_input = int(input("Do you want to view sword or shield \n 1-> Sword \n 2-> Shield \n 3-> Miscellaneous Items \n 4-> Back \n" ))
                if usr_input == 1:
                    try:
                        input(main_character.sword[0])
                        clear()
                        break
                    except IndexError:
                        input("Character does not have any sword. Press any key to continue... ")
                        clear()
                        break
                elif usr_input ==2:
                    try:
                    
                        input(f'{main_character.shield[0]}')
                        clear()
                        break
                    except IndexError:
                        input("Character does not have any shield. Press any key to continue...")
                        clear()
                        break
                elif usr_input ==3:
                    try:
                        if len(main_character.mis_items) != 0:
                            input(f'{main_character.mis_items}')
                            clear()
                            break
                        else:
                            input("Character does not have any miscellaneous items. Press any keys to continue... ")
                            clear()
                            break
                    except IndexError:
                        input("Character does not have any miscellaneous items. Press any key to continue... ")
                elif usr_input ==4:
                    break

                else:
                    input("Invalid choice. Press any key to continue...")
                    clear()
            except ValueError:
                input("Invalid choice. Press any key to continue...")
                clear()
        


def rules(player):
    clear()
    print("There are 6 rooms with 2 of them locked with riddles.")
    print("Your aim is to collect the items and answer riddles within 10 seconds")
    print("In this game actions will be done instantly as this game is based on text.")
    input(f"Press any key to continue player: {player.name} ")
    clear()
          

def character_name(): #Set main player name
    clear()
    global main_character
    tries = 0 #Test variable for yes and no
    triess = 0 #Test variable for invalid character input
    while True:
        print("What will be your name adventurer?")
        if tries >= 3:
            print("Come on just fill it with something! ")
        name = input("> ")
        while True:
            try:
                r_u_sure = int(input(f"Is your name {name}? \n 1-> Yes \n 2-> No \n "))
                if r_u_sure == 1:
                    main_character = Main_Player(name, 10, 100, 100,0)
                    return None
                elif r_u_sure == 2:
                    tries += 1
                    break
                else:
                    triess +=1
                    if triess >= 3:
                        print("If you do not enter a valid number this will go on forever buddy!")
            except ValueError:
                print("Please input a valid number.")
                triess += 1
                if triess >= 3:
                    print("If you do not enter a valid number this will go on forever buddy!")

def confirmed():
    input("Press any key to continue... ")


class Rooms:
    def __init__(self,name,has_shield:bool=None,has_sword:bool=None,riddles:bool=None,item=None,item_pickable:bool=False,visit_count:int = 0,description:str="Oda açiklaması",has_item:bool = False,item2=None):
        self.name = name
        self.has_shield = has_shield
        self.has_sword = has_sword
        self.riddles = riddles
        self.item = item
        self.exits = {"north": None, "south": None, "east": None, "west": None}
        self.item_pickable = item_pickable
        self.description = description
        self.has_item = has_item
        self.visit_count = visit_count
        self.item2 = item2
    def __str__(self):
        return f"{self.name}"


    def search_room(self):
        clear()
        if current_room == fifth_room and current_room.visit_count >= 2 and sixth_room.visit_count > 0 and len(main_character.mis_items) ==1:
            print("There seems to be a key!")
            confirmed()
            return None
        if self.has_item == True and self.item != None:
            print("There seems to be some items.")
            confirmed()
            clear()
        elif self.has_shield == True:
            print("There seems to be a shield.")
            confirmed()
            clear()
        elif self.has_sword == True:
            print("There seems to be a sword.")
            confirmed()
            clear()
        elif self.has_item == False and self.has_shield == False and self.has_sword == True:
            print("There is nothing to find!")
            confirmed()
            clear()
        else:
            print("There is no item in this room!")
            confirmed()
            clear()
        self.item_pickable = True


    def pick_up(self):
        if self.item_pickable == False:
            clear()
            print("You have to search the room first. ")
            confirmed()
            clear()
            return None
        
        elif self.has_shield == True and self.item_pickable == True:
            clear()
            main_character.add_shield(self.item)
            print(f"Picked up {self.item}!")
            self.has_shield = False
            confirmed()
            clear()
            return None
        
        elif self.has_sword == True and self.item_pickable == True:
            main_character.add_sword(self.item)
            print(f"Picked up {self.item}!")
            self.has_sword = False
            confirmed()
            clear()
            return None

        if len(main_character.mis_items) == 0 and current_room.has_item == True:
            main_character.add_item(current_room.item)
            print(f"Picked up {self.item}")
            current_room.has_item = False
            confirmed()
            clear()
            return None

        elif len(main_character.mis_items) == 1 and current_room == fifth_room and sixth_room.visit_count > 0:
            main_character.add_item(current_room.item2)
            print(f"Picked up {self.item2}")
            confirmed()
            clear()
            return None
        else:
            input("There is no item to pick up. Press to continue...")
        



class Room5(Rooms):
    def fighting_with_monster(self):
        input("Monster rush towards to character and character uses it's shield to defend from monster's claw. Press any button to continue... ")
        input("Character pulls up it's sword to begin fighting with the monster. Press any button to continue...")

        while main_character.alive == True and enemy.alive == True :
            enemy.health -= main_character.damage
            print(f"Main character health: {main_character.health} \n Monster heatlh: {enemy.health}")
            time.sleep(1)
            if enemy.health <=0:
                print(f"Main character health: {main_character.health} \n Monster heatlh: 0")
                print("You have defeated the monster.")
                enemy.alive = False
                input("Press to continue... ")
                return None
            elif main_character.health <=0:
                print(f"Main character health: 0 \n Monster health: {enemy.health}")
                print("Monster has killed the character!")
                exit()
            damage = enemy.damage - main_character.armor
            main_character.health -= damage
            if enemy.health <=0:
                print(f"Main character health: {main_character.health} \n Monster heatlh: 0")
                print("You have defeated the monster.")
                enemy.alive = False
                input("Press to continue... ")
                return None 
            elif main_character.health <=0:
                print(f"Main character health: 0 \n Monster health: {enemy.health}")
                print("Monster has killed the character!")
                exit()
    

    

shield_1 = Shields('Big Shield',10)
sword_1 = Swords('Big Sword',10)
start_room = Rooms("First Room",True,False,False,shield_1,False,1,"This room is completely dark and also don't have any lock or door with password. Our character should find a shield in a many stuff.")
second_room = Rooms("Second Room",False,False,True,None,False,0,"Congrats! You have unlocked the door by solving the riddle.")
third_room = Rooms("Third Room",False,True,True,sword_1,False,0,"This room is filled with maps. Our character should find a sword for fighting with monster.")
forth_room = Rooms("Forth Room",False,False,True,False,False,0,"The surroundings are black are bright")
fifth_room = Room5("Fifth Room",False,False,False,"flashlight",False,0,"Our character suddenly sees the expected gigantic monster.\n Remember the rules. You may search for the items first as in this game actions will be done instantly so monster can not harm you in this moment. \n Our character should search through items and find a flashlight",True,"key")
sixth_room = Rooms("Sixth Room",False,False,False,False,False,0,"Character finds a safe and begins searching for a key.And sees that it left the key at fifth room.")
start_room.exits['north'] = second_room
second_room.exits['south'] = start_room
second_room.exits['north'] = third_room
third_room.exits['south'] = second_room
third_room.exits["north"] = forth_room
forth_room.exits["south"] = third_room
forth_room.exits["north"] = fifth_room
fifth_room.exits["south"] = forth_room
fifth_room.exits["north"] = sixth_room
sixth_room.exits["south"] = fifth_room

def open_safe():
    print("You use the flashlight to bright the safe.")
    time.sleep(1)
    print("You use the key you find at fifth room.")

    input("The End. \n Press any button to exit...")
    exit()









def what_do_you_want_from_me(what_do_you_want,current_room):
    if what_do_you_want == 1:
        current_room.search_room()
    elif what_do_you_want ==2:
        if current_room.has_shield == True or current_room.has_sword == True or current_room.has_item == True:
            current_room.pick_up()
        elif current_room == fifth_room and sixth_room.visit_count >= 1 and fifth_room.visit_count >= 2:
            current_room.pick_up()

        else:
            clear()
            input("There is no item to pick up. Press to continue...")
            clear()
    elif what_do_you_want ==3:
        main_character.show_items()
    elif what_do_you_want ==4:
        try:
            try:
                if current_room == start_room:
                    current_room = current_room.exits['north']
                    current_room.visit_count += 1
                    print(f"You move to the next room: {current_room}")
                    time.sleep(1)
                elif current_room != sixth_room:
                    where_do_you_want_to_go = int(input("Where do you want to want to go? \n 1-> North (Next Room) \n 2-> South (Previous Room) \n"))
                    if where_do_you_want_to_go == 1 and current_room.exits['north'] is not None:
                        current_room = current_room.exits['north']
                        current_room.visit_count += 1
                        print(f"You move to the next room: {current_room}")
                        time.sleep(1)
                        if current_room.visit_count ==1:
                            story(current_room)
                    elif where_do_you_want_to_go == 2 and current_room.exits['south'] is not None:
                        current_room = current_room.exits['south']
                        current_room.visit_count += 1
                        print(f"You move to the previous room: {current_room}")
                        time.sleep(1)
                        if current_room.visit_count ==1 and current_room !=2:
                            story(current_room)
                    else:
                        input("Invalid input. Press to continue...")
                        clear()
                else:
                    current_room = current_room.exits['south']
                    current_room.visit_count += 1
                    print(f"You move to the previous room: {current_room}")
                    time.sleep(1)
            except AttributeError:
                input("You can't go that way")
                clear()
            
        except ValueError:
            input("Invalid input. Press to continue...")
            clear()
    elif what_do_you_want ==5:
        input(f"{current_room}. Press any key to continue...")
        clear()
    elif what_do_you_want ==6:
        print(current_room.description)
        input("Press any button to continue... ")
    
    elif what_do_you_want == 7 and current_room == fifth_room and main_character.alive == True and enemy.alive == True:
        fifth_room.fighting_with_monster()
    
    elif what_do_you_want ==7 and current_room == sixth_room and len(main_character.mis_items) == 2 and enemy.alive == True:
        input("You have to kill the monster before opening the safe! Press any button to continue..." )

    elif what_do_you_want ==7 and current_room == sixth_room and len(main_character.mis_items) == 2:
        open_safe()
        
    clear()
    return current_room



        
def second_room_riddle_trial():
    global riddle_tries
    print("As you move forward to the next room.")
    confirmed()

    clear()
    #story(current_room)
    print("Oh snap! This door has a lock and you have to unlock it by answering the riddle! Get ready riddle will come in any moment (don't press any button it will come)")
    time.sleep(1)
    hint_count = 0
    while True:
        if hint_count >=1:
                print(Riddles.all[0].hint)
        if riddle_tries >= 3:
            reason = "Your riddle try limit is over!"
            game_lose(reason)
        try:
            user_input = inputimeout(prompt=f'{Riddles.all[0].__str__()} \nYou have 10 seconds to answer \n', timeout=10).strip().lower()
            if user_input != Riddles.all[0].answer:
                print("Wrong answer")
                riddle_tries +=1
                hint_count +=1
                
            elif user_input == Riddles.all[0].answer:
                print("You got it True.")
                print("Door Unlocked")
                time.sleep(1)
                print("This room seems to have nothing in it so proceed to the next room")
                time.sleep(3)
                clear()
                return None
        except Exception:
            print("Timeout")
            riddle_tries +=1
            hint_count +=1
            print(Riddles.all[0].hint)
            print(f"You have {3 - riddle_tries} chances left")


def forth_room_riddle_trial():
    global riddle_tries
    print("As you move forward to the next room.")
    confirmed()
    clear()
    print("Oh snap! This door has a lock and you have to unlock it by answering the riddle! Get ready riddle will come in any moment (don't press any button it will come)")
    time.sleep(1)
    hint_count = 0
    while True:
        if hint_count >=1:
                print(Riddles.all[1].hint)
        if riddle_tries >= 3:
            reason = "Your riddle try limit is over!"
            game_lose(reason)
        try:
            user_input = inputimeout(prompt=f'{Riddles.all[1].__str__()} \nYou have 10 seconds to answer \n', timeout=10).strip().lower()
            if user_input != Riddles.all[1].answer:
                print("Wrong answer")
                riddle_tries +=1
                hint_count +=1
                
            elif user_input == Riddles.all[1].answer:
                print("You got it True.")
                print("Door Unlocked")
                time.sleep(1)
                print("This room seems to have nothing in it so proceed to the next room")
                time.sleep(3)
                clear()
                return None
        except Exception:
            print("Timeout")
            riddle_tries +=1
            hint_count +=1
            print(Riddles.all[1].hint)
            print(f"You have {3 - riddle_tries} chances left")


    

def game_lose(reason:str):
    print(f"You have lost the game. {reason}")
    exit()

current_room = start_room


def story(current_room):
    print(current_room.description)
    input("Press any button to continue... ")
    clear()


def main_game_loop():
    global current_room
    character_name()
    rules(main_character)
    story(current_room)
    while True:
        if second_room.riddles ==True and current_room == second_room:
           second_room_riddle_trial()
           second_room.riddles = False
        
        if forth_room.riddles ==True and current_room == forth_room:
           forth_room_riddle_trial()
           forth_room.riddles = False
        
        if current_room == sixth_room and len(main_character.mis_items) == 2:
            print("What do you want to do ? \n \n 1-> Search Room \n 2-> Pick Object \n 3-> Show Inventory \n 4-> Proceed to another Room \n 5-> Show current room \n 6-> Show current room's story again \n 7-> Open Safe")
            what_do_you_want = int(input())
            if what_do_you_want <=7 and what_do_you_want>0:
                current_room = what_do_you_want_from_me(what_do_you_want,current_room)
        
        else:

            try:
                
                print("What do you want to do ? \n 1-> Search Room \n 2-> Pick Object \n 3-> Show Inventory \n 4-> Proceed to another Room \n 5-> Show current room \n 6-> Show current room's story again")
                if current_room == fifth_room and enemy.alive == True :
                    print(" 7-> Fight with monster")
                what_do_you_want = int(input())


                if current_room== fifth_room and what_do_you_want <=7 and what_do_you_want>0 and enemy.alive == True:
                    current_room = what_do_you_want_from_me(what_do_you_want,current_room)
                elif current_room== fifth_room and what_do_you_want <=6 and what_do_you_want>0:
                    current_room = what_do_you_want_from_me(what_do_you_want,current_room)
                
                elif current_room != fifth_room and what_do_you_want <=6 and what_do_you_want >0:
                    current_room = what_do_you_want_from_me(what_do_you_want,current_room)
                        
                else:
                    input("Invalid input. Press to continue.")
                    clear()
            except ValueError:
                input("Invalid input. Press to continue.")
                clear()
                
        
        
        
        
main_game_loop()

            

