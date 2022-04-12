label cap_arabe:
    $ drpc_update("finalY")
    $ register_ending("Y")

    play sound menu_start
    scene black
    stop music
    show textbox_black at center
    "{p=4.0}{nw}"
    hide black
    
    
    with dissolve
    
    #play sound footsteps
    #show intro_001 at top
    
    #with dissolve
    #scene bg intro_001 at top
    

    play music audio.fm_freeduel
    
    while(True):
        show cap_arabe_img at top
        $ arabe_cont = 0
        while(arabe_cont < 5):
            $ arabe = texto_arabe()
            voice voz_jailson_arabe
            narrator_arabe "[arabe]"
            $ arabe_cont += 1
        hide cap_arabe_img
        show cap_arabe_img2 at top
        $ arabe = texto_arabe()
        voice voz_guina_arabe
        narrator_arabe "[arabe]"
        hide cap_arabe_img2
    return



