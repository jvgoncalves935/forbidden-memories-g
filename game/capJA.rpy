label capJA:
    
    $ drpc_update("capJA")
    play sound menu_start
    play sound_bg audio.jailson02 noloop

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache() 

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    play music fm_modern_shop
    show ja_01 at top_fade
    play sound_bg audio.jailson03 noloop
    $ renpy.pause(31.0, hard=True)
    hide ja_01


    stop music fadeout 1.0
    show ja_02 at top_fade
    $ renpy.pause(16.0, hard=True)

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    hide ja_02
    $ renpy.pause(1.0, hard=True)
    stop music
    stop sound_bg
    scene black
    

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



