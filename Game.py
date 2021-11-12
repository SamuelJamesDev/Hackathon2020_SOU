# Samuel James
# Hackathon 2020
# Text Adventure About Mt. Shasta
# 04/04/2020 

## Get all appropriate imports for use
from random import randint
from IPython.display import clear_output
import time
import sys


# dictionaries for choices, enemies, and speech responses
dict1 = {1:'attack', 2:'speak', 3:'run'}
dict2 = ['bat', 'skull', 'Lemurian', 'doggo', 'mouse']
dict3 = ['What could you possibly want?', '*barkbark* *tippytaps* (he seems harmless)','*angry squeaks*(he seems harmless)']

#player class
class player:

  def init(self, name):
    self.hp = 100
    #good end/bad end variable
    self.victory = False
    self.name = name
  
  #player attack function
  def attack(self, enemy):
    max_dmg = 15
    min_dmg = 5
    dmg = randint(min_dmg, max_dmg)
    enemy.hp -= dmg 
    print('you attacked: ', enemy.name, ' and did', dmg, ' Damage!')
    time.sleep(1)
    if enemy.hp < 1:
      print('You defeated the:',enemy.name, '!!')  
      print('Current hp: ', self.hp)
    else:
      enemy.Face(enemy.name, enemy)
      enemy.Attack(enemy, player)

#enemy class
class enemy:
  def _init_(self, num):
    talk = 0
    speak = False
    face = ''
    if num == 0:
      self.dmg = 10
      self.speak = False
      self.hp = 10              
      self.name = dict2[0]
      self.run = False
      self.Face(self.name, self)
    elif num == 1:
      self.dmg = 15
      self.speak = False
      self.hp = 40
      self.name = dict2[1]
      self.run = True
      self.Face(self.name, self)
    elif num == 2:
      self.dmg = 10
      self.speak = True
      self.hp = 100
      self.name = dict2[2]
      self.run = False
      self.Face(self.name, self)
    elif num == 3:
      self.dmg = 1
      self.talk = 1
      self.speak = True
      self.hp = 10
      self.name = dict2[3]
      self.run = False
      self.Face(self.name, self)
    elif num == 4:
      self.dmg = 1
      self.talk = 2
      self.speak = True
      self.hp = 10
      self.name = dict2[4]
      self.run = False
      self.Face(self.name, self)
    print(self.name ,'Appeared! ')
  
  #enemy attack function
  def Attack(enemy, player):
    max_dmg = enemy.dmg
    player.hp -= max_dmg
    print('they attack: ', player.name, ' for', max_dmg , ' Damage!')
    if player.hp < 1:
      print('You were defeated by the:',enemy.name, '!!')
      YouDied()
    else:
      player.attack(player, enemy)
  
  #function to display in ascii enemies
  def Face(name, enemy):
    if name == 'bat':
      print('*********************************************************************************')
      print('___*hiss*_______________--____^_________^__--______*hissssss*____________________')
      print('______________________--_-______O_____O____-_--_______________hp:[',enemy.hp,']__')
      print('____________________--____-________X______-____--_______________name: bat________')
      print('__________________--____________\/___\/__________--_____________attack: scratch__')
      print('________________--_________________________________--____________________________')
      print('*********************************************************************************')

    elif name == 'skull':
      print('*********************************************************************************')
      print('_____________________:::!~!!!!!:.________________________________________________')
      print('__________________.xUHWH!! !!?M88WHX:.___________________________________________')
      print('________________.X*#M@$!!  !X!M$$$$$$WWx:._______________________________________')
      print('_______________:!!!!!!?H! :!$!$$$$$$$$$$8X:______________hp:[',enemy.hp,']_______')
      print('_______________!!~  ~:~!! :~!$!#$$$$$$$$$$8X:____________name: skull_____________')
      print('______________:!~::!H!<   ~.U$X!?R$$$$$$$$MM!____________attack: bite____________')
      print('______________~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!____________________________________')
      print('_______________!:~~~ .:!M"T#$$$$WX??#MRRMMM!_____________________________________')
      print('_______________~?WuxiW*`____`"#$$$$8!!!!??!!!____________________________________')
      print('_____________:X- M$$$$________`"T#$T~!8$WUXU~____________________________________')
      print('_____________:%`__~#$$$m:________~!~ ?$$$$$$_____________________________________')
      print('___________:!`.-   ~T$$$$8xx.  .xWW- ~""##*"_____________________________________')
      print('.....   -~~:<` !______~?T#$$@@W@*?$$_______/`____________________________________')
      print('SLJ@@M!!! .!~~ !!_____.:XUW$W!~ `"~:_____:_______________________________________')
      print('#"~~`.:x%`!!  !H:___!WM$$$$Ti.: .!WUn+!`______________*screeeeee*________________')
      print(':::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~__________________________________________')
      print('.~~   :X@!.-~___?@WTWo("*$$$W$TH$! `_____________________________________________')
      print('Wi.~!X$?!-~____:_?$$$B$Wu("**$RM!________________________________________________')
      print('$R@i.~~ !_____:___~$$$$$B$$en:``_________________________________________________')
      print('?SLJ@Wx.~____:_____~"##*$$$$M~___________________________________________________')
      print('*********************************************************************************')

    elif name == 'Lemurian':
      print('*********************************************************************************')
      print('_____________________________________///(())(____________________________________')
      print('__________________________________(((__   __ \\_____________hp:[',enemy.hp,']____')
      print('________________________________))))-O-`."-O- ((___________name: Lemurian________')
      print('__________________________________((\ / |   /))__________________________________')
      print('__________________________________|)|  ~-~  |(|__________________________________')
      print('___________________________________|\ -x-x- /|___________________________________')
      print('___________________________________|_~-___-~_|___________________________________')
      print('___________________________________; ~~~~;~~_____________________________________')

    elif name == 'doggo':                  
      print('***************************************************************************')
      print('____________----((((((((((((((((())))))))))))))))( )0 `-,______________________')
      print('_________---____(((((((((((((()))))))))))))))))))/''"`____hp:[',enemy.hp,']__')
      print('______--________//\\                      //\\________name: Long Boi_______')
      print('________________"" ""_____________________"" ""____________________________')
      print('***************************************************************************')

    elif name == 'mouse':
      print('***************************************************************************')
      print('______________(  )(  )------#__________hp:[',enemy.hp,']___________________')
      print('_______________C___C________#______________________________________________')
      print('_______________\\_/--------#------q_________name: Mouse____________________')
      print('_________________0__TT_____TT______________________________________________')
      print('***************************************************************************')

