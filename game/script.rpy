# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer
    
    #Mod assets
    #define audio.insector_sun = "<loop 0.00>mod_assets/ost/insector_sun.ogg"
    #define audio.vassoura = "<loop 0.00>mod_assets/ost/vassoura.ogg"
    #define audio.suspence01 = "<loop 0.00>mod_assets/ost/its_you_its_me.ogg"
    #define audio.suspence02 = "<loop 0.00>mod_assets/ost/soe.ogg"
    #image sayori happy1 = "mod_assets/characters/sayori/s_kill.png"
    #image sayori happy2 = "mod_assets/characters/sayori/s_kill2.png"
    #image bg psycho_club = "mod_assets/bg/psycho_club.png"
    #image bg happy_club = "mod_assets/bg/happy_club.png"
    #define audio.happy = "<loop 0.00>mod_assets/ost/happy.ogg"
    #define audio.null_exception = "<loop 0.00>mod_assets/sound/exception.ogg"
    #image kurisu 1a = "mod_assets/characters/kurisu/1a.png"
    #image kurisu 1b = "mod_assets/characters/kurisu/1b.png"
    #image kurisu 1c = "mod_assets/characters/kurisu/1c.png"
    #mc art character by Sir French Fries and Childish-N, xd
    #image main_c 1a = "mod_assets/characters/main_c/1a.png"
    #image yuri_y 1y8 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/y8.png")
    #image yuri_y 1y9 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/y9.png")
    

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ persistent.in_my_world_loop = False
    $ persistent.in_end_game = False
    $ persistent.is_yuri_self_aware = False
    $ persistent.allow_yuri_delete = False

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    #if persistent.playthrough == 0:
        #Call example script
    call the_bad_prologue

    #if persistent.playthrough == 1:
        #Stuff here will only play after you increased the playthrough count
        #call tutorial_selection from _call_tutorial_selection
        #pass

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
