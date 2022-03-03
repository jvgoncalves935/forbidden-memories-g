label cap04_03_casa02:
    scene black
    stop music
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
    "Que droga de emprego de segurança, pagam mal pra caramba e eu aqui que nem burro de carga-"
    play sound ctc
    "(telefone tocando)"
    play sound ctc
    "Eu nem acordei direito, seus filha da puta!"
    show textbox_aux
    menu:
        "<Atender o telefone>":
            pass
        "<Desligar o telefone com ignorância>":
            hide textbox_aux
            jump wrong_end_04_03_1
    hide textbox_aux
    "Alexandre aqui."
    play sound ctc
    "Olá, Alexandre. Desculpa te ligar tão cedo!"
    play sound ctc
    "(É o filho da puta do morador do prédio.)"
    play sound ctc
    "Parece que teve um arrombamento aqui no prédio!"
    play sound ctc
    "Não sei quem fez isso mas parece que roubaram um monte de coisa aqui!"
    play sound ctc
    "Eu acordei de manhã e as trancas da porta da entrada tinham sido quebradas!"
    play sound ctc
    "Você pode vir aqui pra verificar a situação?"
    play sound ctc
    "(Já pensou em me PAGAR o que vocês tão me DEVENDO primeiro?)"
    play sound ctc
    "(Mano, que vontade de...)"
    play sound ctc
    show textbox_aux
    menu:
        "<Responder o que ele merece ouvir>":
            hide textbox_aux
            jump wrong_end_04_03_2
        "<\"Tá bom, eu já tô indo.\">":
            pass
    hide textbox_aux
    "Tá bom, eu já tô indo."
    play sound ctc
    "Tudo certo então, desculpa de novo aí te incomodar..."
    play sound ctc
    "Valeu mesmo cara... tô te esperando, tchau."
    play sound ctc
    "(desligou o telefone)"
    play sound ctc
    "Mas esse desgraçado é um folgado mesmo!"
    play sound ctc
    "Você gosta de um garoto de programa que eu sei, seu infeliz!"
    play sound ctc
    "Já não bastava a preguiça de ter que ir fazer o meu turno de manhã..."
    play sound ctc
    "E agora ainda vem um ladrão do cu da mãe e VEM ROUBAR A PORCARIA DO PRÉDIO!"
    play sound ctc
    "Quer me fuder me beija, caralho...!"
    play sound ctc
    "(telefone tocando)"
    play sound ctc
    "AH NÃO CARALHO!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            hide textbox_aux
            "(atendeu o telefone)"
            play sound ctc
            "Alor, é do corpo de bombeiro?"
            play sound ctc
            "MEU IRMÃO, VOCÊ É DEFICIENTE COGNITIVO, FUGIU DO MATERNAL OU O QUÊ, SEU DESGRAÇADO?"
            play sound ctc
            "VOCÊ ACHA GRAÇA NISSO, NÉ?"
            play sound ctc
            "VOCÊ GASTA O TEMPO DO SEU PRECIOSO DIA DE FRACASSADO PASSANDO TROTE PROS OUTROS?"
            play sound ctc
            "VOCÊ SABE PRA ONDE A SUA MÃE VAI QUANDO SAI DE CASA, CUZÃO?"
            play sound ctc
            "ELA VEM SENTAR NA MINHA PICA AQUI TODO DIA!"
            play sound ctc
            "AI MARLENE, SENTA NA PICA GOSTOSO, ISSO, ISSO!"
            play sound ctc
            "(Você começa a dar tapas na sua perna e bota o telefone bem perto pra ele ouvir.)"
            play sound ctc
            "AAAAH CARALHO, EU VOU GOZAR LÁ NO SEU ÚTERO MARLENE!"
            play sound ctc
            "(desligou o fone do outro lado)"
            play sound ctc
            "Haha, ficou putinho ow seu engraçadinho? Vai chorar pra mamãe?"
            play sound ctc
            "Já tava na pilha pra fazer isso tem um tempão, cara otário demais."
            play sound ctc
            "(...)"
            play sound ctc
        "<Desligar e ir pro trampo>":
            hide textbox_aux
            "LIGA PRA SUA MÃE, PRA SUA VÓ, AQUELA PUTA VEIA ESPÍRITO DO EXU POMBA GIRA!"
            play sound ctc
            "(desligou o telefone)"
            play sound ctc
    "Tô atrasado pra carai, tô quase perdendo o ônibus já...!"
    play sound ctc
    "(...)"
    play sound ctc
    "(Você veste sua roupa de segurança e vai correndo pro ponto de ônibus na esquina.)"
    play sound ctc
    return

