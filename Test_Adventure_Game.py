#Use to stagger question and response prompts
import time
#Use to randomize enemies
import random 
#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Possible enemies randomly chosen
possible_enemies = ["Lucious Malfoy", "Fenrir Grayback", "Lord Voldemort"]
final_enemy = random.choice(possible_enemies)

#Grabbing objects
#Elder Wand
wands = 0
#Key for Tri-Wizard Cup
keys = 0

#Used to define the possible answer choices
required = ("\nUse only A, B, or C\n") 

#The story is seperated into sections, starting with "intro"
def intro():
  #The backstory of the game  
  print("You are competing in the Tri-Wizard Tournament as a participant of the Hogwarts School of Witchcraft and Wizardry.\nYou must find your way to the Tri-Wizard Cup to win the tournament.\nGood luck finding the key to unlock the Cup to win the tournament!")
  if final_enemy == "Lucious Malfoy":
      print("\nUnbeknownst to you, the evil wizard Lucious Malfoy is waiting for you in the Forbidden Forest.\nLucious Malfoy played a critical role in Lord Voldemort's climb to power by helping to defeat members\nin The Order Of The Phoenix, including your best friends uncle, Ben Widenber.")
  if final_enemy == "Fenrir Grayback":
      print("\nUnbeknownst to you, the evil wizard/werewolf hybrid Fenrir Grayback is waiting for you in the Forbidden Forest.\nFenrir Grayback is feared across the magical world.\nHe specializes in prying on wizarding children and turning them into werewolfs to grow his future werewolf army to overthrow the Ministry of Magic.")
  if final_enemy == "Lord Voldemort":
      print("\nUnbeknownst to you, the evil and most feared wizard in the world, Lord Voldemort, is waiting for you in the Forbidden Forest.\nLord Voldemort is the most feared dark wizard in the world.\nHe has a massive following that wants to enslave non-magical people to show them that witches and wizards are superior to them.\nIn his climb to power he murdered anyone that got in his way, including your brother, Thomas.\nYou were able to get away, but\nnow he has found you and wants to kill you and wipe out the rest of your family, so that they can no longer oppose him.")
  print ("\nYou are transported to a maze in the Forbidden Forest.\nUpon impact of the ground you are knocked unconscious.\nWhen you awake you can hear the other 3 competitors fighting monsters in the distance.\nYou see the evil", final_enemy, "heading directly towards you!\nYou will:")
  time.sleep(3)
  print ("""  A. Pull out your wand and yell (Stupify)!
  B. Lie there stunned
  C. Run""")
  #First choice in the game
  choice = input(">>> ")
  if choice in answer_A:
    option_1()
  elif choice in answer_B:
    print ("\nYou probably shouldn't have made it this far in the tournament. \n\nYou died!\n\nYou died with your personal wand in your inventory.")
  elif choice in answer_C:
    option_run()
  else:
    #Using this in lieu of while statement 
    print (required)
    intro()

#In the scenario that you fight 
def option_1(): 
  print ("\n",final_enemy, " is stunned, but regains control. He begins "
  "gliding towards you again with his wand drawn. You will:")
  time.sleep(3)
  print ("""  A. Run
  B. Use your wand to cast another stunning spell
  C. Run towards a nearby hut""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to try another spell (Confringo!), thinking that would be more effective. " 
    " It wasn't. Actually, you realized that you didn't enunciate the incantacion properly. ",
    final_enemy, " casts the killing curse (Avada Kadavra). \n\nYou died!\n\nYou died with your personal wand in your inventory")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_1()

#In the scenario that you go into the hut
def option_cave():
  print ("\nYou were a little hesitant, since the hut was dark and "
  "ominous. Before you enter, you notice someone else's wand on "
  "the ground. You notice that it is an Elder Wand - the strongest wand in the world! Do you pick up the wand. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    #Adds an Elder Wand to the inventory
    wands = 1 
  else:
    wands = 0
  print ("\nWhat do you do next?")
  time.sleep(3)
  print ("A. Hide in silence, hoping", final_enemy, "doesn't find you\n"
  "B. Fight with your all-powerful, new wand!\n"
  "C. Run")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark?", final_enemy ,"is blinded by hatred right now BUT "
    "he can still see in the dark with magic.\nHe casts the spell (Luminos) to illuminate the room.\nHe found you. "
    "\n\nYou died!\n\nYou died with 1 Elder Wand in your inventory")
  elif choice in answer_B:
   #If the player has the Elder Wand
   if wands > 0:
    print ("\nThe Elder Wands power attracted", final_enemy,
    ", who thinks you are no match for him. As he walked "
    "closer and closer, your heart started beating rapidly. As", final_enemy ,
    "reached out to grab the Elder Wand, you yelled (SECTUM SEMPRA)! "
    , final_enemy , "is on the ground completely devestated, thanks to the power of your new wand.\n\nYou survived!\n\nYou survived with 1 Elder Wand in your inventory.")
   #If the user didn't grab the Elder Wand
   else: 
     print ("\nYou should have picked up the Elder Wand. Your "
     "wand isn't powerful enough to handle", final_enemy ,". \n\nYou died!\n\nYou died with your personal wand in your inventory")
  elif choice in answer_C:
    print ("As", final_enemy ,"enters the dark cave, you silently "
    "sneak out. You're several feet away, but", final_enemy , "turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

#In the scenario that you run
def option_run():
  print ("\nYou run as quickly as possible, but", final_enemy ,
  "is too quick. You will:")
  time.sleep(3)
  print ("""  A. Hide behind nearby shrubs
  B. Fight!
  C. Run towards a circular formation of Trees""")
  choice = input(">>> ")
  if choice in answer_A:
    print (final_enemy ,"spots you by looking over the shrubs.\n He casts the Avada Kadavra (Killing Curse). "
    "\n\nYou died!\n\nYou died with your personal wand in your inventory")
  elif choice in answer_B:
    print ("\nYou're no match for", final_enemy ,"."
    "\n\nYou died!\n\nYou died with your personal wand in your inventory")
  elif choice in answer_C:
    option_2()
  else:
    print (required)
    option_run()

#In the scenario that you go towards the trees   
def option_2():
  print ("\nWhile running, you notice an old "
  "wand lying in the grass. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated tree, waiting for", final_enemy ,"to "
  "turn the corner. In the distance you see the Tri-Wizard Cup! But it's too far to run and", final_enemy ,"is coming!\nYou notice a Golden Key "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    #adds a Key to the inventory
    keys = 1
  else:
    keys = 0
  print ("You hear his maniacal laugh and ready yourself for "
  "the impending fight.")
  time.sleep(3)
  if keys > 0:
    #If the user grabbed the key
    print ("\nYou remember that the Acio spell locates and attracts any item you name within sight.\nYou quickly hold your wand out and yell\nAccio Tri-Wizard Cup!"
    "The Tri-Wizard Cup quickly springs over to you.\nUpon touching the key to the cup, you're transferred back to the school grounds\nas the winner of the Tri-Wizard Tournament!\n\nCongratulations, you win!  "
    "*Crowd Cheers*. "
    "\n\nyour enemy,",final_enemy ,",is still alive, but at least you survived!\n\nYou won with 1 Key in your inventory.")
  #If the user didn't grab the key
  else: 
     print ("\nMaybe you should have picked up the key. Tragic. "
     "\n\nYou died!\n\nYou died with your personal wand in your inventory")

intro()