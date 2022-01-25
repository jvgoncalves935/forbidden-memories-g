label cap05_02_testeporno:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return


label wrong_end_05_02_1:
    stop music
    $ register_ending("W")
    jump game_over

label wrong_end_05_02_2:
    stop music
    $ register_ending("X")
    jump game_over
