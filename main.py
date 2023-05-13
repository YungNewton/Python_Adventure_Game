import time
Ispotion = False
print('''          |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
jgs =- =- -=.--"
''')
print("Welcome to jumanji.")
time.sleep(1.7)
print('You mysteriously appeared in the forest of choice.')
time.sleep(1.5)
print('You have to Make 10 right choices to survive')
time.sleep(1)
start = input("Are you willing? Y or N: ")
if start.lower() in ["y",'yes']:
  print("You are a brave one.")
  time.sleep(1)
  print("That was your first correct choice")
  time.sleep(1)
  name = input("what name shall we call you Brave Warrior? : ")
  print(f"{name} is a fine choice fit for one as brave as you")
  time.sleep(1)
  print("Here is a gift of gold coins for your journey, you can take as much as you want.")
  time.sleep(1)
  gold = (input("do you accept the gold coins y or n: "))
  print("YOUR JOURNEY BEGINS!!!!!!")
  time.sleep(1.5)
  print("You are at the entrance of the forest of choice, there are two paths. the right leads to a dangerous forest but the left leads to mac Donalds.")
  time.sleep(1)
  path = input("what path are you taking left or right: ")
  if path.lower() in ["left"]:
    print("There is no mac donalds in the forest. This was a trap set by the witches, you got there and they ate your brain.")
    print("GAME OVER")
  else:
    print("Hurray, another correct choice!!!.")
    time.sleep(1)
    print("You get to the dangerous forest you find a poor beggar asking you for gold")
    time.sleep(1)
    beggar = input("would you give him some or would you rather not y or n: ")
    if beggar.lower() in ["y",'yes']:
      print("Great, the beggar is extremely happy, he rewards you with a potion to take when ever you're in trouble")
      time.sleep(1)
      print("He also advices you to cross the river when you get there.")
      Ispotion = True
    else:
      Ispotion = False
      print("the beggar steals all your gold any way and runs away")
    print("You go deeper in the forest. There are two paths. at the right path you find a deep swampy river and at the left you see a clear path")
    time.sleep(1)
    swamp = input("what path are you taking left or right: ")
    if swamp.lower() in ["left"]:
      print("You were eaten by wolves the clear path is the most dangerous")
      print("GAME OVER")
    else:
      print("You cross the river and finally reach the end of the road. Buh a huge Giant is guarding it")
      time.sleep(1)
      if Ispotion == True:
        print("You take the potion the beggar gave you and you defeat the Giant\n helping people actually pays!!")
        time.sleep(1)
        print("CONGRATULATIONS YOU WON")
      else:
        print("The Giant is just too strong for you. Make Better choices\nGAME OVER")
else:
  print("You are not fit to be called a warrior.")
  time.sleep(1)
  print("GAME OVER!")