#death screen function
def YouDied():
  print('________________...____________Y O U______________________')
  print('_____________;::::;___________D I E D_____________________')
  print('___________;::::; :;______________________________________')
  print('________;:::::_____:;_____________________________________')
  print('_______;:::::;_______;____________________________________')
  print('______,:::::__X____X_;__________TT)/______________________')
  print('______::::::;________;___________OOOOO\\__________________')
  print('_____;:::::;_______;____________OOOOOOOOVV________________')
  print('____,;::::::;_____;____________/ OOOOOOOVvV_______________')
  print('____;:::::::::_. ,,,;.________/__/_VOOOOOV________________')
  print('__..;:::::::::::::::::;,_____/__/_____VOOOV_______________')
  print(' ,::::::;::::::;;;;::::;,___/__/_______VOOV_______________')
  print(';`::::::  ::::::;;;::::: ,T/__/_________VOOV______________')
  print(':`:::::::  ::::::;;::: ;::T__/__________VOOV______________')
  print('::`:::::::  :::::::: ;::::T_/___________VOOV______________')
  print('`:`:::::::  :::::: ;::::::T/_____________VOOV_____________')
  print(' :::`:::::::    ;:::::::::TT______________VVV_____________') 
  print(' ::::`:::::::  ::::::::;:::T______________VV______________')
  print(' `:::::`::::::::::::; `:;::T______________V_______________')
  print('  :::::`::::::::;__/__/___:T______________________________')
  print('   ::::::`:::::; __/__/____T______________________________')
  Clear()
  print('G A M E  O V E R')
  sys.exit(0)

#display and take input for choices during class methods
def Choices():
  print('What would you like to do?:\n********\n', dict1,'\n********')
  choice = int(input())
  while(choice not in [1,2,3]):
    print('Invalid Input!!!')
    print('What would you like to do?:', dict1)
    choice = input()
  return int(choice)

#speech method for enemy interaction
def Speak(player, enemy):
  if enemy.speak == True:
    print(dict3[enemy.talk])
  else:
    print('They Just want to fight!!!')
    Fight(player, enemy)

