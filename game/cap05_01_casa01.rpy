label cap05_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_05_01_1:
    $ register_ending("V")
    jump game_over

