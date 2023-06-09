#!/bin/python3
from datetime import *
from random import randint
from time import sleep
  
inventory = []
automaticPotion = 0
skipLevel = 0
play = 1
level = 1
global diamond
diamond = 0
def openShop():
        global diamond
        global inventory
        global level
        print('Diamonds:', diamond)
        print('If you want to exit the shop type QUIT.')
        print('What would you like to buy:')
        print('Automatic Potion . . . . . . 1 diamond')
        print('Skip Level. . . . . 3 diamonds')
        buy = input('What would you like to buy:')
        if buy.lower() == 'automatic potion' and diamond > 0:
          global automaticPotion
          automaticPotion = 1
          diamond = diamond - 1
          print('Your transaction is complete!')
          level1()
        elif buy.lower() == 'skip level' and diamond > 2:
          global skipLevel
          skipLevel = 1
          diamond = diamond - 3
          print('Your transaction is complete!')
          level1()
        elif buy.lower() == 'quit':
          if level == 1:
            level1()
          elif level == 2:
            level2()
        elif diamond > 0:
          print('Sorry I dont understand, repeat that please!')
          openShop()
        elif diamond == 0:
          print('Im sorry, you dont have any diamonds.')
          level1()
def level2():
  def down():
    global diamond
    global inventory
    global level
    play = 1
    health = 10

    while play == 1:
      def showInstructions():
        print('''
        RPG Game
        ========
        You are on Ground Floor
        ========
        Commands:
          go [direction]
          get [item]
          stop (stops game)
        ''')
        
      def showStatus():
        print('---------------------------')
        print('You are in the ' + currentRoom)
        print('Inventory : ' + str(inventory))
        print('Health:', health)
        print('Diamonds:', diamond)
        if "item" in rooms[currentRoom]:
          print('You see a ' + rooms[currentRoom]['item'])
          print("---------------------------")
        
      rooms = {
        
                  'CellOne' : { 
                        'east' : 'EmptyRoom'
                  },
                    
                  'EmptyRoom' : {
                        'west' : 'CellOne',
                        'south' : 'CellTwo',
                        'east' : 'CellThree',
                        'north' : 'Stairs'
                  },
                    
                  'CellTwo' : {
                        'north' : 'EmptyRoom',
                        'item' : 'steak'
                  },
                    
                  'CellThree' : {
                        'west' : 'EmptyRoom',
                        'item' : 'diamond'
                  },
                    
                  'Stairs' : { 
                          'item' : 'diamond'
                  }
                }
        
      currentRoom = 'CellOne'
      showInstructions()
        
      while True:
        
        showStatus()
        move = ''
        while move == '':  
          move = input('>')
            
        move = move.lower().split()
        
        if move[0] == 'go':
          if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
          else:
              print('You can\'t go that way!')
        if move[0] == 'get' :
          if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print(move[1] + ' got!')
            if move[1] == 'diamond' and move[1] in rooms[currentRoom]['item']:
              diamond = diamond + 1
            else:
              inventory += [move[1]]
            del rooms[currentRoom]['item']
          else:
            print('Can\'t get ' + move[1] + '!')
          if move[0] == 'eat':
            if move[1] == 'steak' and 'steak' in inventory:
              if health > 5 and health < 10:
                health = 10
                print('eaten steak')
              if health < 5:
                health = health + 5
                print('eatean steak')
            else:
              print('can eat', move[1])
                  
          if currentRoom == 'Stairs':
            up()
        elif move[0] == 'shop':
          openShop()
  def up():
    global diamond
    global inventory
    global level
    automaticPotion = 0
    play = 1
    health = 10
    while play == 1:
      def showInstructions():
        print('''
      RPG Game
      ========
      You are on First Floor
      ========
      Commands:
        go [direction]
        get [item]
        eat [item]
        hide [object] -- you hide under it
        shop -- you open the shop
      ''')
        
      def showStatus():
        print('---------------------------')
        print('You are in the ' + currentRoom)
        print('Inventory : ' + str(inventory))
        if "item" in rooms[currentRoom]:
          print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")
        
      rooms = {
        
                  'Bedroom1' : { 
                        'east' : 'Bedroom2',
                        'south' : 'Balcony',
                        'item' : 'monster'
                  },
                    
                  'Bedroom2' : {
                        'west' : 'Bedroom1',
                        'north' : 'Stairs',
                        'east' : 'Study'
                  },
                    
                  'Stairs' : {
                    'item' : 'letter'
  
                  },
                    
                  'Balcony' : {
                        'north' : 'Bedroom1',
                  }
                }
        
      currentRoom = 'Bedroom2'
      showInstructions()
        
      while True:
        
        showStatus()
        move = ''
        while move == '':  
          move = input('>')
            
          move = move.lower().split()
        
        if move[0] == 'go':
          if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
          else:
            print('You can\'t go that way!')
        if move[0] == 'get' :
          if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print(move[1] + ' got!')
            if move[1] == 'diamond' and move[1] in rooms[currentRoom]['item']:
              diamond = diamond + 1
            else:
              inventory += [move[1]]
            del rooms[currentRoom]['item']
          else:
             print('Can\'t get ' + move[1] + '!')
          if move[0] == 'eat':
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
              if move[1] == 'steak':
                if health > 5 and health < 10:
                  health = 10
                  print('eaten steak')
                if health < 5:
                  health = health + 5
                  print('eatean steak')
              else:
                print('cant eat', move[1])
                
          if currentRoom == 'Stairs':
            down()
        elif move[0] == 'shop':
          openShop()
  down()
