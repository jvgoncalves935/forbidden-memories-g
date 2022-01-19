label cap01_04_futebol02:
    #(Índio 01:25 - 1:27)
    "Que putaria é essa aí de pau duro aí, olha aí!"
    play sound ctc
    #(Índio 01:26 - 1:31)
    "Porra, vamo lá jogar esse futebol... Bora galera!"
    play sound ctc
    #(Figurante2 01:37 - 1:39)
    "Demoraram, hein?"
    play sound ctc
    #(Figurante3 01:39 - 01:40)
    "Eita, quê que rolou aí, porra?"
    #(Senna 01:41 - 01:42)
    play sound ctc
    "Nois tava aquecendo!"
    #(Goleiro 01:41 - 01:42)
    play sound ctc
    "Nois tava aquecendo..."
    #(Figurante2 01:43 - 1:45)
    play sound ctc
    "ÊÊÊÊÊÊÊ..."
    #(Figurante3 01:43 - 01:45)
    play sound ctc
    "EEEEEITA!"
    #(Goleiro 01:44 - 01:45)
    play sound ctc
    "Foi só aquecimento, cara!"
    #(Figurante4 01:46 - 01:48)
    play sound ctc
    "ÊÊÊÊ, esse aquecimento aí, hein!"
    #(Figurante4 01:50 - 01:51)
    play sound ctc
    "E aí beleza, como é que vai?"
    #(Goleiro 01:50 - 01:51)
    play sound ctc
    "E aí, beleza?"
    #(Senna 01:53 - 01:54)
    play sound ctc
    "É, e esse pintão aí?"
    #(Figurante5 01:59 - 2:00)
    play sound ctc
    "Quem foi que deu pra quem aí?"
    #(Índio 02:06 - 02:10)
    play sound ctc
    "AAAAAAAAAAHHH!"
    play sound ctc
    "AAAAHHH, tu deu pra ele, né?"
    #(Senna 02:11 - 02:19)
    play sound ctc
    "Tsc tsc tsc, dei nada! A gente só tava aquecendo aê, ow Davis... só tava aquecendo aí ó, tsc, nada a ver...!"
    #(Figurante5 02:22 - 02:23)
    play sound ctc
    "Tá me tirando, meu!"
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            call wrong_end_01_04_1
        "<Defender para direita>":
            "Que se dane."
    hide textbox_aux
    stop music
    #(John 02:54 - 02:58)
    "Isso meu goleiro, isso meu goleiro, isso, isso, isso!"
    #(Senna 02:58 - 02:59)
    play sound ctc
    "Valeu!"
    play sound ctc
    "(Você levou uma dedada de James Matarazzo!)"
    #(John 02:59 - 03:00)
    play sound ctc
    "Simbora Simbora Simbora!"
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            call wrong_end_01_04_2
        "<Defender para direita>":
            "Que se dane."
    hide textbox_aux
    stop music

    "Isso meu goleiro, isso meu goleiro, isso, isso, isso!"
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            call wrong_end_01_04_3
        "<Defender para direita>":
            "Que se dane."
    hide textbox_aux
    stop music
    "Isso meu goleiro, isso meu goleiro, isso, isso, isso!"
    #(figurante6 03:00 - 03:02)
    play sound ctc
    "Marca porra, não deixa o cara vim!"
    #(figurante6 03:07 - 03:08)
    play sound ctc
    "Ah não foi nada, não foi nada!" 
    #(Senna 03:10 - 03:13)
    play sound ctc
    "Tira o tênis dele ae o, tira o tênis dele ae o!"
    #(Machucado 03:02 - 03:33)
    play sound ctc
    "CARALHO!"
    #(Figurante7 0:35 - 03:36)
    play sound ctc
    "Calma Calma Calma Calma"
    #(Índio 03:40 - 03:49)
    play sound ctc
    "Pode deixar que agente ele lá, levo!, pode deixar, agente toma conta dele!, ok vamo lá!"
    #(Senna 03:51 - 03:52)
    play sound ctc
    "O cara machucou mesmo?"
    #(Goleiro 03:53 - 03:55)
    play sound ctc
    "Ah meu o cara machucou o cara!"
    #(índio 03:57 - 03:59)
    play sound ctc
    "Tu fez na maldade"
    #(Goleiro 03:59 - 04:00)
    play sound ctc
    "Tamo sem 3 Agora!"
    #(índio 04:00 - 04:05)
    play sound ctc
    "Vai vim junto?, vai cair dentro? não vai cair dentro, então da pra esperar pô!"
    #(Senna 04:10 - 04:00)
    play sound ctc
    "O senta ai o, senta ai!"
    #(índio 04:14 - 04:26)
    play sound ctc
    "Que que foi? que que foi?,.... bom jogo mano!, bom jogo!, ta todo mundo jogando junto aqui uai!"
    #(índio 04:30 - 04:38)
    play sound ctc
    "Aqui o tomei uma aqui também ta roxo aqui vei!, olha aqui o maluco, é olha aqui, TIME DA FRESCURA!"
    #(Goleiro2 04:49 - 04:47)
    play sound ctc
    "Caralho eim, já se passaram horas e os cara nada,puta merda ta quase anoitecendo já!.... foda"
    #(John 04:48 - 04:55)
    play sound ctc
    "Eu não te falei maluco?, eles tão é trepando maluco,eles tão é trepando gostoso!, o galera eu vo dar o fora falow?"
    #Senna(05:00 0 05:01)
    play sound ctc
    "Falou falou!"
    #(índio 05:16 - 05:18)
    play sound ctc
    "Que tesão eim?. gostosão!"
    play sound ctc
    return

