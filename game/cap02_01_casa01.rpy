label cap02_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    return

label wrong_end_02_01_1:
    stop music
    "(Você desliga o telefone o mais rápido que pode.)"
    play sound ctc
    "(\"Eu odeio esse toque!\", você pensa.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Aleatoriamente, você se lembra de que o resultado para a prova do concurso da Polícia Militar de Cupiqueno havia sido divulgado na delegacia.)"
    play sound ctc
    "(Você vai correndo para lá, pois com certeza já haviam se passado vários meses de que você não procurou saber do resultado.)"
    play sound ctc
    "(Chegando lá, você não acredita no que acabou de ler:)"
    play sound ctc
    "(Você foi aprovado no concurso!)"
    play sound ctc
    "(Você foi aprovado em primeiro lugar!)"
    play sound ctc
    "(Você pergunta para o policial se o concurso do ano havia sido encerrado.)"
    play sound ctc
    "\"Você deu sorte rapaz, a última chamada para os aprovados do concurso será exatamente agora!\""
    play sound ctc
    "(Você fica incrédulo de como você deu muita muita muita muita muita sorte.)"
    play sound ctc
    "(\"Essa foi a escolha dos Deuses G.\", você pensa.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(três meses depois)"
    play sound ctc
    "(É o seu primeiro dia no treinamento da Polícia Militar de Cupiqueno!)"
    play sound ctc
    "(Sua mãe te liga, emocionada com sua conquista.)"
    play sound ctc
    "(Muito ocupado com seu treinamento, você apenas responde antes de desligar:)"
    play sound ctc
    "TÁ ATRAPALHANDO MEU TRABALHO, SEU...!"
    play sound ctc
    $ register_ending("F")
    jump game_over

