label cap02_04_roda_amigos:
    $ drpc_update("cap02-2")
    scene black
    stop music
    show textbox_black at center

    #show intro_001 at top
    play music fm_library
    voice voz_cap02_04_01
    "Foi mó legal lá na balada,\nvocês perderam meu..."
    play sound ctc
    
    voice voz_cap02_04_02
    "A gente perdeu o quê?"
    play sound ctc
    
    voice voz_cap02_04_03
    "Ah... Bagnight meu... foi muito louco\nlá!"
    play sound ctc
    
    voice voz_cap02_04_04
    "Mas tinha muita coisa de bom lá?"
    play sound ctc
    
    voice voz_cap02_04_05
    "Nossa senhora... vocês perderam! Ixi,\ntinha muita gente, muita mina... foi\nmuito louco... muito louco mesmo!"
    play sound ctc
    
    voice voz_cap02_04_06
    "Essas balada dele aí acho que é meio\nfurada...!"
    play sound ctc
    
    voice voz_cap02_04_07
    "Que furada?"
    play sound ctc
    
    voice voz_cap02_04_08
    "Lembra aquela que a gente foi lá?"
    play sound ctc
    
    voice voz_cap02_04_09
    "Aquela foi!"
    play sound ctc
    
    voice voz_cap02_04_10
    "Você devia ver, a putaria que rolou\nsolta... né, ow índio? A\nputaria rolou solta..."
    play sound ctc
    
    voice voz_cap02_04_11
    "Não, não, é sério... putaria foi o que\neu fiz outro dia aí com os cara...\nEu saí com os amigos, entendeu?"
    play sound ctc
    
    voice voz_cap02_04_12
    "Aí a gente começou a... a brincar,\na zuar entendeu... Fazer uma\nbrincadeira diferente... Entendeu...?"
    play sound ctc
    
    voice voz_cap02_04_13
    "Aahh, a brincadeira, a\nbrincadeira dele..."
    play sound ctc
    
    voice voz_cap02_04_14
    "É furada essa brincadeira dele!"
    play sound ctc
    
    voice voz_cap02_04_15
    "Não, essa brincadeira não é furada não,\nessa brincadeira é...\nBATATA, muito boa..."
    play sound ctc
    
    voice voz_cap02_04_16
    "Aqui a gente não dá pra fazer essa\nbrincadeira porque a gente é amigo,\nmas dá pra usar a imaginação..."
    play sound ctc
    
    voice voz_cap02_04_17
    "E como é que é?"
    play sound ctc
    
    voice voz_cap02_04_18
    "Ah... tipo... a brincadeira mesmo\né: \"O Que Você Faria Se?\"."
    play sound ctc
    
    voice voz_cap02_04_19
    "Faria o quê?"
    play sound ctc
    
    voice voz_cap02_04_20
    "Uma coisa muito boa..."
    play sound ctc
    
    voice voz_cap02_04_21
    "Que brincadeira é essa... é as mesmas\nde sempre...? Explica um pouco!"
    play sound ctc
    
    voice voz_cap02_04_22
    "Vou explicar direitinho pra você...\nComo é que é o negócio: você\nimagina assim um cara gostosão,\nentendeu?"
    play sound ctc
    
    voice voz_cap02_04_23
    "Todo malhadão, moreno, entendeu? Numa,\nnuma piscina assim, saindo de uma\npiscina, entendeu? Todo malhado,\naqueles braço enorme, entendeu?"
    play sound ctc
    
    voice voz_cap02_04_24
    "Aquela dessa assim, te olhando, se\npegando assim, passando a mão,\nentendeu... Imagina assim... só vai\nimaginando agora, aquele homem te\ncatando assim..."
    play sound ctc
    
    voice voz_cap02_04_25
    "Puta meu, mó tesão assim, oh..."
    play sound ctc
    
    voice voz_cap02_04_26
    "Tá, para..."
    play sound ctc
    
    voice voz_cap02_04_27
    "Te pegar assim oh, te pegar e colocar\nem você assim oh, num lugar,\nentendeu..."
    play sound ctc
    
    voice voz_cap02_04_28
    "Bem, te pegar ali na piscina mesmo,\nentendeu? Começar a fazer assim,\naquelas coisas assim... bem...\ndiferente contigo..."
    play sound ctc
    stop music

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Repreender esse espírito maligno>":
            hide textbox_aux
            jump wrong_end_02_04_1
        "<Entrar no Mundo dos Sonhos>":
            hide textbox_aux
            pass
    stop music

    play music fm_map_select_2
    voice voz_cap02_04_29
    "Posso imaginar...?"
    play sound ctc
    
    voice voz_cap02_04_30
    "Pode, claro!"
    play sound ctc
    
    voice voz_cap02_04_31
    "Então tá..."
    play sound ctc
    
    voice voz_cap02_04_32
    "Fala sua imaginação pra gente..."
    play sound ctc
    
    "(Você adentra no Mundo dos Sonhos.)"
    play sound ctc
    
    stop music fadeout 2.0
    "(...)"
    play sound ctc
    
    "(Você está sozinho, no meio de uma\npiscina misteriosa...)"
    play sound ctc
    
    voice voz_cap02_04_33
    "Pô, essa piscina aqui sozinha...\ne eu queria o homem\ndos meus sonhos... Poxa..."
    play sound ctc
    
    play music fm_egyptian_duel
    "(Um homem misterioso emerge da\nsauna!)"
    play sound ctc
    
    "(Ele é extremamente forte e\nmusculoso...)"
    play sound ctc
    
    voice voz_cap02_04_34
    "Você não pediu o homem dos seus\nsonhos...? Aqui estou!"
    play sound ctc
    
    voice voz_cap02_04_35
    "Pô, você é real mesmo...?\nNão acredito..."
    play sound ctc
    
    voice voz_cap02_04_36
    "Tudo isso só pra mim..."
    play sound ctc
    
    voice voz_cap02_04_40
    "{p=14.0}{nw}"
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop voice
    stop music


    
    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()  


    $ register_ending("C2")
    play music fm_youwin
    scene black

    show capitulo_concluido
    pause 1.0
    play sound voz_cap02_04_44
    pause 3.7
    play sound voz_cap02_04_45
    pause 4.26
    hide capitulo_concluido
    
    show voce_desbloqueou
    show carta_img_cap_02
    show carta_desc_cap_02
    pause 1.5
    play sound voz_cap02_04_46
    pause 5.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 4.0

    hide voce_desbloqueou
    hide carta_img_cap_02
    hide carta_desc_cap_02

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    return


