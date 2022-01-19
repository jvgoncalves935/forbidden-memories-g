label cap02_04_roda_amigos:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return


label wrong_end_02_04_1:
    $ register_ending("L")
    jump game_over
