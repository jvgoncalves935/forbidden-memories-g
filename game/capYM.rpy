label capYM:
    
    $ drpc_update("capYM")
    play sound menu_start
    play sound_bg audio.yeahman_03 noloop

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache() 

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    play music fm_preliminary_faceoff
    show ym_02 at top_fade
    play sound_bg audio.yeahman_04 noloop
    $ renpy.pause(84.0, hard=True)

    stop music fadeout 1.0
    $ renpy.pause(2.0, hard=True)

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    hide ym_02

    $ register_ending("CXY")
    show ym_01 at top_fade
    play sound_bg audio.millenniumitem noloop
    "(Você desbloqueou o capítulo\nsecreto do \"Oh Man\"!!!)"
    play sound ctc
    
    hide ym_01
    "{p=2.0}{nw}"

    stop music
    stop sound_bg
    scene black
    

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



