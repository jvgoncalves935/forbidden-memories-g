label cap01_04_futebol02:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    #(Índio 01:25 - 1:27)
    play music audio.fm_finals_faceoff
    voice voz_cap01_04_01
    "Que putaria é essa aí de pau duro aí,\nolha aí!"
    play sound ctc
    #(Índio 01:26 - 1:31)
    voice voz_cap01_04_02
    "Porra, vamo lá jogar esse futebol,\nvamo lá... Bora galera!"
    play sound ctc
    voice voz_cap01_04_03
    "Chega aê, chega aê!"
    play sound ctc
    #(Figurante2 01:37 - 1:39)
    voice voz_cap01_04_04
    "Demoraram, hein?"
    play sound ctc
    #(Figurante3 01:39 - 01:40)
    voice voz_cap01_04_05
    "Eita, quê que rolou aí, porra?"
    #(Senna 01:41 - 01:42)
    play sound ctc
    voice voz_cap01_04_06
    "A gente tava aquecendo!"
    #(Figurante4 01:46 - 01:48)
    play sound ctc
    voice voz_cap01_04_07
    "Aquecimento, aquecimento, cara!"
    play sound ctc
    voice voz_cap01_04_08
    "ÊÊÊÊ, esse aquecimento aí, hein!"
    #(Figurante4 01:50 - 01:51)
    play sound ctc
    voice voz_cap01_04_09
    "Ow beleza, como é que vai?"
    #(Goleiro 01:50 - 01:51)
    #(Senna 01:53 - 01:54)
    play sound ctc
    voice voz_cap01_04_10
    "É, e esse pintão aí?"
    #(Figurante5 01:59 - 2:00)
    play sound ctc
    voice voz_cap01_04_11
    "Eeeeeeee, aí teve, hein?!"
    play sound ctc
    voice voz_cap01_04_12
    "Ahhhhhhh, aos cara!"
    play sound ctc
    voice voz_cap01_04_13
    "Quem foi que deu pra quem aí?\n(multidão)"
    #(Índio 02:06 - 02:10)
    play sound ctc
    voice voz_cap01_04_14
    "TROCA-TROCA? (ihhh ihhh)"
    play sound ctc
    voice voz_cap01_04_15
    "QUEM QUE DEU PRA QUEM AÍ?"
    play sound ctc
    voice voz_cap01_04_16
    "AAAAAAAAAAHHH! AAAAHHH,\ntu deu pra ele, né?"
    #(Senna 02:11 - 02:19)
    play sound ctc
    voice voz_cap01_04_17
    "Tsc tsc tsc, dei nada! A gente só\ntava aquecendo aê, ow Davis... só tava\naquecendo aí ó, os cara...\nNada a ver...!"
    #(Figurante5 02:22 - 02:23)
    play sound ctc
    voice voz_cap01_04_18
    "Vamo aê, vamo aê!"
    play sound ctc
    voice voz_cap01_04_19
    "Tá me tirando, meu!"
    play sound ctc
    stop music

    $ renpy.movie_cutscene("mod_assets/videos/pelada_james_01.webm")
    
    stop music
    play music "<from 56.2>mod_assets/music/fm_finals.ogg"

    show pelada_james_05
    "{p=1.06}{nw}"
    hide pelada_james_05

    show pelada_james_02

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            hide textbox_aux
            jump wrong_end_01_04_1
        "<Defender para direita>":
            hide textbox_aux
            hide pelada_james_02
            pass
    
    stop music

    play music "<from 21.066>mod_assets/music/fm_finals.ogg"
    queue music audio.fm_finals

    show pelada_james_03
    voice voz_cap01_04_20
    "OLHA A BOMBAAA! AÍ, MEU GOLEIRO!{p=2.5}{nw}"
    hide pelada_james_03

    #(John 02:54 - 02:58)
    voice voz_cap01_04_21
    "ISSO MEU GOLEIRO!! ISSO, ISSO, ISSO!"
    play sound ctc
    voice voz_cap01_04_22
    "ISSO, ISSO, ISSO, FALOU\nMEU GOLEIRO!"
    #(Senna 02:58 - 02:59)
    play sound ctc
    voice voz_cap01_04_23
    "Valeu!"
    play sound ctc
    "(Você levou uma dedada de James\nMatarazzo!)"
    #(John 02:59 - 03:00)
    play sound ctc
    voice voz_cap01_04_24
    "Simbora, simbora, simbora!"
    play sound ctc

    show pelada_james_06
    "{p=3.6}{nw}"
    hide pelada_james_06

    show pelada_james_05
    "{p=1.06}{nw}"
    hide pelada_james_05

    show pelada_james_02

    $ pos_music = renpy.music.get_pos("music")
    stop music

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            hide pelada_james_02
            hide textbox_aux
            jump wrong_end_01_04_2
        "<Defender para esquerda>":
            hide textbox_aux
            hide pelada_james_02
            pass
    stop music

    $ renpy.music.play("<loop 21.066 from {}>mod_assets/music/fm_finals.ogg".format(pos_music))

    show pelada_james_04
    voice voz_cap01_04_21
    "ISSO MEU GOLEIRO!! ISSO, ISSO, ISSO!{p=2.4}{nw}"
    play sound ctc
    hide pelada_james_04

    voice voz_cap01_04_22
    "ISSO, ISSO, ISSO, FALOU\nMEU GOLEIRO!"
    #(Senna 02:58 - 02:59)
    play sound ctc

    show pelada_james_05
    "{p=1.06}{nw}"
    hide pelada_james_05

    show pelada_james_02

    $ pos_music = renpy.music.get_pos("music")
    stop music

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Defender para cima>":
            hide pelada_james_02
            hide textbox_aux
            jump wrong_end_01_04_3
        "<Defender para direita>":
            hide pelada_james_02
            hide textbox_aux
            pass
    
    stop music

    $ renpy.music.play("<loop 21.066 from {}>mod_assets/music/fm_finals.ogg".format(pos_music))

    show pelada_james_03
    voice voz_cap01_04_21
    "ISSO MEU GOLEIRO!! ISSO, ISSO, ISSO!{p=2.4}{nw}"
    play sound ctc
    hide pelada_james_03
    
    voice voz_cap01_04_23
    "Valeu!"
    play sound ctc
    voice voz_cap01_04_24
    "Simbora, simbora, simbora!"
    play sound ctc
    voice voz_cap01_04_25
    "Marca porra, não deixa o\ncara vim!"
    #(figurante6 03:07 - 03:08)
    play sound ctc

    stop music

    voice voz_cap01_04_26
    "AHHHHHH, ARGH!\nAAAAAAAAARRRRRGH!"
    play sound ctc
    voice voz_cap01_04_27
    "Não foi nada, não foi\nnada!"
    #(Senna 03:10 - 03:13)
    play sound ctc
    voice voz_cap01_04_28
    "O cara machucou, o cara\nmachucou! Você é animal?"
    play sound ctc
    voice voz_cap01_04_29
    "Tira o tênis dele ae oh,\ntira o tênis dele ae oh!"
    #(Machucado 03:02 - 03:33)
    play sound ctc
    voice voz_cap01_04_30
    "Pô, pera aí, pera, pera..."
    play sound ctc
    voice voz_cap01_04_31
    "Leva ele lá embaixo, meu!\nLeva ele lá embaixo!"
    #(Figurante7 0:35 - 03:36)
    play sound ctc
    voice voz_cap01_04_32
    "Calma, calma, calma,\ncalma, calma...!"
    #(Índio 03:40 - 03:49)
    play sound ctc
    voice voz_cap01_04_33
    "Pode deixar que a gente leva ele lá!"
    play sound ctc
    voice voz_cap01_04_34
    "A gente toma conta dele!\n(OW QUEIMA ROSCA DO CARALHO!)"
    play sound ctc
    voice voz_cap01_04_35
    "Ok, vamo lá!"
    #(Senna 03:51 - 03:52)
    play sound ctc
    voice voz_cap01_04_36
    "O cara machucou mesmo?"
    #(Goleiro 03:53 - 03:55)
    play sound ctc
    voice voz_cap01_04_37
    "Ah meu, o cara machucou o cara!\n(discussão entre os jogadores)"
    #(índio 03:57 - 03:59)
    play sound ctc
    voice voz_cap01_04_38
    "E agora, a gente vai fazer o\nquê, cara? Falta três agora,\nfalta três agora!"
    #(índio 04:00 - 04:05)
    play sound ctc
    voice voz_cap01_04_39
    "Vai vim junto? Vai cair dentro?\nNão vai cair dentro, então\nvamo sentar e e vamo esperar, pô!"
    #(Senna 04:10 - 04:00)
    voice voz_cap01_04_40
    "Vai cair dentro? Não vai, né.\nEntão vamo esperar!"
    play sound ctc
    voice voz_cap01_04_41
    "Ow senta ai ow, senta ai!"
    #(índio 04:14 - 04:26)
    play sound ctc
    voice voz_cap01_04_42
    "Que que é, mano? Que que é?\nQue que é? Que que é?"
    play sound ctc
    voice voz_cap01_04_43
    "Quê que é? Bom jogo, mano!\nBom jogo! Tá todo mundo\njogando junto aqui, mano!"
    #(índio 04:30 - 04:38)
    play sound ctc
    voice voz_cap01_04_44
    "Aqui oh, tomei uma aqui também, e aí?\nNão, tomei uma aqui também, olha aqui, \ntá roxo aqui, vei! Olha aqui o\nmaluco! Olha aqui! É, TIME\nDA FRESCURA!"
    #(Goleiro2 04:49 - 04:47)
    play sound ctc
    "(uma hora e meia depois)"
    play sound ctc
    voice voz_cap01_04_45
    "Caralho hein, já se passaram horas e\nos cara nada. Puta merda, tá\nquase anoitecendo já! Foda..."
    #(John 04:48 - 04:55)
    play sound ctc
    voice voz_cap01_04_46
    "Eu não te falei, velho? Eles tão é\ntrepando, maluco! Eles tão é trepando\ngostoso!"
    play sound ctc
    voice voz_cap01_04_47
    "Aí, oh galera, eu vo dar\no fora, falou?"
    play sound ctc
    voice voz_cap01_04_48
    #Senna(05:00 0 05:01)
    "E AIIIII, CARAAAALHO...? Ah, tô indo\nembora mano, tá escurescendo o\nbagulho..."
    play sound ctc
    voice voz_cap01_04_49
    "Essa porra melada aí, mano!\nEsse pau duro aí, vei!"
    play sound ctc
    voice voz_cap01_04_50
    "AAAAAH, TÔ SABEEEENDO!!!"
    play sound ctc
    voice voz_cap01_04_51
    "OLHA AQUI, OH, OH, OH, OH!\nAÍ! AÍ PAU DURO, AEEEEE!!!"
    play sound ctc
    voice voz_cap01_04_52
    "Vish, nós cuidamo, bicho!\nVamo voltar o jogo."
    play sound ctc
    "(40 minutos depois)"
    play sound ctc

    play music fm_youwin

    "(O jogo se encerra com a\nvitória do seu time!)"
    play sound ctc
    "(Agora todos estão indo embora\npara casa comemorar...)"
    voice voz_cap01_04_53
    "Falou, falou!"
    #(índio 05:16 - 05:18)
    play sound ctc
    voice voz_cap01_04_54
    "Que tesão, hein? Gostosão..."
    play sound ctc

    stop music
    return