#fight method for enemy interaction
def Fight(player, enemy):
  choice = Choices()
  if choice == 1:
    player.attack(player, enemy)
  elif choice == 2:
    Speak(player, enemy)
    return
  elif choice == 3:
    if enemy.run == True:
      print('You ran away in fear!!!!!!!!!!!!')
      return
    else:
      print("You cannot run")
      Fight(player, enemy)

#simple clear screen and sleep
def Clear():
    time.sleep(4)
    clear_output()
    print(" ")

# Level 1 function
def Level1(player):
  score = 0

  print('Before',player.name, 'begins their journey to Mt. Shasta his knowledge will first be tested.')
  time.sleep(2)
  print('When was the last known eruption of Mt. Shasta:\n')
  print('********\n1- 1250\n2- 1560\n3- 1884\n********')
  choice1 = int(input())
  print(choice1)
  while(choice1 not in [1, 2, 3]):
    print("invalid input")
    print('********\n1- 1250\n2- 1560\n3- 1884\n********')
    choice1 = int(input())

  if choice1 == 1:
    score = score + 1
    print('Correct! ')

  print('how many NAMED glaciers are a part of Mt. Shasta:\n')
  print('********\n1- 9\n2- 7\n3- 18\n********')
  choice2 = int(input())
  while(choice2 not in [1, 2, 3]):
    print("invalid input")
    print('********\n1- 9\n2- 7\n3- 18\n********')
    choice2 = int(input())

  if choice2 == 2:
    score = score + 1
    print('Correct! ')

  print('What is the total elevation of Mt. Shasta:\n')
  print('********\n1- 1,250\n2- 11,560\n3- 14,179\n********')
  choice3 = int(input())
  while(choice3 not in [1, 2, 3]):
    print("invalid input")
    print('********\n1- 1,250\n2- 11,560\n3- 14,179\n********')
    choice3 = int(input())
  
  if choice3 == 3:
    score = score + 1
    print('Correct! ')

  print('Does Mt. Shasta hav a ski park:\n')
  print('********\n1- no\n2- yes\n********')
  choice4 = int(input())
  while(choice4 not in [1, 2]):
    print("invalid input")
    print('********\n1- 1,250\n2- 11,560\n3- 14,179\n********')
    choice4 = int(input())

  if choice4 == 2:
    score = score + 1
    print('Correct! ')

  print('You scored:',score,'/ 4')

  if score < 3:
    print('Alas',player.name,'your journey comes to an end before it can begin.')
    YouDied()
  else:
    print('Congratulations you have passed the test!')
    print('Now the journey to find Lemuria begins...')
    Clear()
    Level2(player)

#Level 2 function
def Level2(player):
  bat = 0
  dog = 3
  path = 0
  print('as',player.name,'begins their journey they reach a fork at the trail')
  print('______________/\\______/\\_______________________*______________-____')
  print('_/\\_________/vv\\____/vv\\_____________________________*_____--____')
  print('/__\\_______/_____\\__/____\\___*______________________________-_____')
  print('____\\__/\\________\\_______\\______---_--_*__--_____________-_______')
  print('_____\\/__\\________\\_______\\__--_____________--________--_________')
  print('___--_/____\\________\\_______\\*_________________--___--____________')
  print('_____---________________---_________________________________________')
  print('______----___________----___________________________________________')
  print('_______------_____------____________________________________________')
  print('_________------------_______________________________________________')

  print('Where will you go:\n********\n 1-left\n 2-right\n********')
  path = int(input())

  while (path not in [1,2]):
    print('Invalid Entry!')
    print('Where will you go:\n********\n 1-left\n 2-right\n********')
    path = int(input())

  if path == 2:
    print('You begin down the right path slowly trudging ever upward')
    enemy._init_(enemy, bat)
    Fight(player, enemy)
    time.sleep(3)
    Clear()
    print('after defeating the bat you continue up the path..')
    Level3(path, player)
  elif path == 1:
    print('You begin down the left path hurrying to find Lemuria')
    enemy._init_(enemy, dog)
    Fight(player, enemy)
    print('Finishing your confrontation with the dog you continue up the path...')
    Level3(path, player) 

