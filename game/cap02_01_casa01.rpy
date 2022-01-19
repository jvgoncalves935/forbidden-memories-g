label cap02_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_02_01_1:
    $ register_ending("F")
    jump game_over

