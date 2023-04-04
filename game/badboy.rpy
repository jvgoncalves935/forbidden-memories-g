label badboy:
    
    play sound menu_start

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    $ play_video("mod_assets/videos/badboy.webm","forbidden_memories_intro_web")

    
    "Bad Boy de Família e\nFelipe Dylon de Família"
    play sound ctc

    stop music
    stop sound_bg
    scene black
    
    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



