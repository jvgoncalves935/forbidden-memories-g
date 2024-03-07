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

label extra_content_ursos_e_lolitos:
    $ play_video("mod_assets/videos/ursos_lolitos.webm","forbidden_memories_intro_web")

    "\"Ursos e Lolitos\"\n\nAlex Lesson, Erick Munhoz"
    play sound ctc
    
    return

label extra_content_maluco_do_casebre:
    $ play_video("mod_assets/videos/maluco_casebre.webm","forbidden_memories_intro_web")

    "\"Maluco do Casebre\"\n\nEd Hector e Vivian Mello"
    play sound ctc
    
    return

label extra_content_dolph_ziggler:
    $ play_video("mod_assets/videos/dolph_ziggler.webm","forbidden_memories_intro_web")

    "\"Dolph Ziggler de Família\"\n\nClone do Dolph Ziggler e\nMr. Bean de Família"
    play sound ctc
    
    return

label extra_content_indios_papacu:
    $ play_video("mod_assets/videos/indios_papacu.webm","forbidden_memories_intro_web")

    "\"Aldeia dos Índios Papacu\"\n\nJames Matarazzo e os Índios\n(Indígenas) Papacu"
    play sound ctc
    
    return

label extra_content_bizarro_de_familia:
    $ play_video("mod_assets/videos/bizarro_de_familia.webm","forbidden_memories_intro_web")

    "\"Realizando Desejos\"\n\nAndré Ferraz"
    play sound ctc
    
    return

label extra_content_empregado_de_familia:
    $ play_video("mod_assets/videos/empregado_de_familia.webm","forbidden_memories_intro_web")

    "\"Lavando os pratos\"\n\nEmpregado de Família\n(Vin Diesel de Família)"
    play sound ctc
    
    return

label extra_content_entregador_de_pizza_g:
    $ play_video("mod_assets/videos/entregador_de_pizza_g.webm","forbidden_memories_intro_web")

    "\"Vida de Entregador de Pizzas G\"\n\nEntregador de Pizza G"
    play sound ctc
    
    return