#Level 3 function
def Level3(path, player):
  choice = 0
  mouse = 4
  if path == 1:
    print('You approach the mouth of a cave after several miles of walking')
    print('_____/\\_________________________________#_________4___________________')
    print('____/___\\____********************_____##_##______4__4_________________')
    print('___/vvvv\\__****$$$$$$$$$$$$$$$$$******#vvvv##___4vvvvv4_______________')
    print('__/_____\\_***$$$$$$$$$$$$$$$$$$$$$*****______##_4_______4_____________')
    print('/_________**$$$$$$$$$$$$$$$$$$$$$$$$$$**_______##_____4____4___________')
    print('_/\\______*$$$$$$$$$$$$$$$$$$$$$$$$$$$$**_______##___4_______4_________')
    print('___\\____*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$**______##_4____________4______')
    print('_____\\__**$$$$$$$$$$$$$$$$$$$$$$$$$$$$**_______###_____________444____')
    print('_________**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$**____________##______________')
    print('Do you enter the cave?:\n********\n1- yes\n 2-no\n********')
    choice = int(input())
    while (choice not in [1,2]):
      print('invalid entry!')
      print('Do you enter the cave?:\n********\n1- yes\n 2-no\n********')
      choice = int(input())
    if choice ==1:
      Clear()
      print('You Enter the cave slowly, you can\'t see very much')
      print('You here what sound like an angry mouse?')
      enemy._init_(enemy, mouse)
      Fight(player, enemy)
      Clear()
      print('You exit the cave and find yourself on Bunny Flat Trail')
      Level4(player)
    else:
      print('You turn around and continue down the trail')
      Clear()
      Level4(player)
  if path == 2:
    print('As you continue down the path an older man also traveling the hills stops you')
    Clear()
    print(("""
                                        /&%/.  %   (,                         
                                                  *%/#  # .* .                  
                                .#%%#.                   &  /*&  *              
                           #@&*                           /  @/( (  ,           
                       &@@                                     % @  @           
                    @@,                                          % ,,@          
                 (@&                                               ,#&          
                @@                                                  *&          
               @/   #.          */     (                             @          
              (/    .      (#      @   #                             &          
           #@*  ,(                               .           .%@@#   @          
          (&     @       &   .&                         ,@,       &(#.          
          .#    /,   & @.    @@/              *#@@@%. #  /@@@@#.   .%           
           % ,&     *#@.    %./.                        ,@        @@*           
          .&          @*    (/  ,         #(,.  .*..     %@@    &@  .           
        @,              #@@&         ,(#/              (. .#   @%               
      @(                            ,/*                     ,@@                 
    ,@            #%     @@(          *                 &@@@                    
    .&,@@@#                  (,       *                @@@@                     
          (              .(@.          .             ,@@@,                      
         @*          .        *       .,            ## @.                       
      ,@@                               .         /@   @/                       
   &@%                                        *@@@&     @@@@%. ,@@/             
  &.                                  .*&@@@@@@(@,       @@@@@     *@           
  ,@                   ,#&@@@@@@@@@@@%@(@&@%(@.            *./@      (% ./@@@&. 
    @      .(&@@@@@@@@@@&#,             #@    &/              @     @.  %       
     ,@@@@&/.                           @,.@                 /(    @,  @        
                                      ,@    @%(              (   *@.  %         
                                      @   %&                    /@  .#          
                                     @   @(                    ,@  ./           
                                    *    &                     @  *             
                                    %    *                    #  (   
    
          """))
    Clear()
    print('YOU SEEK A VALLEY')
    print('OVER THAT GAP AND THROUGH A CAVE')
    print('OR MAYBE')
    print('THROUGH THE TRAIL BUNNY FLAT')
    Clear()
    print('g o o d l u c k')
    Clear()
    print('Do you follow the trail over the gap or on bunny flat?')
    print('********\n1- gap\n2- bunny flat\n********')
    choice = int(input())
    while (choice not in [1,2]):
      print('Do you follow the trail over the gap or on bunny flat?')
      print('********\n1- gap\n2- bunny flat\n********')
      choice = int(input())
    if choice ==1:
      Clear()
      print('You back up near the gap to run and jump as fast as you can')
      print('_____/\\__/\\_________________     _______________________________________')
      print('____/__\\/__\\__/\\____________      _______________________________0_____')
      print('___/_____/___\\/__\\__________       _____________________________/ _ \___')
      print('__/_____/____\\____\\________        ______________________________| |____')
      print('_/______/_____\\____\\________   _________________________________________')
      Clear()
      print('You are not fast enough, at all...')
      YouDied()
    if choice == 2:
      print('You turn around and continue down the trail')
      Clear()
      Level4(player)

