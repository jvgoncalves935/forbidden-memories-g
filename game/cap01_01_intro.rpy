label cap01_01_intro:
    $ drpc_update("intro")

    scene black
    stop music
    show textbox_black at center
    "{p=4.0}{nw}"
    hide black
    play sound footsteps

    show intro_001 at top
    with dissolve
    #scene bg intro_001 at top
    "{p=1.0}{nw}"
    hide intro_001
    show black
    with dissolve
    hide black
    show intro_002 at top
    with dissolve
    "{p=2.0}{nw}"
    hide intro_002
    show black
    with dissolve
    hide black
    show intro_003 at top
    with dissolve
    "{p=1.0}{nw}"
    "Finalmente eu encontrei!"
    play sound ctc
    
    "O Códex G, a História do Alexandre\nSenna!"
    play sound ctc
    
    hide intro_003
    show black
    with dissolve
    hide black
    show intro_004 at top
    with Dissolve(1.5)
    "{p=1.0}{nw}"
    "Hahahahaha!"
    play sound ctc
    
    "Hahahahaha...\nHahahahaha!!!{p=2.5}{nw}"
    
    $ renpy.music.play(audio.fm_intro)
    $ renpy.music.queue(None,clear_queue=True)
    #play music fm_intro
    window hide(None)
    hide intro_004
    show black
    with Dissolve(2.0)
    pause 0.5
    hide black
    show logo01
    with Dissolve(3.0)
    pause 3.0
    hide logo01
    show black
    with Dissolve(3.0)
    pause 3.0
    return



