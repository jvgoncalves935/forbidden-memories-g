label cap02_03_casa02:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Aquele gringo filho da puta me enganou,\ncara safado..."
    play sound ctc
    "Mas eu não resisto vain..."
    play sound ctc
    "A Anita era muito gostosa..."
    play sound ctc
    "(telefone tocando)"
    play sound ctc
    "Que droga, ainda não troquei esse toque\nde telefone!"
    $ telefone_02_03 = False
    play sound ctc
    #play music audio.fm_password
    show textbox_aux
    menu:
        "<Atender o telefone>":
            $ telefone_02_03 = True
            hide textbox_aux
            "Alô?"
            play sound ctc
            "\"Fala aí Senna, a gente vai reunir a\ngalera pra tomar uma gelada na\nminha casa, topa vir?\""
            play sound ctc
            "Topo sim, gente boa! Que horas\nvai ser?"
            play sound ctc
            "\"18 horas, meu parceiro.\""
            play sound ctc
            "Quem que vai chegar aí também?"
            play sound ctc
            "\"O Índio e o Goleiro de Família.\""
            play sound ctc
            "Show, então de noite eu apareço aí,\naté mais."
            play sound ctc
            "(desligou o telefone)"
            play sound ctc
            "Tem que tomar cuidado com esses\nrolês do Mangueira Evil..."
            play sound ctc
        "<Desligar>":
            $ telefone_02_03 = False
            hide textbox_aux
            "(desligou o telefone)"
            play sound ctc
            "Vai tomar no cu, deve ser trote\nessa merda."
            play sound ctc
            "O pessoal não tem mais o que\nfazer nessa porcaria mais não?"
            play sound ctc
            "Acho que eu vou fazer um toddynho\nali pra mim..."
            play sound ctc
    stop music
    "(campainha tocando)"
    play sound ctc
    "VOCÊS (telefone vibrando) NÃO ME DEIXAM\nEM PAZ, SEUS PERTUBADO!"
    play sound ctc
    play music audio.fm_password
    show textbox_aux
    $ wrong_end = False
    menu:
        "<Atender a campainha>":
            hide textbox_aux
            call cap02_03_casa02_campainha from _call_cap02_03_casa02_campainha
        "<Fingir que não está em casa>":
            hide textbox_aux
            "(Você ignora a campainha, fingindo que\nnão tem ninguém em casa)."
            play sound ctc
            "(...Ou fingindo que você é surdo e não\nouviu, sei lá.)"
            play sound ctc
            "Foda-se esse filho da puta."
            play sound ctc
            "(...)"
            play sound ctc
            "(meia hora depois)"
            play sound ctc
            "(Seja lá quem está tocando a campainha,\né uma pessoa muito persistente.)"
            play sound ctc
            "(...)"
            play sound ctc
            "VOCÊ NÃO TEM O QUE FAZER NÃO?"
            play sound ctc
            "(...)"
            play sound ctc
            "(...)"
            play sound ctc
            "(Parece que finalmente o vagabundo\ninconveniente desistiu de\nchamar na campainha.)"
            play sound ctc
            if(telefone_02_03):
                "(Você espera mais uma hora dentro\nde casa, só pra ter certeza\nde que ele foi embora.)"
                play sound ctc
    if(wrong_end):
        return
    stop music
    play sound ctc
    if(telefone_02_03):
        "(Logo após, você sai de casa para\nencontrar com seus amigos na\ncasa do Mangueira Evil.)"
        play sound ctc
        "Será que vai ter alguma coisa pra\ncomer lá?"
        play sound ctc
        "(Mangueira Evil é tão mão de vaca\nque ele nunca compra nada pra\nninguém comer quando recebe\nvisitas.)"
        play sound ctc
    else:
        jump wrong_end_02_03_1
    return

label cap02_03_casa02_campainha:
    stop music
    "Mas que droga!"
    play sound ctc
    "(Irritado, você vai atender a\nporta.)"
    play sound ctc
    "(É um mendigo com umas roupas bem\nvelhas.)"
    play sound ctc
    "\"Bom dia, meu senhor. Tô precisando\nde arrumar um dinheiro pra eu\ne minha filha comer...\""
    play sound ctc
    "(Você pensa se você tem cara de\nbanqueiro que empresta dinheiro\npara os outros.)"
    play sound ctc
    "\"Eu posso limpar a frente da sua\ncasa, é só pra me dar uma\najuda mesmo...\""
    play sound ctc
    "(Realmente, o passeio da sua casa\ntem que tirar os matos e\nas plantas da calçada. Você não\nfaz isso tem dois anos.)"
    play sound ctc
    "(Mas tem algo estranho nisso tudo...)"
    play sound ctc
    "(A voz do mendigo é bem familiar.)"
    play sound ctc
    "(Uma voz meio esquisita, parecendo\nque ele fala bocejando\nque nem um retardado.)"
    play sound ctc
    "(Será que é apenas impressão?)"
    play sound ctc
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Continar ouvindo o mendigo>":
            hide textbox_aux
            jump wrong_end_02_03_2
        "<Fechar a porta com muita ignorância>":
            hide textbox_aux
            stop music
            "(porta fechando com muita ignorância)"
            play sound ctc
            "FILHO DA PUTA!"
            play sound ctc
            "NA VIDA DE VOCÊS VAI CAIR MALDIÇÃO!"
            play sound ctc
            "(Você pensa que deve ser apenas um\npilantra que iria fazer algo\nde ruim com você.)"
            play sound ctc
            "(Pensando assim, você fica mais\ncalmo.)"
            play sound ctc
            "Vou ir lá fazer meu toddynho com\nmisto quente."
            play sound ctc
            "(47 minutos depois)"
            play sound ctc
            "Esse misto tava MUITO gostoso..."
            play sound ctc
    return

