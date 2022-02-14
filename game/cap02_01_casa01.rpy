label cap02_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Nossa, a pelada ontem foi muito top..."
    play sound ctc
    "Deu pra dar uma brincada..."
    play sound ctc
    "..."
    play sound ctc
    "Mas que droga, eu ainda fiquei de ver\no problema no carro."
    play sound ctc
    "Eu tenho certeza que é na mangueira."
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "Mas que toque irritante esse aí, eu vou\ntrocar essa porcaria!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            pass
        "<Desligar>":
            jump wrong_end_02_01_1
    hide textbox_aux
    stop music
    "Alô?"
    play sound ctc
    "Hello, Alexandrêh!"
    play sound ctc
    "Seul charroh estáh quaseh prohtho!\nGostharhia de passahr na oficihnah?"
    play sound ctc
    "No problem."
    play sound ctc
    "(Você desliga o telefone e vai em\ndireção à oficina.)"
    play sound ctc
    "(Você ainda fica curioso sobre onde\nestava o problema no carro.)"
    play sound ctc
    return

label wrong_end_02_01_1:
    stop music
    "(Você desliga o telefone o mais rápido\nque pode.)"
    play sound ctc
    "(\"Eu odeio esse toque!\", você pensa.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Aleatoriamente, você se lembra de que\no resultado para a prova do concurso\nda Polícia Militar de Cupiqueno havia\nsido divulgado na delegacia.)"
    play sound ctc
    "(Você vai correndo para lá, pois com\ncerteza já haviam se passado vários\nmeses que você não procurou\nsaber do resultado.)"
    play sound ctc
    "(Chegando lá, você não acredita no que\nacabou de ler:)"
    play sound ctc
    "(Seu nome está na lista de aprovados!)"
    play sound ctc
    "(Você foi aprovado em primeiro lugar!)"
    play sound ctc
    "(Você pergunta para o policial se o\nconcurso do ano havia sido\nencerrado.)"
    play sound ctc
    "\"Você deu sorte rapaz, a última chamada\npara os aprovados do concurso será\nexatamente agora!\""
    play sound ctc
    "(Você fica incrédulo de como você deu\nmuita muita muita muita muita sorte.)"
    play sound ctc
    "(\"Essa foi a escolha dos Deuses G.\",\nvocê pensa.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(três meses depois)"
    play sound ctc
    "(É o seu primeiro dia no treinamento\nda Polícia Militar de Cupiqueno!)"
    play sound ctc
    play music celular
    "(Sua mãe te liga, emocionada com sua\nconquista.)"
    play sound ctc
    stop music
    "(Muito ocupado com seu treinamento,\nvocê apenas responde antes\nde desligar:)"
    play sound ctc
    "TÁ ATRAPALHANDO MEU TRABALHO, SEU...!"
    play sound ctc
    $ register_ending("F")
    jump game_over

