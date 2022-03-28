label cap05_01_casa01:
    scene black
    stop music
    show textbox_black at center
    "(Alexandre Senna estava em uma\npadaria, procurando onde estava\no arrombamento...)"
    play sound ctc
    "Onde, onde, onde? Cadê o arrombamento?"
    play sound ctc
    "Bem... na verdade não tem arrombamento\nnenhum, só queria que você desse\numa olhada em minha cozinha para\nver se ela segue os padrões\nde segurança..."
    play sound ctc
    "Oh, se tá maluco meu, seu viado! Você\nme deixou nervoso!"
    play sound ctc
    "Calma, calma, mas não se irrite...\ntome um suco de laranja que eu\njá vou buscar o cacetinho\nque acabei de fazer."
    play sound ctc
    "(Alguns momentos se passam e é\npossível escutar murmúrios\nvindo da área do forno.)"
    play sound ctc
    "(Senna decide ir conferir.)"
    play sound ctc
    "Está tudo bem?"
    play sound ctc
    "O meu cacetinho ficou preso no\nfundo do forno e eu não consigo\npegar... você pode pegar\nele para mim?"
    play sound ctc
    "Mas é claro! Sempre adoro ajudar..."
    play sound ctc
    "(Senna se aproxima do forno e fica\nde quatro para pegar o pão\ncom maior facilidade.)"
    play sound ctc
    "(Um pouco depois que ele entra,\nele sente algo GRANDE E\nGOSTOSO LÁ NO ESTÔMAGO PORRA)"
    play sound ctc
    "(É o Padeiro G, demonstrando todo\nseu amor por Senna.)"
    play sound ctc
    "(Senna começa a relaxar com o\nPadeiro G, tentando pegar o\ncacetinho no forno e levando\no outro cacetão atrás.)"
    play sound ctc
    "(\"É possível um homem engravidar?\",\npensou Senna profundamente\nenquanto sentia todo o\namor em sua alma vazia.)"
    play sound ctc
    "(\"Eu vou te encher de recheio\",\ndisse o Padeiro G momentos\nantes de explodir todo o\nseu amor dentro de Senna.)"
    play sound ctc
    "(O Padeiro G solta todo seu líquido\nde amor grudento e viscoso\ndentro de Senna, escorrendo e\nborbulhando sem parar no chão.)"
    play sound ctc
    "E aí, achou meu cacetinho grande?"
    play sound ctc
    "Amei seu cacetinho, quero mais\ne mais!"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "AAAII...!!!"
    play sound ctc
    "(...)"
    play sound ctc
    "Foi um sonho..."
    play sound ctc
    "Que delícia..."
    play sound ctc
    "Acho que o arrombamento me\ndeixou um pouco traumatizado."
    play sound ctc
    "Aquele morador me enganou,\nmaldito mentiroso do caralho."
    play sound ctc
    play music celular
    "(telefone tocando)"
    play sound ctc
    "NENHUM. DIA DE SOSSEGO!"
    play sound ctc
    
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Atender o telefone>":
            hide textbox_aux
            pass
        "<Desligar e dar um passeio na rua>":
            hide textbox_aux
            jump wrong_end_05_01_1
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "Alô?"
    play sound ctc
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
    "Tudo certo, mas tarde vou dar uma\nolhada nele."
    play sound ctc
    "Então até amanhã, Alexandre. Foi\nbom fazer negócio com você!\nTchau tchau."
    play sound ctc
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o telefone)"
    play sound ctc
    "Nossa, que maravilha. Ator pornô..."
    play sound ctc
    "Ganhar dinheiro fácil, viajar pra\nSão Paulo e ainda poder degustar\nvárias mulheres... que incrível."
    play sound ctc
    "Nossa, já tô atrasado pro\ntrabalho. Amanhã eu penso\nnisso."
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(dia seguinte, São Paulo, 10:00,\nRua Serra Paulista,\nnúmero 60)"
    play sound ctc

    return

label wrong_end_05_01_1:
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "(desligou o telefone)"
    play sound ctc
    "Com certeza era aquele filho da\nputa que faz trote todo\nsanto dia."
    play sound ctc
    "Eu vou pegar o número dele\ndepois e chamar a polícia,\nque se dane."
    play sound ctc
    "Quer dizer... depois."
    play sound ctc
    "Agora eu tô a fim de relaxar."
    play sound ctc
    "(...)"
    play sound ctc
    "(Você sai de casa para dar\num passeio no parque,\nsem camisa.)"
    play sound ctc
    "Nossa, mas que parque lindo.\nCoisa linda de se ver."
    play sound ctc
    "(O cheiro das flores e a\nbrisa aconchegante te\nacalmam.)"
    play sound ctc
    "Que sensação maravilhosa-"
    play sound ctc
    "(...!)"
    play sound ctc
    "(Você vê uma linda garota\nno banco do parque,\nparece ser japonesa.)"
    play sound ctc
    "(Ela está usando um roupão\ntradicional japonês\ntambém.)"
    play sound ctc
    "(Como que chama mesmo?)"
    play sound ctc
    "(Guinomo?)"
    play sound ctc
    "(A garota te chama para\nsentar ao lado dela com\no dedo indicador de forma\nbem erótica.)"
    play sound ctc
    "(Eu não resisto, vain.)"
    play sound ctc
    "(Você senta ao lado dela\ne começa a conversar.)"
    play sound ctc
    "Olá, moça. Você é japonesa?\nQue roupa linda a sua!"
    play sound ctc
    "Gostou? A cultura japonesa é\nrealmente encantadora mesmo."
    play sound ctc
    "Encantadora e bem peculiar..."
    play sound ctc
    "(cof cof)"
    play sound ctc
    "(Você sente um cheiro estranho\ne começa a ficar extremamente\ntonto!)"
    play sound ctc
    "(Mooooooççççaaaaa...!)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "AAAHHH!"
    play sound ctc
    "(Você acorda em um tatame,\nvestido com uma roupa igual\na que você usa no judô\ne uma bandana do Japão.)"
    play sound ctc
    "Que porra é essa?"
    play sound ctc
    "(Você vira pra trás e vê a\nmesma garota linda do parque.)"
    play sound ctc
    "(Ela joga a roupa toda dela\nno chão de uma vez,\nficando nua.)"
    play sound ctc
    "(\"Japonesas tem três pernas?\",\né a primeira coisa que você pensa.)"
    play sound ctc
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
    voice voz_cap05_01_01
    "UUUHHH... WAKARANAI... WAKARANAI!\nAAAHHHH!!"
    play sound ctc
    $ register_ending("V")
    jump game_over

