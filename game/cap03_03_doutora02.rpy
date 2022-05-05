label cap03_03_doutora02:
    $ drpc_update("cap03-2")

    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    play music fm_modern_shop
    "(...)"
    play sound ctc
    "Alexandre, vou te encaminhar para\numa especialista da área."
    play sound ctc
    "A consulta será daqui a uma hora,\nsó aguardar na recepção,\ntudo bem?"
    play sound ctc
    "Ok, tudo certo. Muito obrigado!"
    play sound ctc
    "(Você volta para a sala de recepção.\nSeu cu melhorou um pouco,\nmas ele ainda não parou\nde doer.)"
    play sound ctc
    "Tomara que essa outra doutora seja\nmelhor que a primeira...!"
    play sound ctc
    "(...)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"

    play music fm_map_select_1
    "(uma hora depois)"
    play sound ctc
    
    "AI! AI... Que dor horrível...!"
    play sound ctc
    "A qualquer momento a doutora vai\nme chamar..."
    play sound ctc
    "(...)"
    play sound ctc
    "...Não vai?"
    play sound ctc

    stop music fadeout 1.5
    "{p=2.0}{nw}"

    play music fm_map_select_2
    "(uma hora depois)"
    play sound ctc
    "Caramba, mas que demora!"
    play sound ctc
    "Cadê a secretária?"
    play sound ctc
    "Ué... Ela não tá aqui...?"
    play sound ctc
    "Mas que porcaria é essa?"
    play sound ctc

    stop music fadeout 1.5
    "{p=1.5}{nw}"

    play music fm_map_select_2
    "(cinco horas depois)"
    play sound ctc
    "A bateria do meu celular já acabou\nde tanto jogar o jogo\nda cobrinha..."
    play sound ctc
    "E NADA DA MINHA CONSULTA!"
    play sound ctc
    "Hahh... Tô muito cansado... acho\nque vou tirar um\ncochilo..."
    play sound ctc
    
    stop music fadeout 1.5
    "{p=1.5}{nw}"

    play music fm_inside_the_puzzle
    "(no dia seguinte)"
    play sound ctc
    "Nossa, eu dormi a noite\ninteira...? Não é possível!"
    play sound ctc
    "Onde tá essa doutora, meu Deus\ndo céu?!"
    play sound ctc


    stop music fadeout 1.5
    "{p=1.5}{nw}"

    "(no dia seguinte)"
    play sound ctc
    play music fm_modern_shop
    "Olá, Alexandre! Aqui é a secretária!\nA doutora está te aguardando\nno consultório dela. Pode\nentrar."
    play sound ctc
    "(ATÉ QUE ENFIM SUA VADIA\nDESGRAÇADA...!)"
    play sound ctc
    "(Puta merda, mas que serviço de\natendimento maldito é esse?!)"
    play sound ctc
    "(...)"
    play sound ctc
    stop voice

    stop music fadeout 1.5
    "{p=1.5}{nw}"

    $ renpy.movie_cutscene("mod_assets/videos/doutora01.webm")
    
    play music audio.fm_plazatown
    voice voz_cap03_03_01
    "...Muito boa em toque, eu quero saber\no que tá acontecendo com\nmeu cu... só isso..."
    play sound ctc
    voice voz_cap03_03_02
    "Só coceira, e nada mais?"
    play sound ctc
    voice voz_cap03_03_03
    "Coceira... sinto um calor, sabe aquele\ncalor que sai de dentro, eu não sei o\nque é, tô sentindo umas coisas\nesquisitas..."
    play sound ctc
    voice voz_cap03_03_04
    "Né? E eu sou casado e tudo... e pra mim \né estranho isso daí... Né...\ntem como a senhora dar um\ndiagnóstico e tudo?"
    play sound ctc
    voice voz_cap03_03_05
    "Ah, primeiro eu tenho que dar uma\nolhadinha..."
    play sound ctc
    voice voz_cap03_03_06
    "Então vamo lá?"
    play sound ctc
    voice voz_cap03_03_07
    "Deita na mesa!"
    play sound ctc
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Deitar na mesa>":
            hide textbox_aux
            pass
        "<Chutar a porta e sair correndo>":
            hide textbox_aux
            jump wrong_end_03_03_1
    stop music
    play music audio.fm_plazatown
    voice voz_cap03_03_08
    "Já tô há dias aqui meu... Pô...\nÉ... Roupa de hospital e tudo, né..."
    play sound ctc
    voice voz_cap03_03_09
    "Relaxa e fica à vontade!"
    play sound ctc
    voice voz_cap03_03_10
    "O que a senhora vai fazer...?"
    play sound ctc
    stop music fadeout 2.0
    "(Você sente uma aura malígna vindo\nda doutora, ela é indiscritivelmente\nsombria.)"
    play sound ctc
    voice voz_cap03_03_11
    play music fm_kaiba_faceoff
    "Um exame de toque..."
    play sound ctc
    voice voz_cap03_03_12
    "...Toque?"
    play sound ctc
    "{p=0.2}{nw}"
    play sound chaves_punch
    "(Você levou uma dedada da doutora!)"
    play sound ctc
    voice voz_cap03_03_13
    "Ai doutora... coisa mais esquisita..."
    play sound ctc
    "(Seu instinto de sobrevivência te\ndeixa inquieto, o perigo é\niminente...)"
    play sound ctc
    voice voz_cap03_03_14
    "Cuzinho quentinho também..."
    play sound ctc
    voice voz_cap03_03_15
    "Por enquanto vamos ver... a gente\ntem que dar uma olhadinha\nprofundamente... O que\nvocê acha?"
    play sound ctc
    
    stop music
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Pular da janela do consultório>":
            hide textbox_aux
            jump wrong_end_03_03_2
        "<Elogiar a Doutora>":
            hide textbox_aux
            pass
    stop music
    
    voice voz_cap03_03_16
    "Ah, eu acho que... Você é muito\ngostosa..."
    play sound ctc
    voice voz_cap03_03_17
    "Teria que examinar mais profundamente\nseu reto."
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"

    play music fm_kaiba_theme
    voice voz_cap03_03_18
    "Vai coloca de novo puta... COLOCA NO\nMEU CU CARALHO!"
    play sound ctc
    voice voz_cap03_03_19
    "METE... METE NO MEU CU PUTA... VAI\nPUTA... FODE MEU CU..."
    play sound ctc
    voice voz_cap03_03_20
    "VAI TA CANSADINHA TÁ...? NÃO\nGOSTA DE CU NÃO, PORRA?"
    play sound ctc
    voice voz_cap03_03_21
    "AAHH... AAAAHHH... AAAAAHHHH! FODE!\nFODE...! FODE MEU CU...\nFODE PORRA!"
    play sound ctc
    voice voz_cap03_03_22
    "ISSO...VAI CARALHOOO! METE COM FORÇA\nPORRA... METE..."
    play sound ctc
    voice voz_cap03_03_23
    "METE COM FORÇA... METE COM\nFORÇA... METE NO MEU CU\nCOM FORÇA... METE COM FORÇA...\nMETE..."
    play sound ctc
    voice voz_cap03_03_24
    "VAI ESPANCA MEU CU... VAI ME ESTUPRA\nCARALHO... METE COM FORÇA...\nMETE COM FORÇA... ISSOOO!\nAAAH...!"
    play sound ctc
    voice voz_cap03_03_25
    "ISSO, AAAAAHHHH, AAAAHHHHH,\nAAAAIIIIII!!! FODE... FODE RÁPIDO...\nFODE... FODE...!"
    play sound ctc
    voice voz_cap03_03_26
    "FODE RÁPIDO, BEM RÁPIDO\nVAI... VAI VOCÊ NÃO\nTÁ CANSADA... VAI!"
    play sound ctc
    voice voz_cap03_03_27
    "VAI METE, METE, METE,\nMETE, METE NO MEU CU, METE\nRÁPIDO, METE RÁPIDO VAIN, FODE ELE,\nFODE ELE..."
    play sound ctc
    voice voz_cap03_03_28
    "OOOOOOHHHIIHHHH, AAAAAHHHH, AAAAII,\nAIIIII, AI MEU CUHH! UUGH..."
    play sound ctc
    voice voz_cap03_03_29
    "AI QUE DELÍCIA DOUTORA... AI\nDOUTORA, AI DOUTORA,\nAI DOUTORA..."
    play sound ctc
    voice voz_cap03_03_30
    "CARALHO... TO SENTINDO LÁ NO\nESTÔMAGO PORRA, QUE PAUZÃO...\nQUE PAUZÃO GAROTA..."
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"

    play music fm_preliminary_faceoff
    voice voz_cap03_03_31
    "Doutora... Agora eu tô me\nsentindo bem melhor...\nObrigado tá...? A senhora é\nótima."
    play sound ctc
    voice voz_cap03_03_32
    "Sempre que precisar de uma\nconsulta pode vir!"
    play sound ctc
    voice voz_cap03_03_33
    "Tá bom!"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()  


    $ register_ending("C3")
    play music fm_youwin
    scene black

    show capitulo_concluido
    pause 1.0
    play sound voz_cap03_03_36
    pause 3.7
    play sound voz_cap03_03_37
    pause 4.26
    hide capitulo_concluido
    
    show voce_desbloqueou
    show carta_img_cap_03
    show carta_desc_cap_03
    pause 1.5
    play sound voz_cap03_03_35
    pause 5.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 4.0

    hide voce_desbloqueou
    hide carta_img_cap_03
    hide carta_desc_cap_03

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()
    

    return

