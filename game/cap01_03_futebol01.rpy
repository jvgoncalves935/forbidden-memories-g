label cap01_03_futebol01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    #(Goleiro 00:00 - 00:02)
    "Ô meu, chega aê..."
    play sound ctc
    #(Senna 00:03 - 00:03)
    "E aê, legal?"
    play sound ctc
    #(Goleiro 00.07:05 - 00.08:05)
    "Segura a bola, mano."
    play sound ctc
    #(Goleiro 00:13 - 00:13)
    "Belê?"
    play sound ctc
    #(Senna 00:13 - 00:14)
    "Firmeza, tranquilo?"
    play sound ctc
    #(Goleiro 00:15 - 00:15)
    "Tranquilo!"
    play sound ctc
    #(Senna 00:15.10)
    "Chega aí, Jão!"
    play sound ctc
    #(Goleiro 00:18 - 00:19)
    "Hahahahaha... E aí, beleza mano?"
    play sound ctc
    #(Senna 00:20 - 00:20)
    "E aí?"
    play sound ctc
    #(John 00:21 - 0:22)
    "Beleza. Demoraram, hein?"
    play sound ctc
    #(Senna 00:24 - 00:28)
    "Ow, o pessoal tá... vai chegar mais\ntarde, o pessoal!"
    play sound ctc
    #(Goleiro 00:29 - 00:29)
    "Vixe..."
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
    "Da pra gente fazer uma brincadeira\naí! Jogar uma bola.."
    play sound ctc
    #(Senna 00:40 - 00:46)
    "Então... mas já que o pessoal vai\nchegar mais tarde, quê que vocês\nacham da gente fazer uma\nbrincadeirinha?"
    play sound ctc
    #(John 00:46 - 00:47)
    "Hmmm... bem que seria bom, né?"
    play sound ctc
    #(Goleiro 00:49 - 00:49)
    "Demorou!"
    play sound ctc
    #(Senna 00:49 - 00:49)
    "Hã?"
    play sound ctc
    #(Goleiro 00:50 - 00:50)
    "Demorou!"
    play sound ctc
    #(Senna 00:50 - 00:54)
    "Fazer um joguinho diferente, né?"
    play sound ctc
    #(John 01:02 - 01:04)
    "Caraca! Olha os cara, mano..."
    play sound ctc

    #(John 01:04 - 01:11)
    "AAAAHHH!, NOSSA, HMMMM, ASSIM VAIN!"
    play sound ctc
    #(Senna 01:14 - 01:15)
    "Você viu que horas são?"
    #(Goleiro 01:15 - 01:16)
    play sound ctc
    "Nossa, vamo já vestir a roupa!"
    #(Senna 01:15 - 01:16)
    play sound ctc
    "Pessoal tá chegando aí, vai cara...!"
    #(John 01:20 - 01:20)
    play sound ctc
    "Se veste, se veste, se veste!"
    #(Senna 01:22 - 01:23)
    play sound ctc
    "O pessoal tá chegando aí, vamo!"
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