label wrong_end_01_04_common:
    stop music
    play music audio.fm_youlose noloop

    show pelada_james_07
    "{p=10.15}{nw}"
    hide pelada_james_07

    stop music
    scene black
    
    "(VOCÊ ERROU A BOLA E TOMOU UM GOL!)"
    play sound ctc
    "(Seu time perdeu a partida e agora\ntodos estão extremamente irritados\ncom você!)"
    play sound ctc
    "(Você nunca mais vai ter outra\noportunidade para vencer no\nCampeonato G!)"
    play sound ctc
    "(Era sua única oportunidade de\nbrilhar na vida e você\ndesperdiçou ela!)"
    play sound ctc
    "(...)"
    play sound ctc
    return

label wrong_end_01_04_1:
    call wrong_end_01_04_common from _call_wrong_end_01_04_common
    "(Enquanto seu time não para de te\nxingar, você questiona sua própria\nexistência.)"
    play sound ctc
    "Eu não consigo nem defender uma bola\nno gol."
    play sound ctc
    "Essa era a oportunidade da minha vida\ne joguei tudo fora."
    play sound ctc
    "Eu sou real mesmo?"
    play sound ctc
    "Isso tudo é real mesmo?"
    play sound ctc
    $ register_ending("C")
    jump game_over

label wrong_end_01_04_2:
    call wrong_end_01_04_common from _call_wrong_end_01_04_common_1
    "(Você começa a discutir com Índio e\nbotar a culpa nele por não ter\najudado a defender o ataque da\nbola na zaga.)"
    play sound ctc
    "(Revoltadíssimo, ele saca uma faca\ne te apunhala na barriga.)"
    play sound ctc
    "(Você consegue sentir a faca lá no\nestômago, porra, que facona...)"
    play sound ctc
    "(Você cai no chão sem conseguir se\nmover, vendo sua própria vida\nse esVAINdo.)"
    play sound ctc
    "(Todos apavorados começam a fugir do\nÍndio, saindo do campo de\nfutebol o mais rápido possível.)"
    play sound ctc
    "(Índio começa a se aproximar cada vez\nmais perto de você, ainda com a\nfaca na mão e um olhar psicótico.)"
    play sound ctc
    "(Você dá o seu último respiro de\nagonia e desmaia, sem possuir\nmais forças para viver.)"
    play sound ctc
    "(Índio coloca o rosto extremamente\nperto de seu ouvido e\nsussurra algo...)"
    play sound ctc
    "...É BEM A TUA MÃE, SEU FILHO\nDUMA ÉGUA!"
    play sound ctc
    "ÍNDIO É BEM A TUA MÃE, SEU\nFILHO DA PUTA!"
    play sound ctc
    $ register_ending("D")
    jump game_over

