#==========TITLE SEQUENCE==========#
import time
import random

tss = 1.5
introseq = False
tutplay = True
loadsave = False

#introseq = False
#tutplay = False

print("CRITICAL STATUM: CONTAGION V1.6")
print("Select: 'play', 'load/new', 'options', 'credits'")
titleinp = input("Enter command: ")
while titleinp != 'play':
  #if titleinp == "clear data":
  #  inv_save = open('PatchSave/invent.txt', 'w')
  #  loc_save = open('PatchSave/loc.txt', 'w')
  #  stat_save = open('PatchSave/stats.txt', 'w')
  #  vloc_save = open('PatchSave/vloc.txt', 'w')
  #  end_rem = open('PatchSave/EndingCount.txt', 'w')
  #  inv_save.truncate(0)
  #  loc_save.truncate(0)
  #  stat_save.truncate(0)
  #  vloc_save.truncate(0)
  #  end_rem.truncate(0)
  #  loc_save.close()
  #  inv_save.close()
  #  stat_save.close()
  #  vloc_save.close()
  #  end_rem.close()
  #  print("Cleared data")
  if titleinp == "load/new":
    gameinp = ' '
    print("Enter empty line to exit")
    print("WARNING: Loading the game with no saves will stop the game from operation")
    while gameinp:
      print("Current value:", loadsave)
      print("Do you want to load previous game save?")
      gameinp = input("Enter yes or no:")
      if gameinp == 'yes':
        loadsave = True
      elif gameinp == 'no':
        loadsave = False
  if titleinp == "credits":
    print("Critical statum: Contagium")
    time.sleep(2)
    print("Made by Oliver Maxwell Walters")
    time.sleep(2)
    print("For a Year 10 IST project")
    time.sleep(2)
  if titleinp == 'options':
    print("Select: 'text scroll speed', 'toggle intro', 'toggle tutorial', 'exit'")
    opsinp = input("Enter command: ")
    while opsinp != 'exit':
      if opsinp == 'text scroll speed':
        print("Current value:", tss)
        tsspre = float(input("Enter amount of seconds delay: "))
        if tsspre >= 0:
          tss = tsspre
        else:
          print("Cannot be below 0")
      if opsinp == "toggle intro":
        print("Current value:", introseq)
        print("Do you want the introduction?")
        introseq = input("Enter yes or no: ")
        if introseq == 'yes':
          introseq = True
        else:
          introseq = False
      if opsinp == "toggle tutorial":
        print("Current value:", tutplay)
        print("Do you want the tutorial?")
        tutplay = input("Enter yes or no: ")
        if tutplay == 'yes':
          tutplay = True
        else:
          tutplay = False
      print("Select: 'text scroll speed', 'toggle intro', 'toggle tutorial', 'exit'")
      opsinp = input("Enter command: ")
  print("Select: 'play', 'load/new', 'options', 'credits'")
  titleinp = input("Enter command: ")

#==========LOAD SAVES==========#

if loadsave == True:
  introseq = False
  tutplay = False

invent = set()
loc = ''
gac_loc = ''

def loadasave(ls):
  if ls:
    invent_load = open('Save/invent.txt').read().split('\n')
    loc_load = open('Save/loc.txt').read().split('\n')
    stats_load = open('Save/stats.txt').read().split('\n')
    vloc_load = open('Save/vloc.txt').read().split('\n')
    invent_load.pop()
    loc_load.pop()
    stats_load.pop()
    vloc_load.pop()
    for item in invent_load:
      invent.add(item)
    for location in vloc_load:
      v_loc.add(location)
    if stats_load != ['']:
      run = 0
      for line in stats_load:
        if line != '':
          statlist = line.split(':')
          run += 1
          rundir = 0
          if run == 1:
            for key in char:
              char[key] = statlist[rundir]
              rundir += 1
          if run == 2:
            for key in rsc:
              rsc[key] = int(statlist[rundir])
              rundir += 1
          if run == 3:
            for key in lvl:
              lvl[key] = int(statlist[rundir])
              rundir += 1
    if loc_load != ['']:
      loadgacloc, loadloc, loadprevloc = loc_load
      return loadgacloc, loadloc, loadprevloc

def slvar(save):
  if save == True:
    var_save = open('Save/var.txt', 'w')
    var_save.truncate(0)
    for key in varlist:
      print(varlist[key], file=var_save)
    var_save.close()
  elif save == False:
    var_load = open('Save/var.txt').read().split('\n')
    n = 0
    for var in varlist:
      varlist[var] = var_load[n]
      n += 1

def savegame(sgl, sl, spl):
  inv_save = open('Save/invent.txt', 'w')
  loc_save = open('Save/loc.txt', 'w')
  stat_save = open('Save/stats.txt', 'w')
  vloc_save = open('Save/vloc.txt', 'w')
  inv_save.truncate(0)
  loc_save.truncate(0)
  stat_save.truncate(0)
  vloc_save.truncate(0)
  for item in invent:
    print(item, file=inv_save)
  for key in char:
    stat_save.write(char[key] + ':')
  print('\n', file=stat_save)
  for key in rsc:
    stat_save.write(str(rsc[key]) + ':')
  print('\n', file=stat_save)
  for key in lvl:
    stat_save.write(str(lvl[key]) + ':')
  print('\n', file=stat_save)
  for location in v_loc:
    print(location, file=vloc_save)
  print(sgl, file=loc_save)
  print(sl, file=loc_save)
  print(spl, file=loc_save)
  loc_save.close()
  inv_save.close()
  stat_save.close()
  vloc_save.close()
  return 'Game saved'

#==========INTRODUCTION==========#

print('')
print("*")
print('')
print("*")
print('')
print("*")
print('')

if introseq:
  f = open('lines/Introduction-1.txt').read()
  intro1 = f.split(">")
  time.sleep(4)
  print(intro1[1])
  time.sleep(4)
  for line in intro1[2:]:
    print(line)
    time.sleep(3)

#==========CHARACHTERS==========#

char = {'leader':'', 'pilot':'', 'mechanic':'',
  'marksman':'', 'programmer':''
}
lvl = {
  'charisma':1,'piloting':1,'tech. knowledge':1,'attack':1,'intellect':1
}

lvlacss = {
    'leader': 'charisma',
    'pilot': 'piloting',
    'mechanic': 'tech. knowledge',
    'marksman': 'attack',
    'programmer': 'intellect'
}

if loadsave == False:
  char['leader'] =  input("Name of Leader: ")
  char['pilot'] = input("Name of Pilot: ")
  char['mechanic'] = input("Name of Mechanic: ")
  char['marksman'] = input("Name of Marksman: ")
  char['programmer'] = input("Name of Programmer: ")

#==========INVENTORY==========#

if introseq:
  f2 = open('lines/Introduction-2.txt').read()
  intro2 = f2.split(">")
  for line in intro2:
    print(line)
    time.sleep(3)

invent = set()
invent.add('keycard 1')

rsc = {
  'credits':200, 'skillpts':5, 'gas':0, 'cells':0,
  'material':0, "ammo":0, 'tech':0
}
rscass = {
  'leader': 'gas',
  'pilot': 'cells',
  'mechanic': 'material',
  'marksman': "ammo",
  'programmer': 'tech'
}

if loadsave == False:
  print("Hint: enter either gas, cells, materials, ammo or tech")
  startmaterial = input("Reqest supply: ")
  while startmaterial not in rsc:
    print("Hint: enter either gas, cells, material, ammo or tech")
    startmaterial = input("Reqest supply: ")
  rsc[startmaterial] = 20

#==========VARIABLE SETTING==========#

#Set of previous rsc caches
v_loc = set()

#Areas in tutorial
tut_loc = set({'airlock', 'hall', 'generator', 'office', 'bridge', 'quarters', 'store'})

#General location to stop PosStory repeats
loc_list = ''

invent = set()
invent.add('keycard 1')
invent.add('fist')

even = set()

for x in range(50):
  even.add(x*2)

#Converse for dialouge repeat, launch for tutorial ending
converse = False
launch = ''

#Location variable
loc = 't-bridge'

#.txt reader (for while loops)
i = 1

#var0 to start messy stuff after kc1 used
var0 = False

#var5 for checking the amount of bar returns (wolosyd)
var5 = 0

#==========FUNCTIONS==========#
#Help for inputs function
def helpCom(da2):
  print("Commands to enter:")
  if 'gps' in invent:
    print("gps - Gives a geographic position")
  if da2 == 'False':
    print("save - Saves the game")
  print("cheat - Only useful if completed game")
  print("inventory - shows the charachter's inventory")
  print("end - ends the game (Make sure you save before)")
  print("help - gives a list of commands")

#Text scroll function
def txtsc(a, b, c):
  while a <= b:
    print(c[a])
    time.sleep(tss)
    a = a + 1
  return

#Text scroll function for endings
def txtsce(a, b, c, d):
  while a <= b:
    print(c[a])
    time.sleep(d)
    a = a + 1
  return

#Location checker
def loc_check(s, a, b):
  x = 1
  p = 0
  while x <= 5:
    p = x
    if a in area[s][p] and b in area[s][p]:
      return True
    x = x + 1
    p = 0
  return False

#Battleship game for mechanic
dic = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
}
def battleship(s):
  print("Welcome to the battleship game,")
  print("Enter a position from A1 - E5")
  print("If you hit all grid spots, you win")
  x = 0
  a = ''
  while x < s:
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    a += dic[str(b)] + str(c) + '.'
    x += 1
  l = set(a.upper().split('.'))
  i = 15
  hits = set()
  hits.add('')
  n = input("Guess: ")
  while n:
    if n in hits:
      print("You've chosen that square already")
    else:
      print("Hit", n)
      if n in l:
        print("You hit a ship")
        print("+1 guess")
        i += 1
      else:
        print("It's blank")
    hits.add(n)
    if hits.issuperset(l):
      print("You won")
      return True
    if i > 0:
      i = i - 1
      print("Guesses left:", i)
    else:
      print("You are out of guesses")
      break
    n = input("Guess: ")
  return False

#Mapfeild game for programmer
def mapfeild(a, b, c, s):
  print("Welcome to the mapfeild game,")
  print("use wasd to guide the x mark and")
  print("if you do it in the right order, you win")
  size = c
  table = []
  moveset = []
  ms = list(s)
  for i in range(1,size+1):
    row=[]
    for j in range(1,size+1):
      row.append(".")
    table.append(row)
  table[0][0] = "x"
  table[a][b] = "o"

  t = 0
  r = 0

  for row in table:
    output = ""
    for dot in row:
      output += dot
    print(output)
  move = input("Direction: ")
  while move:
    if move == "d" and r < size - 1:
      r = r + 1
    if move == "a" and r > 0:
      r = r - 1
    if move == "w" and t > 0:
      t = t - 1
    if move == "s" and t < size - 1:
      t = t + 1
    table[t][r] = "x"
    moveset.append(move)
    if t == a and r == b:
      if moveset == ms:
        return True
      else:
        return False
    for row in table:
      output = ""
      for dot in row:
        output += dot
      print(output)
    move = input("Direction: ")
  return False

#Pick a number game
def pickanum(a, b):
  print("Welcome to the pick a number game")
  print("Guess a number from 1 to", b)
  guess = a
  ans = str(random.randint(1, b))
  num = input("Pick a number: ")
  while guess > 0:
    if num == ans:
      print("You win")
      return True
    else:
      guess = guess - 1
      print("Wrong,", guess, "guesses left")
    num = input("Pick a number: ")
  return False

#Game for fighting scenes
def combatgame(e, l):
  print("Enter stats to get info")
  print("Enter a number and a tool (default = fist) to fight an enemy")
  print("Enter heal to use credits to heal hp")
  print("You must either lose or win if you want to exit")
  edic = {}
  hp = int(100 + lvl['attack']*(5 + pow(e, 1+l/20)) + pow(e, 1+l/10))
  x = e
  turn = True
  wepdic = {'fist':10, 'pistol':30, 'tazer':15, 'machine gun':45, 'rpg':50, 'shotgun':40, 'sniper':100, 'stun gun':20}
  for term in wepdic:
    wepdic[term] += lvl['attack']
  for nm in range(1, e+1):
    edic[str(nm)] = [l*5, l + random.randint(1, int(float(l)/3)), l]
  while x > 0:
    if turn == True:
      print("-----YOUR TURN-----")
      fight = input("Who do you want (" + str(e) + " enemies) to fight? ")
      if fight in edic:
        weapon = input("What do you want to fight with? ")
        if weapon in wepdic and weapon in invent:
          edic[fight][0] += -1*wepdic[weapon]
          r = random.randint(1, wepdic[weapon])
          edic[fight][0] += -1*r
          print("Dealt", wepdic[weapon] + r, "damage to enemy No.", int(fight))
          print("Critical Hit of", r)
          turn = False
      if fight == 'stats':
        print("stats:")
        print("HP:", str(hp) + ', Credits:', str(rsc['credits']) + ', Attack:', lvl['attack'])
        print("Enemy stats (HP, Attack, Heal):")
        for term in edic:
          n = ''
          for t in edic[term]:
            n += str(t) + ','
          print("Enemy", term + ":", n)
      if fight == 'heal':
        h = random.randint(1, l)
        print("healed", 30 + lvl['attack'] + h,"hp for 10 credits")
        hp += 30 + lvl['attack'] + h
        rsc['credits'] += -10
        turn = False
    if turn == False:
      ran = random.randint(1, 100) - int(float(l)/2)
      en = str(random.randint(1, e))
      if edic[en][0] > 0:
        print("-----ENEMY TURN-----")
        if ran <= 70:
          print("Enemy No.", en, "deals", edic[en][1], "damage")
          hp = hp - edic[en][1]
          turn = True
        else:
          print("Enemy No.", en, "heals", edic[en][2], "HP")
          edic[en][0] = edic[en][0] + edic[en][2]
          turn = True
    x = e
    for term in edic:
      if edic[term][0] < 0:
        x = x - 1
    if hp <= 0: 
      print("You lost")
      return False
  print("You won")
  return True

#Game for corrupted fighting scenes
def corruptfight(e, l):
  print("Enter stats to get info")
  print("Enter a number and a tool (default = fist) to fight an enemy")
  print("Enter heal to use credits to heal hp")
  print("You must either lose or win if you want to exit")
  edic = {}
  hp = int(100 + lvl['attack']*(5 + pow(e, 1+l/20)) + pow(e, 1+l/10))
  x = e
  turn = True
  wepdic = {'fist':10, 'pistol':30, 'tazer':15, 'machine gun':45, 'rpg':50, 'shotgun':40, 'sniper':100, 'stun gun':20}
  for term in wepdic:
    wepdic[term] += lvl['attack']
  for nm in range(1, e+1):
    edic[str(nm)] = [l*5, l + random.randint(1, int(float(l)/3)), l]
  while x > 0:
    if turn == True:
      print("-----yØiu®S-----")
      fight = input("Who do you want (" + str(e) + " enemies) to fight? ")
      if fight in edic:
        weapon = input("What do you want to fight with? ")
        if weapon in wepdic and weapon in invent:
          edic[fight][0] += -1*wepdic[weapon]
          r = random.randint(1, wepdic[weapon])
          edic[fight][0] += -1*r
          print("Dealt", wepdic[weapon] + r, "damage to enemy No.", int(fight))
          print("Critical Hit of", r)
          turn = False
      if fight == 'stats':
        print("stats:")
        print("HP:", str(hp) + ', Credits:', str(rsc['credits']) + ', Attack:', lvl['attack'])
        print("Enemy stats (HP, Attack, Heal):")
        for term in edic:
          n = ''
          for t in edic[term]:
            n += str(t) + ','
          print("Enemy", term + ":", n)
      if fight == 'heal':
        print("healed", 30 + lvl['attack'] + random.randint(1, l),"hp for 10 credits")
        hp += 30 + lvl['attack'] + random.randint(1, l)
        rsc['credits'] += -10
        turn = False
    if turn == False:
      ran = random.randint(1, 100)
      en = str(random.randint(1, e))
      if edic[en][0] > 0:
        print("-----*$#(*@#H)RN(DC@(8xo-----")
        if ran <= 70:
          print("Enemy No.", en, "deals", edic[en][1], "damage")
          hp = hp - edic[en][1]
          turn = True
        else:
          print("Enemy No.", en, "heals", edic[en][2], "HP")
          edic[en][0] = edic[en][0] + edic[en][2]
          turn = True
    x = e
    for term in edic:
      if edic[term][0] < 0:
        x = x - 1
    if hp <= 0: 
      print("You lost")
      return False
  print("You won")
  return True

