label game_over:
    $ game_over = True
    

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()



    if(not game_over_pos_cutscene):
        show textbox_aux
        scene black
        with Dissolve(2.0)
        pause 1.0

        if(game_over_fadeout_musica == 0.0):
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
    
    if(game_over_delay_musica > 0.0):
        pause game_over_delay_musica     
    else:
        pause 8.0

    hide game_over_bg
    with Dissolve(1.5)

    show screen texto_game_over
    with Dissolve(0.5)

    if(game_over_musica):
        stop music fadeout 1.0
    if(game_over_fadeout_musica > 0.0):
        stop music fadeout game_over_fadeout_musica
    if(game_over_fadeout_sound > 0.0):
        stop sound_bg fadeout game_over_fadeout_sound
    

    pause 1.5
    hide screen texto_game_over
    with Dissolve(0.5)

    $ game_over_musica = True
    $ game_over_pos_cutscene = False
    $ game_over_delay_musica = 0.0
    $ game_over_fadeout_musica = 0.0
    $ game_over_fadeout_sound = 0.0


    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()
    

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    return



