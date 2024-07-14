init python:
    def ExtraContentStart(label_name):
        global current_extra_content
        current_extra_content = label_name
        
        renpy.jump_out_of_context("extra_content_label")

    def ExtraContentFacelessGames(flag):
        global faceless_games_active_flag
        faceless_games_active_flag = flag
        renpy.jump_out_of_context("capFACELESSGAMES")

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

    def ExtraContentRestartError242424():
        persistent.error242424 = False
        persistent.is_error242424_splashscreen = False
        SecretError242424()


    global current_extra_content

label capFACELESSGAMES():
    if(faceless_games_active_flag or persistent.faceless_games_first_time): 
        $ renpy.movie_cutscene("mod_assets/videos/FACELESSGAMES.COM.BR.webm")
    
    $ persistent.faceless_games_first_time = False

    if(faceless_screen_paranoiascope == 0):
        play music blessed_land_of_guzar
    if(faceless_screen_paranoiascope == 1):
        play music faceless_games
    if(faceless_screen_paranoiascope == 2):
        play music FACELESS_CONVERSANDO

    
    if(faceless_screen_paranoiascope < 2):
        $ faceless_screen_paranoiascope += 1
    else:
        $ faceless_screen_paranoiascope = 0 

    $ ShowMenu("faceless_games_scr")()
    
    return

label label_error242424_begin:
    
    $ drpc_update("error242424")
    $ persistent.is_error242424_splashscreen = True

    stop music
    stop sound_bg
    stop voice

    $ play_video("mod_assets/videos/error242424.webm","forbidden_memories_intro_web")
    show conehead
    pause 0.05

    $ renpy.quit()
    
    return

label standing_here_i_realize:
    
    $ play_video("mod_assets/videos/standing_here_i_realize.webm","forbidden_memories_intro_web")
    
    return

label extra_content_modo_faceless:

    $ play_video("mod_assets/videos/blessed_land_of_guzar.webm","forbidden_memories_intro_web")

    if(renpy.windows):
        "Você deseja ativar o MODO FACELESS?"
        play sound ctc
        
        show textbox_aux
        menu:
            "<EU QUERO MANO BLZ>":
                hide textbox_aux
                pause 0.2
                python:
                    try:
                        init_subprocess("FACELESSVIRUS.exe")
                    except:
                        pass
                pause 7.0
                "EAE MANO BLZ?"
            "<AH NÃO, EU TÔ DE BORA...>":
                hide textbox_aux
                play sound to_de_bora
                "AH NÃO, EU TÔ... TÔ DE BORA..."
    else:
        play music MARCELO_MUSICA
        "MODO FACELESS disponível apenas\npara Windows blz????"
        play sound ctc
        "Se você quer descobrir o que é o\nMODO FACELESS, jogue o jogo no\nWindows ou procure gameplay\nno YouTube xddd"
        play sound ctc
    if(renpy.linux):
        "Eu juro que eu tentei de\ntudo pra essa porra\nfuncionar no Linux, mas\ncoisa de jogo/interface gráfica\nno Linux é uma merda kkkk"
        play sound ctc
        "É por isso que Linux não tem\njogo nenhum blz??????"
        play sound ctc
        "Deu até erro de driver nessa\nmerda de código KKKKKKKKKKK"
        play sound ctc
        "Cogitei até em chupar meu\npróprio pau, mas no final\nacabei largando fodase"
        play sound ctc
        "use linux cim amiginho\né muinto bom"
        play sound ctc
    if(renpy.macintosh):
        "Infelizmente eu precisava de um Mac\npra fazer isso, mas não\nconheço ninguém que tenha."
        play sound ctc
        "Ao menos que você queira\nme dar um Macbook blzzz????"
        play sound ctc
    if(renpy.mobile):
        "Infelizmente é impossível criar\no MODO FACELESS pra mobile."
        play sound ctc
        "Precisaria de um aplicativo\nseparado pra fazer isso."
        play sound ctc
        "Aí eu teria que chupar\nmeu próprio pau xddddddd"
        play sound ctc
    return
    

label extra_content_label:
    play sound menu_start

    stop music
    
    show textbox_black at center
    "{p=4.0}{nw}"

    call expression "extra_content_"+current_extra_content from _call_expression

    window hide(None)
    stop music
    stop sound_bg
    scene black
    
    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")
    #$ MainMenu()
    #$ ShowMenu("endings")()

    return