#bossfight for bosses
def bossfight(l):
  if l == 'lab':
    bosshits = 5
    while bosshits > 0:
      bosshits += -1
      if corruptfight(1, 40):
        print("ThE 4#$AC82=2#- uSes EœneMies")
      else:
        return False
      if corruptfight(10 - bosshits*2, 20):
        print("&#$)@^YH3ÔÇÎ¨ﬂ„‡b2p02N#(UNP{@-‡˝°Ø)‡°‡·—¨˜∆ª∏NÆ")
      else:
        return False
    return True
  if l == 'spiron city':
    bosshits = 3
    while bosshits > 0:
      bosshits += -1
      if combatgame(1, 50):
        print("Dr. Xenith Calls in his guards")
      else:
        return False
      if combatgame(10 - bosshits*2, 30):
        print("Dr. Xenth steps back in")
      else:
        return False
    return True

#anagram minigame
words = {
         3:['cat', 'dog', 'lol'], 4:['love', 'meet', 'case'],
         5:['cheat', 'steve', 'older'], 6:['aboard', 'eatery', 'sydney'],
         7:['jukebox', 'abdomen', 'aardvark'], 8:['aliterate', 'stallion', 'toleration']
         }
def anagram(l, w):
  a = random.randint(l, w)
  b = random.randint(0, 2)
  word = words[a][b]
  c = random.randint(0, len(word)-1)
  jumb = ''
  while len(jumb) != len(word):
    if jumb.count(word[c]) != word.count(word[c]):
      jumb += word[c]
    c = random.randint(0, len(word)-1)
    if jumb == word:
      jumb = ''
  print("Welcome to Anagram, you must guess the word")
  g = 5
  while g > 0:
    g = g - 1
    print("Guesses left:", g)
    print("Word:", jumb + ',', "Length:", len(word))
    guess = input("Guess word: ")
    if guess == word:
      print("You won")
      return True
    if g == 3:
      print("Hint: The first letter of the word is", word[0])
    if g == 2:
      print("Hint: The last letter of the word is", word[len(word)-1])
    if g == 1 and len(word) > 3:
      print("Hint: The midddle letter of the word is", word[int(float(len(word)-1)/2)])
  print("You loose, the word was", word)
  return False

#Gps funtion
def gps(s, a, b):
  print("Key: O = locaton, x = travelable location, . = out of bounds")
  size = 9
  table = []
  moveset = []
  movedic = {
             'wolosyd':[[2, 3, 4], [3, 4], [3, 4], [3], [1, 2, 3], [1, 2, 3], [1, 2, 3]],
             'tariskor':[[2], [2], [2, 3], [2, 3], [], [], [3], [2, 3], [3]],
             'musk':[[3], [2, 3], [2, 3, 4], [4]],
             'ventrin-426b':[[], [], [0, 1, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6, 7], [3, 4, 5]],
             'lab':[[], [], [3, 4], [2, 3, 4, 5, 6], [3, 5]],
             'spiron city':[[2], [2], [1, 2, 3], [0, 1, 3, 4, 5], [1, 2, 3], [2]]
             }
  for i in range(1,size+1):
    row=[]
    for j in range(1,size+1):
     row.append(".")
    table.append(row)
  x = 0
  while x <= len(movedic[s])-1:
    for t in movedic[s][x]:
      table[x][t] = 'x'
    x += 1
  if s in gps_count:
    if a == 3 and b == 3:
      table[a][b+1] = 'O'
      table[a][b+2] = 'O'
  table[a][b] = 'O'
  for row in table:
    output = ""
    for dot in row:
      output += dot
    print(output)
  m = 'Map of '
  m += s
  return m

gps_count = {
    'ventrin-426b':['hall', 3],
    'lab':['hall', 3]
  }

#Dictonary for gps function
gps_loc = {
  'wolosyd':{'sutherland park':[3, 3], 'otford':[4, 3], 'heathcote':[4, 2], 'campbeltown':[4, 1], 'ruins':[2, 3], 'central':[5, 3], 'kembla-kiama':[6, 3], 'nowra':[6, 2], 'port hacking':[2, 4], 'old bay':[1, 4], 'parramatta':[1, 3], 'avalon':[0, 4], 'penrith':[0, 3], 'bowral':[6, 1], 'picton':[5, 2], 'mountains':[5, 1], 'richmond':[0, 3]},
  'tariskor':{'mt. rextion':[0, 2], 'loading bay':[1, 2],'command center':[2, 2], 'storage':[3, 2], 'metal factory':[2, 3], 'rextion port':[3, 3], 'vulcan plains':[6, 3], 'vestic stockyard':[7, 3], 'mt. vulcan':[7, 2], 'mt. vestic':[8, 3]},
  'musk':{'town hall':[0, 3], 'asimov':[1, 3], 'south musk':[1, 2], 'wells airport':[2, 2], 'city limit':[2, 3], 'cerberus plateau':[2, 4], 'landing site':[3, 4]},
  'ventrin-426b':{'landing pad':[3, 0], 'cliffside':[2, 0], 'cavern':[2, 1], 'unknown location':[3, 1], 'lab entrance':[3, 2], 'hall':[3, 3], 'lab 1':[2, 3], 'lab 2':[4, 3], 'lab 3':[2, 4], 'lab 4':[4, 4], 'study':[2, 5], 'lab #!@%':[4, 5], 'bridge':[3, 6], 'vault door':[3, 7], 'test room':[2, 7]},
  'lab':{'vault door':[3, 2], 'hall':[3, 3], 'quarters':[2, 3], 'common room':[2, 4], 'storeroom':[4, 3], 'lab 6':[4, 5], 'test chamber':[3, 6]},
  'spiron city':{'mt. serins':[0,2], 'outpost':[1,2], 'ventrix':[2,1], 'city entrance':[2,2], 'sector 3':[2,3], 'sector 4':[3,1], 'industrial':[3,3], 'sector 6':[4,1], 'central spiron':[4,2], 'landing bay':[4,3], 'zoo':[3,0], 'larina':[5,2], 'junkyard':[3, 4], 'warehouse':[3, 5]}
}

#==========CHEATS==========#

EndCountvar = set(open('Save/EndingCount.txt').read().split('\n'))

#cheat function
def cheatGame(c):
  if c == 'infLvl' and 'good' in EndCountvar:
    print("Used Infininte levels cheat")
    for key in lvl:
      lvl[key] += 100000000
  elif c == 'infRsc' and 'bad' in EndCountvar:
    print("Used Infininte resources cheat")
    for key in rsc:
      rsc[key] += 100000000
  elif c == 'nameChange' and 'infection' in EndCountvar:
    print("Used Name change cheat")
    char['leader'] =  input("Name of Leader: ")
    char['pilot'] = input("Name of Pilot: ")
    char['mechanic'] = input("Name of Mechanic: ")
    char['marksman'] = input("Name of Marksman: ")
    char['programmer'] = input("Name of Programmer: ")
  elif c == 'playMini' and 'sac' in EndCountvar:
    print("Used play minigame cheat")
    r = random.randint(1, 3)
    if r == 1:
      anagram(random.randint(1, 4), random.randint(4, 8))
    if r == 2:
      battleship(random.randint(8, 20))
    if r == 3:
      ran = random.randint(1, 30)
      pickanum(ran-random.randint(1, 10), ran)
  else:
    print("Cheat not avaliable")

#==========TUTORIAL==========#

print("***")

A0 = open('lines/Tutorial.txt').read().split(">")
if introseq:
  while i <= 4:
    if i in even:
      print(char['pilot'] + A0[i])
      time.sleep(2.5)
    else:
      print(char['leader'] + A0[i])
      time.sleep(2.5)
    i = i + 1
if tutplay:
  i = 5
  while i <= 7:
    print(A0[i])
    time.sleep(tss)
    i = i + 1
  #txtsc(5, 7, A0)

#-----KEYCARD USE-----#
inp = ' '
if tutplay:
  inp = input("What should you do? ")
  while inp != "keycard 1":
    if inp == "end":
     break
    else:
     inp = input("What should you do? ")

var0 == False

if tutplay:
  var0 = True

