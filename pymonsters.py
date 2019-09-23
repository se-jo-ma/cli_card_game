from os import system, name
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class Mon:
    def __init__(self,name,atk,MaxHP,cost,radius):
      self.name = name
      self.atk = atk
      self.maxhp = MaxHP
      self.hp = MaxHP
      self.cost = cost
      self.radius = radius
      self.pos = 0
      self.isEmpty = False
    def isdead(self):
      if self.hp <= 0: return True
      else: return False

#Instantiation Monsters
def xAlpaca(): return Mon("Alpaca",5,9,7,1)
def xBlobus(): return Mon("Blobus",2,4,3,1)
def xGoblin(): return Mon("Goblin",1,7,4,1)
def xKnight(): return Mon("Knight",1,3,2,1)
def xShrimp(): return Mon("Shrimp",3,1,2,1)
def xSpider(): return Mon("Spider",3,3,3,1)
def xTree(): return Mon("A Tree",0,9,5,1)
def xWolfie(): return Mon("Wolfie",1,1,1,1)


#Monster Dictionary
mondic = {
  "Alpaca":xAlpaca,
  "A Tree":xTree,
  "Blobus":xBlobus,
  "Goblin":xGoblin,
  "Knight":xKnight,
  "Shrimp":xShrimp,
  "Spider":xSpider,
  "Wolfie":xWolfie
  }

class Player:
  def __init__(self,name):
    self.name = name
    self.elx = 0
    self.deck = []
    self.hand = []
    self.board = []
    self.endt = False
  def draw(self):
    while len(self.hand) < 3 and len(self.deck) > 0:
      a = self.deck.pop()
      aa = mondic[a]()
      aa.pos = len(self.hand)+1
      self.hand.append(aa)
  def playM(self,r):
    mon = mondic[r.name]()
    if mon.cost > self.elx:
      print("\n You don't have enough elixir. \n")
      input()
    elif  len(self.board) >= 3:
      print("\n There are no open battle slots to play your monster.\n")
      input()
    else:
      mon.pos = len(self.board) + 1
      im = self.hand.index(r)
      self.elx -= mon.cost
      self.board.append(mon)
      self.hand.pop(im)
      for x in self.hand:
        x.pos = self.hand.index(x)+1
  def attack(self,o,oboard):
    for x in self.board:
      a = self.board.index(x)
      if len(oboard) > a:
        oboard[a].hp -= x.atk
        print("{} dealt {} damage to {}.".format(x.name,x.atk,oboard[a].name))
        if oboard[a].isdead():
          print("{} killed {}.".format(x.name,oboard[a].name))
          oboard.pop(a)
          o.elx += 1
      elif 0<len(oboard)<=a:
        b = len(oboard)-1
        oboard[b].hp -= x.atk
        print("{} dealt {} damage to {}.".format(x.name,x.atk,oboard[b].name))
        if oboard[b].isdead():
          print("{} killed {}.".format(x.name,oboard[b].name))
          oboard.pop(b)
          o.elx += 1
  def printHand(self):
    s,r,t,u,v,w = "   ","   ","   ","   ","   ","   "
    print("\n------------------------------------")
    for x in self.hand:
      v += "|------| "
    print(v)
    for x in self.hand:
      s += "|"+str(x.name)+"| "
    print(s)
    for x in self.hand:
      u += "|Cost:"+str(x.cost)+"| "
    print(u)
    for x in self.hand:
      t += "|Atk: "+str(x.atk)+"| "
    print(t)
    for x in self.hand:
      r += "|HP:  "+str(x.hp)+"| "
    print(r)
    for x in self.hand:
      w += "|  #"+str(x.pos)+"  | "
    print(w)
    print(v)
    print("\n------------------------------------")
    print("Cards in Deck: {} | You: {} | Elixir: {} \n".format(len(self.deck),self.name,self.elx))
  def turn(self,o):
    self.endt = False
    self.draw()
    self.elx += 3
    while self.endt != True:
      clear()
      print("------------------------------------\nIt is {}'s turn.".format(self.name))
      printBoard(o,o.board,self.board)
      self.printHand()

      inp = input("Please enter the # of the card you would like\n to play or 0 to end your turn.")
      if inp:
        inp = int(inp)
        a = inp-1
        if inp > len(self.hand):
          print("\nERROR YOU HAVE ENTERED AN INVALID NUMBER. Try again.")
          input()
        elif inp != 0: self.playM(self.hand[a])
        elif inp == 0: self.endt = True
        else:
          print("Please enter 1, 2, 3 or 0.\n")
          input()
    clear()
    print("\n------------------------------------\n{} ends their turn. \n------------------------------------\n".format(self.name))
    self.attack(o,o.board)
    print("\n------------------------------------\nIt is now {}'s turn. \n------------------------------------\n".format(o.name))
    input()
    clear()

