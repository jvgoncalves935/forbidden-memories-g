label cap01_03_futebol01:
    $ drpc_update("cap01")
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
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
    voice voz_cap01_03_07
    "E aê, legal?"
    play sound ctc
    voice voz_cap01_03_08
    "Belê."
    play sound ctc
    voice voz_cap01_03_09
    "Segura a bola, mano."
    play sound ctc
    voice voz_cap01_03_10
    "Firmeza, tranquilo?"
    play sound ctc
    voice voz_cap01_03_11
    "Chega aí, Indião!"
    play sound ctc
    voice voz_cap01_03_12
    "E aí, beleza?"
    play sound ctc
    voice voz_cap01_03_13
    "Demoraram, hein mano..."
    play sound ctc
    voice voz_cap01_03_14
    "Ow, o pessoal tá... vai chegar mais\ntarde, o pessoal!"
    play sound ctc
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

    voice voz_cap01_03_16
    "Da pra gente fazer uma brincadeira\naí! Jogar uma bola..."
    play sound ctc

    voice voz_cap01_03_17
    "É, jogar uma bola, lógico né?"
    play sound ctc
    voice voz_cap01_03_18
    "Então... mas já que o pessoal vai\nchegar mais tarde, pô, quê que\nvocês acham de fazer\numa brincadeira?"
    play sound ctc
    voice voz_cap01_03_19
    "Ahhh... bem que seria bom, né?"
    play sound ctc
    voice voz_cap01_03_20
    "Demorou!"
    play sound ctc
    voice voz_cap01_03_21
    "Fazer um joguinho diferente, né?"
    play sound ctc
    voice voz_cap01_03_22
    "(tirando as luvas)"
    voice voz_cap01_03_23
    "Caraca! Olha os cara, mano..."
    play sound ctc

    voice voz_cap01_03_24
    "AAAAHHH! HMMMM... NOSSA... OHHH\nASSIM VAIN!"
    play sound ctc
    voice voz_cap01_03_25
    "OOHHH... HMMMM!"
    play sound ctc
    voice voz_cap01_03_26
    "Você viu que horas são?"
    play sound ctc
    voice voz_cap01_03_27
    "Nossa, vamo já vestir a roupa!"
    play sound ctc
    voice voz_cap01_03_28
    "Pessoal tá chegando aí, vamo, vamo...!"
    play sound ctc
    "(Você ouve uma voz\nna sua cabeça:)"
    play sound ctc
    voice voz_cap01_03_29
    "(Veste, veste, veste!)"
    play sound ctc
    voice voz_cap01_03_30
    "O pessoal tá chegando aí, vai cara!"
    return

label wrong_end_01_03_1:
    $ drpc_update("finalB")
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
    "(Você será a nova estrela do time\ne ele apenas um verme\ninsignificante!)"
    play sound ctc
    "(O Campeonato irá começar em\ninstantes.)"
    play sound ctc
    $ register_ending("B")
    jump game_over



