label cap05_01_casa01:
    $ drpc_update("cap05")
    
    stop music
    voice voz_cap05_01_02
    "AAAAAAIIIII!!!"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    play music fm_modern_times
    "Foi um sonho, de novo..."
    play sound ctc
    
    "Que delícia..."
    play sound ctc
    "Acho que o arrombamento me\ndeixou um pouco traumatizado."
    
    play sound ctc
    "Aquele morador me enganou,\nmaldito mentiroso do caralho."
    play sound ctc
    
    play sound_bg celular
    stop music
    "(celular tocando)"
    play sound ctc
    
    "NENHUM. DIA DE SOSSEGO!"
    play sound ctc
    
    show textbox_aux
    menu:
        "<Atender o celular>":
            hide textbox_aux
            pass
        "<Desligar e dar um passeio na rua>":
            hide textbox_aux
            jump wrong_end_05_01_1
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    "Alô?"
    play sound ctc
    
    play music fm_tournament
    "Olá, é do número do Alexandre?"
    play sound ctc
    
    "Sim, sou eu mesmo."
    play sound ctc
    
    "Nós temos uma proposta para\nvocê que pode ser\ndo seu interesse."
    play sound ctc
    
    "Nosso recrutador te viu andando\nperto da academia e achou\nseu porte físico muito\ninteressante."
    play sound ctc
    
    "Descobrimos seu número e agora\nestamos te ligando para\nfazer uma proposta\nmuito boa."
    play sound ctc
    
    "E o que seria?"
    play sound ctc
    
    "Atuar em um filme pornográfico\ncom a nossa atriz.\nFilme hétero, padrão."
    play sound ctc
    
    "O nosso cachê é de 300 reais\npor cena. Se a gente gostar da\nprimeira a gente pode fazer\ncenas de outros filmes."
    play sound ctc
    
    "O que você acha da nossa proposta?"
    play sound ctc
    
    "Adorei. Dá pra ganhar um\ndinheirinho e ainda pegar\numa mulher, não é?"
    play sound ctc
    
    "Com certeza meu caro, e a\nnossa atriz é linda, você\nvai gostar muito dela."
    play sound ctc
    
    "Então tudo certo, meu querido.\nLocal, data e hora?"
    play sound ctc
    
    "Vai passar um cara nosso pra ir\nte buscar em frente a academia.\nAmanhã, 05:00h da madrugada."
    play sound ctc
    
    "A gente é de São Paulo capital.\nA viagem é por nossa conta."
    play sound ctc
    
    "Qualquer dúvida só olhar no\nnosso anúncio no jornal."
    play sound ctc
    
    "Caramba, bem rápido hein? Vocês\nlevam isso a sério mesmo,\nhein?"
    play sound ctc
    
    "Tudo bem, eu vou ir aí amanhã.\nDá pra fazer a viagem depois\ndo meu trabalho de noite."
    play sound ctc
    
    "Certo, Alexandre. Primeiro vamos\nfazer um teste com você só\npara confirmar que não vai\ndar problema no filme, certo?"
    play sound ctc
    
    "Sem problemas."
    play sound ctc
    
    "Se você quiser a gente deixou mais\ninformações lá no nosso anúncio que\na gente colocou em frente a\nsua academia."
    play sound ctc
    
    "Tudo certo, mais tarde vou dar uma\nolhada nele."
    play sound ctc
    
    "Então até amanhã, Alexandre. Foi\nbom fazer negócio com você!\nTchau tchau."
    play sound ctc
    
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o celular)"
    play sound ctc
    
    play music fm_free_duel_theme
    "Nossa, que maravilha. Ator pornô..."
    play sound ctc
    
    "Ganhar dinheiro fácil, viajar pra\nSão Paulo e ainda poder degustar\nvárias mulheres... que incrível."
    play sound ctc
    
    "Nossa, já tô atrasado pro\ntrabalho. Amanhã eu penso\nnisso."
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    return

