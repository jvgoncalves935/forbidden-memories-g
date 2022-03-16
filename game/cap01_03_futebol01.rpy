label cap01_03_futebol01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    #(Goleiro 00:00 - 00:02)
    voice voz_cap01_03_01
    "{p=7.0}{nw}"
    play sound ctc
    "(Goleiro de Família começa a\nouvir vozes em sua cabeça:)"
    play sound ctc
    voice voz_cap01_03_02
    "(Vem caminhando pra frente,\nchutando a bola...)"
    play sound ctc
    voice voz_cap01_03_03
    "{p=4.0}{nw}"
    play sound ctc
    voice voz_cap01_03_04
    "(Começa a quicar ela...)"
    play sound ctc
    voice voz_cap01_03_05
    "(Chama teus amigos...)"
    play sound ctc
    voice voz_cap01_03_06
    "Ô meu, chega aê..."
    play sound ctc
    #(Senna 00:03 - 00:03)
    voice voz_cap01_03_07
    "E aê, legal?"
    play sound ctc
    #(Goleiro 00:13 - 00:13)
    voice voz_cap01_03_08
    "Belê."
    play sound ctc
    #(Goleiro 00.07:05 - 00.08:05)
    voice voz_cap01_03_09
    "Segura a bola, mano."
    play sound ctc
    #(Senna 00:13 - 00:14)
    voice voz_cap01_03_10
    "Firmeza, tranquilo?"
    play sound ctc
    #(Goleiro 00:15 - 00:15)
    voice voz_cap01_03_11
    "Chega aí, Indião!"
    play sound ctc
    #(Goleiro 00:18 - 00:19)
    voice voz_cap01_03_12
    "E aí, beleza?"
    play sound ctc
    #(John 00:21 - 0:22)
    voice voz_cap01_03_13
    "Demoraram, hein mano..."
    play sound ctc
    #(Senna 00:24 - 00:28)
    voice voz_cap01_03_14
    "Ow, o pessoal tá... vai chegar mais\ntarde, o pessoal!"
    play sound ctc
    #(Goleiro 00:29 - 00:29)
    voice voz_cap01_03_15
    "Ihh..."
    play sound ctc

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Treinar pênaltis com seu time>":
            jump wrong_end_01_03_1
        "<Propor uma brincadeira>":
            pass
    hide textbox_aux
    stop music

    #(Senna 00:30 - 00:31)
    voice voz_cap01_03_16
    "Da pra gente fazer uma brincadeira\naí! Jogar uma bola..."
    play sound ctc

    voice voz_cap01_03_17
    "É, jogar uma bola, lógico né?"
    play sound ctc
    #(Senna 00:40 - 00:46)
    voice voz_cap01_03_18
    "Então... mas já que o pessoal vai\nchegar mais tarde, pô, quê que\n vocêsacham da gente fazer\numa brincadeira?"
    play sound ctc
    #(John 00:46 - 00:47)
    voice voz_cap01_03_19
    "Ahhh... bem que seria bom, né?"
    play sound ctc
    #(Goleiro 00:49 - 00:49)
    voice voz_cap01_03_20
    "Demorou!"
    play sound ctc
    #(Senna 00:50 - 00:54)
    voice voz_cap01_03_21
    "Fazer um joguinho diferente, né?"
    play sound ctc
    voice voz_cap01_03_22
    "(tirando as luvas)"
    #(John 01:02 - 01:04)
    voice voz_cap01_03_23
    "Caraca! Olha os cara, mano..."
    play sound ctc

    #(John 01:04 - 01:11)
    voice voz_cap01_03_24
    "AAAAHHH! HMMMM... NOSSA... OHHH\nASSIM VAIN!"
    play sound ctc
    voice voz_cap01_03_25
    "OOHHH... HMMMM!"
    play sound ctc
    #(Senna 01:14 - 01:15)
    voice voz_cap01_03_26
    "Você viu que horas são?"
    #(Goleiro 01:15 - 01:16)
    play sound ctc
    voice voz_cap01_03_27
    "Nossa, vamo já vestir a roupa!"
    #(Senna 01:15 - 01:16)
    play sound ctc
    voice voz_cap01_03_28
    "Pessoal tá chegando aí, vamo, vamo...!"
    #(John 01:20 - 01:20)
    play sound ctc
    "(Você ouve uma voz\nna sua cabeça:)"
    play sound ctc
    voice voz_cap01_03_29
    "(Veste, veste, veste!)"
    #(Senna 01:22 - 01:23)
    play sound ctc
    voice voz_cap01_03_30
    "O pessoal tá chegando aí, vai cara!"
    return

label wrong_end_01_03_1:
    stop music
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
    "(Você será a nova estrela do time!)"
    play sound ctc
    "(O Campeonato irá começar em\ninstantes.)"
    play sound ctc
    $ register_ending("B")
    jump game_over