#-----MAIN TUTORIAL-----#
if var0 == True:
  var0 = False
  while inp != "end":
   print(A0[8])
   print(A0[9])
   print("Note: Enter 'inventory' to see your supplies")
   loc = "hall"
   var1 = True
   var2 = False
   while inp != "end":
     #-----start loop-----#
     if var1 == False and inp != 'launched':
       inp = input("What should you do? ")
       if inp in tut_loc:
        loc = inp
        print("Current location:", loc)
     var1 = False
     
     #-----airlock-----#
     if loc == "airlock":
       if inp == "crate" and "crate" not in v_loc:
        print("+40 Gas, +25 credits")
        rsc['gas'] = rsc['gas'] + 40
        rsc['credits'] = rsc['credits'] + 25
        v_loc.add(inp)
       elif inp == "crate" and "crate" in v_loc:
         print("the crate is empty")
       if loc_list != "airlock":
         i = 12
         loc_list = "airlock"
         while i <= 13:
          print(A0[i])
          time.sleep(1)
          i = i + 1
       elif inp == "terminal":
        print("The airlock opens as you get sucked into space, You died")
        inp = 'end'
     #-----generator-----#
     elif loc == "generator":
       iset = set({"fuse 1", "fuse 2"})
       if inp == "fuse box" and iset.issubset(invent) == True:
         print("You insert the fuse into the generator.")
         time.sleep(1)
         print("It makes a clanking sound and then turns on")
         invent.discard(iset)
         var2 = True
       elif inp == "fuse box" and iset.issubset(invent) == False:
         print("You don't have 2 fuses in your invenotry")
       elif inp == "power cell" and inp not in v_loc:
         print("+40 power cells")
         v_loc.add(inp)
         rsc['cells'] = rsc['cells'] + 40
       elif inp == "power cell" and inp in v_loc:
         print("There are no power cells")
       if loc_list != "generator":
         print("Hint: Read the description of the area to find possible command lines")
         print("Enter 'hall' to leave or another room to go to that location")
         i = 14
         loc_list = "generator"
         while i <= 15:
          print(A0[i])
          time.sleep(1)
          i = i + 1
     #-----quarters-----#
     elif loc == "quarters":
       if inp == "locker 1":
         if 'fuse 1' not in invent:
          print("This is your locker, you find a fuse (1/2) inside")
          invent.add('fuse 1')
         else:
           print("There is nothing but clothes here")
       if inp == "locker 2":
         if 'locker' not in v_loc:
           print("This is a spare locker, but it has some ammo in it")
           print("+40 Ammo")
           rsc['ammo'] = rsc['ammo'] + 40
           v_loc.add('locker')
         elif 'locker' in v_loc:
           print("There is nothing but dust here")
       if loc_list != "quarters":
         i = 16
         loc_list = "quarters"
         while i <= 19:
          print(A0[i])
          time.sleep(1)
          i = i + 1
     #-----store-----#
     elif loc == "store":
       if loc_list != "store":
         i = 20
         loc_list = "store"
         while i <= 20:
           print(A0[i])
           time.sleep(1)
           i = i + 1
       if 'fuse 2' not in invent:
         print(A0[21])
         print("fuse (2/2) in put in your inventory")
         invent.add('fuse 2')

       if inp == "boxes" and "boxes" not in v_loc:
         print("+10 Credits, +40 Material")
         rsc['credits'] = rsc['credits'] + 10
         rsc['material'] = rsc['material'] + 40
         v_loc.add('boxes')
       elif inp == "boxes" and "boxes" in v_loc:
         print("The boxes are empty")

    #-----office-----#
     elif loc == "office":
       if loc_list != "office":
         i = 22
         loc_list = "office"
         while i <= 23:
           print(A0[i])
           time.sleep(1)
           i = i + 1
         if converse == False:
           print(char['mechanic'] + A0[24])
           time.sleep(1)
           print(char['programmer'] + A0[25])
           time.sleep(1)
           print(char['leader'] + A0[26])
           time.sleep(1)
           print(char['programmer'] + A0[27])
           time.sleep(1)
           print(char['leader'] + A0[28] + char['programmer'])
           time.sleep(1)
           converse == True
         #=====OFFICE UPGRADE=====#
       if inp == "desk":
         upg = 'empty'
         print("Who would you like to level up?")
         print("Enter the charachter's role in crew")
         print("Enter a blank to leave - you cannot use end here")
         tot_invent = ''
         print("Rescources:")
         for keyterm in rsc:
           tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
         print(tot_invent)
         while upg:
          upg = input("Enter charachter: ")
          for keyterm in char:
            if upg == char[keyterm] or upg == keyterm:
              if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                 print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                 rsc['skillpts'] = rsc['skillpts'] - 1
                 rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                 lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
              else:
               print("Rescoures not present in inventory")
     #-----bridge-----#
     elif loc == "bridge":
       if loc_list != "bridge":
         i = 29
         loc_list = "bridge"
         while i <= 30:
           print(A0[i])
           time.sleep(1)
           i = i + 1
       if inp == "blueprint" and 'blueprint' not in v_loc:
         print("+1 skill point, +40 tech")
         rsc['skillpts'] = rsc['skillpts'] + 1
         rsc['tech'] = rsc['tech'] + 40
         v_loc.add('blueprint')
       elif inp == "blueprint" and 'blueprint' in v_loc:
         print("You know what this blueprint are for")
       if inp == "pilot" and var2 == True:
         print(char['pilot'] + A0[31])
         launch = input("Are you sure you want to end the tuorial? ")
       elif inp == "pilot" and var2 == False:
         print(char['pilot'] + ": You haven't started the generator yet, can you please do that?")
     #-----hall-----#
     elif loc == "hall":
       loc = "hall"
       if loc_list != "hall":
         loc_list = "hall"
         i = 10
         while i <= 11:
           print(A0[i])
           time.sleep(1)
           i = i + 1
         print("(Hint: enter a location to move there)")
    #-----INVENTORY-----#
     if inp == "inventory":
        tot_invent = ''
        print("levels:")
        for keyterm in lvl:
         tot_invent += keyterm + ": " + str(lvl[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Rescources:")
        for keyterm in rsc:
         tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Items:")
        for item in invent:
         tot_invent += item + ", "
        print(tot_invent)
     #-----END TUTORIAL-----#
     if launch == 'yes':
       i = 32
       while i <= 39:
         if i <= 36:
           print(char['pilot'] + A0[i])
           time.sleep(1)
         else:
           print(A0[i])
           time.sleep(2.5)
         i = i + 1
       inp = "end"
       var0 = True

#-----Tutorial Intermission-----#

#Position in Stellar Neighbourhood
gac_loc = 'space'

#Dictionary is now for gac_loc
tut_loc = set({'wolosyd', 'tariskor', 'musk', 'ventrin-426b'})

#Tells if charachter has reached the Rendevnous
rendev = True

#Allows gac_loc loop to Run
var3 = False

#Stores previous location
prevloc = gac_loc

#Lib is for library
Lib = open('lines/library.txt').read().split("\n")

#Allows to enter tenex
var4 = ''

#Allows people to surpass Comms C
var6 = False

#doneA1 is to determine if Act 1 is complete
doneA1 = 0

#doneA2 is to determine if Act 1 is complete
doneA2 = False

#Allows people to pass the city limit
var9 = False

#Allows people to enter Lab 5
var10 = 0

#shows previous gac_loc
prevgacloc = 'space'

ac_loc = {
  'wolosyd':['sutherland park', 'otford', 'heathcote', 'campbeltown', 'ruins', 'central', 'kembla-kiama', 'nowra', 'port hacking', 'old bay', 'parramatta', 'avalon', 'penrith', 'bowral', 'picton', 'mountains', 'richmond'],
  'tariskor':['loading bay', 'mt. rextion', 'command center', 'storage', 'metal factory', 'rextion port', 'vulcan plains', 'vestic stockyard', 'mt. vulcan', 'mt. vestic'],
  'musk':['town hall', 'asimov', 'south musk', 'wells airport', 'city limit', 'cerberus plateau', 'landing site'],
  'ventrin-426b':['landing pad', 'cliffside', 'cavern', 'unknown location', 'lab entrance', 'hall', 'lab 1', 'lab 2', 'lab 3', 'lab 4', 'study', 'lab #!@%', 'bridge', 'vault door', 'test room'],
  'lab':['vault door', 'hall', 'quarters', 'common room', 'storeroom', 'lab 6', 'test chamber'],
  'spiron city':['mt. serins', 'outpost', 'ventrix', 'city entrance', 'sector 3', 'sector 4', 'industrial', 'sector 6', 'central spiron', 'landing bay', 'zoo', 'larina', 'junkyard', 'warehouse']
}

area = {
  'wolosyd':{
    1:['sutherland park', 'otford', 'heathcote', 'campbeltown', 'ruins'],
    2:['central', 'kembla-kiama', 'nowra'],
    3:['port hacking', 'old bay', 'parramatta', 'avalon', 'penrith', 'richmond'],
    4:['bowral', 'picton', 'mountains'],
    5:['tenex', 'offices', 'storage', 'head office', 'security room', 'security bay']
  },
  'tariskor':{
    1:['loading bay', 'mt. rextion', 'command center'],
    2:['storage', 'metal factory', 'rextion port'],
    3:['vulcan plains', 'mt. vulcan', 'vestic stockyard', 'mt. vestic'],
    4:[],
    5:[]
  },
  'musk':{
    1:['town hall', 'asimov', 'south musk'],
    2:['wells airport', 'city limit'],
    3:['cerberus plateau', 'landing site'],
    4:[],
    5:[]
  },
  'ventrin-426b':{
    1:['landing pad', 'cliffside', 'cavern', 'unknown location', 'lab entrance'],
    2:['hall', 'lab 1', 'lab 2', 'lab 3', 'lab 4', 'study', 'lab #!@%'],
    3:['bridge', 'vault door', 'test room'],
    4:[],
    5:[]
  },
  'lab':{
    1:['hall', 'quarters', 'common room', 'storeroom'],
    2:['lab 6'],
    3:['test chamber'],
    4:['vault door'],
    5:[]
  },
  'spiron city':{
    1:['mt. serins', 'outpost'],
    2:['ventrix', 'city entrance', 'sector 3', 'sector 4', 'industrial', 'sector 6', 'central spiron', 'landing bay'],
    3:['zoo'],
    4:['larina'],
    5:['junkyard', 'warehouse']
  }
}

loaded_save = False

if tutplay == False:
  var0 = True

if loadsave == True:
  var0 = False
  loaded_save = True

A7 = open('lines/Spiron.txt').read().split(">")
A6 = open('lines/Lab2.txt').read().split(">")
CT = open('lines/corrupt.txt').read().split(">")
A4 = open('lines/Lab1.txt').read().split(">")
A3 = open('lines/Musk.txt').read().split(">")
A2 = open('lines/Tariskor.txt').read().split(">")
A1 = open('lines/Wolosyd.txt').read().split(">")

varlist = dict({})

#varlist to store variables
def varlistadd(r, v3, v4, v6, v9, v10, a1, a2):
  varlist['rendev'] = r
  varlist['var3'] = v3
  varlist['var4'] = v4
  varlist['var6'] = v6
  varlist['var9'] = v9
  varlist['var10'] = v10
  varlist['doneA1'] = a1
  varlist['doneA2'] = a2

#varlistload
def varlistload(varterm):
  if varterm == 'rendev' or varterm == 'var3' or varterm == 'var6' or varterm == 'var9' or varterm == 'doneA2':
    if varlist[varterm] == 'True':
      return True
    elif varlist[varterm] == 'False':
      return False
  elif varterm == 'var10' or varterm == 'doneA1':
    return int(varlist[varterm])

varlistadd(rendev, var3, var4, var6, var9, var10, doneA1, doneA2)

#---
varloc = False
#---

#==========ACT 1 & 2==========#
if var0 == True:
  var1 = False
  i = 3
  print(char['pilot'] + A1[1])
  time.sleep(2)
  print(char['programmer'] + A1[2])
  time.sleep(2)
  while i <= 7:
    print(A1[i])
    time.sleep(2)
    i = i + 1
  inp = input("Where would you like to investigate first? ")
  while inp not in tut_loc:
    if inp == "end":
      var0 == True
      break
    inp = input("Where would you like to investigate first? ")
  print("You may choose to save the game by inputting 'save'")
  print("You may look up other possible commands by entering 'help'")

if loadsave == True:
  gac_loc, loc, prevloc = loadasave(loadsave)
  #print(gac_loc)
  var1 = False

while inp != 'end': 
  #print(loc, gac_loc, prevloc, 'grehfejr')
  if doneA2:
    tut_loc = set({'lab', 'spiron city'})
    inp == 'end'
    break 
  #-----previous location change-----#
  if varloc:
    print("That location is unreachable from here")
    loc = prevloc
    print("Current location:", loc)
  varloc = True
  #-----locloop-----#
  if var1 == True:
      inp = input("What should you do? ")
      if inp in ac_loc[gac_loc]:
       loc = inp
       print("Current location:", loc)
      if inp == 'cheat':
        cheat = input("What cheat will you use? ")
        cheatGame(cheat)
  #print(inp, var0)
  #-----gac_loc loop-----#
  if inp == "leave" or var0 == True:
    if rendev == True:
      if var3 == True:
        if doneA1 < 3:
          print(char['pilot'] + A1[1])
          print(char['programmer'] + A1[2])
          txtsc(3, 7, A1)
        elif doneA1 >= 3 and doneA2 == False:
          tut_loc.add('ventrin-426b')
          print(char['pilot'] + A4[1])
          print(char['programmer'] + A4[2])
          txtsc(3, 5, A1)
          print(A4[3])
          txtsc(6, 7, A1)
        inp = input("Where would you like to go next? ")
      var3 = True
      if inp in tut_loc:
       gac_loc = inp
       prevgacloc = 'space'
       var1 = True
       var0 = False
       rendev = False
       loc = ac_loc[inp][0]
       print("You Have decided to go to: " + gac_loc)
  #print(loadsave, loaded_save)
  if loadsave and loaded_save:
    var1 = True
    var0 = False
    rendev = False
    loaded_save = False
    slvar(False)
    rendev = varlistload('rendev')
    var3 = varlistload('var3')
    var4 = varlist['var4']
    var6 = varlistload('var6')
    var9 = varlistload('var9')
    var10 = varlistload('var10')
    doneA1 = varlistload('doneA1')
    doneA2 = varlistload('doneA2')
    if doneA2 == True:
      inp = 'end'
      break
  #-----HELP-----#
  if inp == 'help':
    helpCom(doneA2)
  #-----SAVE-----#
  if inp == 'save':
    print(savegame(gac_loc, loc, prevloc))
    varlistadd(rendev, var3, var4, var6, var9, var10, doneA1, doneA2)
    slvar(True)
  #-----GPS-----#
  if 'gps' in invent:
    if inp == 'gps':
      print(gps(gac_loc, gps_loc[gac_loc][loc][0], gps_loc[gac_loc][loc][1]))
  #-----INVENTORY-----#
  if inp == "inventory":
        tot_invent = ''
        print("levels:")
        for keyterm in lvl:
         tot_invent += keyterm + ": " + str(lvl[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Rescources:")
        for keyterm in rsc:
         tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Items:")
        for item in invent:
         tot_invent += item + ", "
        print(tot_invent)
  #-----WOLOSYD-----#
  if gac_loc == "wolosyd":
    #--central roadblock--#
    if loc == ac_loc[gac_loc][5] and 'crimotf' not in v_loc:
      if lvl['attack'] >= 3:
        if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][1]:
          if combatgame(3, 5):
            print("You fight the criminals")
            v_loc.add('crimotf')
          else:
            print("You failed to beat the criminals")
      else:
        print("Requires attack level of 3 or for you to be in Otford")
        loc = prevloc
    #--bowral roadblock--#
    if loc == ac_loc[gac_loc][13] and 'polnow' not in v_loc:
      if 'centcarm' in v_loc:
        if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][7]:
          v_loc.add('polnow')
      else:
        print("Officer: Sorry Sir, there has been a power outage and we are trying to fix it")
        loc = prevloc
    #--Picton/Campbeltown roadblock--#
    if loc == ac_loc[gac_loc][14]: 
      if prevloc == ac_loc[gac_loc][3]:
        if 'picblock' not in v_loc:
          print("There is a massive pile of rocks that is coating the road")
          if 'pickaxe' not in invent:
            loc = prevloc
          elif 'pickaxe' in invent:
            print("You use the pickaxe, the wall of rocks is broken, you are free to pass")
            v_loc.add('picblock')
    if loc == ac_loc[gac_loc][3]: 
      if prevloc == ac_loc[gac_loc][14]:
        if 'picblock' not in v_loc:
          print("There is a massive pile of rocks that is coating the road")
          if 'pickaxe' not in invent:
            loc = prevloc
          elif 'pickaxe' in invent:
            print("You use the pickaxe, the wall of rocks is broken, you are free to pass")
            v_loc.add('picblock')
    #--port hacking roadblock--#
    if loc == ac_loc[gac_loc][8] and 'ruinswall' not in v_loc:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][4]:
        if 'border wall keycard' in invent and lvl[lvlacss['programmer']] >= 2:
          if mapfeild(2, 3, 5, 'dsssddw'):
            v_loc.add('ruinswall')
            print("You pass the border wall")
          else:
            print("The border wall door is still closed")
            loc = prevloc
        else:
          print("You need a programming level of 2 and a border wall keycard")
          loc = prevloc
    #=====Sutherland park=====#
    if loc == ac_loc[gac_loc][0]:
      prevloc = loc
      varloc = False
      if loc_list != loc:
         loc_list = loc
         txtsc(8, 12, A1)
      if inp == 'shrubs' and 'wolshrub' not in v_loc:
        print("+20 cells, tenex keycard found")
        rsc['cells'] = rsc['cells'] + 20
        invent.add('tenex keycard')
        v_loc.add('wolshrub')
      elif inp == 'shrubs' and 'wolshrub' in v_loc:
        print("It's just bushes")
    #=====Otford=====#
    if loc == ac_loc[gac_loc][1]:
      if prevloc == ac_loc[gac_loc][5] or loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
           loc_list = loc
           txtsc(13, 17, A1)
        if inp == 'man':
          print("man: If you want to know some secrets, you've got to talk")
          if lvl['charisma'] >= 2:
            print("man: You'll need to bust in to tenex to get some info on the SAC virus")
          else:
            print("Requires charisma level of 2")
        if inp == 'building' and 'otfbd' not in v_loc:
          print("You walk into the building, and you find some stores")
          print("+5 cells, +12 credits, +2 skillpts")
          rsc['cells'] = rsc['cells'] + 5
          rsc['skllipts'] = rsc['skillpts'] + 5
          rsc['credits'] = rsc['credits'] + 12
          v_loc.add('otfbd')
        elif inp == 'building' and 'otfbd' in v_loc:
          print("It's just a normal apartment block")
    #=====Heathcote=====#
    if loc == ac_loc[gac_loc][2] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
         loc_list = loc
         txtsc(23, 25, A1)
      if inp == "weapons crate" and 'hccrate' not in v_loc:
        print("+30 ammo")
        rsc['ammo'] = rsc['ammo'] + 30
        v_loc.add('hccrate')
      elif inp == "weapons crate" and 'hccrate' in v_loc:
        print("It's empty")
      if inp == 'building':
        #=====HEATHCOTE UPGRADE=====#
        upg = 'empty'
        print("Who would you like to level up?")
        print("Enter the charachter's role in crew")
        print("Enter a blank to leave - you cannot use end here")
        tot_invent = ''
        print("Rescources:")
        for keyterm in rsc:
          tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
        print(tot_invent)
        while upg:
          upg = input("Enter charachter: ")
          for keyterm in char:
            if upg == char[keyterm] or upg == keyterm:
              if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                 print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                 rsc['skillpts'] = rsc['skillpts'] - 1
                 rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                 lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
              else:
               print("Rescoures not present in inventory")
    #=====Campbeltown=====#
    if loc == ac_loc[gac_loc][3]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][14]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(26, 32, A1)
        if inp == 'man' and 'pickaxe' in invent:
          if 'campman' not in v_loc:
            print("man: I see you are a miner just like me, here have this")
            print("obtained tenex master key")
            invent.add('tenex master key')
            v_loc.add('campman')
          else:
            print("You can use the card to acsess the important rooms")
        elif inp == 'man' and 'pickaxe' not in invent:
          print("man: who the hell are you?")
        if inp == 'robot':
          print(char['marksman'] + A1[33])
          time.sleep(2)
          print(char['programmer'] + A1[34])
          time.sleep(2)
          print(char['leader'] + A1[35])
          time.sleep(2)
          print(char['programmer'] + A1[36])
          time.sleep(2)
          print(char['mechanic'] + A1[37])
    #=====Ruins=====#
    if loc == ac_loc[gac_loc][4]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][8]:
        varloc = False
        prevloc = loc
        if loc_list != loc:
          loc_list = loc
          txtsc(38, 41, A1)
    #=====Central=====#
    if loc == ac_loc[gac_loc][5]:
      if prevloc == ac_loc[gac_loc][1] or loc_check(gac_loc, loc, prevloc):
        varloc = False
        prevloc = loc
        if loc_list != loc:
          loc_list = loc
          txtsc(18, 22, A1)
        if inp == "car mechanic" and lvl[lvlacss['mechanic']] >= 2:
          if 'centcarm' not in v_loc:
            print("You walk into the workshop and help the")
            print("man who needs help fixing his car")
            if battleship(10):
              print("he pays you for your work and helps restores power to bowral")
              print("+1 skillpts, tech. knowledge leveled up")
              rsc['skillpts'] = rsc['skillpts'] + 1
              lvl[lvlacss['mechanic']] = lvl[lvlacss['mechanic']] + 1
              v_loc.add('centcarm')
            else:
              print("You failed to fix his car")
          elif 'centcarm' in v_loc:
            print("Just a normal autoshop")
        elif inp == "car mechanic" and lvl[lvlacss['mechanic']] < 2:
          print("Requires tech. knowledge level of 2")
        if inp == "gas station":
          print("Welcome to the central gas station, we sell gas for 8 credits and tech for 10")
          print("enter a blank to leave")
          item = input("Enter an item: ")
          while item:
            if item == 'gas' and rsc['credits'] >= 8:
              print("bought 5 gas for 8 credits")
              rsc[item] = rsc[item] + 5
              rsc['credits'] = rsc['credits'] - 8
            elif rsc['credits'] < 8:
              print("Not enough credits")
            if item == 'tech' and rsc['credits'] >= 10:
              print("bought 5 tech for 10 credits")
              rsc['credits'] = rsc['credits'] - 10
              rsc[item] = rsc[item] + 5
            elif rsc['credits'] < 10:
              print("Not enough credits")
            item = input("Enter an item: ")
        if inp == "library":
          print("Welcome to the Wolosyd library, you can freely choose to read if you want")
          print("type an empty line to leave")
          book = ' '
          while book:
            print("There are 3 books available today, Oceana, WW3 and the Great war")
            book = input("What would you like to read? ")
            if book == "oceana":
              txtsc(1, 16, Lib)
              if book not in v_loc:
                print("+1 skillpts")
                rsc['skillpts'] = rsc['skillpts'] + 1
                v_loc.add(book)
            if book == "ww3":
              txtsc(17, 26, Lib)
              if book not in v_loc:
                print("+1 skillpts")
                rsc['skillpts'] = rsc['skillpts'] + 1
                v_loc.add(book)
            if book == "great war":
              txtsc(27, 39, Lib)
              if book not in v_loc:
                print("+1 skillpts")
                rsc['skillpts'] = rsc['skillpts'] + 1
                v_loc.add(book)
    #=====Kembla-kiama=====#
    if loc == ac_loc[gac_loc][6] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
       d = 0
       loc_list = loc
       txtsc(42, 45, A1)
      if inp == 'beach':
        beach = ' '
        print('The beach is pretty popular, it is full of people,')
        print('there is a bar and a rock pool here')
        print('enter a blank to leave')
        while beach:
          if beach == 'rock pool' and 'kkrp' not in v_loc:
            print("+25 material")
            rsc['material'] = rsc['material'] + 25
            v_loc.add('kkrp')
          elif beach == 'rock pool' and 'kkrp' in v_loc:
            print("Stop searchng the rock pools for 'material', it's creepy")
          if beach == 'bar' and var5 < 5:
            var5 = var5 + 1
            d = var5
            print('You take a quick break at the bar')
          elif beach == 'bar' and var5 >= 5:
            if 'kkbb' not in v_loc:
              d = var5
              print("You've been to the bar so many times you become incredibly social")
              print("Charisma leveled up by 1, +100 intoxication levels")
              lvl['charisma'] += 1
              v_loc.add('kkbb')
            elif 'kkbb' in v_loc:
              d = var5
              print("You need to be sober to complete the mission, you know")
          beach = input("What do you want to do here?")
      if inp == 'warehouse':
        beach = ' '
        print('The warehouse is fairly modern,')
        print('there is a pile of boxes, a car and a crate')
        print('enter a blank to leave')
        while beach:
          if beach == 'boxes' and 'kkwb' not in v_loc:
            print("+5 ammo, +18 credits")
            rsc['ammo'] = rsc['ammo'] + 5
            rsc['credits'] = rsc['credits'] + 18
            v_loc.add('kkwb')
          if beach == 'boxes' and 'kkwb' in v_loc:
            print("Noting but cardboard")
          if beach == 'car':
            print('A brand new sports car, you decide to take it for a spin')
            if d >= 5:
              print("You decide to drive the sports car even though")
              print("you are heavily drunk, you crash and die")
              beach = ''
              inp = 'end'
            elif d < 5:
              print("You decide do drive the car for a while, you return back")
              print("to the warehouse to continue the mission")
          if beach == 'crate':
            print('The crate has a slip of paper inside it')
            print('It reads a code: 249375, (code added to invent)')
            invent.add('code: 249375')
          if inp != 'end':
            beach = input("What do you want to do here?")
    #=====Nowra=====#
    if loc == ac_loc[gac_loc][7]:
      if prevloc == ac_loc[gac_loc][13] or loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(46, 49, A1)    
        if inp == 'cave' and 'nowcave' not in v_loc:
          print("You enter into the cave, it is dark but you find a large cart of iron ore")
          print("+10 material, +20 credits")
          rsc['ammo'] = rsc['ammo'] + 5
          rsc['credits'] = rsc['credits'] + 18
          v_loc.add('nowcave')
        elif inp == 'cave' and 'nowcave' in v_loc:
          print("just a normal cave")
        if inp == 'clearing':
          print("In the clearing you find a slip of paper")
          print("It reads: To get past the ruins, you don't just need a good hacker")
    #=====Bowral=====#
    if loc == ac_loc[gac_loc][13]:
      if prevloc == ac_loc[gac_loc][7] or loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(50, 52, A1)
        if inp == 'cricket oval' and 'bco' not in v_loc:
          print("You find some abandoned filming equipment used to record the game")
          print("+5 tech")
          rsc['tech'] = rsc['tech'] + 5
          v_loc.add('bco')
        elif inp == 'cricket oval' and 'bco' in v_loc:
          print("It's a regular cricket oval")
        if inp == 'general store':
          print("Welcome to the bowral general store, we sell these items:")
          print("Gps (30 crds), Gas barrel (2 crds), Pistol (35 crds)")
          print("enter a blank to leave")
          item = input("Enter an item: ")
          while item:
            if item == 'gps' and rsc['credits'] >= 30:
              if 'gps' not in invent:
                print("bought Gps for 30 credits")
                print("This will be used to tell your location, enter 'gps' to show position")
                invent.add('gps')
                rsc['credits'] = rsc['credits'] - 30
            elif rsc['credits'] < 30:
              print("Not enough credits")
            if item == 'gas barrel' and rsc['credits'] >= 2:
              if 'gsgas' not in v_loc:
                print("bought 5 gas for 2 credits")
                rsc['credits'] = rsc['credits'] - 2
                rsc['gas'] = rsc['gas'] + 5
                v_loc.add('gsgas')
            elif rsc['credits'] < 10:
              print("Not enough credits")
            if item == 'pistol' and rsc['credits'] >= 35:
              if 'pistol' not in invent:
                print("bought pistol for 35 credits")
                print("attack leveled up by 1")
                invent.add('pistol')
                rsc['credits'] = rsc['credits'] - 35
                lvl['attack'] = lvl['attack'] + 1
            elif rsc['credits'] < 35:
              print("Not enough credits")
            item = input("Enter an item: ")
    #=====Mountains=====#
    if loc == ac_loc[gac_loc][15]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(53, 56, A1)
        if inp == 'river' and 'mtsr' not in v_loc:
          print("in the river you find a gold nugget, you realise how rich")
          print("you are now until you remember the price of")
          print("gold is practically nothing")
          print('+5 credits')
          rsc['credits'] = rsc['credits'] + 5
          v_loc.add('mtsr')
        elif inp == 'river' and 'mtsr' in v_loc:
          print("You still feel robbed that you didn't find anything of worth")
        if inp == 'cavern' and 'mtsc' not in v_loc:
          print(A1[57])
          time.sleep(2)
          print(char['mechanic'] + A1[58])
          time.sleep(2)
          print(char['marksman'] + A1[59])
          time.sleep(2)
          print(A1[60])
          time.sleep(2)
          print(char['leader'] + A1[61])
          time.sleep(2)
          print(char['programmer'] + A1[62])
          time.sleep(2)
          print(char['pilot'] + A1[63])
          time.sleep(2)
          print(char['programmer'] + A1[64])
          time.sleep(2)
          print(char['leader'] + A1[65])
          time.sleep(2)
          v_loc.add('mtsc')
        elif inp == 'cavern' and 'mtsc' in v_loc:
          print("There is a dead bear on the ground")
    #=====Picton=====#
    if loc == ac_loc[gac_loc][14]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][3]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(66, 68, A1)
        if inp == 'mine' and 'picmine' not in v_loc:
          print("You find a pickaxe while wandering the mineshaft")
          print("pickaxe added to inventory")
          invent.add('pickaxe')
          v_loc.add('picmine')
        elif inp == 'mine' and 'picmine' in v_loc:
          print("It's just a regular iron mine")
        if inp == 'deposit' and 'picdep' not in v_loc:
          print("You find a pile of gold in the deposit,")
          print("you think you are now the superich")
          print("but then you remember that the price of gold is almost nil")
          print("+15 credits")
          rsc['credits'] = rsc['credits'] + 15
          v_loc.add('picdep')
        elif inp == 'deposit' and 'picdep' in v_loc:
          print("You're still incredibly salty from your ventures into the gold industry")
    #=====Tenex HQ=====#
    if inp == area[gac_loc][5][0] and 'tenex keycard' in invent:
      if loc_check(gac_loc, loc, prevloc) or loc == ac_loc[gac_loc][5]:
        varloc = False
        if loc_list != 'tenex HQ':
          loc_list = 'tenex HQ'
          txtsc(69, 78, A1)
          txin = ' '
          print("Note: enter 2 empty lines to get back to wolosyd, you can't use invent/gps/end at all")
          riddle = ' '
        while txin:
          txin = input("What should you do? ")
          if txin == 'help desk':
            print("if you want to get past that door you need to use a 6-digit acsess code")
          if txin == 'door':
            print("inventory:")
            for items in invent:
               print(items)
            var4 = ' '
            while var4:
              var4 = input("enter a code: ")
              if var4 == '249375':
                var4 = 'done'
                print("The door opens")
                print("Enter 'offices' or 'storage' to get into the main building")
                break
              print("Wrong code")
          if var4 == 'done':
            if txin == area[gac_loc][5][1]:
              txtsc(79, 81, A1)
            if txin == 'desk' and 'txndes' not in v_loc:
              print("You head over to the office desk")
              print("+10 tech")
              rsc['tech'] = rsc['tech'] + 10
              v_loc.add('txndes')
            elif txin == 'desk' and 'txndes' in v_loc:
              print("You know these documents")
            if txin == area[gac_loc][5][2]:
              txtsc(82, 84, A1)
            if txin == 'computer' and 'txntx' not in v_loc:
              print("You go onto the laptop and see some plans")
              print("+2 skillpts")
              rsc['skillpts'] = rsc['skillpts'] + 2
              v_loc.add('txntx')
            elif txin == 'computer' and 'txntx' in v_loc:
              print("Don't keep peering into someone's computer")
            if txin == 'crate' and 'txnsc' not in v_loc:
              print("You open the crate, it is full of rescourses")
              print("+20 material")
              rsc['material'] = rsc['material'] + 20
              v_loc.add('txnsc')
            elif txin == 'crate' and 'txnsc' in v_loc:
              print("It's empty")
            if txin == area[gac_loc][5][3]:
              if 'tenex master key' not in invent:
                print('requires tenex master key')
              elif 'tenex master key' in invent and riddle != 'done':
                txtsc(85, 93, A1)
                riddle = ' '
                while riddle:
                  riddle = input("enter an answer: ")
                  if riddle == 'robot':
                    riddle = 'done'
                    print("Malcom: Very well, enjoy the information")
                    break
                  print("Wrong answer")
            if 'tenex master key' in invent and riddle == 'done':
              if txin == area[gac_loc][5][4]:
                txtsc(94, 95, A1)
              if txin == area[gac_loc][5][5]:
                print(A1[96])
                print("border wall keycard added to inventory")
                invent.add('border wall keycard')
              if txin == 'filing cabinet':
                print(char['leader'] + A1[97])
                time.sleep(2)
                print(char['pilot'] + A1[98])
                time.sleep(2)
                print(char['leader'] + A1[99])
                time.sleep(2)
                print(char['programmer'] + A1[100])
                time.sleep(2)
                print(char['mechanic'] + A1[101])
                time.sleep(2)
                if 'tenexfilcab' not in v_loc:
                  doneA1 = doneA1 + 1
                  v_loc.add('tenexfilcab')
                  if doneA1 >= 3:
                    print(char['mechanic'] + A3[63])
                    print(char['marksman'] + A3[64])
                    txtsc(65, 67, A3)
                    if combatgame(4, 18):
                      print("You beat the guards, and run outside the structure")
                      print(char['pilot'] + A3[68])
                    else:
                      print("The guards beat you, you have lost keycard 1")
                      invent.remove('keycard 1')
    if inp == area[gac_loc][5][0] and 'tenex keycard' not in invent:
      print("tenex HQ requires a tenex keycard to acsess")
    #=====Port Hacking=====#
    if loc == ac_loc[gac_loc][8]:
      if prevloc == ac_loc[gac_loc][4] or loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(102, 107, A1)
        if rendev == False:
          print("You have reached the redevenous point, enter leave to fly to another location")
          rendev = True
        if inp == 'cliff' and 'phcliff' not in v_loc:
          txtsc(108, 110, A1)
          print("+ 25 tech, +10 credits")
          rsc['tech'] = rsc['tech'] + 25
          rsc['credits'] = rsc['credits'] + 10
          v_loc.add('phcliff')
        elif inp == 'cliff' and 'phcliff' in v_loc:
          print("Its a very nice skyline")
        if inp == 'bushes' and 'phbus' not in v_loc:
          print("+ 5 material")
          rsc['material'] = rsc['material'] + 5
          v_loc.add('phbus')
        elif inp == 'bushes' and 'phbus' in v_loc:
          print("Its just bushes")
        if inp == 'airport':
          print("welcome to the botany shop")
          print("were selling cells for 20 credits")
          beach = ' '
          while beach:
            beach = input("What would you like to buy? ")
            if beach == 'cells':
              print("bought 5 cells for 20 credits")
              rsc['cells'] = rsc['cells'] + 5
              rsc['credits'] = rsc['credits'] - 20
    #=====Old Bay (Sydney)=====#
    if loc == ac_loc[gac_loc][9]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(111, 114, A1)
        if inp == 'golf course' and 'obgc' not in v_loc:
          print("The golf course is still full of discarded plastic balls")
          print("+10 gas")
          rsc['gas'] = rsc['gas'] + 10
          v_loc.add('obgc')
        elif inp == 'golf course' and 'obgc' in v_loc:
          print("It's full of grass and sand")
        if inp == 'bridge' and 'obhb' not in v_loc:
          txtsc(115, 119, A1)
          print("+ 5 material")
          rsc['material'] = rsc['material'] + 5
          v_loc.add('obhb')
        elif inp == 'bridge' and 'obhb' in v_loc:
          print("Don't spend too much time on the bridge!")
        if inp == 'school':
          school = ' '
          txtsc(120, 124, A1)
          while school:
            school = input("Where do you want to visit? ")
            if school == "dining hall":
              print("You walk into the dining hall, you can clearly tell")
              print("the poor quality of the food by just smelling it, Yuck!")
            if school == "boarding house" and 'scotsbh' not in v_loc:
              print("You walk to the building called 'Aspinall house',")
              print("its amazing that this is still functional after 394 years of use")
              print("+ 10 material")
              rsc['material'] = rsc['material'] + 10
              v_loc.add('scotsbh')
            elif school == "boarding house" and 'scotsbh' in v_loc:
              print("It is a very old building")
            if school == 'classroom':
              print("The principal explains how this classroom was") 
              print("one to teach IT students, you still can see the freezing cold")
              print("A/C unit being set to 'Artic Winter'")
    #=====Parramatta=====#
    if loc == ac_loc[gac_loc][10]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(125, 127, A1)
        if inp == 'car' and 'paracar' not in v_loc:
          print("+15 material, +5 gas")
          rsc['gas'] = rsc['gas'] + 5
          rsc['material'] = rsc['material'] + 15
          v_loc.add('paracar')
        elif inp == 'car' and 'paracar' in v_loc:
          print("It's a car")
        if inp == 'river' and 'parariv' not in v_loc:
          print("'A gold nugget!' you say, 'oh wait, gold is worthless, dammit'")
          print('+5 credits')
          rsc['credits'] += 5
          v_loc.add('parariv')
        elif inp == 'river' and 'parariv' in v_loc:
          print("You can't belive that gold is still worthless")
        if inp == "apartments":
          print("You enter into the apartment block, it is full of")
          print("people who still think sydney is a city")
    #=====Avalon=====#
    if loc == ac_loc[gac_loc][11]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(128, 131, A1)
        if inp == "beach" and 'avabeach' not in v_loc:
          print("The beach is fairly empty, but there is some old cars here")
          print("+10 gas")
          rsc['gas'] = rsc['gas'] + 10
          v_loc.add('avabeach')
        elif inp == "beach" and 'avabeach' in v_loc:
          print("The beach is fairly empty")
        if inp == "man":
          print("man: I'll give you a tip if you want to")
          if lvl['charisma'] >= 4:
            print("man: There is not a lot of stuff going on here,")
            print("but there is one thing that you require to complete the mission")
          else:
            print("Requires a charisma level of 4")
    #=====Richmond=====#
    if loc == ac_loc[gac_loc][16]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(132, 133, A1)
        if inp == 'box':
          print("lab keycard 2 added to inventory")
          invent.add('lab keycard 2')
        if inp == 'blacktown' and 'richblac' not in v_loc:
          print("You walk into the local town called blacktown,")
          print("On the ground you find some ammo")
          print("+25 ammo")
          v_loc.add('richblac')
          rsc['ammo'] = rsc['ammo'] + 25
        elif inp == 'blacktown' and 'richblac' in v_loc:
          print("It's just a town")
    #=====Penrith=====#
    if loc == ac_loc[gac_loc][12]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(134, 135, A1)
        if inp == 'regatta center':
          print("You head to the regatta center, the head of the center")
          print("challenges you to a race")
          if lvl['charisma'] >= 4:
            if anagram(5, 6):
              print("You accept and win")
              print("+2 skillpts")
              rsc['skillpts'] = rsc['skillpts'] + 2
            else:
              print("You lost the race")
          else:
            print("Requires Charisma level 4")
  #-----TARISKOR-----#
  if gac_loc == "tariskor":
    #--command center (2 way) roadblock--#
    if loc == ac_loc[gac_loc][3] or loc == ac_loc[gac_loc][4]:
      if 'cctwrb' not in v_loc:
        if lvl['intellect'] >= 4:
          if var6 == True:
            if mapfeild(3, 1, 5, 'dsdssa'):
              print("You open the doors")
              v_loc.add('cctwrb')
            else:
              print("The doors remain closed")
          else:
            print("The power is off")
            loc = prevloc
        else:
          print("Requires an Intellect of 4")
          loc = prevloc
    #=====Loading bay=====#
    if loc == ac_loc[gac_loc][0]:
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(1, 5, A2)
      if inp == "metal deposit" and 'lbmd' not in v_loc:
        print("+20 material")
        rsc['material'] = rsc['material'] + 20
        v_loc.add('lbmd')
      elif inp == "metal deposit" and 'lbmd' in v_loc:
        print("The metal is red hot")
    #=====Mt. Rextion=====#
    if loc == ac_loc[gac_loc][1] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(6, 9, A2)
      if inp == "gun case" and 'mrrexgc' not in v_loc:
        print("+20 ammo")
        v_loc.add('mrrexgc')
        rsc['ammo'] = rsc['ammo'] + 20
      elif inp == "gun case" and 'mrrexgc' in v_loc:
        print("It's empty")
      if inp == "thermal vent" and var6 == False:
        print("You walk inside the vent, there is a")
        print("geothermal generator inside that is broken")
        if lvl[lvlacss['mechanic']] >= 3:
          if battleship(10):
            print("You fix the geothermal generator")
            var6 = True
          else:
            print("You failed to fix the generator")
        else:
          print("Requires a tech. knowledge of 4")
      elif inp == "thermal vent" and var6 == True:
        print("You should get out of there, its very hot")
    #=====Command Center=====#
    if loc == ac_loc[gac_loc][2]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][3]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(10, 15, A2)
        if inp == "spare parts" and 'tccsp' not in v_loc:
          print("+30 tech, +1 skillpts")
          v_loc.add('tccsp')
          rsc['tech'] = rsc['tech'] + 30
          rsc['skillpts'] += 3
        elif inp == "spare parts" and 'tccsp' in v_loc:
          print("It's old tech")
        #=====COMMAND CENTER UPGRADE=====#
        if inp == "desk":
          upg = 'empty'
          print("Who would you like to level up?")
          print("Enter the charachter's role in crew")
          print("Enter a blank to leave - you cannot use end here")
          tot_invent = ''
          print("Rescources:")
          for keyterm in rsc:
            tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
          print(tot_invent)
          while upg:
            upg = input("Enter charachter: ")
            for keyterm in char:
              if upg == char[keyterm] or upg == keyterm:
                if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                  print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                  rsc['skillpts'] = rsc['skillpts'] - 1
                  rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                  lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
                else:
                 print("Rescoures not present in inventory")
    #=====Storage=====#
    if loc == ac_loc[gac_loc][3]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][2]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(16, 18, A2)
        if inp == "bin" and 'tarstbin' not in v_loc:
          rsc['cells'] += 30
          print("There are alot of power cells here")
          print("+30 cells")
          v_loc.add("tarstbin")
        elif inp == "bin" and 'tarstbin' in v_loc:
          print("Stop rummaging through bins! That's disgusting!")
        if inp == "trash pile":
          print("You search the pile")
          if "rextion keycard" not in invent and pickanum(10, 20):
            print("rextion keycard added to your inventory")
            invent.add("rextion keycard")
          else:
            print("... And find nothing (because it's trash)")
        if inp == "bookcase":
            print("Welcome to the Tariskor library, you can freely choose to read if you want")
            print("type an empty line to leave")
            book = ' '
            while book:
              print("There are 3 books here on this shelf: coloran z-flu, colorans and spirons, after the dark ages")
              book = input("What would you like to read? ")
              if book == "coloran z-flu":
                txtsc(40, 59, Lib)
                if book not in v_loc:
                  print("+1 skillpts")
                  rsc['skillpts'] = rsc['skillpts'] + 1
                  v_loc.add(book)
              if book == "colorans and spirons":
                txtsc(60, 83, Lib)
                if book not in v_loc:
                  print("+1 skillpts")
                  rsc['skillpts'] = rsc['skillpts'] + 1
                  v_loc.add(book)
              if book == "after the dark ages":
                txtsc(84, 103, Lib)
                if book not in v_loc:
                  print("+1 skillpts")
                  rsc['skillpts'] = rsc['skillpts'] + 1
                  v_loc.add(book)
    #=====Metal factory=====#
    if loc == ac_loc[gac_loc][4]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][2]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(19, 23, A2)
        if inp == 'operator':
          print(char['leader'], "We need you to let us into the port")
          if lvl[lvlacss['leader']] >= 3:
            print("Operator: I can't open it for you, but the number is 42")
          else:
            print("Operator: You're not supposed to be here!")
        if inp == 'hopper' and 'tarfachop' not in v_loc:
          print("You grab the gold, 'I'm rich!!' you shout.")
          print("you have finally reached your childhood dream of becoming this wealthy,")
          print("you calculate how much this is worth,")
          print("+21 credits")
          print("Your childhood dreams are crushed by the worhtlessnes of gold")
          rsc['credits'] += 21
          v_loc.add('tarfachop')
        elif inp == 'hopper' and 'tarfachop' in v_loc:
          print("You run through your calculations again to check if anything is wrong")
    #=====Rextion port=====#
    if loc == ac_loc[gac_loc][5]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][6]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(24, 27, A2)
        if inp == 'blueprints' and 'tarrpbl' not in v_loc:
          print("The blueprints are plans for a new extention of the metal factory")
          print("+3 skillpts")
          rsc['skillpts'] += 3
          v_loc.add('tarrpbl')
        elif inp == 'blueprints' and 'tarrpbl' in v_loc:
          print("The blueprints are blue, odd")
        if inp == "boat" and 'tarboat' not in v_loc:
          print("It's a metal boat hull, could be able to fix it")
          if lvl[lvlacss['mechanic']] >= 4:
            if anagram(3, 4):
              print("You fix the boat, and drag it into the drop zone")
              v_loc.add('tarboat')
            else:
              print("The boat is still broken")
          else:
            print("Requires Tech. Knowledge level of 4 to fix boat")
        if inp == "drop zone" and 'rextion keycard' in invent:
          print("You walk into the dropzone,")
          if 'tarboat' in v_loc:
            print("You but the metal boat into the harness and your crew")
            print("prepares to drop into the magma below")
            print("The boat drops, and you travel to vulcan plains")
            loc = ac_loc[gac_loc][6]
            print("Current location:", loc)
          else:
            print("You can't drop into the flow yet")
        elif inp == "drop zone" and 'rextion keycard' not in invent:
          print("Requires Rextion keycard")
    #=====Vulcan plains=====#
    if loc == ac_loc[gac_loc][6]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][5]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(28, 30, A2)
        if inp == "pool" and 'tarvppolg' not in v_loc:
          print("Holy moly! Its pure gold!, how is this possible")
          print("You think about it then realise that it is worthless")
          print("+14 credits")
          rsc['credits'] += 14
          v_loc.add('tarvppolg')
        elif inp == "pool" and 'tarvppolg' in v_loc:
          print(char['leader'], ": Godamn government, taking our gold!")
        if inp == "port":
          print("You exit the port on the boat and sail towards rextion port,")
          print("press a blank space to continue")
          loc = ac_loc[gac_loc][5]
          print("Current location:", loc)
    #=====Vestic stockyard=====#
    if loc == ac_loc[gac_loc][7]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(31, 34, A2)
        if inp == 'pile' and 'tarstkpi' not in v_loc:
          print("This is full of stuff")
          print("+8 cells, +7 material, +30 gas")
          rsc['cells'] += 8
          rsc['material'] += 7
          rsc['gas'] += 30
          v_loc.add('tarstkpi')
        if inp == 'pile' and 'tarstkpi' in v_loc:
          print("It's a lot of stuff")
        if inp == 'security guard' and 'tarvstscgar' not in v_loc:
          if lvl['attack'] >= 2:
            print("You approach the guard")
            print("guard: Hey! Get away from me!")
            if combatgame(1, 10):
              print("guard: here, have this")
              print("safe key added to inventory")
              invent.add('safe key')
              v_loc.add('tarvstscgar')
          else:
            print("Requires an attack of 2")
        elif inp == 'security guard' and 'tarvstscgar' in v_loc:
          print("guard: You beat me fair and square")
    #=====Mt. Vulcan=====#
    if loc == ac_loc[gac_loc][8]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(35, 39, A2)
        if inp == 'gps' and 'gps' not in invent:
          invent.add('gps')
          print("Gps added to inventory")
          print("You can now use the gps command to get a location")
        if inp == 'tazer' and 'tazer' not in invent:
          invent.add('tazer')
          print("Tazer added to invent")
          print("The tazer can be used in fight sequences")
        if inp == 'collapsed mine' and 'mtvulccolm' not in v_loc:
          print("You walk into the collapsed mine, the rumble from the volcano")
          print("is immense as you find some mineshaft plans")
          print("+1 skillpts")
          rsc['skillpts'] += 1
          print("The mineshaft begins folding under pressure")
          print("as you and your crew rush out.")
          print("The mine crushes in on itself as a huge")
          print("surge of molten rock escapes from the hole")
          v_loc.add('mtvulccolm')
        elif inp == 'collapsed mine' and 'mtvulccolm' in v_loc:
          print("The lava has slowed to a halt, you better get away from here")
    #=====Mt. Vestic=====#
    if loc == ac_loc[gac_loc][9]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(40, 43, A2)
        if inp == "power cells" and 'powcmtvestic' not in v_loc:
          print("+10 power cells")
          rsc['cells'] += 10
          v_loc.add('powcmtvestic')
        if inp == "office":
          print("The office is empty, exept for a safe, you could open it")
          if 'safe key' in invent:
            rendev = True
            print("You have now reached the rendevenous location,")
            print("enter leave to go to another system")
            if 'tarvesoffsc' not in v_loc:
              print("You open the safe")
              doneA1 += 1
              print(char['leader'] + A2[44])
              print(char['pilot'] + A2[45])
              print(char['leader'] + A2[46])
              print(char['programmer'] + A2[47])
              print(char['mechanic'] + A2[48])
              v_loc.add('tarvesoffsc')
              if doneA1 >= 3:
                print(char['mechanic'] + A3[63])
                print(char['marksman'] + A3[64])
                txtsc(65, 67, A3)
                if combatgame(4, 18):
                  print("You beat the guards, and run outside the structure")
                  print(char['pilot'] + A3[68])
                else:
                  print("The guards beat you, you have lost keycard 1")
                  invent.remove('keycard 1')
            elif 'tarvesoffsc' in v_loc:
              print("It's those files on SAC-26")
  #--musk roadblock--#
  if gac_loc == "musk":
    if lvl[lvlacss['pilot']] < 4:
      print("Requires piloting level 4")
      rendev = True
      inp = 'leave'
      var1 = False
      gac_loc = 'space'
  #-----MUSK-----#
  if gac_loc == "musk":
    #--wells roadblock--#
    if loc == ac_loc[gac_loc][3] and prevloc == loc == ac_loc[gac_loc][2]:
      if 'radio' in invent and lvl['charisma'] >= 6:
        if 'wellsrblk' not in v_loc:
          if anagram(4, 6):
            print("You pass the blockade")
            v_loc.add('wellsrblk')
          else:
            print("You failed to pass the blockade")
            loc = prevloc
      else:
        print("Guard: Sorry Sir, the blockade is still up")
        print("Requires a charisma of 6")
        loc = prevloc
    #--cerebus plateau roadblock--#
    if loc == ac_loc[gac_loc][5] and prevloc == ac_loc[gac_loc][4]:
      if  'muskclairlockconf' not in v_loc:
        if var9 == True:
          print("You open the airlock and exit the city")
          v_loc.add('muskclairlockconf')
        else:
          print("The airlock to exit the city is broken")
          loc = prevloc
    #=====Town hall=====#
    if loc == ac_loc[gac_loc][0]:
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(1, 5, A3)
      if inp == 'parlament' and 'muskthparl' not in v_loc:
        print("You watch the parlamentary debate")
        if anagram(8, 8):
          print("You learn a lot of knowledge from the debate")
          print("+2 skillpts")
          v_loc.add('muskthparl')
          rsc['skillpts'] += 2
        else:
          print("To you, this debate is all a bunch of jibberish")
      elif inp == 'parlament' and 'muskthparl' in v_loc:
        print("They are debating on a bill to claim another asteroid")
      if inp == "office block":
        print("You walk into the office building, it is grand")
        print("there is a mural on the wall of a map of mars and its 2 moons")
        office = ' '
        while office:
          if office == 'filing cabinet':
            txtsc(6, 24, A3)
          if office == 'help desk' and 'muskoffhelp' not in v_loc:
            print("You walk up to the desk, there is some cash here")
            print("+20 credits")
            rsc['credits'] += 20
            v_loc.add('muskoffhelp')
          elif office == 'help desk' and 'muskoffhelp' in v_loc:
            print("It's just paper on this desk")
          print("There are 2 options here: filing cabinet or help desk")
          office = input("What should you do?")
    #=====Asimov=====#
    if loc == ac_loc[gac_loc][1]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][4]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(25, 27, A3)
        if inp == "museum":
          mus = ' '
          while mus:
            print("You walk into the museum, there are 3 exibhits:")
            print("energy, space travel and dark age solar system")
            print("Enter a blank to leave")
            mus = input("Which exhibit? ")
            lib = False
            if mus == "energy":
              txtsc(104, 118, Lib)
              lib = True
            if mus == "space travel":
              txtsc(119, 134, Lib)
              lib = True
            if mus == "dark age solar system":
              txtsc(135, 154, Lib)
              lib = True
            if lib == True and mus not in v_loc:
              print("+1 skillpts")
              rsc['skillpts'] += 1
              v_loc.add(mus)
        if inp == "mint" and 'muskasimovmint' not in v_loc:
          print("You walk into the mint and find barrels of gold coins")
          print("You think to yourself how lucky you are")
          print("and why the mint has so many gold coins about")
          print("Until you realise that gold is worth nothing, your dreams are crushed")
          print("+18 credits")
          rsc['credits'] += 18
          v_loc.add('muskasimovmint')
        elif inp == "mint" and 'muskasimovmint' in v_loc:
          print("They still need some security here")
        if inp == "space port":
          print("You enter into the space port, developed by spaceX in 2064")
          off = ' '
          while off:
            print("There are a few barrels of oil,")
            print("a space ship and a elevator")
            print("Enter a blank to leave")
            off = input("Where do you want to go? ")
            if off == "barrels" and 'muskasimovspbar' not in v_loc:
              print("+21 gas")
              rsc['gas'] += 21
              v_loc.add('muskasimovspbar')
            if off == 'ship' and 'muskasimovspsac' not in v_loc:
              rsc['skillpts'] += 1
              print("You enter the spaceship, there are some blueprints inside")
              print("+1 skillpts")
              print("Spaceship pilot: Hey! what are you doing in there!")
              if combatgame(1, 25):
                print("You beat the ship pilot")
                print("He has something on him, its a radio")
                print("You use the radio to lift the airport blockade")
                print("radio added to inventory")
                invent.add('radio')
                v_loc.add('muskasimovspsac')
              else:
                print("You fail to beat the pilot,")
                print("He puts the blueprints back into the ship")
                print("-1 skillpts")
                rsc['skillpts'] += -1
            if off == "elevator":
              print("You board the elevator. But litte did you know,")
              print("that it was a space elevatior!")
              print("The moment you exit the martian atmosphere,")
              print("you feel your lungs collapse as you suffocate in the vaccum of space")
              print("You die")
              off = ''
              inp = 'end'
    #=====South Musk=====#
    if loc == ac_loc[gac_loc][2]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][3]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(28, 31, A3)
        if inp == "greenhouse":
          print("There is alot of plants for sale here")
          off = ' '
          while off:
            print("You can buy: material for 10 credits and a shotgun for 50")
            print("Enter a empty line to leave")
            off = input("What do you want to buy? ")
            if off == "material" and rsc['credits'] >= 10:
              rsc['material'] += 5
              rsc['credits'] += -10
              print("bought 5 material for 10 credits")
            elif off == "material" and rsc['credits'] <= 10:
              print("Not enough credits")
            if off == "shotgun" and 'shotgun' not in invent:
              if rsc['credits'] >= 50:
                invent.add('shotgun')
                rsc['credits'] += -50
                print("Bought shotgun for 50 credits")
              else:
                print("Not enough credits")
        if inp == "university":
          uni = ' '
          print("You are now in the university,")
          while uni:
            print("There is a boarding house, a lab and a lecture hall")
            print("Enter a blank to leave")
            uni = input("Where do you want to go? ")
            if uni == "boarding house":
              print("You walk into the boarding house,")
              print("it looks alot nicer than the other ones you have seen")
              #=====UNIVERSITY BH UPGRADE=====#
              upg = 'empty'
              print("Who would you like to level up?")
              print("Enter the charachter's role in crew")
              print("Enter a blank to leave - you cannot use end here")
              tot_invent = ''
              print("Rescources:")
              for keyterm in rsc:
                tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
              print(tot_invent)
              while upg:
                upg = input("Enter charachter: ")
                for keyterm in char:
                  if upg == char[keyterm] or upg == keyterm:
                    if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                      print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                      rsc['skillpts'] = rsc['skillpts'] - 1
                      rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                      lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
                    else:
                      print("Rescoures not present in inventory")
            if uni == "lab" and 'musksmunilab' not in v_loc:
              print("You walk into the lab, there is a pile of documents on the floor")
              print("You read the documents - it's about continuing the")
              print("terraforming of mars by pumping more coal into the atmosphere")
              print("There's some gas in here")
              print("+15 gas")
              rsc['gas'] += 15
              v_loc.add('musksmunilab')
            elif uni == "lab" and 'musksmunilab' in v_loc:
              print("It's full of science stuff")
            if uni == "lecture hall" and 'musksmunilecha' not in v_loc:
              print("There is a bunch of tech lying here,")
              print("the crew can use this - but it needs to be hacked into")
              print(char['programmer'] + ": Don't worry, I'll fix this")
              if mapfeild(4, 0, 5, 'ddddssssaaaa'):
                print("The tech has been hacked into")
                print("+10 tech, +2 skillpts")
                rsc['tech'] += 10
                rsc['skillpts'] += 2
                v_loc.add('musksmunilecha')
              else:
                print("You failed to hack the tech")
            if uni == "lecture hall" and 'musksmunilecha' in v_loc:
              print("The room is empty")
        if inp == "neighbourhood":
          nei = ' '
          print("You enter into the neighbourhood,")
          while nei:
            print("There are 3 thing here: a house,")
            print("an gas station, and a man.")
            print("Enter a line")
            nei = input("Where are you going to go? ")
            if nei == 'house':
              print("You walk up to the house, there playing some board games")
              print("You decide to play with them")
              if battleship(11):
                print("+23 credits, +2 skillpts")
                rsc['credits'] += 23
                rsc['skillpts'] += 2
              else:
                print("Dammit, get 'em next time")
            if nei == 'gas station' and 'musksmneigassta' not in v_loc:
              print("+10 gas")
              rsc['gas'] += 10
              v_loc.add('musksmneigassta')
            elif nei == 'gas station' and 'musksmneigassta' in v_loc:
              print("You don't have a car, you don't need that much gas")
            if nei == "man" and lvl['charisma'] >= 5:
              print("man: In order to get to the airport")
              print("you need to go to the space port first")
            elif nei == "man" and lvl['charisma'] < 5:
              print("man: Get away from me!")
    #=====Wells Airport=====#
    if loc == ac_loc[gac_loc][3]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][2]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(32, 34, A3)
        if inp == "immigration counter" and 'keycard 2' not in invent:
          print("Guard: What are you doing here?")
          guard = input("What are you doing here? ")
          if guard == 'sabar':
            print(A3[35])
            print(char['leader'] + A3[36])
            txtsc(37, 40, A3)
            invent.add('keycard 2')
        if inp == "box" and 'muskwellsairbox' not in v_loc:
          print("+2 power cells")
          rsc['cells'] += 2
          v_loc.add('muskwellsairbox')
        elif inp == "box" and 'muskwellsairbox' in v_loc:
          print("The box is empty")
        if inp == "storeroom" and 'keycard 2' in invent:
          if 'sabar' not in v_loc:
            txtsc(41, 43, A3)
            print(char['leader'] + A3[44])
            txtsc(45, 47, A3)
            invent.add("MIA keycard")
            v_loc.add('sabar')
          else:
            print("There's noting but duct tape in here")
        elif inp == "storeroom" and 'keycard 2' not in invent:
          print("The door is not opening, it's probably broken")
    #=====City Limit=====#
    if loc == ac_loc[gac_loc][4]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][5]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(48, 52, A3)
        if inp == "guard tower" and 'musclgt' not in v_loc:
          print("You walk up the guard tower, it has plans for the growth of the city")
          print("+3 skillpts")
          rsc['skillpts'] += 3
          v_loc.add('musclgt')
        elif inp == "guard tower" and 'musclgt' in v_loc:
          print("The guard tower is very tall")
        if inp == "hangar" and 'muskclhang' not in v_loc:
          print("The hangar is filled with martian rovers")
          print("+23 cells")
          rsc['cells'] += 23
          v_loc.add('muskclhang')
        elif inp == "hangar" and 'muskclhang' in v_loc:
          print("The hangar is filled with martian rovers")
        if inp == 'airlock':
          print("You are at the airlock, the panel to fix the airlock is in front of you")
          print("It appears that it is operated via FM radio frequencies")
          print("You somehow need to emit a radio signal")
          radio = input("What will you do? ")
          if radio == 'radio' and 'radio' in invent:
            if lvl[lvlacss['mechanic']] >= 6 and 'muskclairrad' not in v_loc:
              if pickanum(10, 20):
                print("You fix the airlock and contact the person running the blockade")
                var9 = True
              else:
                print("You failed to fix the airlock")
            elif lvl[lvlacss['mechanic']] < 6 and 'muskclairrad' not in v_loc:
              print("Requires tech. knowledge of 6")
            else:
              print("It's the airlock controls")
    #=====Cerberus plateau=====#
    if loc == ac_loc[gac_loc][5]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][4]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(53, 56, A3)
        if inp == "moss patch" and 'muskcplamossp' not in v_loc:
          print("You walk onto the mossy bed, it's slimy")
          print("There seems to be something here")
          print("its an old satelite, odd")
          print("+30 tech, +1 skillpts")
          rsc['tech'] += 30
          rsc['skillpts'] += 1
          v_loc.add('muskcplamossp')
        elif inp == "moss patch" and 'muskcplamossp' in v_loc:
          print("It's very green")
        if inp == "mountain":
          print("You walk up to the mountaintop,")
          print("you can see the entire city of musk here")
        if inp == 'rover' and 'muskcplarovaba' not in v_loc:
          print("You walk up to the rover, you might be able to fix it")
          if lvl[lvlacss['programmer']] >= 5:
            if anagram(3, 5):
              print("You fix the rover")
              v_loc.add('muskcplarovaba')
              rsc['tech'] += 15
              rsc['skillpts'] += 1
              print("+15 tech, +1 skillpts")
            else:
              print("You failed to fix the rover")
          else:
            print("Requires programming level 5")
    #=====Landing site=====#
    if loc == ac_loc[gac_loc][6]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(57, 58, A3)
        if inp == 'landing craft' and 'Note: Sabar' not in invent:
          if lvl[lvlacss['programmer']] >= 6:
            if mapfeild(1, 3, 5, 'ssdddw'):
              print("You enter into the landing craft,")
              print("someone's been here in the past week")
              print("You find a note on the floor")
              print("Note: Sabar added to inventory")
              invent.add('Note: Sabar')
            else:
              print("The landing craft remains locked")
          else:
            print("Requires programming of 6")
        elif inp == 'landing craft' and 'Note: Sabar' in invent:
          print("The craft is empty")
        if inp == 'settlement' and 'musklandsset' not in v_loc:
          print("You walk into the abandoned settlement, it is almost clear of stuff")
          print("you do still find some info on the mars project")
          rsc['skillpts'] += 4
          print("+4 skillpts")
          v_loc.add('musklandsset')
        elif inp == 'settlement' and 'musklandsset' in v_loc:
          print("It's empty")
    #=====MIA=====#
    if inp == 'mia' and loc == ac_loc[gac_loc][0]:
      varloc = False
      print("You walk up to the front entrance of MIA,")
      if 'MIA keycard' in invent and 'mia' not in v_loc:
        print("You have reached the rendevenous location, enter 'leave' to exit the planet")
        txtsc(59, 60, A3)
        print(char['leader'] + A3[61])
        print(char['leader'] + A3[62])
        #doneA1 = 3
        doneA1 += 1
        v_loc.add('mia')
        rendev == True
        if doneA1 >= 3:
          print(char['mechanic'] + A3[63])
          print(char['marksman'] + A3[64])
          txtsc(65, 67, A3)
          if combatgame(4, 18):
            print("You beat the guards, and run outside the structure")
            print(char['pilot'] + A3[68])
          else:
            print("The guards beat you, you have lost keycard 1")
            invent.remove('keycard 1')
      else:
        print("The front entrance is locked")
        if 'MIA keycard' in invent:
          print("You have reached the rendevenous location, enter 'leave' to exit the planet")
          rendev == True
  #--Lab A2 roadblock--#
  if gac_loc == "ventrin-426b":
    if lvl[lvlacss['pilot']] < 6:
      print("Requires piloting level 6")
      rendev = True
      inp = 'leave'
      var1 = False
    if loadsave == False:
      gac_loc = 'space'
    if gac_loc not in v_loc:
      txtsc(10, 12, A4)
      v_loc.add(gac_loc)
  #-----LAB ACT2-----#
  if gac_loc == "ventrin-426b":
    #--Lab 5 roadblock--#
    var10 = 4
    if loc == ac_loc[gac_loc][11] and loc_check(gac_loc, loc, prevloc):
      if var10 != 4:
        loc = prevloc
        print("CRITICAL ERROR: Location does not exist")
    #=====Landing pad=====#
    if loc == ac_loc[gac_loc][0]:
      if prevgacloc == 'space' or loc_check(gac_loc, loc, prevloc):
        varloc = False
        prevgacloc = gac_loc
        rendev = True
        prevloc = loc
        if loc_list != loc:
          loc_list = loc
          txtsc(13, 14, A4)
          print("You have reached the rendevenous location, you may leave at any time")
        if inp == 'barrel' and 'lablandingpadbar' not in v_loc:
          print("There is a barrel of gas here,")
          print("It's glowing")
          print("+ 10 gas")
          rsc['gas'] += 10
          v_loc.add('lablandingpadbar')
        if inp == 'dirt mound':
          print("It's a mound of blue-ish soil")
          print("There are no items here")
    #=====Cliffside=====#
    if loc == ac_loc[gac_loc][1] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(15, 17, A4)
      if inp == "abyss":
        print("You jump into the abyss, you die")
        time.sleep(4)
        print("Or did you? You wake up next to the abyss.")
        print("Very, very interesting.")
        print('programming leveled up by 1')
        lvl[lvlacss['programmer']] += 1
      if inp == 'crystal' and "lab1cliffcrystal" not in v_loc:
        print("You walk toward a neon blue crystal, you get an intense headace")
        print("Luckily, it's just a placebo effect - It's actually a diamond")
        print("+6 credits, +20 material")
        rsc['credits'] += 6
        rsc['material'] += 20
        v_loc.add("lab1cliffcrystal")
    #=====Cavern=====#
    if loc == ac_loc[gac_loc][2] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(18, 20, A4)
      if inp == "crate" and 'lab1cratecavern' not in v_loc:
        print("Its some documents on the use of this planet")
        print("It reads: This planet is for the specific use of isolated labratories")
        print("The rest is redacted")
        print("+3 skillpts")
        rsc['skillpts'] += 3
        v_loc.add('lab1cratecavern')
      elif inp == "crate" and 'lab1cratecavern' in v_loc:
        print("It's that same paper again")
      if inp == 'river':
        print("Why are you doing this? You have an objective.")
    #=====Unkown Location=====#
    if loc == ac_loc[gac_loc][3] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(21, 23, A4)
      if loc not in v_loc:
        print(A4[24])
        print(char['marksman'] + A4[25])
        print(char['leader'] + A4[26])
        print(char['programmer'] + ": It's", char['marksman'] + ",")
        print(char['programmer'] + A4[27])
        v_loc.add(loc)
      if inp == 'lab equipment' and 'lab1unkloclabeq' not in v_loc:
        print("+20 tech, programming leveled up by 1")
        rsc['tech'] += 20
        lvl[lvlacss['programmer']] += 1
        v_loc.add('lab1unkloclabeq')
      elif inp == 'lab equipment' and 'lab1unkloclabeq' in v_loc:
        print("It's just old tech")
      if inp == 'man':
        print("The man is lying on the floor. Dead.")
        print("He is covered in blue crystals")
    #=====Lab entrance=====#
    if loc == ac_loc[gac_loc][4] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(28, 29, A4)
      print("How will you get past this door?")
      labe = input("What will you do? ")
      if labe == 'keycard 2':
        if lvl[lvlacss['programmer']] >= 8:
          if anagram(6, 8):
            print("You open the doors to the lab")
            loc = ac_loc[gac_loc][5]
            prevloc = ac_loc[gac_loc][5]
          else:
            print("You failed to open the door")
        else:
          print("Requires a programming of 8")
      else:
        print("Access denied")
    #=====Hall=====#
    if loc == ac_loc[gac_loc][5]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(30, 32, A4)
        rendev = False
    #=====Lab 1=====#
    if loc == ac_loc[gac_loc][6]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(33, 35, A4)
        if inp == 'dead body':
          print("It's cold. Probably beginning to be infected by SAC-26")
          if 'lab1check' not in v_loc:
            var10 += 1
            v_loc.add('lab1check')
        if inp == 'documents' and 'ventrinlab1docos' not in v_loc:
          print("The documents are messy and disorganised")
          time.sleep(tss)
          print(char['leader'] + ": Look at this, it's about SAC-26")
          time.sleep(tss)
          print(char['mechanic'] + ": What's it about?")
          time.sleep(tss)
          print(char['leader'] + ": It was designed ... to erase the alien p0puLation")
          time.sleep(tss)
          print("+2 skillpts")
          rsc['skillpts'] += 2
          v_loc.add('ventrinlab1docos')
        elif inp == 'documents' and 'ventrinlab1docos' in v_loc:
          print("You know these documents")
    #=====Lab 2=====#
    if loc == ac_loc[gac_loc][7]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(36, 39, A4)
        if inp == 'crystals' and 'ventrinlab21oddc' not in v_loc:
          print("You walk up to the crystal. It has some material beside it")
          print("+ µaterial")
          rsc['material'] += 20
          v_loc.add('ventrinlab21oddc')
        elif inp == 'crystals' and 'ventrinlab21oddc' in v_loc:
          print("It's pulsating")
        if inp == 'microscope':
          print("You look in†o the microscope. It is full of SAC crystals")
          print("You can see the silicon cells that make up it")
          if 'lab2check' not in v_loc:
            var10 += 1
            v_loc.add('lab2check')
    #=====Lab 3=====#
    if loc == ac_loc[gac_loc][8]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(40, 42, A4)
        if inp == 'barrel' and 'ventrinlab3glitchb' not in v_loc:
          print("+20 gas")
          rsc['gas'] += 20
          v_loc.add('ventrinlab3glitchb')
        elif inp == 'barrel' and 'ventrinlab3glitchb' in v_loc:
          print("+20 gas")
          time.sleep(2)
          print("You really thought you could get away with stealling?")
          print('')
        if inp == 'whiteboard':
          print("It says on the whiteboard that the sAC-26 virus is a sentient object")
          if 'lab3check' not in v_loc:
            var10 += 1
            v_loc.add('lab3check')
    #=====Lab 4=====#
    if loc == ac_loc[gac_loc][9]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(43, 43, A4)
        if inp == 'window':
          print("CrrITICAL ERROR: Location dd0Es not ∑xist")
          if 'lab4check' not in v_loc:
            var10 += 1
            v_loc.add('lab4check')
    #=====Study=====#
    if loc == ac_loc[gac_loc][10]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(44, 45, A4)
        if inp == 'desk':
          #=====LAB ACT 1 DESK UPGRADE=====#
              upg = 'empty'
              print("Who would you like to level up?")
              print("Enter the charachter's role in crew")
              print("Enter a blank to leave - you cannot use end here")
              tot_invent = ''
              print("Rescources:")
              for keyterm in rsc:
                tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
              print(tot_invent)
              while upg:
                upg = input("Enter charachter: ")
                for keyterm in char:
                  if upg == char[keyterm] or upg == keyterm:
                    if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                      print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                      rsc['skillpts'] = rsc['skillpts'] - 1
                      rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                      lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
                    else:
                      print("Rescoures not present in inventory")
        if inp == 'library':
          print("Welcone to the Lab library, you can freely choose to read if you want")
          print("type an empty line to leave")
          book = ' '
          while book:
            print("There are 3 books here, emergence period, ww4 and soviets")
            book = input("What would you like to read? ")
            lib = False
            if book == "emergence period":
              txtsc(155, 168, Lib)
              lib = True
            if book == "ww4":
              txtsc(169, 187, Lib)
              lib = True
            if book == "soviets":
              txtsc(188, 205, Lib)
              lib = True
            if book not in v_loc and lib == True:
              print("+1 skillpts")
              rsc['skillpts'] = rsc['skillpts'] + 1
              v_loc.add(book)
    #=====Lab !#@% (Lab 5/Glitched lab)=====#
    if loc == ac_loc[gac_loc][11]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(46, 48, A4)
        if inp == 'document':
          print("It sshowś the %U# creatoR of SAC-26: Dr. I@˜ X*$#*-3")
        if inp == 'crystal' and 'A2LABCRYS' not in v_loc:
          print("Yÿou wwłkå towarddddS †hE crrystaˇ.~")
          ctld = 0
          while ctld <= 10:
            print(CT[ctld])
            time.sleep(3)
            ctld += 1
          while ctld <= 50:
            print(CT[11])
            time.sleep(0.3)
            ctld += 1
          corruptfight(1, 100000000000)
          time.sleep(0.3)
          while ctld <= 100:
            print(CT[13])
            time.sleep(0.3)
            ctld += 1
          v_loc.add('A2LABCRYS')
          txtsc(49, 52, A4)
          print(char['marksman'] + A4[53])
          time.sleep(tss)
          print(char['pilot'] + A4[54])
          time.sleep(tss)
          print(char['leader'] + A4[55])
          time.sleep(tss)
          print(A4[56])
          time.sleep(tss)
          print(char['programmer'] + A4[57])
        elif inp == 'crystal' and 'A2LABCRYS' in v_loc:
          print("CRITICAL ERROR: Object does not exist")
    #=====Bridge=====#
    if loc == ac_loc[gac_loc][12]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(63, 64, A4)
        if inp == 'terminal' and 'laba1birterm' not in v_loc:
          print("You log on to the terminal, a very old one from 2039")
          print("There's some documents on the ventrin system")
          print("+3 skillpts")
          rsc['skillpts'] += 3
          v_loc.add('laba1birterm')
        elif inp == 'terminal' and 'laba1birterm' in v_loc:
          print("It's very old")
        if inp == 'door':
          print("How will you get past this door?")
          labe = input("Enter code: ")
          if labe == '26934':
            if pickanum(17, 25):
              print("You open the doors to the lab and escape into space")
              rendev = False
              doneA2 = True
              inp = 'end'
              break
            else:
              print("You failed to open the door")
          else:
            print("Access denied")  
    #=====Vault door=====#
    if loc == ac_loc[gac_loc][13]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(60, 62, A4)
    #=====Test room=====#
    if loc == ac_loc[gac_loc][14]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(58, 59, A4)
        if inp == 'biohazard box':
          print("You look into the box, it's full of SAC-26 filled needles")
          print("There's something on top, it's a code")
          print("Code: 26934 added to inventory")
          invent.add('Code: 26934')
        if inp == 'table' and 'laba1testrtable' not in v_loc:
          print("+30 power cells")
          rsc['cells'] += 30
          v_loc.add('laba1testrtable')
        elif inp == 'table' and 'laba1testrtable' in v_loc:
          print("It's just a table")

