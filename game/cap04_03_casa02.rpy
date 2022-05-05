label cap04_03_casa02:
    $ drpc_update("cap04-2")

    scene black
    stop music
    play music fm_simon_muran
    show textbox_black at center
    #show intro_001 at top
    "(...)"
    play sound ctc
    "Já é de manhã?"
    play sound ctc
    "Caramba, acho que eu dormi demais."
    play sound ctc
    "Porra meu, hoje é o dia do trampo."
    play sound ctc
    "Que droga de emprego de segurança,\npagam mal pra caramba e eu\naqui que nem burro de carga-"
    play sound ctc
    play sound_bg celular
    stop music
    "(celular tocando)"
    play sound ctc
    "Eu nem acordei direito, seus\nfilha da puta!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o celular>":
            hide textbox_aux
            stop sound_bg
            pass
        "<Desligar o celular com ignorância>":
            hide textbox_aux
            jump wrong_end_04_03_1
    
    "{p=0.2}{nw}"
    play sound phone_click
    "Alexandre aqui."
    play sound ctc
    play music fm_map_select_2
    "Olá, Alexandre. Desculpa te\nligar tão cedo!"
    play sound ctc
    "(É o filho da puta do morador\ndo prédio.)"
    play sound ctc
    "Parece que teve um arrombamento\naqui no prédio!"
    play sound ctc
    "Não sei quem fez isso mas parece\nque roubaram um monte de\ncoisa aqui!"
    play sound ctc
    "Eu acordei de manhã e as trancas\nda porta da entrada tinham\nsido quebradas!"
    play sound ctc
    "Você pode vir aqui pra verificar\na situação?"
    play sound ctc
    "(Já pensou em me PAGAR o que vocês\ntão me DEVENDO primeiro?)"
    play sound ctc
    stop music fadeout 2.0
    "(Mano, que vontade de...)"
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Responder o que ele merece ouvir>":
            hide textbox_aux
            stop music
            jump wrong_end_04_03_2
        "<\"Tá bom, eu já tô indo.\">":
            stop music
            hide textbox_aux
            pass
    play music fm_modern_times
    "Tá bom, eu já tô indo."
    play sound ctc
    "Tudo certo então, desculpa de novo\naí te incomodar..."
    play sound ctc
    "Valeu mesmo cara... tô te esperando,\ntchau."
    play sound ctc
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o celular)"
    play sound ctc
    "Mas esse desgraçado é um folgado\nmesmo!"
    play sound ctc
    "Você gosta de um garoto de programa\nque eu sei, seu infeliz!"
    play sound ctc
    "Já não bastava a preguiça de ter que\nir fazer o meu turno de manhã..."
    play sound ctc
    "E agora ainda vem um ladrão do cu da\nmãe e VEM ROUBAR A PORCARIA DO PRÉDIO!"
    play sound ctc
    "Quer me fuder me beija, caralho...!"
    play sound ctc
    play sound_bg celular
    stop music
    "(celular tocando)"
    play sound ctc
    "AH NÃO CARALHO!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o celular>":
            hide textbox_aux
            stop sound_bg
            "{p=0.2}{nw}"
            play sound phone_click
            "(atendeu o celular)"
            play sound ctc
            voice voz_cap03_01_01
            play music fm_kaiba_theme
            "ALOR, É DO CORPO DE BOMBEIRO?"
            play sound ctc
            voice voz_cap04_03_04
            "VOU CHUPAR A BUCETA DA SUA\nMÃE E O CU DESSA VAGABUNDA\nQUE TÁ DO SEU LADO!"
            play sound ctc
            voice voz_cap04_03_05
            "ELA É PUTA, PUTA IGUAL VOCÊ\nQUE É UM VIADINHO!"
            play sound ctc
            voice voz_cap04_03_06
            "VAI VIRAR HOMEM, RAPAZ!\nVAI CRIAR PELO NA BUNDA."
            play sound ctc
            voice voz_cap04_03_07
            "VAI, ME ESQUECE, MOLEQUE.\nOW, VAI SE FUDER, MOLEQUE."
            play sound ctc
            "{p=0.2}{nw}"
            stop music
            play sound phone_end_call
            "(desligou o fone do outro lado)"
            play sound ctc
            play music fm_preliminary_faceoff
            "Haha, ficou putinho ow seu\nengraçadinho? Vai chorar\npra mamãe?"
            play sound ctc
            "Já tava na pilha pra fazer isso tem\num tempão, cara otário\ndemais."
            play sound ctc
            stop music fadeout 2.0
            "(...)"
            play sound ctc
        "<Desligar e ir pro trampo>":
            hide textbox_aux
            "LIGA PRA SUA MÃE, PRA SUA VÓ, AQUELA\nVEIA ESPÍRITO DO\nEXU POMBA GIRA!"
            play sound ctc
            "{p=0.2}{nw}"
            play sound phone_click
            "(desligou o celular)"
            play sound ctc
    play music fm_modern_shop
    "Tô atrasado pra carai, tô quase\nperdendo o ônibus já...!"
    play sound ctc
    "(...)"
    play sound ctc
    "(Você veste sua roupa de segurança\ne vai correndo pro ponto\nde ônibus na esquina.)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice

    return