#level 4 function
def Level4(player):
  skel = 1
  print('As you travel further up the mountains through Bunny Flat you come to dreaded Red Banks...')

  print('This climb seems somewhat deadly but you can feel yourself getting closer to Lemuria')
  print('will you take the deady climb over Reb Banks or take the path further up:')
  print('********\n1- climb\n2- trail\n*********')

  choice = int(input())
  while (choice not in [1,2]):
      print('invalid entry!')
      print('will you take the deady climb over Reb Banks or take the path further up:')
      print('********\n1- climb\n2- trail\n*********')
      choice = int(input())
  if choice == 1:
    print('Although treachorous you easily ascend the mountain through Red Banks.')
    print('You find a small game trail and begin to follow it.')

    print('You come to a small door guarded by what looks like a long dead soldier of some sorts')
    print('_______/\\________________________________________________')
    print('______/___\\_________----------------_____________________')
    print('_____/vvvvv\\_______--______________--____________________')
    print('____/_______\\______--______________--_......_____________')
    print('___/_________\\_____--_0____________--( X  X )____________')
    print('__/___________\\____--______________--__[__]______________')
    print('_/_____________\\___--______________--____________________')

    print('you go to enter this mysterious door when the skeleton soldier rises from the dead!!!')
    print('*YOU',player.name,'WILL NEVER EXPOSE LEMURIA.....')
    enemy._init_(enemy, skel)
    Fight(player, enemy)
    Clear()
    print('You defeated the guardian of Lemuria...')
    print('You open the door to find a trail with rocks lining both sides.')
    print('the path curves and winds upwards until you reach a glaciel opening...')
    Clear()
    print('You can feel the energy of spirits all around you')
    Clear()
    Level5(player)

#level 5 function
def Level5(player):
  lem = 2
  print('You have finally found the fabled entrance to Lemuria!!!!')
  print(("""   
               /\                             /  \
   __________ /vv\      ______         _____ /vvvv\     __________
   [   ]    |     \     |   U |_ _ _ _| R   |      \    |    [   ]
   [___]    |_ _ _ \__ _|     | U U U |     |_ _ _ _\ _ |    [___]
   \XXX/    | Z Z Z Z Z |     |=======|     | Z Z Z Z Z |    \XXX/
    \>/     |===========| M   | + W + |   I |===========|     \</
     |      |           |     |_______|     |           |      |
     |      |           |  E  ||||||||| A   |           |      |
     |      |           |     ||vvvvv||     |           |      |
 _-_-|______|-----------|____L||     ||_____|-----------|______|-_-_
    /________\         /______||     ||______\         /________\
   |__________|-------|________\_____/________|-------|__________|
        """))
  time.sleep(5)
  print('A man approachs you in leather adorned clothing and a serious face')
  Clear()
  print(("""*********************************************************************************
        _____________________________________///(())(____________________________________
        __________________________________(((__   __ \\__________________________________
        __________________________________))-O-`."-O-((_________________________________
        __________________________________((\ / |   /))__________________________________
        __________________________________|)|  ~-~  |(|__________________________________
        ___________________________________|\ -x-x- /|___________________________________
        ___________________________________|_~-___-~_|___________________________________
        ___________________________________; ~~~~;~~_____________________________________
        *********************************************************************************"""))
  time.sleep(1)
  print('Hello, I am one of many people living in this beautiful land.')
  print('I want to know only if you will expose our secret valley in the mountains')
  print('Will you tell others of Lemuria?:\n1- No\n2- Yes')
  choice = int(input())
  while (choice not in [1,2]):
      print('I want to know only if you will expose our secret valley in the mountains')
      print('Will you tell others of Lemuria?:\n1- No\n2- Yes')
      print('1- climb\n2- trail')
      choice = int(input())
  if choice == 1:
    player.victory = True
  elif choice == 2:
    enemy._init_(enemy, lem)
    Fight(player, enemy)
  end(player)