label wrong_end_02_04_1:
    $ drpc_update("finalL")
    stop music
    
    play music fm_seto_encounter
    voice voz_cap02_04_37
    "EU AMALDIÇOO TODO MUNDO QUE FAZ PARTE\nDESSE GRUPO!"
    play sound ctc
    
    voice voz_cap02_03_02
    "NA VIDA DE VOCÊS VAI CAIR MALDIÇÃO!"
    play sound ctc
    
    voice voz_cap02_03_04
    "NÃO TEM O QUE FAZER NÃO, RAPAZ?"
    play sound ctc
    
    voice voz_cap02_04_38
    "VAI SE FODER!"
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound plates_dropping
    "(Furioso, você vira a mesa no chão,\nderrubando tudo com muita\nignorância.)"
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound door_kick
    "(Logo em seguida, você dá um chute com\ntoda a força na porta e sai\ncorrendo daquela casa.)"
    play sound ctc
    
    "(É inadmissível para você ser\nconsiderado como homossexual.)"
    play sound ctc
    
    "(Você é hétero!)"
    voice voz_cap02_04_41
    "EU SOU HÉTERO!"
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    
    play music fm_high_mages_duel
    "(Você começa a fugir da casa\ndo Mangueira Boy.)"
    play sound ctc
    
    "(Você continua correndo na rua.)"
    play sound ctc
    
    voice voz_cap02_04_41
    "EU SOU HÉTERO!"
    play sound ctc
    
    play sound_bg siren2 fadein 3.0
    "(Ainda correndo na rua, você nota que\nestá sendo seguido...)"
    play sound ctc
    
    "É a polícia...!"
    play sound ctc
    
    "(De repente, um policial surge\nrepentinamente da sua frente e pula\nem cima de você, te imobilizando.)"
    play sound ctc
    
    voice voz_cap02_04_39
    "AHHHHHH!"
    play sound ctc
    
    "\"Você que é o ladrão de residências\nde Cupiqueno?\", diz o policial."
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound handcuffs
    "(Enquanto ele faz a pergunta, ele\ncomeça a te algemar!)"
    play sound ctc
    
    voice voz_cap02_04_42
    "EU SOU HÉTERO! EU SOU HÉTERO!"
    play sound ctc
    
    "\"Parece que ele está sob efeito de\nnarcóticos, será necessário uma análise\ndetalhada na delegacia.\""
    play sound ctc
    
    "\"Esse aí tá mais pro Presídio\nAry Fontoura!\""
    play sound ctc
    
    voice voz_cap02_04_41
    "EU SOU HÉTERO!"
    play sound ctc
    
    voice voz_cap02_04_43
    "EU SOU HÉTERO...!"
    play sound ctc
    
    stop music fadeout 2.0
    stop sound_bg fadeout 3.0
    $ register_ending("L")
    jump game_over
    return