#-----Act 1 & 2 Intermission-----#

#Allows player to get to ACT 3
fight = True

#==========Pre-ACT 3==========#

loc = 'space elevator'
prevloc = 'space elevator'
gac_loc = 'space elevator'

if loadsave == True:
  gac_loc, loc, prevloc = loadasave(loadsave)

A5 = open('lines/Space.txt').read().split('>')

if doneA2 and loc == 'space elevator':
  while fight:
    #Add dialouge pre-fight
    print(char['leader'] + A5[1])
    time.sleep(tss)
    print(char['pilot'] + A5[2])
    time.sleep(tss)
    print(char['leader'] + A5[3])
    time.sleep(tss)
    print(char['mechanic'] + A5[4])
    time.sleep(tss)
    print(char['marksman'] + A5[5])
    time.sleep(tss)
    print(char['programmer'] + A5[6])
    time.sleep(tss)

    countvloc = set()
    comcount = 0
    print('You only have time to choose 3 things here before the ambushers arrive')
    while comcount < 3:
      print("There is a shotgun for free, machine gun for 30,")
      print("an RPG for 50, 3 attack levels for 3 skillpts and 20 credits (enter attack)")
      inp = input("What will you choose? ")
      if inp == 'shotgun' and 'shotgun' not in invent:
        print("Bought shotgun for 0 credits")
        invent.add('shotgun')
        countvloc.add('shotgun')
      if inp == 'machine gun' and 'machine gun' not in invent:
        print("Bought machine gun for 30 credits")
        rsc['credits'] += -30
        invent.add('machine gun')
        countvloc.add('machine gun')
      if inp == 'rpg' and 'rpg' not in invent:
        print("Bought rpg for 30 credits")
        rsc['credits'] += -50
        invent.add('rpg')
        countvloc.add('rpg')
      if inp == 'attack' and 'attack' not in countvloc:
        print("Bought RPG for 30 credits")
        rsc['credits'] += -20
        rsc['skillpts'] += -3
        lvl['attack'] += 3
        countvloc.add('attack')
      if inp == 'cheat':
        cheat = input("What cheat will you use? ")
        cheatGame(cheat)
      #-----SAVE-----#
      if inp == 'save':
        print(savegame(gac_loc, loc, prevloc))
        varlistadd(rendev, var3, var4, var9, var10, doneA1, doneA2)
        slvar(True)
      #-----INVENTORY-----#
      if inp == "inventory":
        tot_invent = ''
        print("levels:")
        for keyterm in lvl:
          tot_invent += keyterm + ": " + str(lvl[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Rescources:")
        for keyterm in rsc:
          tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Items:")
        for item in invent:
          tot_invent += item + ", "
        print(tot_invent)
      print(len(countvloc))
      comcount = len(countvloc)
    txtsc(7, 7, A5)
    time.sleep(tss)
    if combatgame(10, 15):
      fight = False
    else:
      print("You failed to defeat the ambushers, starting from checkpoint...")

  #Add dialouge post-fight
  print("This will be your last checkpoint. No saving after this")
  print(char['marksman'] + A5[8])
  time.sleep(tss)
  print(char['mechanic'] + A5[9])
  time.sleep(tss)
  print(char['leader'] + A5[10])
  time.sleep(tss)
  print(char['leader'] + A5[11])
  time.sleep(tss)
  print(char['pilot'] + A5[12])
  time.sleep(tss)
  print(char['leader'] + A5[13])
  time.sleep(tss)
  print(char['marksman'] + A5[14])
  time.sleep(tss)
  print(char['programmer'] + A5[15])
  time.sleep(tss)
  print(char['leader'] + A5[16])
  time.sleep(tss)
  print(char['programmer'] + A5[17])
  time.sleep(tss)
  print(char['pilot'] + A5[18])
  time.sleep(tss)
  print(savegame('ending', 'ending', 'ending'))
  varlistadd(rendev, var3, var4, var6, var9, var10, doneA1, doneA2)
  slvar(True)
  
if doneA2 and loc == 'ending':
  print('lab keycard added to inventory')
  invent.add('lab keycard')
  print(char['programmer'] + A5[19])
  time.sleep(tss)
  txtsc(20, 23, A5)
  tut_loc = set({'lab', 'spiron city'})
  inp = input("Where would you like to go next? ")
  while inp not in tut_loc:
    inp = input("Where would you like to go next? ")
  if inp in tut_loc:
    gac_loc = inp
    loc = ac_loc[inp][0]
    prevloc = ac_loc[inp][0]
    print("You Have decided to go to: " + gac_loc)

#-----Pre-Act 3 Intermission-----#

#allows input in Act 3
var12 = False

#Determines which of the 4 endings and the no ending
ending = 'end'

#Starts a fight scene in the hall
hallfight = True

#tells if the bossfight is complete
doneA3 = False

#tells if all of spiron city is complete
doneSpiron = 0

#==========ACT 3==========#

while inp != 'end':
  #-----locloop-----#
  if var12:
    inp = input("What should you do? ")
  #print(inp, loc, var12, inp in ac_loc[gac_loc])
  if inp in ac_loc[gac_loc]:
    loc = inp
    print("Current location:", loc)
  if inp == 'cheat':
      cheat = input("What cheat will you use? ")
      cheatGame(cheat)
  var12 = True
  #-----previous location change-----#
  if varloc:
    print("That location is unreachable from here")
    loc = prevloc
    print("Current location:", loc)
  varloc = True
  #-----GPS-----#
  if 'gps' in invent:
    if inp == 'gps':
      print(gps(gac_loc, gps_loc[gac_loc][loc][0], gps_loc[gac_loc][loc][1]))
  #-----INVENTORY-----#
  if inp == "inventory":
        tot_invent = ''
        print("levels:")
        for keyterm in lvl:
         tot_invent += keyterm + ": " + str(lvl[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Rescources:")
        for keyterm in rsc:
         tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
        print(tot_invent)
        tot_invent = ''
        print("Items:")
        for item in invent:
         tot_invent += item + ", "
        print(tot_invent)
  #-----LAB ACT3-----#
  if gac_loc == "lab":
    #=====Vault door=====#
    if loc == ac_loc[gac_loc][0] and loc_check(gac_loc, loc, prevloc):
      varloc = False
      prevloc = loc
      if loc_list != loc:
        loc_list = loc
        txtsc(1, 3, A6) 
      if inp == 'lab keycard':
        print("You open the vault door to find an extenstion of the lab")
        inp = 'hall'
        prevloc = 'hall'
        var12 = False
    if loc == ac_loc[gac_loc][1] and loc_check(gac_loc, loc, prevloc):
      if hallfight:
        txtsc(6, 7, A6)
        if combatgame(5, 15):
          print("You beat the infected people")
          hallfight = False
          prevloc = ac_loc[gac_loc][1]
        else:
          print("You have to get out of the hall as you get kicked back to the vault door")
          loc_list = 'non'
          inp = 'vault door'
          prevloc = inp
          var12 = False
    #=====Hall=====#
    if loc == ac_loc[gac_loc][1] and loc_check(gac_loc, loc, prevloc):
      varloc = False
      prevloc = loc
      if loc_list != loc:
        loc_list = loc
        txtsc(4, 5, A6)
    #=====Quarters=====#
    if loc == ac_loc[gac_loc][2] and loc_check(gac_loc, loc, prevloc):
      varloc = False
      prevloc = loc
      if loc_list != loc:
        loc_list = loc
        txtsc(8, 8, A6)
      if inp == 'locker' and 'lab2quarterslock' not in v_loc:
        print("You walk up to the locker, there is an old computer inside")
        print("+5 tech")
        rsc['tech'] += 5
        v_loc.add('lab2quarterslock')
      elif inp == 'locker' and 'lab2quarterslock' in v_loc:
        print("The locker is empty")
      if inp == 'table' and 'lab2quarterstab' not in v_loc:
        print("The table is full of information on some lab experiments")
        print("+2 skillpts")
        rsc['skillpts'] += 2
        v_loc.add('lab2quarterstab')
      elif inp == 'table' and 'lab2quarterstab' in v_loc:
        print("The table's quite messy")
    #=====Common room=====#
    if loc == ac_loc[gac_loc][3] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(9, 9, A6)
      if inp == 'computer' and 'lab2comrcomp' not in v_loc:
        print("The computer is very old, from 2041. Why is all the technology here so old?")
        print("+15 tech")
        rsc['tech'] += 15
        v_loc.add('lab2comrcomp')
      elif inp == 'computer' and 'lab2comrcomp' in v_loc:
        print("Why is the technology here so old?")
      if inp == 'bookshelf':
        print("You thought there were books here?")
        print("Of course there isn't any. It's the most isolated place in the systems!")
    #=====Storeroom=====#
    if loc == ac_loc[gac_loc][4] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(10, 11, A6)
      if inp == 'box' and 'lab2stobox' not in v_loc:
        print("The box is full of wires")
        print("+10 tech")
        rsc['tech'] += 10
        v_loc.add('lab2stobox')
      elif inp == 'box' and 'lab2stobox' in v_loc:
        print("It's still pretty full")
      if inp == 'desk':
        #=====LAB ACT 3 DESK UPGRADE=====#
              upg = 'empty'
              print("Who would you like to level up?")
              print("Enter the charachter's role in crew")
              print("Enter a blank to leave - you cannot use end here")
              tot_invent = ''
              print("Rescources:")
              for keyterm in rsc:
                tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
              print(tot_invent)
              while upg:
                upg = input("Enter charachter: ")
                for keyterm in char:
                  if upg == char[keyterm] or upg == keyterm:
                    if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                      print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                      rsc['skillpts'] = rsc['skillpts'] - 1
                      rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                      lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
                    else:
                      print("Rescoures not present in inventory")
    #--Lab 6 roadblock--#
    if loc == ac_loc[gac_loc][5]:
      if prevloc == ac_loc[gac_loc][1] or loc_check(gac_loc, loc, prevloc):
        if 'lab 6' not in v_loc:
          if doneA3:
            if 'lab keycard 2' in invent:
              print("The door opens")
              v_loc.add('lab 6')
            else:
              print("Requires lab keycard 2")
              print("Oh no. The door is still shut.")
              txtsc(13, 15, A6)
              ending = 'infection'
              inp = 'end'
              loc = 'end'
          else:
            print("The door is jammed shut")
            loc = prevloc
    #=====Lab 6=====#
    if loc == ac_loc[gac_loc][5]:
      if prevloc == ac_loc[gac_loc][1] or prevloc == ac_loc[gac_loc][5]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(12, 12, A6)
        if inp == 'vile':
          print("You open the vile and take a whiff. You immediately feel relaxed")
          time.sleep(tss)
          print("as the crystals growing out of your body secede. You found the cure.")
          time.sleep(tss)
          ending = 'sac'
          inp = 'end'
    #--Test chamber roadblock--#
    if loc == ac_loc[gac_loc][6]:
      if prevloc == ac_loc[gac_loc][1] or loc_check(gac_loc, loc, prevloc):
        if lvl[lvlacss['programmer']] <= 11:
          print("Requires a intellect level of 11")
          loc = prevloc
    #=====Test Chamber=====#
    if loc == ac_loc[gac_loc][6]:
      print(loc, prevloc, ac_loc[gac_loc][1])
      if prevloc == ac_loc[gac_loc][1] or prevloc == ac_loc[gac_loc][6]:
        prevloc = loc
        varloc = False
        if doneA3 == False:
          loc_list = loc
          txtsc(16, 18, A6)
          ctld = 10
          print('')
          while ctld <= 20:
            print(CT[11])
            time.sleep(0)
            ctld += 1
          if bossfight(gac_loc):
            doneA3 = True
            print("You defeated the beast, you leave to the hall")
            loc = 'hall'
            prevloc = 'hall'
            inp = 'hall'
            var12 = False
            print(A6[19])
            time.sleep(tss)
            print(char['leader'] + A6[20])
            time.sleep(tss)
            print(char['programmer'] + A6[21])
            time.sleep(tss)
            print(char['pilot'] + A6[22])
            time.sleep(tss)
            print(char['pilot'] + A6[23])
            time.sleep(tss)
            print(char['programmer'] + A6[24])
            time.sleep(tss)
            print(char['programmer'] + A6[25])
            time.sleep(tss)
            print(char['mechanic'] + A6[26])
            time.sleep(tss)
          else:
            var12 = False
            print("You failed to defeat the beast")
        elif doneA3:
          print("The Crystals are laid across the floor in a random order")
  #-----SPIRON CITY-----#
  if gac_loc == "spiron city":
    #=====Mt. Serins=====#
    if loc == ac_loc[gac_loc][0] and loc_check(gac_loc, loc, prevloc):
      prevloc = loc
      varloc = False
      if loc_list != loc:
        loc_list = loc
        txtsc(1, 3, A7)
      if inp == 'pile of rocks' and 'spironserinsbarrel' not in v_loc:
        print("+20 material, +1 skillpts")
        rsc['material'] += 20
        rsc['skillpts'] += 20
        v_loc.add('spironserinsbarrel')
      if inp == 'cave':
        print("Stop walking inside a living creature! The mountain is alive you know?")
    #=====Outpost=====#
    if loc == ac_loc[gac_loc][1]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][3]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(4, 7, A7)
        if inp == 'flagpost' and 'flag' not in invent:
          print("It's just an unused flagpost")
        elif inp == 'flagpost' and 'flag' in invent:
          if 'stun gun' not in invent:
            print("You hoist the flag,")
            txtsc(38, 39, A7)
            print("stun gun added to inventory")
            invent.add('stun gun')
            invent.remove('flag')
        if inp == 'desk':
          #=====SPIRON CITY DESK UPGRADE=====#
              upg = 'empty'
              print("Who would you like to level up?")
              print("Enter the charachter's role in crew")
              print("Enter a blank to leave - you cannot use end here")
              tot_invent = ''
              print("Rescources:")
              for keyterm in rsc:
                tot_invent += keyterm + ": " + str(rsc[keyterm]) + ", "
              print(tot_invent)
              while upg:
                upg = input("Enter charachter: ")
                for keyterm in char:
                  if upg == char[keyterm] or upg == keyterm:
                    if rsc['skillpts'] > 0 and rsc[rscass[keyterm]] >= 10:
                      print("Upgraded", upg, "for 1 skillpt and 10", rscass[keyterm])
                      rsc['skillpts'] = rsc['skillpts'] - 1
                      rsc[rscass[keyterm]] = rsc[rscass[keyterm]] - 10
                      lvl[lvlacss[keyterm]] = lvl[lvlacss[keyterm]] + 1
                    else:
                      print("Rescoures not present in inventory")
    #--City Entrance roadblock--#
    if loc == ac_loc[gac_loc][3]:
      if prevloc == ac_loc[gac_loc][1] and loc not in v_loc:
        print("There is an airlock here, maybe it could be fixed")
        if lvl[lvlacss['mechanic']] >= 11:
          if battleship(9):
            print("You fixed the airlock")
            v_loc.add(loc)
          else:
            print("The airlock is still broken")
            loc = prevloc
        else:
          print("Requires tech. knowledge of 11 to fix the airlock")
          loc = prevloc
    #=====City Entrance=====#
    if loc == ac_loc[gac_loc][3]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][1]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(8, 8, A7)
        if inp == 'barrel' and 'spironcitenbarrel' not  in v_loc:
          print("+10 gas")
          rsc['gas'] += 10
          v_loc.add('spironcitenbarrel')
        elif inp == 'barrel' and 'spironcitenbarrel' in v_loc:
          print("The barrel is empty")
        if inp == 'prison':
          prison = ' '
          print("Enter a blank to leave.")
          while prison:
            print("Welcome to the Spiron city prison.")
            print("We have here a cell and a cafeteria")
            prison = input("Where would you like to visit? ")
            if prison == 'cell':
              print(char['leader'] + ": This cell here, is where we put the creator of SAC-26 once i'm done with him.")
            if prison == 'cafeteria' and 'spcitenprcaf' not in v_loc:
              print("You walk in and talk to some of the guards.")
              print("+1 lvl charisma")
              lvl['charisma'] += 1
              v_loc.add('spcitenprcaf')
            elif prison == 'cafeteria' and 'spcitenprcaf' in v_loc:
              print("The food is mediocre")
    #=====Ventrix=====#
    if loc == ac_loc[gac_loc][2]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(9, 10, A7)
        if inp == 'man' and lvl['charisma'] >= 9:
          print("man: You need a level of at least 11 in every person to beat the game")
        elif inp == 'man' and lvl['charisma'] <= 9:
          print("Requires a charisma level of 9")
        if inp == 'car' and 'spironventrixcar' not in v_loc:
          v_loc.add('spironventrixcar')
          print("+15 gas")
          rsc['gas'] += 15
        elif inp == 'car' and 'spironventrixcar' in v_loc:
          print("It's a car")
    #=====Sector 3=====#
    if loc == ac_loc[gac_loc][4]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(11, 12, A7)
        if inp == 'office' and 'spironsector3office' not in v_loc:
          print("You walk into the office building and find some paperwork there")
          print("+2 skillpts")
          rsc['skillpts'] += 2
        elif inp == 'office' and 'spironsector3office' in v_loc:
          print("It's just an office block")
        if inp == 'store':
          store = ' '
          print("Welcome to the sector 3 store. Enter a blank to leave.")
          while store:
            print("We have a rpg for 30, a barrel of gas for 5")
            print("and a gps for 10. Enter a blank to leave")
            store = input("What do you want to buy? ")
            if store == 'rpg' and 'rpg' not in invent:
              if rsc['credits'] >= 30:
                print("Bought rpg for 30")
                invent.add('rpg')
                rsc['credits'] += -30
              else:
                print("Not enough credits")
            elif store == 'rpg' and 'rpg' in invent:
              print("rpg already in inventory")
            if store == 'barrel' and 'gasatspir' not in v_loc:
              if rsc['credits'] >= 5:
                print("Bought 20 gas for 5")
                rsc['gas'] += 5
                rsc['credits'] += -5
                v_loc.add('gasatspir')
              else:
                print("Not enough credits")
            if store == 'gps' and 'gps' not in invent:
              if rsc['credits'] >= 10:
                print("Bought gps for 10")
                invent.add('gps')
                rsc['credits'] += -10
                print("By entering 'gps', you can get a position on where you are")
              else:
                print("Not enough credits")
            elif store == 'gps' and 'gps' in invent:
              print("Gps already in inventory")
    #=====Sector 4=====#
    if loc == ac_loc[gac_loc][5]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][10]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(13, 16, A7)
        if inp == 'clothing shop' and 'sec4clothshop' not in v_loc:
          print("You walk into the clothing shop. There is alot of material here")
          v_loc.add('sec4clothshop')
          rsc['material'] += 5
          print("+5 material")
        elif inp == 'clothing shop' and 'sec4clothshop' in v_loc:
          print("It's full of clothes")
        if inp == 'casino':
          print("welcome to the casino,")
          if pickanum(10, 25):
            print("+30 credits")
            rsc['credits'] += 30
          else:
            print("Too bad.")
    #=====Industrial=====#
    if loc == ac_loc[gac_loc][6]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][12]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(17, 19, A7)
        if inp == "factory" and 'industrialfactory' not in v_loc:
          print("You walk into the factory, there is a case full of ammo and material")
          print("+20 ammo, +10 material")
          v_loc.add('industrialfactory')
          rsc['ammo'] += 20
          rsc['material'] += 10
        elif inp == "factory" and 'industrialfactory' in v_loc:
          print("The factory floor is full of robots")
    #=====Sector 6=====#
    if loc == ac_loc[gac_loc][7]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(20, 21, A7)
        if inp == 'theme park' and 'sec6themepar' not in v_loc:
          print("You walk into the theme park where")
          print("there is a pile of cells used for the rides")
          print("+30 cells")
          rsc['cells'] += 30
          v_loc.add('sec6themepar')
        elif inp == 'theme park' and 'sec6themepar' in v_loc:
          print("the roller coasters are loud")
        if inp == 'stadium' and 'sec6stadium' not in v_loc:
          print("You walk to the seating area of the  stadium.")
          print("You learn alot about the sport ny watching.")
          print("+3 skillpts")
          v_loc.add('sec6stadium')
          rsc['skillpts'] += 3
        elif inp == 'stadium' and 'sec6stadium' in v_loc:
          print("This sport is a very interesting one")
    #=====Central Spiron=====#
    if loc == ac_loc[gac_loc][8]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][11]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(22, 24, A7)
        if inp == "capitol" and 'centspircapitol' not in v_loc:
          print("You walk into the capitol building as")
          print("you find some information on the design of it")
          print("+2 skillpts, +10 credits")
          rsc['skillpts'] += 2
          rsc['credits'] += 10
          v_loc.add('centspircapitol')
        elif inp == "capitol" and 'centspircapitol' in v_loc:
          print("The bulding is a very nice design")
        if inp == 'statue':
          txtsc(25, 27, A7)
    #=====Landing bay=====#
    if loc == ac_loc[gac_loc][9]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(28, 29, A7)
        if inp == 'elevator':
          print("You know what kind of elevator it is, don't step into it")
        if inp == 'pile' and 'landbaypilegold' not in v_loc:
          print("You walk up to the pile of gold. It looks shiny and expensive.")
          print("but you know that gold is still worthless")
          print("But you still would like to see it")
          print("+25 credits")
          rsc['credits'] += 25
          v_loc.add('landbaypilegold')
        elif inp == 'pile' and 'landbaypilegold' in v_loc:
          print("It's a pile of gold")
        if inp == 'desk' and 'landbaydesk' not in v_loc:
          print("The desk has a lot of ammunition on it with some information too.")
          print("+1 skillpts, +10 ammo")
          rsc['skillpts'] += 1
          rsc['ammo'] += 10
          v_loc.add('landbaydesk')
        elif inp == 'desk' and 'landbaydesk' in v_loc:
          print("It's a desk with paperwork on it")
    #--Zoo roadblock--#
    if loc == ac_loc[gac_loc][10]:
      if prevloc == ac_loc[gac_loc][5] and loc not in v_loc:
        print("You walk up to the person at the zoo entrance.")
        print("He speaks to you in spironian, Can't enter through without a ticket")
        if lvl['charisma'] >= 11:
          if anagram(7, 8):
            print("The man lets you through")
            v_loc.add(loc)
          else:
            print("You weren't let in")
            loc = prevloc
        else:
          print("Requires a charisma level of 11")
          loc = prevloc
    #=====Zoo=====#
    if loc == ac_loc[gac_loc][10]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][5]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(30, 31, A7)
        if inp == 'exhibit':
          print("The exhibit is full of lions, snakes and birds.")
        if inp == 'pile of rocks' and 'zoopor' not in v_loc:
          print("You walk up to the pile, and pick up one of them.")
          print("The park ranger runs over to you, 'don't touch the animals, Sir.'")
          print("Here, have this rock, it's not alive")
          doneSpiron += 1
          v_loc.add('zoopor')
          print("rock added to inventory")
          invent.add('rock')
        elif inp == 'pile of rocks' and 'zoopor' not in v_loc:
          print("Does the rock have sentience if it is living?")
        if inp == 'library':
          print("Welcone to the Spiron City library, you can freely choose to read if you want")
          print("type an empty line to leave")
          book = ' '
          while book:
            print("There are 3 books here, 2nd great depression, technological revolution and modern dark ages")
            book = input("What would you like to read? ")
            lib = False
            if book == "2nd great depression":
              txtsc(206, 222, Lib)
              lib = True
            if book == "technological revolution":
              txtsc(223, 237, Lib)
              lib = True
            if book == "modern dark ages":
              txtsc(238, 240, Lib)
              lib = True
            if book not in v_loc and lib == True:
              print("+1 skillpts")
              rsc['skillpts'] = rsc['skillpts'] + 1
              v_loc.add(book)
    invent.add('rock')
    #--Larina roadblock--#
    if loc == ac_loc[gac_loc][11]:
      if prevloc == ac_loc[gac_loc][8] and loc not in v_loc:
        print("You need to be a certified pilot and have some samples to enter")
        if lvl[lvlacss['pilot']] >= 11:
          doneSpiron = 1
          if 'rock' in invent and doneSpiron >= 1:
            print("You provide your rock as a sample")
            v_loc.add(loc)
          else:
            print("You don't have a sample")
            loc = prevloc
        else:
          print("Requires a piloting level of 11 to enter")
          loc = prevloc
    #=====Larina=====#
    if loc == ac_loc[gac_loc][11]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][8]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(32, 33, A7)
        if inp == 'office building' and 'fightatofflar' not in v_loc:
          txtsc(34, 35, A7)
          if combatgame(1, 39):
            print("You beat the guard")
            doneSpiron += 1
            v_loc.add('fightatofflar')
          else:
            print("The guard beats you")
        elif inp == 'office building' and 'fightatofflar' in v_loc:
          print("The office building is locked")
        if inp == 'lab' and 'larlab' not in v_loc:
          print("The lab as a bunch of documents inside")
          rsc['skillpts'] += 3
          print("+3 skillpts")
          v_loc.add('larlab')
        elif inp == 'lab' and 'larlab' in v_loc:
          print("The lab is empty")
    #--Junkyard roadblock--#
    if loc == ac_loc[gac_loc][12]:
      if prevloc == ac_loc[gac_loc][6] and loc not in v_loc:
        print("Thug: Hey! Don't enter here with out getting through us")
        if lvl[lvlacss['marksman']] >= 11:
          doneSpiron = 2
          v_loc.add('fightatofflar')
          if 'fightatofflar' in v_loc and doneSpiron >= 2:
            print("Thug: Wait a second!, you're that guy who beat up our freind at larina!")
            if combatgame(5, 25):
              print('The thugs let you through')
              v_loc.add(loc)
            else:
              print('The thugs beat you up')
              loc = prevloc
          else:
            print("Thug: Get outta here!")
            loc = prevloc
        else:
          print("Requires a attack level of 11 to enter")
          loc = prevloc
    #=====Junkyard=====#
    if loc == ac_loc[gac_loc][12]:
      if loc_check(gac_loc, loc, prevloc) or prevloc == ac_loc[gac_loc][6]:
        prevloc = loc
        varloc = False
        if loc_list != loc:
          loc_list = loc
          txtsc(36, 37, A7)
        if inp == 'flag' and 'flag' not in invent:
          print("Flag added to inventory")
          invent.add('flag')
        if inp == 'pile of trash':
          if pickanum(15, 30):
            print("You won")
            if lvl['attack'] >= 25:
              print("attack leveled up by 1")
              lvl['attack'] += 1
    #=====Warehouse=====#
    if loc == ac_loc[gac_loc][13]:
      if loc_check(gac_loc, loc, prevloc):
        prevloc = loc
        varloc = False
        print(char['pilot'] + ": This is it. He should be inside.")
        weapon = ' '
        while weapon != 'pistol':
          if 'stun gun' in invent:
            print("We have 2 options: Use a pistol or a stun gun")
          else:
            print("We have 1 option: Use a pistol")
          weapon = input("What is your weapon of choice?")
          if weapon == 'stun gun' and 'stun gun' in invent:
            break
        txtsc(40, 41, A7)
        print(char['leader'] + A7[42])
        print(A7[43])
        while doneA3 == False:
          if bossfight(gac_loc):
            txtsc(44, 66, A7)
            if weapon == 'stun gun':
              ending = 'good'
              txtsce(70, 70, A7, 2.5)
            elif weapon == 'pistol':
              ending = 'bad'
              txtsce(67, 69, A7, 2.5)
            doneA3 = True
            inp = 'end'
            

