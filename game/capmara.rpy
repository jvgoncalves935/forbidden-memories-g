label mara_ending:
    
    $ drpc_update("finalmara")
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
    show ym_02 at r2_out
    play sound_bg audio.yeahman_04 noloop
    $ renpy.pause(84.0, hard=True)

    stop music fadeout 1.0
    $ renpy.pause(2.0, hard=True)

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    hide ym_02

    
    show ym_01 at top_fade
    play sound_bg audio.millenniumitem noloop
    "(Você desbloqueou o capítulo\nsecreto do \"Oh Man\"!!!)"
    play sound ctc
    
    hide ym_01
    "{p=2.0}{nw}"

    stop music
    stop sound_bg
    scene black

    $ register_ending("mara")

    show screen texto_final_mara
    with Dissolve(0.5)
    

    pause 1.5
    hide screen texto_final_mara
    with Dissolve(0.5)
    

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



