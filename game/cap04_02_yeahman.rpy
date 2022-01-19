label cap04_02_yeahman:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    $ renpy.movie_cutscene("mod_assets/videos/yeahman.webm")
    return

label wrong_end_04_02_1:
    $ register_ending("R")
    jump game_over


