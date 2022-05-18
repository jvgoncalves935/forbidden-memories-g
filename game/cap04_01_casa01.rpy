label cap04_01_casa01:
    $ drpc_update("cap04-1")
    
    scene black
    stop music

    show header_cap_04 at intro_cap
    pause 7.0
    hide header_cap_04 

    show textbox_black at center
    #show intro_001 at top
    play music fm_map_select_2
    "(...)"
    play sound ctc

    "(Hmm... ainn...)"
    stop music fadeout 1.5
    play sound ctc
    
    "(...)"
    play sound ctc
    
    play music fm_modern_times
    "(Você está na academia fazendo seus\ntreinos de fisiculturismo.)"
    play sound ctc
    
    "(Parece que chegou um aparelho novo\nna academia...)"
    play sound ctc
    
    "(Ele é meio... diferente...)"
    play sound ctc
    
    voice voz_cap04_01_01
    stop music
    "Ahhh, que exercício ótimo..."
    play sound ctc
    
    voice voz_cap04_01_02
    "Que máquina BOA cara... Porra..."
    play sound ctc
    
    voice voz_cap04_01_03
    "Tô sentindo o músculo\ndo meu CU crescer..."
    play sound ctc
    
    voice voz_cap04_01_04
    "Isso, assim..."
    play sound ctc
    
    "(...)"
    play sound ctc
    
    voice voz_cap05_01_02
    stop music
    "AAAAIIII!"
    play sound ctc
    
    "..."
    play sound ctc
    
    play music fm_library
    "Outro sonho, de novo..."
    play sound ctc
    
    "Que sonho bom, cara."
    play sound ctc
    
    "Nossa, coisa mais esquisita..."
    play sound ctc
    
    "Tô sentindo uma dor lá no estômago,\nporra..."
    play sound ctc
    
    "Será que foi alguma coisa que eu\ncomi antes de dormir?"
    play sound ctc
    
    "Não lembro de ter comido nada\ntão pesado-"
    play sound ctc
    
    play sound_bg celular
    stop music
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
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    play music fm_shadi_future
    "Fala meu querido, tudo bem?"
    play sound ctc
    
    voice voz_cap04_01_05
    "YEAH MAN!"
    play sound ctc
    
    "Eu já tô indo aí pra academia, só tô\narrumando umas coisas aqui\nem casa primeiro..."
    play sound ctc
    
    "Você já chegou na esquina aqui já?"
    play sound ctc
    
    voice voz_cap04_01_06
    "YEAH MAN!"
    play sound ctc
    
    "Beleza, querido. Espera só dois\nminutinhos."
    play sound ctc
    
    voice voz_cap04_01_05
    "YEAH MAN!"
    play sound ctc
    
    "Tudo bem, falou."
    play sound ctc
    
    voice voz_cap04_01_07
    "OH CARALHO!"
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o celular)"     
    play sound ctc
    
    "Esse cara é louco, puta que\npariu... Só me meto\ncom louco cretino!"
    play sound ctc
    
    play sound_bg celular
    stop music
    "(celular tocando)"
    play sound ctc
    
    "Lá vem de novo essa bosta!"
    play sound ctc

    show textbox_aux
    menu:
        "<Atende essa porra>":
            hide textbox_aux
            stop sound_bg
            "{p=0.2}{nw}"
            play sound phone_click
            "Alou?"
            play sound ctc
            voice voz_cap03_01_01
            play music fm_preliminary_faceoff
            "ALOR, É DO CORPO DE BOMBEIRO?"
            play sound ctc
            voice voz_cap04_01_08
            "AH MULEQUE, VAI SE FODER\nMANO! E AÍ, ESQUECE O\nMEU NÚMERO!"
            play sound ctc
            voice voz_cap04_01_09
            "VAI TOMAR NO OLHO DO\nSEU CU, MANO!"
            play sound ctc
            "{p=0.2}{nw}"
            play sound phone_click
            "(desligou o celular)"
            play sound ctc
            voice voz_cap04_01_10
            "Ah vai dar meia hora de\nbunda, cara chato..."
            play sound ctc
            stop music fadeout 2.0

        "<Não>":
            hide textbox_aux
            stop sound_bg
            "{p=0.2}{nw}"
            play sound phone_click
            "(desligou o celular)"
            play sound ctc
            "Foda-se, não era nada\nimportante mesmo."
            play sound ctc
    stop sound_bg

    "Ok, vou botar o kimono e já\nto vazando..."
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice

    return

label wrong_end_04_01_1:
    $ drpc_update("finalQ")
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    play music fm_nameinput
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
    
    "(Você deixa seu celular em casa\ne vai para o Parque Kukepal.)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice

    window hide(None)
    $ game_over_pos_cutscene = True
    $ renpy.movie_cutscene("mod_assets/videos/skate.webm")
    $ register_ending("Q")
    jump game_over
    return


