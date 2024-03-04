init python:
    def ExtraContentStart(label_name):
        global current_extra_content
        current_extra_content = label_name
        
        renpy.jump_out_of_context("extra_content_label")


    def ExtraContentCapXY():
        renpy.jump_out_of_context("capXY")

    def ExtraContentYeahMan():
        renpy.jump_out_of_context("capYM")

    def ExtraContentCapSenna():
        renpy.jump_out_of_context("capSN")

    def ExtraContentCapJailson():
        renpy.jump_out_of_context("capJA")

    def ExtraContentChurrasco():
        renpy.jump_out_of_context("churrasco")

    def ExtraContentOnlyMen():
        renpy.jump_out_of_context("onlymen")

    def ExtraContentBadBoy():
        renpy.jump_out_of_context("badboy")

    def SecretError242424():
        renpy.jump_out_of_context("label_error242424_begin")
    
    def ExtraContentStandingHereIRealize():
        renpy.jump_out_of_context("standing_here_i_realize")

    global current_extra_content

label extra_content_label:
    play sound menu_start

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    call expression "extra_content_"+current_extra_content

    stop music
    stop sound_bg
    scene black
    
    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")

    return

label extra_content_churrasco:

    $ play_video("mod_assets/videos/churrasco_gino.webm","forbidden_memories_intro_web")
    
    "Churrasco do Paulo Gino AMV\nNamorada Vegana (MC VV)\nMúsica: Namorada Vegana\nArtista: BOFE\nÁlbum: BONDA (MC VV)"
    play sound ctc

    return

label extra_content_onlymen:
    $ play_video("mod_assets/videos/onlymen.webm","forbidden_memories_intro_web")

    "Alexandre Senna no OnlyFans AMV\nOnly Men (MC VV)\nMúsica: Only Men\nArtista: MC VV prod. Launzera\nÁlbum: BONDA 2 (MC VV)"
    play sound ctc
    
    return

label extra_content_badboy:
    $ play_video("mod_assets/videos/badboy.webm","forbidden_memories_intro_web")

    "\"Felipe De Nylon quebra a matrix\"\n\nFelipe de Nylon G e Boy Stronda\n(Badboy de Família)"
    play sound ctc
    
    return

label extra_content_felipe_de_nylon:
    $ play_video("mod_assets/videos/felipe_de_nylon.webm","forbidden_memories_intro_web")

    "\"Que bonito bolo, que bonitas velas\"\n\nFelipe de Nylon G e\nPrimo Pobre de Família"
    play sound ctc
    
    return

label standing_here_i_realize:
    
    $ play_video("mod_assets/videos/standing_here_i_realize.webm","forbidden_memories_intro_web")
    
    return

