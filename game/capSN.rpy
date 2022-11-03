label capSN:
    
    $ drpc_update("capSN")
    #play sound menu_start

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache() 

    stop music

    show jumpscare at center
    show ctc

    play sound_bg audio.violencia_auditiva noloop
    #"{cps=400}Atenção: esta parte pode conter um\njumpscare. Recomendamos que você\nabaixe o volume do seu fone de\nouvido e definitivamente não assista\nisso na sua TV."
    $ renpy.pause(14.6, hard=True)
    stop sound_bg

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    $ renpy.quit()

    $ renpy.pause(5.0, hard=True)

    stop music
    stop sound_bg
    scene black
    

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