def level1():
  global diamond
  global inventory
  global automaticPotion
  global monHealth
  health = 10
  play = 1
  
  while play == 1:
    ow = input()
    if ow == 'start':
      def showInstructions():
        print('''
      RPG Game
      ========
      Commands:
        go [direction]
        get [item]
        shop -- you open the shop
      ''')
      
      def showStatus():
        global inventory
        global diamond
        print('---------------------------')
        print('You are in the ' + currentRoom)
        print('Health:', health)
        print('Diamonds:', diamond)
        print('Inventory : ', str(inventory))
        if "item" in rooms[currentRoom]:
          print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")
      
      rooms = {
      
                  'Hall' : { 
                        'north' : 'Bedroom',
                        'west' : 'Kitchen',
                        'item' : 'potion'
                  },
                  
                  'Bedroom' : {
                        'south' : 'Hall',
                        'item' : 'monster'
                  },
                  
                  'Kitchen' : {
                        'east' : 'Hall',
                        'item' : 'diamond'
                  }
               }
      
      currentRoom = 'Hall'
      showInstructions()
      
      while True:
      
        showStatus()
      
        move = ''
        while move == '':  
          move = input('>')
          
        move = move.lower().split()
        if move[0] == 'shop':
          openShop()
        if move[0] == 'go':
          if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
          else:
              print('You can\'t go that way!')
      
        if move[0] == 'get' :
          if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            print(move[1] + ' got!')
            if move[1] == 'diamond' and move[1] in rooms[currentRoom]['item']:
              diamond = diamond + 1
            else:
              inventory += [move[1]]
            del rooms[currentRoom]['item']
            
          else:
            print('Can\'t get ' + move[1] + '!')
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
          if automaticPotion == 1:
            monsterHealth = 100
            print('You weakened the monster with your potion!')
            print('Type kick or punch to decrease its health!                      ')
            print('Monster Health: ' + monsterHealth)
            while monHealth > 0:
              fight = input()
              if fight == 'kick':
                monsterHealth -= 25
                print('Monster Health: ' + monsterHealth)
              elif fight == 'punch':
                monsterHealth -= 10
                print('Monster Health: ' + monsterHealth)
            print('You defeated the monster with your potion! You win!')
            print('You earned a DIAMOND!')
            diamond = diamond + 1
            level2()
          if automaticPotion == 0:
            if 'potion' in inventory:
              monsterHealth = 100
              print('You weakened the monster with your potion!')
              print('You see a monster you need to fight it!!')
              print('3')
              sleep(1)
              print('2')
              sleep(1)
              print('1')
              print('Type kick or punch to decrease its health!!')
              while monsterHealth > 0:
                fight = input()
                if fight == 'kick':
                  monsterHealth -= 25
                  print('Monster Health: ', monsterHealth)
                elif fight == 'punch':
                  monsterHealth -= 10
                  print('Monster Health: ', monsterHealth)
              print('You defeated the monster with your potion! You win!')
              print('You earned a DIAMOND!')
              diamond = diamond + 1
              level2()
            else:
              monsterHealth = 100
              def updateMonHealth():
                global monsterHealth
                print('Monster Health: ', monsterHealth)
              print('You see a monster you need to fight it!!')
              print('3')
              sleep(1)
              print('2')
              sleep(1)
              print('1')
              print('Type kick or punch to decrease its health!!')
              while monHealth > 0:
                fight = input()
                if fight == 'kick':
                  monsterHealth -= 25
                  print('Monster Health: ' + monsterHealth)
                elif fight == 'punch':
                  monsterHealth -= 10
                  print('Monster Health: ' + monsterHealth)
              print('You defeated the monster with your potion! You win!')
              print('You earned a DIAMOND!')
              diamond = diamond + 1
              level2()
    elif ow == 'shop':
      openShop()
        
    print('''
    ----------------------
    Type 'next' for the next level
    Type 'again' to replay
    Type 'shop' to open the shop
    ----------------------
    ''')
    playagain = input()
    if playagain == 'again':
      play = 1
      inventory = []
    if playagain == 'next':
      play = 0
      level2()
    if playagain == 'shop':
      openShop()
def startScreen():
  print('''
  
              |\  /|         |\  /|
              | \/ |         | \/ |
              |    | AZE     |    | ASTER
  
  -------------------------
  Type 'start' to start
  Type 'shop' to open the shop 
  -------------------------
  As this is your first time playing you get a free DIAMOND
  -------------------------
  ''')
diamond = diamond + 1
startScreen()
level1()
