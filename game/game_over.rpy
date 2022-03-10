label game_over:
    $ game_over = True
    
    if(not game_over_pos_cutscene):
        show textbox_aux
        scene black
        with Dissolve(2.0)
        pause 1.0
        stop sound fadeout 2.0
        stop music fadeout 2.0
    else:
        scene black
        hide textbox_aux
        pause 1.0
    
    if(game_over_musica):
        play music fm_gameover2

    show game_over_bg
    with Dissolve(2.0)
    
    pause 8.0
    if(game_over_musica):
        stop music fadeout 2.0
    hide game_over_bg
    with Dissolve(2.0)

    $ game_over_musica = True
    $ game_over_pos_cutscene = False

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    return



