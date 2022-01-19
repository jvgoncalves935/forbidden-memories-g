label cap04_03_casa02:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_04_03_1:
    $ register_ending("S")
    jump game_over

label wrong_end_04_03_2:
    $ register_ending("T")
    jump game_over