label wrong_end_02_03_1:
    stop music
    $ wrong_end = True
    "(Como você não tem nada para fazer,\nvocê decide jogar o jogo da\ncobrinha.)"
    play sound ctc
    "(Você sempre foi bom nele...)"
    play sound ctc
    "(O som da cobrinha andando na tela\ne comendo os asteriscos faz você\nse esquecer dos problemas da\nvida adulta.)"
    play sound ctc
    "(Não tem contas para pagar, apenas\nfazer a cobra comer os asteriscos\nsem encostar nas beiradas.)"
    play sound ctc
    "(Se você encostar na beirada é que\nnem enconstar numa cerca elétrica\nde uma base militar:)"
    play sound ctc
    "(Você morre.)"
    play sound ctc
    "Esse jogo é muito realista, bem a\nfrente do seu tempo!"
    play sound ctc
    "(30 minutos depois)"
    play sound ctc
    "Eu realmente sou bom nesse jogo!"
    play sound ctc
    "(64 minutos depois)"
    play sound ctc
    "Não é possível, eu acho que devo\nser profissional ou alguma coisa\ndo tipo."
    play sound ctc
    "(Você liga para o pessoal do Guinnass\nBook para tentar registrar um\nnovo recorde.)"
    play sound ctc
    "(A ligação por interurbano fica em\nmais de 100 reais, você agora tem\numa nova dívida a pagar!)"
    play sound ctc
    "(Você gasta suas últimas despesas\npara viajar de Cupiqueno para São Paulo\nem busca de registrar o novo\nRecorde Mundial do Jogo da\nCobrinha.)"
    play sound ctc
    "(Depois de muito esforço, você consegue\nbater o recorde como Melhor\nJogador do Jogo da Cobrinha\ndo Guinnass Book!)"
    play sound ctc
    "(Você ganha 6.000 dólares como\nrecompensa!)"
    play sound ctc
    "(O que você faria com um dinheiro\ndesses?)"
    play sound ctc
    "(Faria certas coisas que você nunca\nimaginaria que eu tinha que eu,\nTERIA coragem de fazer!)"
    play sound ctc
    $ register_ending("J")
    jump game_over
    return

label wrong_end_02_03_2:
    stop music
    $ wrong_end = True
    "Tá bom então, quanto que você vai\ncobrar?"
    play sound ctc
    "\"15 reau, senhor.\""
    play sound ctc
    "(Você não acha o preço caro, pois\nrealmente o passeio tá uma coisa\nhorrorosa. Ele vai ter muito\ntrabalho pra tirar tudo.)"
    play sound ctc
    "Hmm, tá beleza então. Vou te dar\numa ajuda pois você parece ser\num cara legal."
    play sound ctc
    "\"Muito obrigado, senhor.\nDeus te pague.\""
    play sound ctc
    "Beleza, vou ir ali pegar a faca-"
    play sound ctc
    "(Quando você se vira para dentro\nde casa pra pegar a faca\npra ele tirar o mato...)"
    play sound ctc
    "(Você sente algo batendo na sua\ncabeça com muita força...!)"
    play sound ctc
    "(Você desmaia no chão.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...!)"
    play sound ctc
    "AI CARA! Puta que pariu, que\nporra é essa?!"
    play sound ctc
    "(Você sente uma dor de cabeça\nabsurda!)"
    play sound ctc
    "Eu tô sangrando...!"
    play sound ctc
    "(Tem sangue saindo da sua\nnuca!)"
    play sound ctc
    "AQUELE MENDIGO FILHO DA PUTA!"
    play sound ctc
    "Desesperado, você olha em volta\nda sua casa para ver se\ntudo está no lugar..."
    play sound ctc
    "(...)"
    play sound ctc
    "(Não tem literalmente NADA\nno lugar!)"
    play sound ctc
    "(Não tem NENHUM móvel e NENHUM\naparelho na sua casa!\nLevaram absolutamente TUDO!)"
    play sound ctc
    "SÓ DEIXARAM A PRIVADA...!"
    play sound ctc
    "COMO QUE ESSE FILHO DA PUTA\nLEVOU TUDO SOZINHO?!\nISSO É IMPOSSÍVEL!"
    play sound ctc
    "(Você tranca sua casa e vai\nfazer uma OCOrrência na delegacia,\npois levaram até o seu celular.)"
    play sound ctc
    $ register_ending("K")
    jump game_over
    return


