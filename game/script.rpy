# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:
    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer
    

    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    #if persistent.playthrough == 0:
        #Call example script
    
    $ cap_choosed = 1
    $ game_over = False
    play sound menu_start

    if(not game_over):
        call cap01
    if(not game_over):
        call cap02
    if(not game_over):
        call cap03
    if(not game_over):
        call creditos
    if(not game_over):
        call capXX

    $ game_over = False

    $ renpy.movie_cutscene("mod_assets/videos/intro.webm")
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
