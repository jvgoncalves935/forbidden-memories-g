label cap03_01_casa01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top

    "Hmm..."
    play sound ctc
    "..."
    play sound ctc
    "Hmm..."
    play sound ctc
    $ renpy.movie_cutscene("mod_assets/videos/recruta.webm")
    "Ahh!"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "Foi só um sonho..."
    play sound ctc
    "Será que é a minha mente\ndizendo que eu esqueci de\nfazer alguma coisa?"
    play sound ctc
    "Eu acho que realmente esqueci\n de alguma coisa."
    play sound ctc
    "..."
    play sound ctc
    "Então que se foda."
    play sound ctc
    "Enfim, a brincadeira de ontem\nfoi maravilhosa..."
    play sound ctc
    "Acho que a gente deveria fazer\nisso mais vezes..."
    play sound ctc
    "Mas aquela dor estranha ainda\ntá me atacando, é foda..."
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "Lá vem essa porcaria de novo..."
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            hide textbox_aux
            call telefone_03_01_01 from _call_telefone_03_01_01
        "<Desligar>":
            hide textbox_aux
            stop music
            "Que se dane."
            play sound ctc
            "(desliga o telefone)"
            play sound ctc
    stop music
    "Mas que droga, o pessoal do\nconsultório não me liga..."
    play sound ctc
    "Eles ficam atrasando a minha\nconsulta, que droga!"
    play sound ctc
    "Essa dor tá me incomodando\nmuito, mal consigo me\nconcentrar!"
    play sound ctc
    "Eu preciso resolver logo essa\nsituação mas eles ficam de\nenrolação comigo!"
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "Mas que porra, hein?!"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            hide textbox_aux
            call telefone_03_01_02 from _call_telefone_03_01_02
        "<Desligar>":
            hide textbox_aux
            stop music
            "Ah, vai tomar no seu cu."
            play sound ctc
            "Vai ver se eu tô lá na esquina!"
            play sound ctc
            "O pessoal não tem mais o que fazer não?"
            play sound ctc
    hide textbox_aux
    stop music
    play music celular
    "(celular tocando)"
    play sound ctc
    "CARALHO, DE NOVO?"
    play sound ctc
    show textbox_aux
    menu:
        "<Atender o telefone>":
            hide textbox_aux
            stop music
            "Alô?"
            play sound ctc
            "Bom dia, eu falo com o\nAlexandre?"
            play sound ctc
            "Sim, sou eu mesmo."
            play sound ctc
            "Olá Alexandre, aqui é do Consultório\nSanta Mônica, estamos ligando para\nconfirmar sua consulta hoje,\nduas da tarde."
            play sound ctc
            "Está confirmado, estou disponível\npara a consulta."
            play sound ctc
            "Tudo certo, então você pode vir ao\nnosso consultório no horário\nmarcado."
            play sound ctc
            "Tudo bem, agradeço a atenção.\nMuito obrigado."
            play sound ctc
            "Obrigada, Alexandre. Até logo..."
            play sound ctc
            "(desligou o telefone)"
            play sound ctc
        "<Desligar>":
            $ wrong_end = True
            hide textbox_aux
            stop music
            "FODA-SE ESSE TELEFONE MALDITO!"
            play sound ctc
            "MAIS ALGUÉM VAI ME LIGAR?"
            play sound ctc
            "(...)"
            play sound ctc
            "(...)"
            play sound ctc
            "Parece que não..."
    hide textbox_aux
    stop music 
    
    if(wrong_end):
        jump wrong_end_03_01
    else:
        pass
    
    "Até que enfim, esse telefone já\ntava me dando nos nervos..."
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "Ah, foda-se quem tá ligando, já\nme ligaram do consultório\nmesmo..."
    stop music
    "(desligou o telefone)"
    play sound ctc
    "AI! AI... Que dor horrível...!"
    play sound ctc
    "Partiu ir pro hospital..."
    play sound ctc
    return

label telefone_03_01_01:
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "Alô?"
    play sound ctc
    voice voz_cap03_01_01
    "Alôr? É do corpo de bombeiro?"
    play sound ctc
    "Não parceiro. Até mais."
    play sound ctc
    "(desliga o telefone)"
    play sound ctc
    return

