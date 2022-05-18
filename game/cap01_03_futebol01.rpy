label cap01_03_futebol01:
    $ drpc_update("cap01")
    scene black
    play music fm_modern_shop
    show textbox_black at center
    #show intro_001 at top
    voice voz_cap01_03_01
    show img_01_03_01 at top_fade
    "{p=2.0}{nw}"
    
    hide img_01_03_01
    show img_01_03_02 at top_fade
    "{p=2.0}{nw}"
    
    hide img_01_03_02
    show img_01_03_03 at top_fade
    "{p=3.0}{nw}"

    hide img_01_03_03
    show img_01_03_04 at top_fade
    "(Goleiro de Família começa a\nouvir vozes em sua cabeça:)"
    play sound ctc

    hide img_01_03_04
    show img_01_03_05 at top_fade
    voice voz_cap01_03_02
    "(Vem caminhando pra frente,\nchutando a bola...)"
    play sound ctc

    hide img_01_03_05
    show img_01_03_06 at top_fade
    voice voz_cap01_03_03
    "{p=1.5}{nw}"

    hide img_01_03_06
    show img_01_03_07 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_07
    show img_01_03_08 at top_fade
    voice voz_cap01_03_04
    "(Começa a quicar ela...)"
    play sound ctc

    voice voz_cap01_03_01
    hide img_01_03_08
    show img_01_03_09 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_09
    show img_01_03_10 at top_fade
    "{p=2.0}{nw}"

    hide img_01_03_10
    show img_01_03_11 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_11
    show img_01_03_12 at top_fade
    voice voz_cap01_03_05
    "(Chama teus amigos...)"
    play sound ctc

    voice voz_cap01_03_01
    hide img_01_03_12
    show img_01_03_13 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_13
    show img_01_03_14 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_14
    show img_01_03_15 at top_fade
    voice voz_cap01_03_06
    "Ô meu, chega aê..."
    play sound ctc

    hide img_01_03_15
    show img_01_03_16 at top_fade
    voice voz_cap01_03_07
    "E aê, legal?"
    play sound ctc
    
    hide img_01_03_16
    show img_01_03_17 at top_fade
    voice voz_cap01_03_08
    "Belê."
    play sound ctc

    hide img_01_03_17
    show img_01_03_18 at top_fade
    voice voz_cap01_03_09
    "Segura a bola, mano."
    play sound ctc
    
    hide img_01_03_18
    show img_01_03_19 at top_fade
    voice voz_cap01_03_10
    "Firmeza, tranquilo?"
    play sound ctc
    
    hide img_01_03_19
    show img_01_03_20 at top_fade
    voice voz_cap01_03_11
    "Chega aí, Indião!"
    play sound ctc
    
    hide img_01_03_21
    show img_01_03_22 at top_fade
    voice voz_cap01_03_12
    "E aí, beleza?"
    play sound ctc
    
    hide img_01_03_22
    show img_01_03_23 at top_fade
    voice voz_cap01_03_13
    "Demoraram, hein mano..."
    play sound ctc
    
    hide img_01_03_20
    show img_01_03_21 at top_fade
    voice voz_cap01_03_14
    "Ow, o pessoal tá... vai chegar mais\ntarde, o pessoal."
    play sound ctc
    
    hide img_01_03_23
    show img_01_03_24 at top_fade
    voice voz_cap01_03_15
    "Ihh..."
    play sound ctc

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Treinar pênaltis com seu time>":
            hide textbox_aux
            jump wrong_end_01_03_1
        "<Propor uma brincadeira>":
            hide textbox_aux
            pass
    stop music
    play music fm_preliminary_duel

    hide img_01_03_24
    show img_01_03_25 at top_fade
    voice voz_cap01_03_16
    "Da pra gente fazer uma brincadeira\naí! Jogar uma bola..."
    play sound ctc

    hide img_01_03_25
    show img_01_03_23 at top_fade
    voice voz_cap01_03_17
    "É, jogar uma bola, lógico né?"
    play sound ctc
    
    hide img_01_03_23
    show img_01_03_27 at top_fade
    voice voz_cap01_03_18
    "Então... mas já que o pessoal vai\nchegar mais tarde, pô, quê que\nvocês acham de fazer\numa brincadeira?"
    play sound ctc
    
    hide img_01_03_25
    show img_01_03_26 at top_fade
    voice voz_cap01_03_19
    "Ahhh... bem que seria bom, né?"
    play sound ctc
    
    
    voice voz_cap01_03_20
    "Demorou!"
    play sound ctc
    
    hide img_01_03_27
    show img_01_03_28 at top_fade
    voice voz_cap01_03_21
    "Fazer um joguinho diferente, né?"
    play sound ctc
    
    hide img_01_03_28
    show img_01_03_29 at top_fade
    voice voz_cap01_03_22
    "(tirando as luvas)"

    hide img_01_03_29
    show img_01_03_30 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_30
    show img_01_03_31 at top_fade
    voice voz_cap01_03_23
    "Caraca! Olha os cara, mano..."
    play sound ctc

    hide img_01_03_31
    show img_01_03_32 at top_fade
    "{p=1.5}{nw}"

    hide img_01_03_32
    show img_indio_cavalo at top_fade
    voice voz_cap01_03_24
    "AAAAHHH! HMMMM... NOSSA... OHHH\nASSIM VAIN!"
    play sound ctc
    
    voice voz_cap01_03_25
    "OOHHH... HMMMM!"
    play sound ctc
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    
    hide img_indio_cavalo
    show img_01_03_35 at top_fade
    voice voz_cap01_03_26
    "Você viu que horas são?"
    play sound ctc

    voice voz_cap01_03_27
    "Nossa, vamo já vestir a roupa!"
    play sound ctc
    
    hide img_01_03_35
    show img_01_03_36 at top_fade
    voice voz_cap01_03_28
    "Pessoal tá chegando aí, vamo, vamo...!"
    
    play sound ctc
    "(Goleiro de Família ouve uma\nvoz na sua cabeça:)"
    
    hide img_01_03_36
    show img_01_03_37 at top_fade
    play sound ctc
    voice voz_cap01_03_29
    "(Veste, veste, veste!)"
    play sound ctc

    voice voz_cap01_03_30
    "O pessoal tá chegando aí, vai cara!"
    play sound ctc

    hide img_01_03_37
    return

