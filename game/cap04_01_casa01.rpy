label cap04_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_04_01_1:
    $ register_ending("Q")
    jump game_over


