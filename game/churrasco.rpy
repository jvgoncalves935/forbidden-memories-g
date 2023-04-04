label churrasco:
    
    play sound menu_start

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    $ play_video("mod_assets/videos/churrasco_gino.webm","forbidden_memories_intro_web")

    
    "Churrasco do Paulo Gino AMV\nNamorada Vegana (MC VV)\nMúsica: Namorada Vegana\nArtista: BOFE\nÁlbum: BONDA (MC VV)"
    play sound ctc

    stop music
    stop sound_bg
    scene black
    
    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