label extra_content_mc_vv:
    $ play_video("mod_assets/videos/onlymen.webm","forbidden_memories_intro_web")

    "Alexandre Senna no OnlyFans AMV\nOnly Men (MC VV)\nMúsica: Only Men\nArtista: MC VV prod. Launzera\nÁlbum: BONDA 2 (MC VV)"
    play sound ctc

    $ play_video("mod_assets/videos/churrasco_gino.webm","forbidden_memories_intro_web")
    
    "Churrasco do Paulo Gino AMV\nNamorada Vegana (MC VV)\nMúsica: Namorada Vegana\nArtista: BOFE\nÁlbum: BONDA (MC VV)"
    play sound ctc

    return

label extra_content_badboy:
    $ play_video("mod_assets/videos/badboy.webm","forbidden_memories_intro_web")

    "\"Felipe De Nylon quebra a matrix\"\n\nFelipe de Nylon G e Boy Stronda\n(Badboy de Família, Rico Vidal)"
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

label extra_content_magrinho:
    $ play_video("mod_assets/videos/magrinho.webm","forbidden_memories_intro_web")

    "\"Teste G do Magrinho\"\n\"Bait and Switch: The Big Deception\"\n\nMagrinho, Alemão e Bob"
    play sound ctc
    
    return

label extra_content_akuma_de_familia:
    $ play_video("mod_assets/videos/akuma_de_familia.webm","forbidden_memories_intro_web")

    "\"Akuma de Família\"\n\nAkuma de Família e Alexandre Senna"
    play sound ctc
    
    return

label extra_content_saci:
    $ play_video("mod_assets/videos/saci.webm","forbidden_memories_intro_web")

    "\"O Saci de Duas Pernas\"\n\nSaci de Duas Pernas e\nCUripira G"
    play sound ctc
    
    return

label extra_content_papai_noel:
    $ play_video("mod_assets/videos/papai_noel.webm","forbidden_memories_intro_web")

    "\"Papai Noel de Família\"\n\nPapai Noel da Hot Boys"
    play sound ctc
    
    return

label extra_content_zeh:
    $ play_video("mod_assets/videos/zeh.webm","forbidden_memories_intro_web")

    "\"Zeh Está Bolado (Dublado)\"\nZeh Está Bolado (Bolado de\nFamília, Gomez Aguilar)"
    play sound ctc
    
    return

label extra_content_corvo:
    $ play_video("mod_assets/videos/corvo.webm","forbidden_memories_intro_web")

    "\"Corvo Jailson Mendes\""
    play sound ctc
    
    return

label extra_content_mara_mara:
    $ play_video("mod_assets/videos/mara_mara.webm","forbidden_memories_intro_web")

    "\"mara mara\"\n\nhttps://mara-mara.itch.io/mara-mara"
    play sound ctc
    
    return

label extra_content_alemao_escravo:
    $ play_video("mod_assets/videos/alemao_escravo.webm","forbidden_memories_intro_web")

    "\"Escravo do Meu Mestre\"\n\nAlemão Escravo e Carrasco G"
    play sound ctc
    
    return

label extra_content_senhor_dos_anais:
    $ play_video("mod_assets/videos/senhor_dos_anais.webm","forbidden_memories_intro_web")

    "\"Senhor dos Anais\""
    play sound ctc
    
    return

label extra_content_nimpf:
    $ play_video("mod_assets/videos/nimpf.webm","forbidden_memories_intro_web")

    "\"nine inch metal pipes fodase\"\n\nRemix: Macho\nTrack Original: The Perfect Drug\nArtista: Nine Nich Nails"
    play sound audio.barra_de_metal

    $ play_video("mod_assets/videos/intro.webm","forbidden_memories_intro_web")

    jump extra_content_nimpf_end
    
    return

label extra_content_nimpf_end:
    window hide(None)
    play sound audio.barra_de_metal
    $ renpy.full_restart()
    return

label extra_content_ursos_grandes:
    "como seria os créditos do fim\ndo mundo:"
    play sound ctc

    pause 0.5

    $ play_video("mod_assets/videos/ursos_grandes01.webm","forbidden_memories_intro_web")

    "como eu gostaria que realmente fosse:"
    play sound ctc

    pause 0.5
    window hide(None)
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/ursos_grandes02.webm","forbidden_memories_intro_web")
    
    return

label extra_content_dramatv:
    call cap05_00_padeiro from _call_cap05_00_padeiro

    pause 2.0

    "\"Sonho do Padeiro G\"\n\nDublagem: DRAMA TV 3D"
    play sound ctc

    return

label extra_content_ana:
    $ play_video("mod_assets/videos/ana.webm","forbidden_memories_intro_web")

    "\"Senna e a Anã\"\n\nAlexandre Senna e a Anã Ativa"
    play sound ctc
    
    return