label wrong_end_01_04_3:
    call wrong_end_01_04_common from _call_wrong_end_01_04_common_2
    "(Completamente frustrado, você joga\nsuas luvas de goleiro no chão\ne sai correndo do campo.)"
    play sound ctc
    "(Você perdeu o campeonato e foi\nbanido da Série G.)"
    play sound ctc
    "(Seus dias como goleiro\nacabaram.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(três dias depois)"
    play sound ctc
    "\"O Asteroide Guinárnia está em\nrota de colisão da Terra!\""
    play sound ctc
    "\"O tempo aproximado para impacto\ncontra a superfície é de\nexatamente 32 horas!\""
    play sound ctc
    "\"Está previsto que o estrago\ncausado pela colisão resultará\nna extinção de toda a vida humana!\""
    play sound ctc
    "\"O caos preenche as ruas de\nCupiqueno e de todo o mundo. Assaltos,\nestupros e assassinatos tomam conta do\ncenário pré-apocaliptico.\""
    play sound ctc
    "\"Este é o nosso fim. Protejam-se\nem suas casas ou em abrigos\nmais próximos!\""
    play sound ctc
    "(Você desliga o rádio após ouvir\neste delírio coletivo.)"
    play sound ctc
    "RAPAZ, CÊ TÁ MALUCO?"
    play sound ctc
    "Coisa mais esquisita."
    play sound ctc
    "(É possível ouvir sirenes e\npessoas gritando nas ruas como\nse não houvesse amanhã.)"
    play sound ctc
    "(Será que as notícias no\nrádio eram verdade?)"
    play sound ctc
    "(O que você faria se elas\nfossem?)"
    play sound ctc
    "(Pensando em uma resposta, você\ndecide voltar a dormir. Amanhã será\numa noite difícil no seu turno\ncomo segurança.)"
    play sound ctc
    "\"Onde foi que eu deixei minhas\nluvas de goleiro?\", você pensa\nconsigo."
    play sound ctc
    "(Você sente uma sensação sinistra\nao pensar que perdeu elas.)"
    play sound ctc
    "(Inexplicavelmente, um sentimento\nde culpa bate em você lá no\nestômago, porra.)"
    play sound ctc
    "(Algo que você nunca sentiu em\ntoda a sua vida.)"
    play sound ctc
    "(Logo após, você se lembra de uma\nteoria que leu em uma revista\nde ficção científica:)"
    play sound ctc
    "\"O Efeito Borboleta\""
    play sound ctc
    $ register_ending("E")
    jump game_over