label wrong_end_03_03_1:
    $ drpc_update("finalO")
    stop music
    play music fm_3d_duel
    "(Você se levanta da cadeira de uma\nvez. A Doutora te encara,\nbastante confusa.)"
    play sound ctc
    play sound door_kick
    "(Sem dar satisfação nenhuma para a\ndoutora, você chuta a\nporta com muita ignorância\ne sai correndo.)"
    play sound ctc
    play sound_bg running_footsteps
    "(Você ignora os gritos da\nsecretária e corre o\nmais rápido possível.)"
    play sound ctc
    "(...)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    
    play music fm_shadi_egypt
    "(Faz dez minutos que você está\ncorrendo, parece finalmente ser\numa boa hora para descansar.)"
    stop sound_bg
    play sound ctc
    "Vão tomar no cu, hospital\nmaldito."
    play sound ctc
    play sound_bg energy_source fadein 7.0
    "(Você se encontra na frente do\nFerro-Velho de Cupiqueno, um\nlugar completamente sem\ninteresse para você.)"
    play sound ctc
    stop music fadeout 2.0
    "(Bem, não deveria ter interesse\nnenhum... entretanto, você vê\nde longe um objeto\nbrilhante.)"
    play sound ctc
    
    "(Ele brilha com uma cor laranja muito,\nmuito forte. Que nem nos\nfilmes de ficção.)"
    play sound ctc
    "(Ele fica pulsando, como se\nestivesse vivo.)"
    play sound ctc
    "Isso é uma pedra preciosa?"
    play sound ctc
    "(Inicialmente com medo, você chega\nperto da pedra mágica e\na observa, cautelosamente.)"
    play sound ctc
    play music fm_shadi_future
    "(...)"
    play sound ctc
    "Que se foda."
    play sound ctc
    "(Você pega a pedra mágica, coloca\nno bolso e volta para sua\ncasa como se nada tivesse\nacontecido.)"
    play sound ctc

    stop sound_bg fadeout 2.0
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    
    play sound_bg energy_source fadein 2.0
    play music fm_shadi_egypt
    "(Você chega em casa, ansioso para\nguardar seu novo enfeite\npara casa.)"
    play sound ctc
    "Essa pedra ficaria linda na\nminha sala!"
    play sound ctc
    "(Não deu outra. Você coloca a\npedra laranja na estante\nda sala.)"
    play sound ctc
    "(Pelo menos agora você não\nprecisa mais gastar energia\ncom a luz da sala,\nvocê pensa.)"
    play sound ctc
    "Essa pedra é tão linda..."
    play sound ctc
    stop music fadeout 2.0
    "(...)"
    play sound ctc
    
    stop sound_bg fadeout 2.0
    "{p=2.0}{nw}"

    "(no dia seguinte)"
    play sound ctc
    "(Você acabou de acordar e foi\nlogo para o banheiro escovar\nseus dentes...)"
    play sound ctc
    "(Você foi pegar a escova de\ndentes e olhou para o\nespelho do banheiro...)"
    play sound ctc
    "(...)"
    play sound ctc
    play music fm_seto_encounter
    "(...!)"
    play sound ctc
    #Senna mutante
    voice voz_cap03_03_34
    "{p=4.0}{nw}"

    stop music fadeout 2.0
    $ register_ending("O")
    jump game_over

