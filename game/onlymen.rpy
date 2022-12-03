label onlymen:
    
    play sound menu_start

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    $ play_video("mod_assets/videos/onlymen.webm","forbidden_memories_intro_web")

    
    "Alexandre Senna no OnlyFans AMV\nOnly Men (MC VV)\nMúsica: Only Men\nArtista: MC VV prod. Launzera\nÁlbum: BONDA 2 (MC VV)"
    play sound ctc

    stop music
    stop sound_bg
    scene black
    
    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



