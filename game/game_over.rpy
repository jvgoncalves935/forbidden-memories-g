label game_over:
    scene black
    with Dissolve(2.0)
    pause 1.0
    stop sound fadeout 2.0
    stop music fadeout 2.0
    
    show game_over_bg
    play music fm_gameover
    with Dissolve(2.0)
    pause 8.0
    stop music fadeout 2.0
    hide game_over_bg
    with Dissolve(2.0)

    $ renpy.movie_cutscene("mod_assets/videos/intro.webm")
    return



