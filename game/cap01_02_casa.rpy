label cap01_02_casa:
    $ drpc_update("cap01")

    scene black
    stop music

    show header_cap_01 at intro_cap
    pause 7.0
    hide header_cap_01 

    show textbox_black at center
    play music fm_modern_times
    #show intro_001 at top
    "Nossa, hoje é o dia da pelada com o\nJames..."
    play sound ctc
    "Cadê a galera aí pra gente matar a\nsaudade?"
    play sound ctc
    "Bora esperar a ligação de alguém\naí e eu já vou lá pro futebol."
    play sound ctc
    play sound_bg celular

    $ pos_music = renpy.music.get_pos("music")
    stop music
    
    "(celular tocando)"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o celular>":
            hide textbox_aux
            pass
        "<Ignorar>":
            hide textbox_aux
            jump wrong_end_01_02_1
    
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    "{p=0.2}{nw}"
    $ renpy.music.play("<loop 1.633 from {}>mod_assets/music/fm_modern_times.ogg".format(pos_music))
    "Alô?"
    play sound ctc
    "Fala aí Senna, aqui é o Índio,\nbora lá pro futebol\nagora, eu já tô indo mano..."
    play sound ctc
    "Beleza meu querido, já tô saindo\nde casa agora."
    play sound ctc
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o celular)"
    play sound ctc
    "Tava esperando a semana inteira\npra jogar essa bola..."
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    
    return

label wrong_end_01_02_1:
    $ drpc_update("finalA")
    play sound ctc
    "Quer saber? Que se foda esse\ncelular, tô cansado pra caralho..."
    play sound ctc
    "(Você deixa o celular tocando sem\natendê-lo...)"
    play sound ctc
    "(O barulho irritante parece nunca\nter fim...)"
    play sound ctc
    "(Você decide tacar o celular pela\njanela da rua e um carro passa em\ncima dele.)"
    play sound ctc
    "(Mas o celular simplesmente não para\nde tocar.)"
    play sound ctc
    voice voz_cap01_02_01
    "CAMBADA DE DEMÔNIO!"
    play sound ctc
    "(O barulho de seu toque ainda ecoa em\nsua mente, te levando à insanidade...)"
    play sound ctc
    voice voz_cap01_02_02
    "VOCÊS NÃO ME DEIXAM EM PAZ!\n(celular vibrando)"
    play sound ctc
    "(Você decide ir até o aterro\nsanitário mais próximo e enterra o\ncelular satânico no meio da\npilha de lixo.)"
    play sound ctc
    "(Ele ainda não para de tocar, mas\nisso não importa mais.)"
    play sound ctc
    "(Você volta para casa e decide jogar\npalavras-cruzadas.)"
    play sound ctc
    stop sound_bg fadeout 3.0
    $ register_ending("A")
    jump game_over