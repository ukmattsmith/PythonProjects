import sys
import time

repeated_once = False
inventory = []
health = 10
magic = 0
strength = 0

print("Welcome to the world of Gwyn!")

name = input("What is your hero's name? ")
print("Hello,", name)

age = int(input("What is your age? "))
if age >= 14:
    while True:
        choice = input("It is your goal to become safe, Would you like to play? ").lower()
        if choice == "yes":
                print("The lights around you blind your eyes shut, when you open them you see a vast medieval landscape.")
                time.sleep(1.5)
                print("Your inventory: Empty")
                print("You have", health, "health.")
                print("Magic Level: 0")
                print("Strength Level: 0")
                time.sleep(1.5)
                break
        elif choice == "no":
            print("That sure is a shame.")
            time.sleep(1.5)
            print("fuck u")
            sys.exit()
        else:
            if not repeated_once:
                print ("Invalid choice. Please enter 'yes' or 'no'.")
                repeated_once = True
                continue
            else:
                print ("Invalid choice again. Please enter 'yes' or 'no'.")
                continue

    choice1 = input("Do you walk towards the kingdom you can see in the distance? Or, will you turn back into the forest behind you? (kingdom/forest) ").lower()
    if choice1 == "forest":
        print("You turn away from the magnificent view and walk through the thick brush.")
        time.sleep(1.5)

    elif choice1 == "kingdom":
        print("Because the kingdom you see is so amazing, you are distracted from the high cliff you're on top of. When taking your next step you fall to your demise.")
        time.sleep(1.5)
        health -= 10
        print("Your health is now", health)
        time.sleep(1.5)
        print("You have lost.")
        sys.exit()

    choice2 = input("You hear goblins far in the distance, do you set up camp or journey on through the night? (camp/onward) ").lower()
    if choice2 == "camp":
        print("You set up a small camp with what little supplies you have, you manage to sleep on the wet dirt.")
        time.sleep(1.5)
        print ("*",name,"lets out cute little bubbles of snot while sleeping. *")
        time.sleep(1.5)
        print("You are awoken by arrows flying towards you! One slightly grazes your shoulder taking 1 health.")
        health -= 1
        print("Your health is now", health)
        time.sleep(1.5)

        choice2a = input("It's the goblin horde, do you stand and fight or run for your life? (fight/run) ").lower()
        if choice2a == "fight":
            print("You choose to stand your ground, a group of 12 goblins emerge from the trees.")
            time.sleep(1.5)
            print("Seeing that they're small creatures, you run full sprint towards them and stomp on 4 of their skulls. Increasing your strength by 2")
            strength += 2
            time.sleep(1.5)
            print("The other goblins damage you a little while in combat, taking away 2 health.")
            health -= 2
            print("Your health is now", health)
            time.sleep(1.5)
            print("You steal an Iron Dagger dropped by a fallen goblin and manage to slice 3 more to death. Increasing your strength by a further 2.")
            strength += 2
            inventory.append("Iron Dagger")
            time.sleep(1.5)
            print("the remaining 5 goblins flee back into the depths of the forest.")
            time.sleep(1.5)
            print("An Iron Dagger has been added to your inventory.")
            print("Inventory:",inventory)
            print("Strength Level:", strength)
            time.sleep(1.5)
            
            choice2a1 = input ("Will you chase after the final few goblins or carry on your adventure? (chase/onward) ").lower()
            if choice2a1 == "chase":
                print("As you race after the goblins you manage to catch up to the fleeing foes.")
                time.sleep(1.5)
                print("You slice 2 with your iron dagger, hearing chanting from the remaining 3 goblins you see a big wave of green earth magic come crashing towards you.")
                time.sleep(2)
                print("'AHHHH',", name, "exclaims! As you are sent flying through the trees being impaled on a thick branch as you land")
                time.sleep(1.5)
                print("This kills you...")
                health -= 7
                print("Your health is now", health)
                time.sleep(1.5)
                print("You have lost.")
                sys.exit()

            elif choice2a1 == "onward":
                print("You march on through the trees and notice you have lots of cuts over your body.")
                time.sleep(1.5)
                print("After journeying through the forest you find a path.")
                time.sleep(1.5)
                print("There's screaming coming from the left and it turns into darkness from the right.")
                time.sleep(1.5)

                choice2a1a = input ("Which direction will you go down? (left/right) ").lower()
                if choice2a1a == "right":
                    print("You turn away from the screaming and walk towards the darkness.")
                    time.sleep(1.5)
                    print("Your surroundings begin to disappear into the pitch black.")
                    time.sleep(1.5)
                    print("There is a low growling of something behind you in the trees.")
                    time.sleep(1.5)
                    print("You turn and see 2 glowing red eyes staring at you.")
                    time.sleep(1.5)
                    print("*", name, "gulps *")
                    time.sleep(1.5)
                    print("A large necro-bear explodes out from the trees and tears you to pieces")
                    health -= 7
                    print("Your health is now", health)
                    time.sleep(1.5)
                    print("You have lost.")
                    sys.exit()

                elif choice2a1a == "left":
                    print("The darkness scares you so you walk towards the screaming.")
                    time.sleep(1.5)
                    print("Eventually you reach a cottage and hear the screaming coming from inside.")
                    time.sleep(1.5)
                    choice2a1b = input ("Do you enter the house? (yes/no) ").lower()
                    if choice2a1b == "yes":
                        print("You approach the front door, which you notice is open. As you put your hand on the door the screaming stops...")
                        time.sleep(2)
                        print("The door creaks as you slowly push it wider, an old woman wearing a shimmering gold necklace becomes visible sitting in a rocking chair.")
                        time.sleep(2)
                        print("'Come to die?', the withered lady asks.")
                        time.sleep(1.5)
                        print("She roars and you are blown away back into the tress")
                        time.sleep(1.5)
                        print("'AHHHH',", name, "exclaims! As you are sent flying through the trees being impaled on a thick branch as you land")
                        time.sleep(1.5)
                        print("This kills you...")
                        health -= 7
                        print("Your health is now", health)
                        time.sleep(1.5)
                        print("You have lost.")
                        sys.exit()
                    
                    elif choice2a1b == "no":
                        print("You look at the house and turn away and head back down the path.")
                        time.sleep(1.5)
                        print("The screams sound so painful.")
                        time.sleep(1.5)
                        print("*BOOM*")
                        time.sleep(1.5)
                        print("The house behind you has exploaded!")
                        time.sleep(1.5)
                        print("Debris comes flying towards you and pieces of brick and wood injury your face and legs. Taking away 2 health.")
                        health -= 2
                        print("Your health is now", health)
                        time.sleep(2)
                        print("It knocks you down to the floor and as you look beside you there is a shimmering golden necklace.")
                        time.sleep(2)
                        print("You pick up the Gold Necklace and feel a surge of power.")
                        inventory.append ("Gold Necklace")
                        time.sleep(1.5)
                        print("Your magic has increased by 3.")
                        magic += 3
                        time.sleep(1.5)
                        print("A Gold Necklace has been added to your inventory.")
                        print("Inventory:", inventory)
                        print("Magic Level:", magic)
                        time.sleep(2)
                        print("You get up and make your way down the path in a hurry.")
                        time.sleep(1.5)
                        print("As you continue down the path you hear a thundering stampede fastly approaching.")
                        time.sleep(1.5)
                        choice2a1c = input ("Do you stand strong on the path or will you hide? (hide/pose) ").lower()
                        if choice2a1c == "pose":
                            print("You stand strong in the middle of the path.")
                            time.sleep(1.5)
                            print("A hoard of goblin chieftens on horseback race towards you, picking up speed as they notice you.")
                            time.sleep(1.5)
                            print("*", name, "gulps *")
                            time.sleep(1.5)
                            print("You are trampled and flattened by the oncoming horde")
                            health -= 5
                            print("Your health is now", health)
                            time.sleep(1.5)
                            print("You have lost.")
                            sys.exit()

                        elif choice2a1c == "hide":
                            print("You dive into the bushes at the edge of the path.")
                            time.sleep(1.5)
                            print("A swarm of orc chieftens on horseback race past making the ground tremble.")
                            time.sleep(2)
                            print("They didn't notice you and you see from far away they stopped at the recently exploaded house.")
                            time.sleep(1.5)
                            print("You get up and sprint down the path until you reach a town. It has gotten dark and you see an suspicious looking Inn.")
                            time.sleep(1.5)
                            choice2a1d = input ("Do you trust the Inn and book a room or carry on your journey? (inn/onward) ").lower()
                            if choice2a1d == "onward":
                                print("You turn away from the town and walk towards the darkness.")
                                time.sleep(1.5)
                                print("Your surroundings begin to disappear into the pitch black.")
                                time.sleep(1.5)
                                print("There is a low growling of something behind you in the trees.")
                                time.sleep(1.5)
                                print("You turn and see 2 glowing red eyes staring at you.")
                                time.sleep(1.5)
                                print("*", name, "gulps *")
                                time.sleep(1.5)
                                print("A large necro-bear explodes out from the trees and tears you to pieces")
                                health -= 5
                                print("Your health is now", health)
                                time.sleep(1.5)
                                print("You have lost.")
                                sys.exit()
                            elif choice2a1d == "inn":
                                print("You open the door to the inn and see a creepy man at a rotten wooden desk.")
                                time.sleep(1.5)
                                print("'May I have a room?', You ask politely. The man continues to stare.")
                                time.sleep(1.5)
                                print("After putting some gold pieces on the table, the man grunts and hands you a key to room 101.")
                                time.sleep(2)
                                print("You make your way upstairs to your room.")
                                time.sleep(1.5)
                                print("As you approach your door you hear the sound of cheering inside...")
                                time.sleep(1.5)
                                print("You put your key into the lock and force the door open.")
                                time.sleep(2)
                                print("'SUPRIIIIIIIIIIISEE!!!'")
                                time.sleep(1.5)
                                print("Confetti flies above you, as you step into the room you see all your noble knight friends.")
                                time.sleep(1.5)
                                print("You have found your friends and you are safe!")
                                time.sleep(1.5)
                                print("Congratulations, You have WON!")
                                time.sleep(1.5)
                                print("You walked away with:")
                                print("Inventory:", inventory)
                                print("Health:", health)
                                print("Magic Level:", magic)
                                print("Strength Level:", strength)
                                sys.exit()

        elif choice2a == "run":
            print("You turn to run away from the barrage of arrows whilstling past you.")
            time.sleep(1.5)
            print("One of the arrows strikes you in the center of you skull. Killing you dead...")
            health -= 9
            print("Your health is now", health)
            time.sleep(1.5)
            print("You have lost.")
            sys.exit()
                             
    elif choice2 == "onward":
        print("You journey deeper into the forest, eventually seeing the patrol of 12 goblins.")
        time.sleep(1.5)

        choice2b = input ("Do you launch a suprise attack or wait for them to pass? (attack/wait) ").lower()
        if choice2b == "attack":
            print("You crunch on leaves and branches as you emerge from the bushes, alerting the goblins of your presence.")
            time.sleep(1.5)
            print("Since you are unarmed, you take lots of slashings from their rusty blades, taking away 4 health.")
            time.sleep(1)
            print("'OOF' screams", name)
            health -= 4
            time.sleep(1.5)
            print("You manage to kill 3. Increasing your strength by 1")
            strength =+ 1
            time.sleep(1.5)
            print("Your health is now", health)
            print("Your strength level is now", strength)
            time.sleep(1.5)

            choice2b1 = input ("Will you keep up the fight or run? (fight/run) ").lower()
            if choice2b1 == ("fight"):
                print("The remaining 9 goblins all swarm you, stabbing you repeatedly until you fall to the ground bleeding out.")
                time.sleep(1.5)
                health -= 6
                print("Your health is now", health)
                time.sleep(1.5)
                print("You have lost.")
                sys.exit()

            elif choice2b1 == ("run"):
                print("You turn to run away with a barrage of arrows whilstling past you.")
                time.sleep(1.5)
                print("Feeling a sharp pain in your back you realise you have been struck by multiple arrows. Taking away 6 health.")
                health -= 6
                print("Your health is now", health)
                time.sleep(1.5)
                print("You have lost.")
                sys.exit()

        elif choice2b == ("wait"):
            print("You hide in some bushes and watch as the goblins walk past, going deeper into the forest.")
            time.sleep(1.5)
            print("As the sounds of goblin footsteps disapear you emerge from the bushes.")
            time.sleep(1.5)
            print("You look towards where the goblins came from and see they had dropped an Iron Dagger")
            time.sleep(1.5)
            print("*", name, "picks up the Iron Dagger *")
            inventory.append("Iron Dagger")
            time.sleep(1)
            print("An Iron Dagger has been added to your inventory.")
            print("Inventory:",inventory)
            time.sleep(1.5)

            choice2b2 = input ("You continue your journey into the forest, noticing it's getting darker. Will you set up camp or carry on? (camp/onward) ").lower()
            if choice2b2 == ("camp"):
                print("Setting up a small camp and fire, you fall asleep in the light of the embers.")
                time.sleep(1.5)
                print ("*",name,"lets out cute little bubbles of snot while sleeping. *")
                time.sleep(2)
                print ("As you open your eyes you can see further through the trees and notice a small inn.")
                time.sleep(1.5)

                choice2b2a = input ("Will you head into the inn or explore the forest? (inn/forest) ").lower()
                if choice2b2a == ("inn"):
                    print("You walk towards the inn and open the door, seeing a creepy man at a rotten wooden desk.")
                    time.sleep(1.5)
                    print("'May I have a room?', You ask politely. The man continues to stare.")
                    time.sleep(1.5)
                    print("After putting some gold pieces on the table, the man grunts and hands you a key to room 101.")
                    time.sleep(2)
                    print("You make your way upstairs to your room.")
                    time.sleep(1.5)
                    print("As you approach your door you hear the sound of cheering inside...")
                    time.sleep(1.5)
                    print("You put your key into the lock and force the door open.")
                    time.sleep(2)
                    print("'SUPRIIIIIIIIIIISEE!!!'")
                    time.sleep(1.5)
                    print("Confetti flies above you, as you step into the room you see all your noble knight friends.")
                    time.sleep(1.5)
                    print("You have found your friends and you are safe!")
                    time.sleep(1.5)
                    print("Congratulations, You have WON!")
                    time.sleep(1.5)
                    print("You walked away with:")
                    print("Inventory:", inventory)
                    print("Health:", health)
                    print("Magic Level:", magic)
                    print("Strength Level:", strength)
                    sys.exit()

                elif choice2b2a == ("forest"):
                    print("You stay to enjoy the last few embers of your dying fire")
                    time.sleep(1.5)
                    print("There is a low growling of something behind you in the trees.")
                    time.sleep(1.5)
                    print("You turn and see 2 glowing red eyes staring at you.")
                    time.sleep(1.5)
                    print("*", name, "gulps *")
                    time.sleep(1.5)
                    print("A large necro-bear explodes out from the trees and tears you to pieces")
                    health -= 10
                    print("Your health is now", health)
                    time.sleep(1.5)
                    print("You have lost.")
                    sys.exit()
                
            elif choice2b2 == ("onward"):
                print("As you journey on the path gets shrouded in darkness.")
                time.sleep(1.5)
                print("You hear the low growling of something towering over you...")
                time.sleep(1.5)
                print("*", name, "gulps *")
                time.sleep(1.5)
                print("You are bitten in half by a giant bear")
                time.sleep(1.5)
                health -= 10
                print("Your health is now", health)
                time.sleep(1.5)
                print("You have lost.")
                sys.exit()

else:
    print("You are too young. Goodbye...")
    sys.exit()