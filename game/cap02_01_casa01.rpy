label cap02_01_casa01:
    $ drpc_update("cap02-1")
    scene black
    stop music

    show header_cap_02 at intro_cap
    pause 7.0
    hide header_cap_02 

    show textbox_black at center
    #show intro_001 at top
    play music fm_map_select_1
    "Nossa, a pelada ontem foi muito top..."
    play sound ctc
    
    "Deu pra dar uma brincada..."
    play sound ctc
    
    "..."
    play sound ctc
    
    "Mas que droga, eu ainda fiquei de ver\no problema no carro."
    play sound ctc
    
    "Eu tenho certeza que é na mangueira."
    play sound ctc
    
    stop music
    play sound_bg celular
    "(celular tocando)"
    play sound ctc
    
    "Mas que toque irritante esse aí, eu vou\ntrocar essa porcaria!"
    play sound ctc
    
    show textbox_aux
    menu:
        "<Atender o celular>":
            hide textbox_aux
            pass
        "<Desligar>":
            hide textbox_aux
            jump wrong_end_02_01_1
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    "{p=0.2}{nw}"
    play music fm_simon_muran
    "Alô?"
    play sound ctc
    
    "Hello, Alexandrêh!"
    play sound ctc
    
    "Seul charroh estáh quaseh prohtho!\nGostharhia de passahr na oficihnah?"
    play sound ctc
    
    voice voz_cap02_02_37
    "No problem."
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound phone_click
    "(Você desliga o celular e vai em\ndireção à oficina.)"
    
    play sound ctc
    "(Você ainda fica curioso sobre onde\nestava o problema no carro.)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    return

label wrong_end_02_01_1:
    $ drpc_update("finalF")
    stop sound_bg
    
    "{p=0.2}{nw}"
    play sound phone_click
    "(Você desliga o celular rápido bem\nrápido, vai.)"
    play sound ctc
    
    "(\"Eu odeio esse toque!\", você pensa.)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    play music fm_seto_theme
    "(Aleatoriamente, você se lembra de que\no resultado para a prova do concurso\nda Polícia Militar de Cupiqueno havia\nsido divulgado na delegacia.)"
    play sound ctc
    
    "(Você vai correndo para lá, pois com\ncerteza já haviam se passado vários\nmeses que você não procurou\nsaber do resultado.)"
    play sound ctc
    
    "(Chegando lá, você não acredita no que\nacabou de ler:)"
    play sound ctc
    
    stop music fadeout 2.0
    "(Seu nome está na lista de aprovados!)"
    play sound ctc
    
    play music fm_nameinput
    "(Você foi aprovado em primeiro lugar!)"
    play sound ctc
    
    "(Você pergunta para o policial se o\nconcurso do ano havia sido\nencerrado.)"
    play sound ctc
    
    "\"Você deu sorte rapaz, a última chamada\npara os aprovados do concurso será\nexatamente agora!\""
    play sound ctc
    
    "(Você fica incrédulo de como você deu\nmuita muita muita muita muita sorte.)"
    play sound ctc
    
    "(\"Essa foi a escolha dos Deuses G.\",\nvocê pensa.)"
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    play music fm_modern_times
    "(seis meses depois)"
    play sound ctc
    
    play sound_bg audio.radio_chatter
    "(É o seu primeiro dia de ronda\nna Polícia Militar de Cupiqueno!)"
    play sound ctc
    
    stop music
    $ pos_music = renpy.music.get_pos("sound_bg")

    stop sound_bg
    play sound_bg celular
    "(Sua mãe te liga, emocionada com sua\nconquista.)"
    play sound ctc
    
    $ renpy.music.play("<loop 44.7 from {}>mod_assets/sounds/radio_chatter.ogg".format(pos_music),channel="sound_bg")
    play music fm_mages_duel
    "(Você acaba de receber um chamado de\noutra viatura, você apenas\nresponde antes de desligar:)"
    play sound ctc
    
    voice voz_cap02_01_01
    "TÁ ATRAPALHANDO MEU TRABALHO, SEU...!"
    play sound ctc
    
    "{p=0.3}{nw}"
    play sound phone_click
    "(desligou o celular)"
    play sound ctc
    
    "Tenho que atender o chamado\nda viatura...!"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    stop sound_bg
    stop voice
    stop music

    window hide(None)
    $ game_over_pos_cutscene = True
    $ renpy.movie_cutscene("mod_assets/videos/policial.webm")
    $ register_ending("F")
    jump game_over
    return