label wrong_end_04_03_1:
    stop music
    "AAARRRGHH PORRA!"
    play sound ctc
    "(Você segura o botão de desligar do celular com toda sua força.)"
    play sound ctc
    "(Ele fica na parte de cima do celular e é pequeno pra caralho.)"
    play sound ctc
    "(Depois de machucar seu dedo você consegue desligar o celular.)"
    play sound ctc
    "(Você joga o celular no chão, com toda a raiva acumulada pela dor na sua alma.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(O celular fez um buraco no chão.)"
    play sound ctc
    "(...)"
    play sound ctc
    "Essa vida da cidade é uma DROGA mesmo!"
    play sound ctc
    "Quer saber mermão?"
    play sound ctc
    "Eu vou tirar uma semana de férias na fazenda do meu tio e é isso aí!"
    play sound ctc
    "Aquele pessoal do condomínio pode ir enfiar o dedo no cu, foda-se, tá ligado?"
    play sound ctc
    "Já tô indo fazer as malas agora."
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(dois dias depois)"
    play sound ctc
    "Ah, a vida no campo tem as suas vantagens, sabia?"
    play sound ctc
    "Não tem gente te ligando, atendente de telemarketing nem nada do tipo."
    play sound ctc
    "O pasto é tão bonito, é algo tão maravilhoso..."
    play sound ctc
    "Dar uma cavalgada é tão relaxante..."
    play sound ctc
    "Tirar leitinho da vaquinha..."
    play sound ctc
    "Nossa, que demais."
    play sound ctc
    "(...)"
    play sound ctc
    $ register_ending("S")
    jump game_over

label wrong_end_04_03_2:
    stop music
    "OW SEU FILHO DA PUTA, JÁ PENSOU EM ME PAGAR O QUE VOCÊ TÁ ME DEVENDO?"
    play sound ctc
    "MANDA O VIADO ENRUSTIDO DO PAI IR AÍ VER O ARROMBAMENTO NO OLHO DO SEU CU!"
    play sound ctc
    "VOCÊ ACHA QUE EU SOU SEU ESCRAVO PRA TRABALHAR DE GRAÇA?"
    play sound ctc
    "PARA DE DAR DINHEIRO PRA SUA MÃE FAZER PROGRAMA, SEU DESGRAÇADO!"
    play sound ctc
    "ROUBARAM SEU PRÉDIO? EU QUE QUERIA TER ROUBADO SE PUDESSE!"
    play sound ctc
    "TOMARA QUE VOCÊ FIQUE SEM DINHEIRO E MORRA DE FOME PAU NO-"
    play sound ctc
    "(desligou o telefone do outro lado)"
    play sound ctc
    "É isso que você merece, desgraçado!"
    play sound ctc
    "Agora tô fudido, com certeza ele vai chamar a polícia..."
    play sound ctc
    "Acho melhor abaixar a poeira e fazer uma viagem pra qualquer lugar aqui..."
    play sound ctc
    "Hmm... será que tem ônibus pra Pau Grande?"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(no dia seguinte)"
    play sound ctc
    "(...)"
    play sound ctc
    $ renpy.movie_cutscene("mod_assets/videos/praia.webm")
    $ register_ending("T")
    jump game_over

