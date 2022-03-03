label cap02_04_roda_amigos:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top

    #(0:00 - 0:02 magrelo)
    "Foi mó legal lá na balada,\nvocês perderam meu..."
    play sound ctc
    #(0:02 - 0:04 Senna)
    "A gente perdeu o quê?"
    play sound ctc
    #(0:04 - 0:07 magrelo)
    "Ah... Bagnight meu... foi muito louco\nlá!"
    play sound ctc
    #(0:07 - 0:09 índio)
    "Mas tinha muita coisa de bom lá?"
    play sound ctc
    #(0:09 - 0:18 magrelo)
    "Nossa senhora... vocês perderam! Ixi,\ntinha muita gente, muita mina... foi\nmuito louco... muito louco mesmo!"
    play sound ctc
    #(0:19 - 0:22 Senna)
    "Essas balada dele aí acho que é meio\nfurada!..."
    play sound ctc
    #(0:22 - 0:22 magrelo)
    "Que furada?"
    play sound ctc
    #(0:22 - 0:24 Senna)
    "Aquela que a gente foi, foi muito\nlegal, não foi?"
    play sound ctc
    #(0:24 - 0:25 índio)
    "Aquela foi!"
    play sound ctc
    #(0:26 - 0:33 Senna)
    "Você devia ver, a putaria né ow\níndio... a putaria rolou solta..."
    play sound ctc
    #(0:36 - 0:47 mangueira evil)
    "Não, não, é sério... putaria foi o que\neu fiz outro dia aí com os cara...\nEu saí com os amigos, meu..."
    play sound ctc
    "Aí a gente começou a... a brincar,\na zuar entendeu... Fazer uma\nbrincadeira diferente, entendeu...?"
    play sound ctc
    #(0:47 - 0:54 Senna)
    "AAAAH, a brincadeira dele..."
    play sound ctc
    #(0:54 - 0:55 magrelo)
    "É furada essa brincadeira dele!"
    play sound ctc
    #(0:55 - 1:04 mangueira evil)
    "Não, essa brincadeira não é furada não,\nessa brincadeira é batata, muito boa..."
    play sound ctc
    "Aqui a gente não dá pra fazer essa\nbrincadeira porque a gente é amigo,\nmas dá pra usar a imaginação..."
    play sound ctc
    #(1:04 - 1:05 índio)
    "E como é que é?"
    play sound ctc
    #(1:06 - 1:09 mangueira evil)
    "Ah... tipo... a brincadeira mesmo\né: \"O Que Você Faria Se?\"."
    play sound ctc
    #(1:10 - 1:10 Senna)
    "Faria o quê?"
    play sound ctc
    #(1:11 - 1:12 mangueira evil)
    "Uma coisa muito boa..."
    play sound ctc
    #(1:12 - 1:17 Senna)
    "Que brincadeira é essa... é as mesmas\nde sempre...? Explica um pouco aí!"
    play sound ctc
    #(1:17 - 1:44 mangueira evil)
    "Vou explicar direitinho pra você,\nentão... como é que é o negócio, você\nimagina assim um cara gostosão,\nentendeu?"
    play sound ctc
    "Todo malhadão, moreno, entendeu? Numa\npiscina assim, saindo de uma piscina,\nentendeu? Todo malhadão, aqueles\nbravo enorme, entendeu?"
    play sound ctc
    "Aquela dessa assim, te olhando, se\npegando assim, passando a mão,\nentendeu... Imagina assim... só vai\nimaginando agora, aqueles olhos te\ncatando assim..."
    play sound ctc
    "Puta meu, mó tesão assim, oh..."
    play sound ctc
    #(1:44 - 1:44 Senna)
    "Tá, para..."
    play sound ctc
    #(1:45 - 1:59 mangueira evil)
    "Te pegar assim oh, te pegar e colocar\nem você assim oh, num lugar,\nentendeu..."
    play sound ctc
    "Bem, te pegar ali na piscina mesmo,\nentendeu? Começar a fazer assim,\naquelas coisas assim... bem...\ndiferente contigo..."
    
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Repreender esse espírito maligno>":
            jump wrong_end_02_04_1
        "<Entrar no Mundo dos Sonhos>":
            pass
    hide textbox_aux
    stop music

    #(2:02.- 2;02 Senna)
    "Posso imaginar...?"
    play sound ctc
    #(2:02 - 2:03 mangueira evil)
    "Pode!"
    play sound ctc
    #(2:04 - 2:05 Senna)
    "Então tá..."
    play sound ctc
    #(2:06 - 2:07 mangueira evil)
    "Pode, claro... Fala sua imaginação\npra gente..."
    play sound ctc
    #(2:08 - 2:35 Senna)
    "Então... pô, essa piscina aqui\nsozinho... e eu queria o homem\ndos meus sonhos... Poxa..."
    play sound ctc
    #(2:41 - 2:44 homem dos sonhos)
    "Você não pediu o homem dos seus\nsonhos...? Aqui estou!"
    play sound ctc
    #(3:01 - 3:11 Senna)
    "Pô, você é real mesmo...?\nNão acredito..."
    play sound ctc
    "Tudo isso só pra mim..."
    play sound ctc
    return


label wrong_end_02_04_1:
    stop music
    "EU AMALDIÇOO TODO MUNDO QUE FAZ PARTE\nDESSE GRUPO!"
    play sound ctc
    "NA VIDA DE VOCÊS VAI CAIR MALDIÇÃO!"
    play sound ctc
    "NÃO TEM O QUE FAZER NÃO, RAPAZ?"
    play sound ctc
    "VAI SE FUDER, CAMBADA DE VIADO\nDESGRAÇADO!"
    play sound ctc
    "(Furioso, você vira a mesa no chão,\nderrubando tudo com muita\nignorância.)"
    play sound ctc
    "(Logo em seguida, você dá um chute com\ntoda a força na porta e sai\ncorrendo daquela casa.)"
    play sound ctc
    "(É inadmissível para você ser\nconsiderado como homossexual.)"
    play sound ctc
    "(Você é hétero!)"
    play sound ctc
    "(Ainda correndo na rua, você nota que\nestá sendo seguido...)"
    play sound ctc
    "É a polícia...!"
    play sound ctc
    "(De repente, um policial surge\nrepentinamente da sua frente e pula\nem cima de você, te imobilizando.)"
    play sound ctc
    "AHHHHHH!"
    play sound ctc
    "\"Você que é o ladrão de residências\nde Cupiqueno?\", diz o policial."
    play sound ctc
    "EU SOU HÉTERO! EU SOU HÉTERO!"
    play sound ctc
    "\"Parece que ele está sob efeito de\nnarcóticos, será necessário uma análise\ndetalhada na delegacia.\""
    play sound ctc
    "\"Esse aí tá mais pro Presídio\nAry Fontoura!\""
    play sound ctc
    "EU SOU HÉTERO!"
    play sound ctc
    "EU SOU HÉTERO...!"
    play sound ctc
    $ register_ending("L")
    jump game_over
