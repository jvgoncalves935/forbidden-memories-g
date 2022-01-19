label cap02_02_oficina_gringo:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return


label wrong_end_02_02_1:
    $ register_ending("H")
    jump game_over

label wrong_end_02_02_2:
    $ register_ending("I")
    jump game_over