p1 = Player("")
p2 = Player("")

#Decks
deck1 = ["Knight","Wolfie","Goblin","Blobus","Blobus","Shrimp","Shrimp","Knight"]
deck2 = ["Goblin","Blobus","Goblin","Blobus","Alpaca","Knight","Spider","Spider"]
deck3 = ["Knight","Wolfie","Goblin","Spider","Blobus","Shrimp","A Tree","Alpaca"]
deck4 = ["Goblin","Blobus","Wolfie","Blobus","Wolfie","Shrimp","Spider","Spider"]

def deckPrint(deck):
  lo = []
  lo1 = []
  for x in deck:
    mon = mondic[x]()
    if len(lo) >= 4: lo1.append(mon)
    if len(lo) < 4: lo.append(mon)
  print("\n------------------------------------")
  s,r,t,u,v,w = " "," "," "," "," "," "
  for x in lo:
    v += "|------| "
  print(v)
  for x in lo:
    s += "|"+str(x.name)+"| "
  print(s)
  for x in lo:
    u += "|Cost:"+str(x.cost)+"| "
  print(u)
  for x in lo:
    t += "|Atk: "+str(x.atk)+"| "
  print(t)
  for x in lo:
    r += "|HP:  "+str(x.hp)+"| "
  print(r)
  print(v)
  s,r,t,u,v,w = " "," "," "," "," "," "
  for x in lo1:
    v += "|------| "
  print(v)
  for x in lo1:
    s += "|"+str(x.name)+"| "
  print(s)
  for x in lo1:
    u += "|Cost:"+str(x.cost)+"| "
  print(u)
  for x in lo1:
    t += "|Atk: "+str(x.atk)+"| "
  print(t)
  for x in lo1:
    r += "|HP:  "+str(x.hp)+"| "
  print(r)
  print(v)
def deckPick(player):
  d = False
  while d != True:
    print("\n-----------------Deck #1-----------------")
    print(deck1[:4])
    print(deck1[4:])
    print("\n-----------------Deck #2-----------------")
    print(deck2[:4])
    print(deck2[4:])
    print("\n-----------------Deck #3-----------------")
    print(deck3[:4])
    print(deck3[4:])
    print("\n-----------------Deck #4-----------------")
    print(deck4[:4])
    print(deck4[4:])

    deck_choice = input("\nPlease enter 1,2,3 or 4 to select a deck")
    deck_foo = "deck"+deck_choice
    deck_foo1 = eval(deck_foo)

    print("Below is the deck you have chosen: \n")
    deckPrint(deck_foo1)
    ans = input("Would you like to choose this deck? Y/N \n")
    if ans == "Y" or ans == "y":
      player.deck = deck_foo1
      d = True
    elif ans == "N" or ans == "n":clear()
    else:print("Please stop breaking me :'(")

#Misc
def winCheck(player1,player2):
  if len(player1.deck) == 0 and len(player1.hand) == 0 and len(player1.board) == 0:
    print("\n{} wins!\n".format(player2.name))
    return True
  elif len(player2.deck) == 0 and len(player2.hand) == 0 and len(player2.board) == 0:
    print("\n{} wins!\n".format(player1.name))
    return True
  else: return False
def printBoard(o,board,pboard):
  print("------------------------------------")
  print("       Opp: {}    Elixir: {}\n Cards in Hand: {} Cards in Deck: {}".format(o.name,o.elx,len(o.hand),len(o.deck)))
  print("------------------------------------\n")
  s,r,t,u,v,w = "   ","   ","   ","   ","   ","   "
  for x in board:
    s += "|"+str(x.name)+"| "
  print(s)
  for x in board:
    r += "|Atk: "+str(x.atk)+"| "
  print(r)
  for x in board:
    t += "|HP:  "+str(x.hp)+"| "
  print(t)
  print("------------------------------------")
  for x in pboard:
    u += "|"+str(x.name)+"| "
  print(u)
  for x in pboard:
    v += "|Atk: "+str(x.atk)+"| "
  print(v)
  for x in pboard:
    w += "|HP:  "+str(x.hp)+"| "
  print(w)
def battle(p1,p2):
  win = False
  while win != True:
    p1.turn(p2)
    win = winCheck(p1,p2)
    p2.turn(p1)
    win = winCheck(p1,p2)

#Start printing things
p1.name = input("Player 1 please enter your name:")
deckPick(p1)
print("\nNow entering the Arena: {} The Brave! \n------------------------------------\n".format(p1.name))
input()
clear()
p2.name = input("Player 2 please enter your name:")
deckPick(p2)
print("\nNow entering the Arena: {} The Careless! \n------------------------------------".format(p2.name))

print("------------------------------------\nFor now both of your decks have been\nassigned to you. In the future maybe\nyou will get to build your own!\n------------------------------------\n")
input()
clear()

battle(p1,p2)