label wrong_end_01_03_1:
    $ drpc_update("finalB")
    stop music
    play music fm_tournament
    "(Igual qualquer pessoa normal em um\ncampo de futebol, você propõe para os\ncolegas de time a treinarem pênaltis.)"
    play sound ctc

    "(Ambos concordam e vocês começam a\ntreinar para o jogo que irá acontecer\nassim que o outro time chegar.)"
    play sound ctc
    
    "(Índio não consegue acertar nenhum\ngol em você, parece que você virou o\npróprio Rogério Senna em pessoa!)"
    play sound ctc
    
    "(Você nunca defendeu tão bem no gol\nem toda a sua vida!)"
    play sound ctc
    
    "\"Caramba, você não defenderia\nbolas que jamais - teria a capacidade\nde defender!\", diz Índio."
    play sound ctc
    
    "(Você está completamente preparado\npara ganhar o Campeonato G contra o\ntime adversário!)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    "(Parece que eles chegaram.)"
    play sound ctc
    
    "\"PODEM VIR, SEUS FILHOS DA PUTA!\",\nvocê berra com toda a sua força."
    play sound ctc
    
    "(Os adversários tremem de medo de sua\neminente derrota...)"
    play sound ctc
    
    "(Sua vingança contra James será\nabsoluta e implacável!)"
    play sound ctc
    
    "(Você será a nova estrela do time\ne ele apenas um verme\ninsignificante!)"
    play sound ctc
    
    "(O Campeonato irá começar em\ninstantes.)"
    play sound ctc

    stop music fadeout 2.0
    $ register_ending("B")
    jump game_over
    return
