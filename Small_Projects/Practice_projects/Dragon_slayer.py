print('''
*******************************************************************************
                            ==(W{==========-      /===-                        
                              ||  (.--.)         /===-_---~~~~~~~~~------____  
                              | \_,|**|,__      |===-~___                _,-' `
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~      
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`         
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'             
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /               
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'                
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'                  
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`                   
                  \_|      /        _) | ;  ),   __--~~                        
                    '~~--_/      _-~/- |/ \   '-~ \                            
                   {\__--_/}    / \\_>-|)<__\      \                           
                   /'   (_/  _-~  | |__>--<__|      |                          
                  |   _/) )-~     | |__>--<__|      |                          
                  / /~ ,_/       / /__>---<__/      |                          
                 o-o _//        /-~_>---<__-~      /                           
                 (^(~          /~_>---<__-      _-~                            
                ,/|           /__>--<__/     _-~                               
             ,//('(          |__>--<__|     /                  .----_          
            ( ( '))          |__>--<__|    |                 /' _---_~\        
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\      
        ,/,'//( (             \__>--<__\    \            /'  //        ||      
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'       
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/                  
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~                    
   ;'( ')/ ,)(                              ~~~~~~~~~~                         
  ' ') '( (/                                                                   
    '   '  `                                                                   
*******************************************************************************''')

print('Welcome to "DRAGON SLAYER"!\nYour mission is to slay the dragon.')


weapon = input("What weapon would you like? 'axe', 'wand', 'dagger'? ").lower()

if weapon == "axe":
    dodge = input("The dragon is preparing a breath attack! What do you do? Dodge 'left' or 'right'? ").lower()
    if dodge == 'left':
        action = input("You barely manage to roll away from the dragon fire! Do you 'attack' or 'wait'? ").lower()
        if action == "attack":
            print("With a single swing of your axe you kill the dragon! YOU WIN!")
        else:
            print("You hesitate and the dragon uses the opportunity to cut you in half with his claws! GAME OVER!")
    else:
        print("The dragon predicts your move and your are engulfed in flames! GAME OVER")
elif weapon == "wand":
    print("You don't know any magic spells... the dragon eats you alive! GAME OVER!")
elif weapon == "dagger":
    print("You try and cut the dragon with your dagger, but it is no match for the dragon's thick scales. The dragon "
          "squishes you with his giant tail!")
else:
    print("You try and stab the dragon in the heart, but your sword breaks and the dragon's breath engulfs "
          "you in"
          "flames! GAME OVER")




