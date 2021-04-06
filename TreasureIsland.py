print('''
*******************************************************************************
        
                   .     .  *     . .       .     *
                   *   .  *  . +..  . . . . .  .   .  + .
                .   .  +  . . . *   .  *  . +..  .
                  + .  .  .  .. + .  .   .    .    . .
               + .  .  .  .. +  .  .     . +.    +  .
                + .  .  .  .. +  .  .   . .
          .    + .  .  .  .. +  .    * . . .  .  +   .
           +      .  + .  .  .  .. +  .   . +
              + .  .  .  .. +   .  . +  .+. .
            + .  .  .  .. + . . + .  . .     .    
           .  .  .    .   . .   . . .     
      *  + .  .  .  .. +  .  . .  +    .  .       
   *  .     .    .  +   . .  *  .      
.  .  .. . + .  .  .  .. + 
..  .  .. .  .  .  *   .  *  . +..  .        
 .      .   . .   .   .   . .  
   ,-' ;  ! `-.     .. +   .. + 
  / :  !  :  . \  *  . +..  .  
 |_ ;   __:  ;  |  .. 
 )| .  :)(.  !  |
 |"    (##)  _  | *
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

*******************************************************************************
''')
# Use of If/Else Statements
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\nYour adventure awaits beyond this door.\nNow open it...") 

choice1 = input("There is a road to your left, which takes you into the woods, and a road to your right, which takes you aboar a ship. L or R?\n")
choice1_lower = choice1.lower()

# ****************************

if choice1_lower == "l":
  lchoice_1 = input("You find a knife on the ground, do you take it? Y or N?\n").lower()
  if lchoice_1 == "y":
    lchoice_2 = input("You warded off the wolves with your knife and made it to the cabin!\nThere is a box inside...Open it? Y or N?\n").lower()
    if lchoice_2 == "y":
      print("There is a bomb inside! GAME OVER!")
      print('''
      ______________________________    . \  | / .
     /                            / \     \ \ / /
    |                            | ==========  - -
     \____________________________\_/     / / \ \
  ______________________________      \  | / | \
 /                            / \     \ \ / /.   .
|                            | ==========  - -
 \____________________________\_/     / / \ \    /
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |                            | ==========  -  - -
     \____________________________\_/     / / \ \
                                        .  / | \  .''')
    else:
      lchoice_3 = input("You leave the cabin and find a nearby hole with a shovel. Dig deeper? Y or N?\n").lower()
      if lchoice_3 == "y":
        print("You found the treasure!")
        print('''
                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
                 ''')
      else:
        print("You wasted too much time outside, you are struck by lightning! GAME OVER!")
        print('''
                                   ,/
                                 ,'/
                               ,' /
                             ,'  /_____,
                           .'____    ,'    
                                /  ,'
                               / ,'
                              /,'
                             /''''') 
  else:
    print("You are attacked by wolves. GAME OVER!")
    print('''   _..._     ___     ___     ___     ___     _..._
             ,'   `::. ,~  `:. ,~  `:. ,~  `:. ,~  `:. ,'   `::.
            :      `:::     `::     `::     `::     `::      `:::
            :      .:::     .::     .::     .::     .::      .:::
            :      .:::`.  .;' `.  .;' `.  .;'.`.  .;':      .:::
            :      .:::  `.'    .`.'.:   `.'   ::`.'  :.     .:::
            :.     .::'          :::            :     `:     .:::
            `:     .::            :                    :     .::'
             :     .::            .                    :.    .::
              :    ::'                                 `:   .::.
              .\   `:      ,:                   :.      :  .::.:
              :.\   :.    :.:                   :`:    .' .::.:
               ::`.  :   :'::                   : `:   : .;'.:
                :  `.;  :'.::                   :  ::  ;:' ::
                    .  :' .::.                 .:  .::     :
                    : :'   :::                 :'   .::    .
                      :    `::                 :    .::
                     :'    .::.               .:    .:::
                     :     .:::  ,:.     .:.  :'    .:::
                     :     .:::,'  `:. ,'  `:.:     .:::
                     :     .:::     :::     :::     .:::
                     :     .:::     :::     :::     .:::
                      `._ .::'.`._.::' `._.::'.`._ .::''')
else:
  choice_2 = input("You board the ship, you see a fish. Do you kill it? Y or N?\n").lower()
  if choice_2 == "y":
    choice_3 = input("You made it to the island. You start getting hungry, You see a lobster, do you eat it? Y or N?\n").lower()
    if choice_3 == "y":
      print("You die of poisoning. GAME OVER!")
      print(''' 
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
      ''')
    else:
      choice_4 = input("You make it to a nearby cabin, still hungry. You see a chest. Open it? Y or N?\n").lower()
      if choice_4 == "y":
        print("You found the treasure and loads of food!")
        print('''
                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
                 ''')
      else:
        print("You came for nothing and die of exhaustion. GAME OVER!")
        print('''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
   ''')

  else:
    print("You die of starvation, GAME OVER!")
    print('''       
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"''')
