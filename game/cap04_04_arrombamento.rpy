label cap04_04_arrombamento:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    #(Senna 00:00 - 00:07)
    "Onde, onde, onde?" 
    "Cadê o arromabento? Foi aqui, foi aonde?"
    play sound ctc
    #(Morador 00:07 - 00:00)
    "Err, por aqui..."
    play sound ctc
    #(Senna 00:08  - 00:15)
    "Porra, se ta me tirando mermão?"
    "Aonde tá tendo arrombamento aqui, seu viado!"
    play sound ctc
    #(Morador 00:16 - 00:16)
    "Pode parar de bater na minha cara?"
    #(Senna 00:16 - 00:16)
    play sound ctc
    "Você tá louco?"
    #(Morador 00:17 - 00:18)
    play sound ctc
    "Não, na verdade não teve nada aqui..."
    #(Senna 00:19 - 00:21)
    play sound ctc
    "Onde que teve o arrombamento aqui, mano?"
    #(Morador 00:20 - 00:20)
    play sound ctc
    "NENHUM!" 
    #(Senna 00:21 - 00:23)
    play sound ctc
    "VOCÊ TÁ MALUCO, RAPAZ? TÁ ATRAPALHANDO MEU TRABALHO, SEU...!" 
    #(Morador 00:23 - 00:25)
    play sound ctc
    "N-não é isso!, deixa eu te explicar!"
    #(Senna 00:25 - 00:25)
    play sound ctc
    "PORRA!"
    #(Morador 00:26 - 00:27)
    play sound ctc
    "Dexa eu te explicar..."
    #(Senna 00:27 - 00:28)
    play sound ctc
    "Eu tô nervoso!"
    #(Morador 00:30 - 00:33)
    play sound ctc
    "Deixa eu te explicar, calma, calma!"
    "O arrombamento mesmo é esse aqui que eu queria!"
    #(Senna 00:34 - 00:36)
    play sound ctc
    "OW, RAPAZ CÊ TÁ MALUCO, MERMÃO?"
    #(Morador 00:36 - 00:39)
    play sound ctc
    "Eu tô de olho nesse teu cuzinho a tempo cara, eu queria arrombar teu CU!"
    #(Senna 00:40 - 00:41)
    play sound ctc
    "FILHA DA PUTA!"
    #(Morador 00:41 - 00:42)
    play sound ctc
    "Quero comer esse cu gostoso...!"
    #(Senna 00:42 - 00:43)
    play sound ctc
    "Tira a mão do meu cu, mermão!"
    #(Morador 00:44 - 00:45)
    play sound ctc
    "Tu não é segurança aqui, cara?"
    #(Senna 00:45 - 00:45)
    play sound ctc
    "Eu sou segurança...!"
    #(Morador 00:46 - 00:47)
    play sound ctc
    "ENTÃO SEGURA NO MEU PAU AQUI, OH!"

    show textbox_aux
    play music audio.fm_password
    menu:
        "<Empurrar o cabação e fugir do local do arrombamento>":
            jump wrong_end_04_04_1
        "<Não fazer nada>":
            pass
    hide textbox_aux
    stop music
    #(Senna 00:49 - 00:56)
    play sound ctc
    "AAAGRH! PISA NA MINHA CABEÇA VAI! PISA!"
    "JUDIA DE MIM, FILHA DA PUTA!, AAAAGHH!"
    #(Morador 00:56 - 00:57)
    play sound ctc
    "ISSO QUE EU QUERIA A MUITO TEMPO!!!"
    #(Senna 01:01 - 01:03)
    play sound ctc
    "VAI, ENFIA A CARA NESSE CU VAIN!"
    "SÓ QUER JUDIAR? FAZ CARINHO TAMBÉM! VAI, METE NO MEU CU? METE?"
    #(Senna 01:08 - 01:16)
    play sound ctc
    "VEM CÁ FILHO DA PUTA, FODE! ISSO, METE NO MEU CU, VAI! METE NO MEU CU! METE NO CU!"
    #(Senna 01:17 - 01:20)
    play sound ctc
    "Ai, agora eu sei onde tá o arrombamento, cara..."
    #(Morador 00:20 - 00:20)
    play sound ctc
    "É?"
    #(Senna 00:20 - 00:23)
    play sound ctc
    "é, esse arrombamento tá no meu cu, né?"
    #(Morador 00:24 - 00:26)
    play sound ctc
    "Gostou do arrombamento?"
    play sound ctc
    return

label wrong_end_04_04_1:
    $ register_ending("U")
    jump game_over