label wrong_end_05_01_1:
    $ drpc_update("finalV")
    stop sound_bg
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o celular)"
    play sound ctc
    
    play music fm_modern_times
    "Com certeza era aquele filho da\nputa que faz trote todo\nsanto dia."
    play sound ctc
    
    "Eu vou pegar o número dele\ndepois e chamar a polícia,\nque se dane."
    play sound ctc
    
    "Quer dizer... depois."
    play sound ctc
    
    "Agora eu tô a fim de relaxar."
    play sound ctc
    
    stop music fadeout 2.0
    "{p=2.0}{nw}"

    
    play sound_bg park fadein 4.0
    "(Você sai de casa para dar\num passeio no parque,\nsem camisa.)"
    play sound ctc
    
    "Nossa, mas que parque lindo.\nCoisa linda de se ver."
    play sound ctc
    
    "(O cheiro das flores e a\nbrisa aconchegante te\nacalmam.)"
    play sound ctc
    
    "Que sensação maravilhosa-"
    play sound ctc
    
    stop sound_bg fadeout 2.0
    "(...!)"
    play sound ctc
    
    play music fm_forbidden_ruins
    "(Você vê uma linda garota\nno banco do parque,\nparece ser japonesa.)"
    play sound ctc
    
    "(Ela está usando um roupão\ntradicional japonês\ntambém.)"
    play sound ctc
    
    "(Como que chama mesmo?)"
    play sound ctc
    
    "(Guinomo?)"
    play sound ctc
    
    play sound_bg park fadein 4.0
    "(A garota te chama para\nsentar ao lado dela com\no dedo indicador de forma\nbem erótica.)"
    play sound ctc
    
    "(Eu não resisto, vain.)"
    play sound ctc
    
    "(Você senta ao lado dela\ne começa a conversar.)"
    play sound ctc
    
    "Olá, moça. Você é japonesa?\nQue bonita a sua roupa!"
    play sound ctc
    
    "Gostou? A cultura japonesa é\nrealmente encantadora mesmo."
    play sound ctc
    
    "Encantadora e bem peculiar..."
    play sound ctc
    
    "{p=0.2}{nw}"
    stop sound_bg fadeout 5.0
    play sound spray
    stop music
    "(cof cof)"
    play sound ctc
    
    play music fm_sebek_neku
    "(Você sente um cheiro estranho\ne começa a ficar extremamente\ntonto!)"
    play sound ctc
    
    voice voz_cap05_01_22
    "AAAAAAaaaAaAahhaHAAHahAHhaHhhhhhh...!"
    play sound ctc
    
    "(...)"
    play sound ctc

    stop music fadeout 2.0
    "{p=2.0}{nw}"

    "(...)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    voice voz_cap02_04_39
    "AAAHHH!"
    play sound ctc
    
    "(Você acorda em um tatame,\nvestido com uma roupa igual\na que você usa no judô\ne uma bandana do Japão.)"
    play sound ctc
    
    voice voz_cap05_01_23
    "Que porra é essa?"
    play sound ctc
    
    play sound_bg kabuki noloop
    "(Você vira pra trás e vê a\nmesma garota linda do parque.)"
    play sound ctc
    
    "(Ela joga a roupa toda dela\nno chão de uma vez,\nficando nua.)"
    play sound ctc
    
    "(\"Japonesas tem três pernas?\",\né a primeira coisa que você pensa.)"
    play sound ctc
    
    stop sound_bg
    play music fm_kaiba_theme
    "(Não, espera aí...!)"
    play sound ctc
    
    "Vou te ensinar muita coisa nova\nhoje, gostosão."
    play sound ctc
    
    "(Antes que você pudesse pensar em\nalguma coisa, você começa a ter\numa aula de cultura japonesa.)"
    play sound ctc
    
    "(\"Que cultura esquisita!\",\nvocê pensa novamente.)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    voice voz_cap05_01_01
    "UUUHHH... WAKARANAI... WAKARANAI!\nAAAHHHH!!"
    play sound ctc
    
    stop voice
    stop music fadeout 2.0
    $ register_ending("V")
    jump game_over
    return