label telefone_03_01_02:
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "ALÔ!!!"
    play sound ctc
    "Alô, boa noite? Eu falo do setor\nde promoções, eu falo com\no Vinícius?"
    play sound ctc
    "PARA DE ME ADICIONAR NESSES GRUPO,\nCAMBADA DE MARDITO!"
    play sound ctc
    "SABEM O QUE VOCÊS DEVEM FAZER?"
    play sound ctc
    "COLOCAR A MÃE DE VOCÊS...\nJUNTAMENTE COM A VÓ DE VOCÊS,\nA RAPARIGA DA TIA DE VOCÊS..."
    play sound ctc
    "E O LÍDER DA RELIGIÃO QUE\nVOCÊS TEM!"
    play sound ctc
    "(desliga o telefone)"
    play sound ctc
    "NA VIDA DE VOCÊS VAI CAIR\nMALDIÇÃO!"
    play sound ctc
    return

label wrong_end_03_01:
    "Esse telefone não para de tocar,\nmas que porcaria!"
    play sound ctc
    play music celular
    "(celular tocando)"
    play sound ctc
    "AHHHHHHH...!!!"
    play sound ctc
    "..."
    play sound ctc
    "Quer saber? Eu vou SACANEAR ESSE\nPALHAÇO!"
    play sound ctc
    stop music
    "(atendeu o telefone)"
    play sound ctc
    stop music
    "{p=0.2}{nw}"
    play sound phone_click
    "Alou, Jefferson?"
    play sound ctc
    "AQUI NÃO TEM JEFFERSON NENHUM NÃO,\nQUEBRADA. TÁ QUERENDO ALGUMA\nCOISA, PALHAÇO?"
    play sound ctc
    "Ow mano, tá maluco rapá?"
    play sound ctc
    "MALUCO É O DESGRAÇADO DO TEU PAI,\nQUE TE BOTOU NO MUNDO!"
    play sound ctc
    "Você sabe com quem tá falando,\nseu noia?"
    play sound ctc
    "MERMÃO, AQUI É DA CADEIA! A GENTE\nÉ DA FACÇÃO! VOCÊ NÃO ACHA QUE\nA GENTE AQUI NÃO TE ACHA?"
    play sound ctc
    "A GENTE RASTREIA SEU NÚMERO E\nMANDA OS CARRO AÍ NA FRENTE\nDA TUA CASA TE ENCHER\nDE PORRADA, LADRÃO!"
    play sound ctc
    "Beleza então, parceiro. Eu vou\nachar teu endereço e eu mesmo\nvou aí te encher de bala."
    play sound ctc
    "QUE VAI O QUÊ, SEU BOSTINHA? AMANHÃ\nQUEM VAI TOMAR PIPOCO DE AK\nVAI SER VOCÊ! AQUI É DE\nGUARULHOS, ARY FONTOURA!"
    play sound ctc
    "{p=0.2}{nw}"
    play sound phone_end_call
    "(desligou o telefone na outra linha)"
    play sound ctc
    "Grande bosta."
    play sound ctc
    "(...)"
    play sound ctc
    "(no dia seguinte)"
    play sound ctc
    "Acabou o pão, vou ter que ir na\npadaria..."
    play sound ctc
    "(Você decide para a padaria. Coloca\no dinheiro no bolso e pega a\nchave pra abrir a porta.)"
    play sound ctc
    "(Assim que você abre a porta...)"
    play sound ctc
    "(disparos de tiros)"
    play sound ctc
    "OOOOOHHHHHH!!! OOOOOHHHHH!!!\nAAAAAAIIIII!!!"
    play sound ctc
    "(Você cai no chão com tudo,\nsangrando pelo peito.)"
    play sound ctc
    "(Logo em seguida, um homem com uma\nmeia calça na cabeça vem pra\ncima de você.)"
    play sound ctc
    "Falei que ia te achar, otário."
    play sound ctc
    "(O homem aponta a arma bem no\nmeio da sua cabeça.)"
    play sound ctc
    "{p=3.0}{nw}"
    $ register_ending("M")
    jump game_over
    return
