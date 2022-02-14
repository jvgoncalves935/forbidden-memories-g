label cap02_02_oficina_gringo:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    
    play sound ctc
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Entrar na oficina>":
            pass
        "<Dar meia volta e sair berrando>":
            jump wrong_end_02_02_1
    hide textbox_aux
    stop music

    play sound ctc
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Sair do local o mais rápido possível>":
            jump wrong_end_02_02_2
        "<\"No problem.\">":
            pass
    hide textbox_aux
    stop music
    return


label wrong_end_02_02_1:
    stop music
    "(Sua consciência diz para você sair da\noficina o mais rápido que\nvocê puder!)"
    play sound ctc
    "(...)"
    play sound ctc
    "OH, OH, OH, OH, OH, OH, OH!"
    play sound ctc
    "(Você decide sair correndo na rua\nimitando o Quico.)"
    play sound ctc
    "(Por algum motivo, parece ser\nengraçado...)"
    play sound ctc
    "(Você está bem no centro da rua\nda Avenida PrinciPAL...)"
    play sound ctc
    "OH, OH, OH, OH, OH, OH, OH!"
    play sound ctc
    "(carro freando bruscamente)"
    play sound ctc
    "(Você é atingido por um carro e\nacaba sendo arremessado\npara longe!)"
    play sound ctc
    "OOOOOOHHHH, OOOOOOHHHH, AAAAHHHH,\nAIIIII...!"
    play sound ctc
    "(Todos na rua ficam assustados com o\nacidente, algumas pessoas vêm\nte ajudar.)"
    play sound ctc
    "(Sua perna doi muito, ela está\njorrando muito sangue!)"
    play sound ctc
    "(A ambulância chega 5 minutos depois\ne te socorre.)"
    play sound ctc
    "(Você começa a ficar fraco devido a\nperda excessiva de sangue\ne desmaia...)"
    play sound ctc
    "(A última coisa que você ouve\nsocorrista dizer é:)"
    play sound ctc
    "\"Vamos ter que levá-lo para\na Doutora de Plantão!\""
    play sound ctc
    $ register_ending("H")
    jump game_over

label wrong_end_02_02_2:
    stop music
    "(Inicialmente, você pensa em sair\ncorrendo o máximo que puder\nda Oficina do Kawan...)"
    play sound ctc
    "(Mas uma onda emergente de maldade\nconsome o seu coração!)"
    play sound ctc
    "OW SEU FILHO DA PUTA!"
    play sound ctc
    "(Indignado com a armadilha que o Gringo\narmou, você dá um soco na\ncara dele e sai tranquilamente\nda oficina.)"
    play sound ctc
    "(Anita, ainda com o pezão pra fora,\nfica chocada.)"
    play sound ctc
    "(Revoltado com a humilhação que passou,\nvocê decide tacar o foda-se e\ncompra um bilhete na Tele Senna.)"
    play sound ctc
    "(Você preenche o bilhete puto e entrega\npara a atendente, ainda puto.)"
    play sound ctc
    "(Você vai para a casa puto, com a\nsensação de que se esqueceu de\nalguma coisa... mas continua puto.)"
    play sound ctc
    "(cinco dias depois)"
    play sound ctc
    "\"E o ganhador do Chevromete Blazer\npreto é... Alexandre Senna de\nCupiqueno!\", você ouve na TV."
    play sound ctc
    "(Ainda puto, você vai para a casa\nlotérica resgatar seu prêmio.)"
    play sound ctc
    "\"Meu sonho foi sempre viajar pra\numa cachoeira...\", você ainda diz."
    play sound ctc
    "(Puto.)"
    play sound ctc
    "(uma semana depois)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Não mais puto, você curte a viagem\ncom o carro novo na\nCachoeira Talargo.)"
    play sound ctc
    "(A sensação de aventura e liberdade\né muito gostosa...)"
    play sound ctc
    $ register_ending("I")
    jump game_over
