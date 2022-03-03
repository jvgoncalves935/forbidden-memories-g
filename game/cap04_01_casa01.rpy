label cap04_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Nossa, coisa mais esquisita..."
    play sound ctc
    "Tô sentindo uma dor lá no estômago, porra..."
    play sound ctc
    "Será que foi alguma coisa que eu comi antes de dormir?"
    play sound ctc
    "Não lembro de ter comido nada tão pesado-"
    play sound ctc
    "(celular tocando)"
    play sound ctc
    "NÃO TEM UM DIA DE SOSSÊGO, NÉ?"
    play sound ctc
    "Hmm, pera aí..."
    play sound ctc
    "Hoje é o dia do judô, né?"
    play sound ctc
    "Tô com uma preguiça do caralho pra ir pro treino, que droga."
    play sound ctc
    "Aí, sabia que era o Yeah Man me ligando pra ir pro treino."
    play sound ctc
    "Atende essa porra ou não?"
    play sound ctc
    show textbox_aux
    menu:
        "<Atende essa porra>":
            pass
        "<Não>":
            hide textbox_aux
            jump wrong_end_04_01_1
    hide textbox_aux
    "Fala meu querido, tudo bem?"
    play sound ctc
    "(YEAH MAN!)"
    play sound ctc
    "Eu já tô indo aí pra academia, só tô arrumando umas coisas aqui em casa primeiro..."
    play sound ctc
    "Você já chegou na esquina aqui já?"
    play sound ctc
    "(YEAH MAN!)"
    play sound ctc
    "Beleza, querido. Espera só dois minutinhos."
    play sound ctc
    "(YEAH MAN!)"
    play sound ctc
    "Tudo bem, falou."
    play sound ctc
    "(OH CARALHO, OH!)"
    play sound ctc
    "(desligou o telefone)"     
    play sound ctc
    "Esse cara é louco, puta que pariu..."
    play sound ctc
    "Ok, vou botar o kimono e já to vazando..."
    play sound ctc
    "(...)"
    play sound ctc
    "(Na academia...)"
    play sound ctc
    stop music
    return

label wrong_end_04_01_1:
    stop music
    "Que se foda aquele esquizofrênico do caralho."
    play sound ctc
    "Vai ver se eu tô lá na esquina!"
    play sound ctc
    "Pior que o retardado deve estar me esperando lá mesmo..."
    play sound ctc
    "Foda-se, pode ficar o dia inteiro aí, otário."
    play sound ctc
    "(...)"
    play sound ctc
    "Porra meu, tô querendo fazer uma parada... diferente, saca..."
    play sound ctc
    "Tô achando que eu vou dar uma volta no parque e é isso aí."
    play sound ctc
    "(...)"
    play sound ctc
    $ renpy.movie_cutscene("mod_assets/videos/skate.webm")
    $ register_ending("Q")
    jump game_over


