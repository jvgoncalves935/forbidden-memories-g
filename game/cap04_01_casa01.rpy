label cap04_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Nossa, coisa mais esquisita..."
    play sound ctc
    "Tô sentindo uma dor lá no estômago,\nporra..."
    play sound ctc
    "Será que foi alguma coisa que eu\ncomi antes de dormir?"
    play sound ctc
    "Não lembro de ter comido nada\ntão pesado-"
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "NÃO TEM UM DIA DE SOSSÊGO, NÉ?"
    play sound ctc
    "Hmm, pera aí..."
    play sound ctc
    "Hoje é o dia do judô, né?"
    play sound ctc
    "Tô com uma preguiça do caralho pra\nir pro treino, que droga."
    play sound ctc
    "Aí, sabia que era o Yeah Man me\nligando pra ir pro treino."
    play sound ctc
    "Atende essa porra ou não?"
    play sound ctc
    show textbox_aux
    menu:
        "<Atende essa porra>":
            hide textbox_aux
            pass
        "<Não>":
            hide textbox_aux
            jump wrong_end_04_01_1
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "Fala meu querido, tudo bem?"
    play sound ctc
    "YEAH MAN!"
    play sound ctc
    "Eu já tô indo aí pra academia, só tô\narrumando umas coisas aqui\nem casa primeiro..."
    play sound ctc
    "Você já chegou na esquina aqui já?"
    play sound ctc
    "YEAH MAN!"
    play sound ctc
    "Beleza, querido. Espera só dois\nminutinhos."
    play sound ctc
    "YEAH MAN!"
    play sound ctc
    "Tudo bem, falou."
    play sound ctc
    "OH CARALHO, OH!"
    play sound ctc
    "(desligou o telefone)"     
    play sound ctc
    "Esse cara é louco, puta que\npariu... Só me meto\ncom louco cretino!"
    play sound ctc
    "Ok, vou botar o kimono e já\nto vazando..."
    play sound ctc
    "(...)"
    play sound ctc
    "(Na academia...)"
    play sound ctc
    stop music
    return

label wrong_end_04_01_1:
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "Que se foda aquele esquizofrênico\ndo caralho."
    play sound ctc
    "Vai ver se eu tô lá na esquina!"
    play sound ctc
    "Pior que o retardado deve estar me\nesperando lá mesmo..."
    play sound ctc
    "Foda-se, pode ficar o dia inteiro\naí, otário."
    play sound ctc
    "(...)"
    play sound ctc
    "Porra meu, tô querendo fazer uma\nparada... diferente, saca..."
    play sound ctc
    "Tô achando que eu vou dar uma\nvolta no parque e é isso aí."
    play sound ctc
    "(...)"
    play sound ctc

    window hide(None)
    $ game_over_pos_cutscene = True
    $ renpy.movie_cutscene("mod_assets/videos/skate.webm")
    $ register_ending("Q")
    jump game_over