label extra_content_vurlcao:
    $ play_video("mod_assets/videos/vurlcao.webm","forbidden_memories_intro_web")

    "\"Cena do Vurlcão\"\n\nAlexandre Senna e o Vurlcão"
    play sound ctc

    if(renpy.windows):
        "Você deseja ativar o MODO SENNINHA?"
        play sound ctc
        
        show textbox_aux
        menu:
            "<EU QUERO VAIN>":
                hide textbox_aux
                pause 0.2
                python:
                    try:
                        init_subprocess("SENNINHAVIRUS.exe")
                    except:
                        pass
                pause 7.0
                "EAE MANO BLZ?"
            "<AH NÃO, EU TÔ DE BORA...>":
                hide textbox_aux
                play sound to_de_bora
                "AH NÃO, EU TÔ... TÔ DE BORA..."
    else:
        play music MARCELO_MUSICA
        "MODO SENNINHA disponível apenas\npara Windows blz????"
        play sound ctc
        "Se você quer descobrir o que é o\nMODO SENNINHA, jogue o jogo no\nWindows ou procure gameplay\nno YouTube xddd"
        play sound ctc
    if(renpy.linux):
        "Eu juro que eu tentei de\ntudo pra essa porra\nfuncionar no Linux, mas\ncoisa de jogo/interface gráfica\nno Linux é uma merda kkkk"
        play sound ctc
        "É por isso que Linux não tem\njogo nenhum blz??????"
        play sound ctc
        "Deu até erro de driver nessa\nmerda de código KKKKKKKKKKK"
        play sound ctc
        "Cogitei até em chupar meu\npróprio pau, mas no final\nacabei largando fodase"
        play sound ctc
        "use linux cim amiginho\né muinto bom"
        play sound ctc
    if(renpy.macintosh):
        "Infelizmente eu precisava de um Mac\npra fazer isso, mas não\nconheço ninguém que tenha."
        play sound ctc
        "Ao menos que você queira\nme dar um Macbook blzzz????"
        play sound ctc
    if(renpy.mobile):
        "Infelizmente é impossível criar\no MODO SENNINHA pra mobile."
        play sound ctc
        "Precisaria de um aplicativo\nseparado pra fazer isso."
        play sound ctc
        "Aí eu teria que chupar\nmeu próprio pau xddddddd"
        play sound ctc
    play sound ctc
    return
    
    return

label extra_content_coringa_dano:
    $ play_video("mod_assets/videos/coringa_dano.webm","forbidden_memories_intro_web")

    "\"Entrevista Alexandre Senna PapoMix\"\n\nCoringa Dano"
    play sound ctc
    
    return

label extra_content_toqueo_couhl:
    $ play_video("mod_assets/videos/toqueo_couhl.webm","forbidden_memories_intro_web")

    "\"Alexandre Senna em TOQUEO COUHL\""
    play sound ctc
    
    return

label extra_content_mangueira_evil:
    $ play_video("mod_assets/videos/e_o_que_voce_faria.webm","forbidden_memories_intro_web")

    "\"E O Que Você Faria?\"\nAlexandre e Índio\n\nVain e Come, Operation: Senna"
    play sound ctc
    
    return

label extra_content_maldita_hora:
    $ play_video("mod_assets/videos/maldita_hora_1.webm","forbidden_memories_intro_web")
    
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/maldita_hora_2.webm","forbidden_memories_intro_web")
    
    $ play_video("mod_assets/videos/maldita_hora_3.webm","forbidden_memories_intro_web")

    "\"Alexandre Senna no Banco\"\n\nAlexandre Senna e Renzo"
    play sound ctc
    
    return

label extra_content_ricardo_milos:
    $ play_video("mod_assets/videos/ricardo_milos.webm","forbidden_memories_intro_web")

    "\"Ricardo Milos\""
    play sound ctc
    
    return

label extra_content_indiana_torres:
    $ play_video("mod_assets/videos/indiana_torres_1.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/indiana_torres_1_cena_g.webm","forbidden_memories_intro_web")

    "\"Indiana Torres - Parte 1/4\"\n\"Bare Ass Bandidos\"\n\nDouglas Torres (Yeah Man)"
    play sound ctc

    $ play_video("mod_assets/videos/indiana_torres_2.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/indiana_torres_2_cena_g.webm","forbidden_memories_intro_web")

    "\"Indiana Torres - Parte 2/4\"\n\"Bare Ass Bandidos\"\n\nDouglas Torres (Yeah Man),\nAlexandre Senna e Alemão"
    play sound ctc

    $ play_video("mod_assets/videos/indiana_torres_3.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/indiana_torres_3_cena_g.webm","forbidden_memories_intro_web")

    "\"Indiana Torres - Parte 3/4\"\n\"Bare Ass Bandidos\"\n\nDouglas Torres (Yeah Man)"
    play sound ctc

    $ play_video("mod_assets/videos/indiana_torres_4.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/indiana_torres_4_cena_g.webm","forbidden_memories_intro_web")
    $ play_video("mod_assets/videos/indiana_torres_5.webm","forbidden_memories_intro_web")

    "\"Indiana Torres - Parte 4/4\"\n\"Bare Ass Bandidos\"\n\nDouglas Torres (Yeah Man)"
    play sound ctc
    
    return