#end of game function
def end(player):
  if player.victory:
    print(player.name, " BEAT THE GAME!!!! With:", player.hp,"health points left!!!!")
  else:
    print("OH NO! Although you defeated the lemurian and escaped.")
    print("YOU HAVE EXPOSED THE LAND OF LEMURIA LEADING TO IT\'S DESTRUCTION")
    print(("""    THE CASTLE NOW LIES IN RUIN.......
            __________ /vv\      ______         _____ /vvvv\     __________
            [   ]    |     \     |   U |_ _ _ _| R   |      \    |    [   ]
            [___]    |_ _ _ \__ _|     | U U U |     |_ _ _ _\ _ |    [___]
            \XXX/    |           ======|     | Z Z Z Z Z |    \XXX/
             \>/     |===========| M   | + W + |   I |===========|     \</
            |      |           |     |_______|     |           |      |
            |      |            >           |        |      |
            |      |            >    ||vvvvv||     |           |      |
 _-_-       |______|-----------|____L||     ||_____|-----------|______|-_-_
            /________\         /______||     ||______\         /________\
            |__________|-------|________           -------|__________|"""))

# simple menu function 
def menu():
  print("CREATED BY: SAMUEL JAMES")
  Clear()
  print(("""

                                                                                                                
       ##.                                                                      
        .%%#.                                                                  
       %,   #%%(                                                                
        (%#.   %#                                  
          .#%%%%/   A L L E N  &  P R I S C I L L A     
          /%%(/%#                                                               
       ,%%,   ,%%   O P P E N H E I M E R                                                    
      .%   *%%%.                   
       ,%%%*                                                                    
       %/ (%%/                                                              
       (%,   *%%/                         
         (%%*  #%                      
            (#%%.   F O U N D A T I O N                                         
         #%%*  (%  .,.,.,.,..........,.,.,.,.,.*.*.,.,.,.,.,.,.,.....,..,..   
       #%,                                                              
      .                                                                  


                    """))
  Clear()
  print(("""
  
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,*(@@@@&(,. @@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@& &*  *@@@@@@@@@@@@@@@@@@&.  (%*,@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@(% .@@@@@@,.&.,#/., @@@@@ @,*@ (@@@@&  &**@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#/% (@@@@.& ( % &% @*@&@@@@@@@( ,@ .@@ &@(/@@@* &/&@@@@@@@@@@@@@@
@@@@@@@@@@@@@ / @@@@@*,@ &@/@@@@@@#*         ,(&@@@@@@@ @ /@*/@@& %.@@@@@@@@@@@@
@@@@@@@@@@%& &@@&  #.  @@@@/ .&,                  %/  @@@@@ @@ @*@@( (@@@@@@@@@@
@@@@@@@@@& @@@/@ *( @@@  @      &@@@@,      &@@@/      *, @@@@ @ @ @@@ &#@@@@@@@
@@@@@@*& @@@@@*@ @@@ ,.      (@@@@@@@@@@ @@@@@@@@@@#       @ @@@/@@@@@ # (@@@@@@
@@@@@. (##.*@@@@@@ %          @@@@@@/    @@@@  &@@@@          ..@@*,#####,**@@@@
@@@(% ########./ (                (@@@@% @@@@  &@@@@            ,.######### ,@@@
@@@@ ##%###@@&/@,            ,@@@@@@@@@@ @@@@@@@@@@(            (@,@@@###@## #@@
@@& #########@@@ (@             .(%%*       /&&%,            #@@#@@@/######## .@
@  ######### @@,@ @@@ ,                                   % @@(&((@*,/#######( @
@# ######## & @@@@/@.@ #                                 # @@@ @@@& . ######## @
  ########(.  @@ @ #@@,,(    ##### ,@@@@#####  @@@@&    # @@#@%@ @#  &.#######/.
/ ########,%  @@@@.@@@  #    ##### ,@@@@#####  @@@@&   .# @@@.@@@@.  / ######## 
# ########.%  # @@,@@,@ #    ##### ,@@@@#####  @@@@&   *,/&@@#@@@*   , ######## 
* ########,#  ,@@&@@ @@ (    ##### ,@@@@#####  @@@@&   # /@@( @@@@   ( ######## 
  #########    (@@@ @@#@ *   ##### ,@@@@#####  @@@@&   # ,@@@ @@@    %.#######*,
@& ######## &  ,@,@*@*@@ #   *####, @@@@####( (@@@@,   ,#@,@,@@ @   , ######## &
@  ######### #  @@@@ @@@@ /   ######         @@@@@&   # @@@@(@@@,    (#######,,@
@@( ######### %   @@@ @.@@ (    ########@@@@@@@@@    /,@@@@#@@#     (########  @
@@@% #########./  @@@@,(@@@@       /####@@@@@#     . @@@@ @@@@@  % ######### *@@
@@@(/ #######.(@ & %@@@@(@@@%                       @@@@ @@@@. , /########/ .@@@
@@@@@/,.#/.@@@@@@@ &  @@@@@@@     ,( &,,  @ & @     @@@@@@%  ( #@@@ (#### #@@@@@
@@@@@@@( %@@@@@@@@@@* #    &@@    ,(.@(( @  .@/   *@@%     * @@@@@@@@@,. .@@@@@@
@@@@@@@@@& %@@@@@@@@@@@# (.     /@#           #@*      @  @@@@@@@@@@@* /@@@@@@@@
@@@@@@@@@@@/ .@@@@@@@@@.@@@@  *&.                ##  #@@@@@ @@@@@@@ , @@@@@@@@@@
@@@@@@@@@@@@@/& ,@@@@@ @& @.*@@@@@@&(,.    ,(%@@@@@@@. /@@@ %@@@  %@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%  &@@@@@,,// @/.& @@.@..@.  #@ %@@ &@,.@@@# ./&@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%. .@@@@@@@ @@/ #@@ @@%  *@* ,@@@@&  *(@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@(@,   *&@@@@@SOU@@@@@%,   *&*@@@@@@@@@@@@@@@@@@@@@@@@@
  
  
  
                    """))   
  Clear()    
  print(("""
                                  *#####                                       
                                 ##########*                                    
                              *###############                                  
                            ((((((((############*                               
                         ,(((((((((((, ############                             
                       ((((((((((((      ,###########*                          
                    ,(((((((((((,           ############                        
                  ((((((((((((                ,###########*                     
                (((((((((((,                     ############                   
                                                                                
               @@                                                               
               @@                                     ///                       
               @@                                     @@@                       
     @@@@@@&   @@  @@@@(       @@@@@@ @@@   @@@@@@ (@@@@@@@@(  @@@@@@  @@       
   @@@     @   @@@%   .@@@  @@@@     @@@@ @@#         @@@   %@@@     @@@@       
    @@@@(      @@       @@ ,@@        @@@ @@@@,       @@@   @@        @@@       
         @@@@  @@       @@ @@@        @@@     .@@@@%  @@@   @@        @@@       
   @@      @@@ @@       @@  @@@      @@@@ @@     %@@  @@@   #@@@     @@@@       
     @@@@@@@   @@       @@    /@@@@@@ @@@  (@@@@@@      @@@@%  @@@@@@  @@       
                                                                                
                                                                            
      N        E         T        W         O        R        K        S        
                                                                         
  """)) 
  Clear()     

  print(("""
         / \\                   / \\
        /vvv\\    Mt. Shasta   /vvv\\
       /     \\               /     \\
      /       \\             /       \\
      ##################################
      #________________________________#
      #________________________________#
      #_____PLAY: 1____________________#
      #________________________________#
      #_____EXIT: 0____________________#
      ##################################

        """))
  play = int(input('Enter Choice:'))
  while(play not in [0,1]):
    print('invalid input!')
    play = int(input('Enter Choice:'))
  if play == 1:
    main()
  elif play == 0:
    sys.exit(0)                               