label wrong_end_04_03_1:
    $ drpc_update("finalS") 
    voice voz_cap04_03_02
    play music fm_preliminary_faceoff
    "AI CARALHO!"
    play sound ctc
    "(Você segura o botão de desligar do\ncelular com toda sua força.)"
    play sound ctc
    "(Ele fica na parte de cima do\ncelular e é pequeno para\num cacete.)"
    play sound ctc
    "DESLIGA ESSA PORRA!"
    play sound ctc
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    "(Depois de machucar seu dedo você\nconsegue desligar o celular.)"
    play sound ctc
    "QUE MERDA DE TELEFONE!"
    play sound ctc
    "{p=0.2}{nw}"
    play sound floor_slam
    "(Você joga o celular no chão, com\ntoda a raiva acumulada pela\ndor na sua alma.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(O celular fez um BURACO\nENORME no chão.)"
    play sound ctc
    voice voz_cap04_03_01
    "PUTA QUE PARIU MEU!"
    play sound ctc
    stop music fadeout 2.0
    "(...)"
    play sound ctc
    "Essa vida da cidade é uma\nDROGA mesmo!"
    play sound ctc
    play music fm_modern_shop
    "Quer saber mermão?"
    play sound ctc
    "Eu vou tirar uma semana de férias\nna fazenda do meu amigo\nMarcinho e é isso aí!"
    play sound ctc
    "Aquele pessoal do condomínio pode\nir enfiar o dedo no cu,\nfoda-se, tá ligado?"
    play sound ctc
    "Já tô indo fazer as malas agora."
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice
    
    "(dois dias depois)"
    play music fm_duel_grounds
    play sound_bg cicadas fadein 6.0
    play sound ctc
    "Ahhhh... a vida no campo tem\nas suas vantagens, sabia?"
    play sound ctc
    "Não tem gente te ligando,\natendente de telemarketing\nnem nada do tipo."
    play sound ctc
    "O pasto é tão bonito, é algo\ntão maravilhoso..."
    play sound ctc
    "Dar uma cavalgada é tão\nrelaxante..."
    play sound ctc
    "Tirar leitinho da vaquinha..."
    play sound ctc
    "Nossa, que demais."
    play sound ctc
    stop music fadeout 3.0
    "(...)"
    play sound ctc
    "Só o barulho dessas cigarras\nque já encheu o saco."
    play sound ctc
    play music fm_finals_faceoff
    "Não tem como fazer elas\npararem não?"
    play sound ctc
    voice voz_cap04_03_03
    "EU AMALDIÇOO TODO MUNDO!"
    play sound ctc
    stop music fadeout 2.0
    "(...)"
    play sound ctc
    "Bora encontrar com\no Marcinho então, né..."
    play sound ctc
    stop sound_bg

    window hide(None)
    $ game_over_pos_cutscene = True
    $ renpy.movie_cutscene("mod_assets/videos/cowboy.webm")

    $ register_ending("S")
    jump game_over

label wrong_end_04_03_2:
    $ drpc_update("finalT")
    stop music
    play music fm_finals_faceoff
    "OW SEU FILHO DA PUTA, JÁ PENSOU\nEM ME PAGAR O QUE\nVOCÊ TÁ ME DEVENDO?"
    play sound ctc
    "MANDA O VIADO ENRUSTIDO DO PAI\nIR AÍ VER O ARROMBAMENTO\nNO OLHO DO SEU CU!"
    play sound ctc
    "VOCÊ ACHA QUE EU SOU SEU ESCRAVO\nPRA TRABALHAR DE GRAÇA?"
    play sound ctc
    "PARA DE DAR DINHEIRO PRA SUA MÃE\nFAZER PROGRAMA, SEU DESGRAÇADO!"
    play sound ctc
    "ROUBARAM SEU PRÉDIO? EU QUE QUERIA\nTER ROUBADO SE PUDESSE!"
    play sound ctc
    "TOMARA QUE VOCÊ FIQUE SEM DINHEIRO\nE MORRA DE FOME PAU NO-"
    play sound ctc
    stop music
    "{p=0.2}{nw}"
    play sound phone_end_call
    "(desligou o celular do outro lado)"
    play sound ctc
    "É isso que você merece, desgraçado!"
    play sound ctc
    play music fm_mages_duel
    "Agora tô fudido, com certeza ele\nvai chamar a polícia..."
    play sound ctc
    "Acho melhor abaixar a poeira e\nfazer uma viagem pra\nqualquer lugar fora daqui..."
    play sound ctc
    "Hmm... será que tem ônibus\npra Pau Grande?"
    play sound ctc
    stop music fadeout 2.0
    "(...)"
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"
    stop music
    stop voice

    "(no dia seguinte)"
    play sound ctc

    window hide(None)
    $ game_over_pos_cutscene = True
    $ renpy.movie_cutscene("mod_assets/videos/praia.webm")
    $ register_ending("T")
    jump game_over

