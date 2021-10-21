# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character(_("You"), color="#c8ffc8")
define m = Character(_("Megacorp"), color="#c8c8ff")
define gui.bar_range = 100
define gui.bar_tile = False
define fadehold = Fade(0.5, 0, 0.5)
define fadehold1 = Fade(0.5, 1.0, 0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_room
    with fade

    show spritething

    m "Hello citizen! Megacorp sponsors you this beautiful morning."
    y "Hello Megacorp."
    m  "What do you want to do today?"
    hide spritething
    
    menu:
        "Go to the moon":
            jump gotomoon
          
        "Go to work":
            jump gotowork
          
        "Play games":
            jump playgames
    
    
    label gotomoon:
        m "Silly thing, you cannot go to the Moon. Choose something else"
        ""
    menu:
            "Go to work":
               jump gotowork
     
        
            "Play games":
               jump playgames

    label playgames:
        show spritething
        m "I don't think this is the right choice, but it's not like I can force you."
        m "Enjoy wasting your day without generating profit for Megacorp. Megacorp cares."
        m "Remember. Megacorp cares."
        "During the game you accidentally drop your controller. It falls under your coffee table."
        "You bend to pick it up and hit your head on the table."
        scene bg_room with vpunch
        

    jump bang


    label gotowork:
        show spritething
        m "I'm glad you're choosing to be a good member of society. Now go earn your money so you can buy more things. Remember, Megacorp cares."
        scene bg_work
        show spritething
        "You work diligently the whole day. Just when you're about to go home you drop your phone."
        "You bend to pick it up and hit your head on the desk."
        scene bg_work with vpunch


    label bang:
        show spritething_sad
        y "Ouch, that hurt."
        y "Good thing this isn't some kind of a story or I would have knocked myself out."
        scene black with fade
        scene bg_room with fadehold1



 
    # bar appears
    show spritething_sad
    y "Uh, that was unpleasant."
    "You decide to treat yourself to make yourself better."   
    "You buy a new IGadget."

    #bar gets shorter
        
    hide spritething_sad
    show spritething
    
    y "Maybe the day wasn't so bad after all."
    scene black with fade   


    scene bg_room with fadehold1

    show spritething

    m "Hello citizen! Megacorp sponsors you this beautiful morning."
    y "Hello Megacorp."
    m  "What do you want to do today?"
    hide spritething
    
    menu:
         
        "Go to work":
            jump gotowork1
          
        "Play games":
            jump playgames1 

    label playgames1:
        show spritething
        m "I don't think this is the right choice, but it's not like I can force you."
        m "Enjoy wasting your day without generating profit for Megacorp. Megacorp cares."
        m "Remember. Megacorp cares."
        hide spritething

        jump backhome
    # bar gets smaller
    
    
    label gotowork1:
        scene bg_work
        show spritething_suspicious
        m "I'm glad you're choosing to be a good member of society. Now go earn your money so you can buy more things. Remember, Megacorp cares."
        "You work diligently the whole day."
        jump backhome
    
   # bar gets smaller more than the game one

    
    label backhome:
    scene bg_room
    show spritething
    m "Oh look, we're going to release a new mPhone. Do you want to preorder?"
    y "Of course I want to preorder"
    hide spritething
    show spritething_concern
    #bar gets smaller
    y "I wanted what that bar I keep seeing means."
    hide spritething_concern
    show spritething
    y "Whatever, guess I'll just sleep."

    scene bg_room with fadehold1

    show spritething
    #bar is shorter than before

    m "Hello citizen! Megacorp sponsors you this beautiful morning."
    y "Hello Megacorp."
    m  "What do you want to do today?"
    hide spritething
        
    menu:
             
        "Go to work":
            jump gotowork2
              
        "Play games":
            jump playgames2 

    label playgames2:
        show spritething
        m "I don't think this is the right choice, but it's not like I can force you."
        m "Enjoy wasting your day without generating profit for Megacorp. Megacorp cares."
        m "Remember. Megacorp cares."
        jump tospace
    # bar gets smaller
    
    
    label gotowork2:
        scene bg_work
        show spritething
        m "I'm glad you're choosing to be a good member of society. Now go earn your money so you can buy more things. Remember, Megacorp cares."
        "You work diligently the whole day."
        jump tospace
    
   # bar gets smaller more than the game one
    label tospace:
    scene bg_room
    show spritething
    m "We welcome everyone this evening to watch Jeff Musk go into space for 5 minutes."
    m "Sponsored by Megacorp. Megacorp cares."
    y "Oh, that is so cool!"
    y "Look at the rocket go!"
    hide spritething

#bar gets SIGNIFICANTLY smaller

  
    show spritething_point
    
    y "Uhm, Megacorp?"
    y "This energy bar thingy… it’s getting pretty low."
    m "Don’t worry about it citizen, Megacorp ca... "
    m "Wait. You can see it?"
    hide spritething_point
    show spritething_concern
    y "Yes, and it only seems to be going down…"
    
    m "..."
    m "................."
    m "ALERT! Illegal hacking detected!"
    hide spritething_concern
    show spritething_suspicious
    y "What? But I didn’t DO anything. I was just looking…"
    m "Cease your illegal activity citizen, or there will be consequences."
    hide spritething_suspicious
    show spritething_point
    y "But it’s just THERE"
    m "Cease your illegal activity citizen, or there will be consequences."
    hide spritething_point
    show spritething_concern
    y "What am I supposed to do, pretend it’s not there?"
    m "Make a smart decision, citizen."
    hide spritething_concern
    
    menu:
        "Pretend it’s not there":
           jump notthere
    
        "Keep insisting":
           jump insisting

    label notthere:
        show spritething_suspicious
        y "Ah, you're right, I can't actually see anything."
        y "It must have been my imagination."
        m "Yes, must have been, citizen."
        m "Why not rest and buy yourself a brand new Product?"
        y "Yes... ok..."
        m "Have a good night citizen. Megacorp cares."
        jump final


        
    label insisting:
        show spritething_suspicious
        y "But look, there it is running out."
        m "You seem disturbed citizen. Please wait for our Authority Enforcers to help you understand the truth."
        "Your door opens suddenly and black-clad figures surround you."
        hide spritething_suspicious
        show spritething_concern
        y "Hey, who are you?!"
        scene bg_room with vpunch
        scene black with fade
        hide spritething_concern
        show spritething_sad
        scene bg_room with fade
        show spritething_sad
        "You wake up in an empty room. There is only a chair to sit on and a huge screen on the wall."
        jump final



    label final:
    scene bg_room  with fade

    show spritething_sad

    m "Hello citizen! Megacorp sponsors you this beautiful morning."
    y "...yeah"
    m "We are proud to announce Megacorp is releasing a new cryptocurrency Megacoin."
    y "Won't this eat more of the energy bar thing?"
    m "The release will be done in 3"
    m "2"
    hide spritething_sad
    show spritething_concern
    y "WAIT!!!"
    m "1"

    scene black with fade 

    # bar reaches 0



    "Everything stops."
    "nothing"

    "THE END (of the world)"

    # This ends the game.

    return