# main function 
def main():
  print(' __  __ _______    _____ _    _           _____ _______    ')       
  print('|  \/  |__   __|  / ____| |  | |   /\    / ____|__   __|/\ ')    
  print('| \  / |  | |    | (___ | |__| |  /  \  | (___    | |  /  \ ')  
  print('| |\/| |  | |     \___ \|  __  | / /\ \  \___ \   | | /vvvv\ ')  
  print('| |  | |  | |_    ____) | |  | |/ ____ \ ____) |  | |/      \ ') 
  print('|_|  |_|  |_(_)  |_____/|_|  |_/_/    \_\_____/   |_/________\ ')
  time.sleep(3)

  print('You see Mt. Shasta in the distance sun rising over the peak at 14,179ft.')
  print('It is believed Mt. Shasta is the Spirit of the Above-World by the Klamath Tribes')
  print('You are an adventurer searching for Lemuria the mythical hidden land of Mt. Shasta.')
  print('enter____your____name____wanderer\n')

  name = input("enter name:")
  player.init(player, name)
  Level1(player)
# start menu to promt user for input, catch any errors that may occur
try:
  menu()

except KeyboardInterrupt:
  print("KeyboardInterrupt Game Exited")
except SystemExit:
  print("GOODBYE!")
except ValueError:
  print("non-numerical value entered! Game Exited")
