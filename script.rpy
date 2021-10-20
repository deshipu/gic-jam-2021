# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character(_("You"), color="#c8ffc8")
define m = Character(_("Megacorp"), color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade



    m "Hello citizen! Megacorp sponsors you this beautiful morning."
    y "Hello Megacorp."
    m  "What do you want to do today?"
    
    menu:
        "Go to the moon":
            jump gotomoon
          
        "Go to work":
            jump gotowork
          
        "Play games":
            jump playgames
    
    
    label gotomoon:
        m "Silly thing, you cannot go to the Moon. Choose something else"
        
    menu:
            "Go to work":
               jump gotowork
     
        
            "Play games":
               jump playgames
        
    label gotowork:
        m "I'm glad you're choosing to be a good member of society. Now go earn your money so you can buy more things. Remember, Megacorp cares."
        
    label playgames:
        m "I don't think this is the right choice, but it's not like I can force you."
        
        
    
    
    
    
    
    
    
    
    
    
    y "Uhm, Megacorp?"
    y "This energy bar thingy… it’s getting pretty low."
    m "Don’t worry about it citizen, Megacorp ca... "
    m "Wait. You can see it?"
    y "Yes, and it only seems to be going down…"
    
    m "..."
    m "................."
    m "ALERT! Illegal hacking detected!"
    y "What? But I didn’t DO anything. I was just looking…"
    m "Cease your illegal activity citizen, or there will be consequences."
    y "But it’s just THERE"
    m "Cease your illegal activity citizen, or there will be consequences."
    y "What am I supposed to do, pretend it’s not there?"
    m "Make a smart decision, citizen."
    
    menu:
        "Pretend it’s not there":
           jump notthere
    
        "Keep insisting":
           jump insisting

    label notthere:
        y "aaa"




        
    label insisting:
        m "zzz"



    # This ends the game.

    return