label wrong_end_03_03_2:
    $ drpc_update("finalP")
    stop music
    play sound running_window_breaking
    play music fm_heishin_theme
    "(Você se levanta rapidamente da mesa\ncomo se não houvesse amanhã e pula\npela janela do segundo andar.)"
    play sound ctc
    "{p=0.2}{nw}"
    play sound running_footsteps
    "(Você lesiona sua perna, mas você\nainda consegue sair correndo pela\nrua.)"
    play sound ctc
    stop music fadeout 2.0
    "(A doutora não pode ser mais vista\nem seu campo de visão,\nparece que você\nconseguiu escapar dela com sucesso.)"
    play sound ctc
    play music fm_vast_shrine
    "(Você reflete sobre o que poderia\nter acontecido caso tivesse\noptado em continuar com\no exame...)"
    play sound ctc
    "EU VOU PROCESSAR ESSE HOSPITAL\nMALIGNO!"
    play sound ctc
    voice voz_cap02_03_02
    "NA VIDA DE VOCÊS VAI CAIR\nMALDIÇÃO!"
    play sound ctc
    "(IndiGUINAdo, você decide abrir\num processo contra o\nConsultório Santa Mônica\npor injúria e difamação.)"
    play sound ctc
    "Fiquei dois dias na fila, levei\numa dedada da doutora e\nmachuquei a perna quando\npulei da janela..."
    play sound ctc
    "Isso tudo vai ir no processo,\nquero nem saber!"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    
    "(no dia do julgamento)"
    play sound ctc
    "(...)"
    play sound ctc
    play music fm_temple_ruins
    "(Você PERDEU o processo contra\no consultório!)"
    play sound ctc
    "(O juiz considerou como\n\"improcedente\" sua acusação\nde difamação.)"
    play sound ctc
    "(Pelo visto, advocacia nunca\npoderia ser o seu\nforte...)"
    play sound ctc
    "(Em retalialção, o consultório\npediu uma indenização de\nR$31.450 reais!)"
    play sound ctc
    "(Você nunca vai conseguir\npagar essa dívida!)"
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    "(duas semanas depois)"
    play sound ctc
    play sound_bg audio.city_02 fadein 4.0
    "(...)"
    play sound ctc
    "(Você está morando na rua.)"
    play sound ctc
    "(Você teve que vender sua casa\ninteira para pagar a dívida,\ne mesmo assim ainda faltam\n1000 reais para pagar.)"
    play sound ctc
    "(A única coisa que você tem é\na sua roupa do corpo.)"
    play sound ctc
    "(Até sua dignidade levaram\nde você.)"
    play sound ctc
    "(Você cogita suas opções para\ntentar arrumar dinheiro.)"
    play sound ctc
    "(Fazer favores, catar lixo,\nroubar...)"
    play sound ctc
    "(Pensar em tudo isso suga\ntodas as suas forças que\ntalvez ainda não foram roubadas.)"
    play sound ctc
    "(Você nem mesmo tem um\ncobertor para dormir\nno chão.)"
    play sound ctc
    "(Cobertor, não existe\n- Deus, não existe.)"
    play sound ctc
    stop sound_bg fadeout 3.0
    $ game_over_musica = False
    $ game_over_delay_musica = 5.0
    $ game_over_fadeout_musica = 5.0
    $ register_ending("P")
    jump game_over



