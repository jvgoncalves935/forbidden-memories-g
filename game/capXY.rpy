label capXY:
    #Yuri encontra Seto
    $ drpc_update("capXY")
    play sound menu_start

    stop music
    show textbox_black at center
    "{p=4.0}{nw}"
    hide black

    play music fm_kaiba_faceoff
    "(Em algum universo paralelo\ndentro do Kenoverso...)"
    play sound ctc

    "(Simplesmente ele:)"
    play sound ctc

    "(Oh Man, a versão \"Ativa\"\ndo Yeah Man!)"
    play sound ctc

    stop music fadeout 1.0
    "{p=1.0}{nw}"
    play music fm_inside_the_puzzle

    "aaaaaaaaa"
    play sound ctc

    hide textbox_black
    "{p=1.0}{nw}"

    stop music
    stop sound_bg
    scene black
    #$ register_ending("CXY")

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    
    return



