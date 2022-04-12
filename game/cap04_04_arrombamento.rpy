label cap04_04_arrombamento:
    $ drpc_update("cap04-2")
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    voice voz_cap04_04_01
    "Onde, onde, onde?"
    play sound ctc
    voice voz_cap04_04_02
    "Cadê o arromabento? Foi aqui, foi\naonde?"
    play sound ctc
    voice voz_cap04_04_03
    "Err, por aqui..."
    play sound ctc
    voice voz_cap04_04_04
    "Porra, se ta me tirando mermão?"
    play sound ctc
    voice voz_cap04_04_05
    "Aonde tá tendo arrombamento aqui,\nseu viado?!"
    play sound ctc
    voice voz_cap04_04_06
    "Posso falar a verdade?"
    play sound ctc
    voice voz_cap04_04_07
    "Você tá louco?"
    play sound ctc
    voice voz_cap04_04_08
    "Não, na verdade não teve nada\naqui..."
    play sound ctc
    voice voz_cap04_04_09
    "Onde que teve o arrombamento\naqui, mano?"
    play sound ctc
    voice voz_cap04_04_10
    "TÁ MALUCO, RAPAZ? TÁ ATRAPALHANDO\nMEU TRABALHO, SEU...!"
    play sound ctc
    voice voz_cap04_04_11
    "N-não é isso, deixa eu te explicar!"
    play sound ctc
    voice voz_cap04_04_12
    "Porra, eu tô nervoso.\nVocê me deixou nervoso..."
    play sound ctc
    voice voz_cap04_04_13
    "Fica calmo, calma!"
    play sound ctc
    voice voz_cap04_04_14
    "O arrombamento mesmo é esse aqui que\neu queria!"
    play sound ctc
    voice voz_cap04_04_15
    "OU, RAPAZ CÊ TÁ MALUCO, MERMÃO?"
    play sound ctc
    voice voz_cap04_04_16
    "Eu tô de olho nesse teu cuzinho a\ntempo cara, eu queria\narrombar teu CU!"
    play sound ctc
    voice voz_cap04_04_17
    "FILHA DA PUTA!"
    play sound ctc
    voice voz_cap04_04_18
    "Eu vou comer esse cu gostoso...!"
    play sound ctc
    voice voz_cap04_04_19
    "Comer meu cu, mermão?!"
    play sound ctc
    voice voz_cap04_04_20
    "Tu não é segurança aqui, cara?"
    play sound ctc
    voice voz_cap04_04_21
    "Eu sou segurança...!"
    play sound ctc
    voice voz_cap04_04_22
    "ENTÃO SEGURA NO MEU PAU AQUI, OH!"

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Empurrar o cabação e fugir do local do arrombamento>":
            hide textbox_aux
            jump wrong_end_04_04_1
        "<Não fazer nada>":
            hide textbox_aux
            "(...)"
            play sound ctc
            pass
    
    stop music
    play sound ctc
    voice voz_cap04_04_23
    "AAAGRH! PISA NA MINHA CABEÇA VAI!\nPISA!"
    play sound ctc
    voice voz_cap04_04_24
    "JUDIA DE MIM, FILHA DA PUTA!"
    play sound ctc
    voice voz_cap04_04_25
    "ISSO QUE EU QUERIA A MUITO TEMPO!!!"
    play sound ctc
    voice voz_cap04_04_26
    "VAI, ENFIA A CARA NESSE CU VAIN!"
    play sound ctc
    voice voz_cap04_04_27
    "SÓ QUER JUDIAR? FAZ CARINHO TAMBÉM!\nVAI? VAI, METE NO MEU CU?\nMETE?"
    play sound ctc
    voice voz_cap04_04_28
    "VEM CÁ FILHO DA PUTA, FODE! ISSO,\nMETE NO CU, VAI!\nMETE NO CU!\nMETE NO CU!"
    play sound ctc
    voice voz_cap04_04_29
    "Ai, agora eu sei onde tá o\narrombamento, cara..."
    play sound ctc
    voice voz_cap04_04_30
    "Não é?"
    play sound ctc
    voice voz_cap04_04_31
    "é, esse arrombamento tá no\nmeu cu, né?"
    play sound ctc
    voice voz_cap04_04_32
    "Gostou do arrombamento?"
    play sound ctc
    stop voice

    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()  


    $ register_ending("C4")
    play music fm_youwin
    scene black

    show capitulo_concluido
    pause 1.0
    play sound voz_cap01_04_21
    pause 3.7
    play sound voz_cap01_04_65
    pause 4.26
    hide capitulo_concluido
    
    show voce_desbloqueou
    show carta_img_cap_04
    show carta_desc_cap_04
    pause 1.5
    play sound voz_cap01_04_64
    pause 5.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    pause 4.0

    hide voce_desbloqueou
    hide carta_img_cap_04
    hide carta_desc_cap_04

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()


    return

label wrong_end_04_04_1:
    $ drpc_update("finalU")
    stop music
    "(Você empurra o morador e se\nliberta dos braços dele.)"
    play sound ctc
    "(Ele te agarra de novo pelo braço\nmas você joga ele com toda\na força contra a parede.)"
    play sound ctc
    "(Ele bate forte com a cabeça na\nparede, parece que ele\nficou inconsciente.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    voice voz_cap04_04_33
    "CADÊ O ARROMBAMENTO?"
    play sound ctc
    "(Você fica frenético enquanto\nprocura o arrombamento.)"
    play sound ctc
    voice voz_cap04_04_33
    "CADÊ O ARROMBAMENTO?"
    play sound ctc
    "(Onde está o arrombamento? Será\nque foi do lado de fora\ndo prédio?)"
    play sound ctc
    voice voz_cap04_04_33
    "CADE O ARROMBAMENTO?"
    play sound ctc
    "(CADÊ O ARROMBAMENTO?)"
    play sound ctc
    voice voz_cap04_04_33
    "CADÊ O ARROMBAMENTO?"
    play sound ctc
    "(Você corre para o beco do lado\nde fora do prédio na rua,\nesperando encontrar o arrombamento.)"
    play sound ctc
    "...?"
    play sound ctc
    "(...)"
    play sound ctc
    "(Tem... alguma coisa no meio do\nbeco.)"
    play sound ctc
    "(Parece ser um portal... mágico?)"
    play sound ctc
    voice voz_cap04_04_33
    "CADÊ O ARROMBAMENTO?"
    play sound ctc
    "(Parece que essa porta mágica\npode te levar para o\nlocal do ARROMBAMENTO!)"
    play sound ctc
    "(Você fica com medo, mas acaba\nchegando perto do círculo\nmágico.)"
    play sound ctc
    "(...)"
    play sound ctc
    voice voz_cap04_04_34
    "ARROMBAMENTO"
    play sound ctc
    "(Você corre com tudo, pula e se\njoga dentro do círculo\nmágico.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    $ register_ending("U")
    jump game_over