label cap02_03_casa02:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_02_03_1:
    stop music
    $ register_ending("J")
    jump game_over

label wrong_end_02_03_2:
    stop music
    $ register_ending("K")
    jump game_over


