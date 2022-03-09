label cap01_02_casa:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Nossa, hoje é o dia da pelada com o\nJames..."
    play sound ctc
    "Cadê a galera aí pra gente matar a\nsaudade?"
    play sound ctc
    "Bora esperar a ligação de alguém\naí e eu já vou lá pro futebol."
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            pass
        "<Ignorar>":
            jump wrong_end_01_02_1
    hide textbox_aux
    stop music
    "Alô?"
    play sound ctc
    "Fala aí Senna, bora lá pro futebol\nagora, eu já tô indo mano..."
    play sound ctc
    "Beleza meu querido, já tô saindo\nde casa agora."
    play sound ctc
    "(desliga o telefone)"
    play sound ctc
    "Tava esperando a semana inteira\npra jogar essa bola..."
    play sound ctc
    return

label wrong_end_01_02_1:
    play sound ctc
    "Quer saber? Que se foda esse\ntelefone, tô cansado pra caralho..."
    play sound ctc
    "(Você deixa o telefone tocando sem\natendê-lo...)"
    play sound ctc
    "(O barulho irritante parece nunca\nter fim...)"
    play sound ctc
    "(Você decide tacar o telefone pela\njanela da rua e um carro passa em\ncima dele.)"
    play sound ctc
    "(Mas o telefone simplesmente não para\nde tocar.)"
    play sound ctc
    "CAMBADA DE DEMÔNIO!"
    play sound ctc
    "(O barulho de seu toque ainda ecoa em\nsua mente, te levando à insanidade...)"
    play sound ctc
    "VOCÊS NÃO ME DEIXAM EM PAZ!"
    play sound ctc
    "(Você decide ir até o aterro\nsanitário mais próximo e enterra o\ntelefone satânico no meio da\npilha de lixo.)"
    play sound ctc
    "(Ele ainda não para de tocar, mas\nisso não importa mais.)"
    play sound ctc
    "(Você volta para casa e decide jogar\npalavras-cruzadas.)"
    play sound ctc
    $ register_ending("A")
    jump game_over