label extra_content_senna_dona_de_casa:
    $ play_video("mod_assets/videos/senna_dona_de_casa.webm","forbidden_memories_intro_web")

    "\"Alexandre Senna Dona de Casa\"\n\nAlexandre Senna e Ucraniano\nde Família"
    play sound ctc
    
    return

label extra_content_xaropinho_de_familia:
    $ play_video("mod_assets/videos/xaropinho_de_familia.webm","forbidden_memories_intro_web")

    "\"Xaropinho de Família\""
    play sound ctc
    
    return

label extra_content_jo_abdul:
    $ play_video("mod_assets/videos/jo_abdul.webm","forbidden_memories_intro_web")

    "\"Jô Abdul e Demacol\"\n\nJô Abdul e Demacol\n(Ivan Holmes)"
    play sound ctc
    
    return

label extra_content_guilhotina_g:
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/guilhotina_g.webm","forbidden_memories_intro_web")

    "\"Guilhotina G\"\n\nJames Matarazzo e Índio (Indígena)"
    play sound ctc
    
    return

label extra_content_caverna_g:
    $ play_video("mod_assets/videos/caverna_g.webm","forbidden_memories_intro_web")

    "\"Alexandre Senna na Caverna\"\n\nCaverna G"
    play sound ctc
    
    return

label extra_content_pai_de_familia_1:
    play music duelista_de_familia
    show primeiro_machinho at top_fade
    "{p=1.2}{nw}"

    "Você se diz fã do Pai de Família?"
    play sound ctc

    "Só é fã DE VERDADE MESMO quem\nassistiu Pai de Família\nsem censura!"
    play sound ctc

    hide primeiro_machinho
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/jailson_mendes.webm","forbidden_memories_intro_web")

    play music duelista_de_familia
    show primeiro_machinho at top_fade

    "E assim nasceu o Universo G!"
    play sound ctc

    "Já parou pra pensar que alguém teve\nque editar o Pai de Família 1\npela primeira vez?"
    play sound ctc

    "Ou seja, pelo menos algum herói teve\nque assistir o vídeo original\nsem censura xdddddd"
    play sound ctc

    "\"Pai de Família 1\"\n\nJailson Mendes e Paulo Gino"
    play sound ctc
    
    hide primeiro_machinho
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    
    return

label extra_content_boys_do_ano:
    $ play_video("mod_assets/videos/boys_do_ano.webm","forbidden_memories_intro_web")

    "\"Boys do Ano\"\n\nAlexandre Senna e Mangueira Evil"
    play sound ctc
    
    return

label extra_content_os_bem_vestidos:
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/os_bem_vestidos.webm","forbidden_memories_intro_web")

    "\"Os Bem Vestidos\"\n\nAlexandre Senna e Bob"
    play sound ctc
    
    return

label extra_content_rocky_gaucho:
    $ play_video("mod_assets/videos/reveillon_de_familia.webm","forbidden_memories_intro_web")

    "\"Rocky Gaúcho no Réveillon de Família\"\n\nRocky Gaúcho"
    play sound ctc

    $ play_video("mod_assets/videos/rocky_gaucho.webm","forbidden_memories_intro_web")

    "\"Rocky - A Revanche do Garanhão\"\n\nRocky Gaúcho e Passivão Desumilde\n(Marcelo Lagoas)"
    play sound ctc
    
    return

label extra_content_paulo_gino_piscineiro:
    $ play_video("mod_assets/videos/paulo_gino_piscineiro.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/paulo_gino_piscineiro_cena_g.webm","forbidden_memories_intro_web")

    "\"The Biggest Dick I Ever Had\"\n\nPaulo Gino Piscineiro\nPaulo Gino Limpador de Piscina"
    play sound ctc
    
    return

label extra_content_mangueira_boy:
    $ play_video("mod_assets/videos/mangueira_boy.webm","forbidden_memories_intro_web")
    if(persistent.streamer_mode):
        call censored_content
    else:
        $ play_video("mod_assets/videos/mangueira_boy_cena_g.webm","forbidden_memories_intro_web")

    "\"Mangueira Boy\"\n\nPaulo Gino Bombeiro e\nMangueira Boy ao som de\nArt Attack 4"
    play sound ctc
    
    return