#-----Act 3 Intermission-----#

if ending != 'end':
  txtsce(71, 73, A7, 2.5)
  time.sleep(2)
print('')

End = open('lines/endings.txt').read().split('>')
Credits = open('lines/credits.txt').read().split('>')

#ending = 'bad'

if ending not in EndCountvar:
  EndCountvar.add(ending)
  EndCount = open('Save/EndingCount.txt', 'w')
  for term in EndCountvar:
    print(term, file=EndCount)
  print()
  EndCount.close()

#==========ENDING==========#

if ending == 'bad':
  txtsce(2, 17, End, 2)
elif ending == 'good':
  txtsce(19, 32, End, 2)
elif ending == 'infection':
  txtsce(34, 47, End, 2)
elif ending == 'sac':
  txtsce(49, 62, End, 2)

if ending != 'end':
  txtsce(0, 10, Credits, 4)
  print("Congratulations! You beat the game! \n")
  time.sleep(2.5)
  print("You got the", ending, "Ending. You have (" + str(len(EndCountvar)-2) + "/4) endings \n")

if len(EndCountvar)-2 >= 4:
  time.sleep(2.5)
  print("You got all endings!")
  time.sleep(2.5)
  print("Here's a cool fact: there are 69 locations in this game!")
  time.sleep(2.5)
  print("So ... This game is techically one big 69 joke :)")

#Last line - Huzzah!
print("Ending game...")