label wrong_end_01_04_common:
    "(VOCÊ ERROU A BOLA E TOMOU UM GOL!)"
    play sound ctc
    "(Seu time perdeu a partida e agora todos estão extremamente irritados com você!)"
    play sound ctc
    "(Você nunca mais vai ter outra oportunidade para vencer no Campeonato G!)"
    play sound ctc
    "(Era sua única oportunidade de brilhar na vida e você desperdiçou ela!)"
    play sound ctc

label wrong_end_01_04_1:
    call wrong_end_01_04_common
    "(Enquanto seu time não para de te xingar, você questiona sua própria existência.)"
    play sound ctc
    "Eu não consigo nem defender uma bola no gol."
    play sound ctc
    "Essa era a oportunidade da minha vida e joguei tudo fora."
    play sound ctc
    "Eu sou real mesmo?"
    play sound ctc
    "Isso tudo é real mesmo?"
    play sound ctc
    $ register_ending("D")
    jump game_over

label wrong_end_01_04_2:
    call wrong_end_01_04_common
    "(Você começa a discutir com Índio e botar a culpa nele por não ter ajudado a defender o ataque da bola na zaga.)"
    play sound ctc
    "(Revoltadíssimo, ele saca uma faca e te apunhala na barriga.)"
    play sound ctc
    "(Você consegue sentir a faca lá no estômago, porra, que facona...)"
    play sound ctc
    "(Você cai no chão sem conseguir se mover, vendo sua própria vida se esvaindo.)"
    play sound ctc
    "(Todos apavorados começam a fugir do Índio, saindo do campo de futebol o mais rápido possível.)"
    play sound ctc
    "(Índio começa a se aproximar cada vez mais perto de você, ainda com a faca na mão e um olhar psicótico.)"
    play sound ctc
    "(Você dá o seu último respiro de agonia e desmaia, sem possuir mais forças para viver.)"
    play sound ctc
    "(Índio coloca o rosto extremamente perto de seu ouvido e sussurra algo...)"
    play sound ctc
    "...É BEM A TUA MÃE, SEU FILHO DUMA ÉGUA!"
    play sound ctc
    "ÍNDIO É BEM A TUA MÃE, SEU FILHO DA PUTA!"
    play sound ctc
    $ register_ending("E")
    jump game_over

label wrong_end_01_04_3:
    call wrong_end_01_04_common
    $ register_ending("F")
    jump game_over