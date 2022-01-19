label cap03_01_casa01:
    play music celular
    "(celular tocando)"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            call telefone_03_01_01
        "<Recusar a chamada>":
            "Que se dane."
    hide textbox_aux
    stop music
    "Mas que droga, o pessoal do consultório não me liga..."
    play music celular
    "(celular tocando)"
    play sound ctc
    "Mas que porra, hein?!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            call telefone_03_01_02
        "<Recusar a chamada>":
            "Que se dane."
    hide textbox_aux
    stop music
    "Esse telefone não para de tocar, mas que porcaria!"
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "AHHHHHHH...!!!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            call telefone_03_01_03
        "<Recusar a chamada>":
            "Que se dane."
    hide textbox_aux
    stop music
    "NA VIDA DE VOCÊS VAI CAIR MALDIÇÃO"
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "AHHHHHHH...!!!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            pass
        "<Recusar a chamada>":
            jump wrong_end_03_01
    hide textbox_aux
    stop music
    return

label telefone_03_01_01:
    "Alô?"
    play sound ctc
    "Alôr? É do corpo de bombeiro?"
    play sound ctc
    "Não parceiro. Até mais."
    play sound ctc
    "(desliga o telefone)"
    play sound ctc

label telefone_03_01_02:
    "Alô???"
    play sound ctc
    "Alôr? É do corpo de bombeiro?"
    play sound ctc
    "PARA DE ME LIGAR"
    play sound ctc
    "(desliga o telefone)"
    play sound ctc


label telefone_03_01_03:
    "ALÔ!!!"
    play sound ctc
    "Alô, boa noite? Meu nome é Ludmila, eu falo do setor de promoções da operadora Vivo, eu falo com o Vinícius?"
    play sound ctc
    "PARA DE ME ADICIONAR NESSES GRUPO, CAMBARDA DE MARDITO!"
    play sound ctc
    "(VAI TOMAR NO SEU)"
    play sound ctc
    "(desliga o telefone)"
    play sound ctc

label wrong_end_03_01:
    "OH SEU FILHO DA PUTA, PARA DE ME LIGAR"
    jump game_over

label wrong_end_03_01_1:
    $ register_ending("M")
    jump game_over

