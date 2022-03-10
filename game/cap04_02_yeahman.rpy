label cap04_02_yeahman:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    $ renpy.movie_cutscene("mod_assets/videos/yeahman.webm")
    "(...!)"
    play sound ctc
    "Machucou, cara?"
    play sound ctc
    "YEAH MAN!"
    show textbox_aux
    menu:
        "<Socorrer Yeah Man>":
            hide textbox_aux
            pass
        "<Deixar ele agonizando no chão>":
            hide textbox_aux
            jump wrong_end_04_02_1
    "(Como que esse louco conseguiu\nmachucar a perna no saco\nde pancada...?)"
    play sound ctc
    "(...)"
    play sound ctc
    "Na perna... tá doendo muito?"
    play sound ctc
    "Pera aí, deixa eu dar uma olhada..."
    play sound ctc
    "(...)"
    play sound ctc
    "Já sei o que fazer."
    play sound ctc
    "Tenho o remédio certinho pra você,\nbeleza?"
    play sound ctc
    "Fica tranquilo aí..."
    play sound ctc
    "OOHH!"
    play sound ctc
    "(Yeah Man começa a te encarar,\ncom medo do que você\nirá fazer com ele.)"
    play sound ctc
    "(...)"
    play sound ctc
    $ renpy.movie_cutscene("mod_assets/videos/yeahman2.webm")
    return

label wrong_end_04_02_1:
    stop music
    "(Você vê a dor e agonia na expressão\naflita de Yeah Man...)"
    play sound ctc
    "(Isso te enche de DETERMINAÇÃO.)"
    play sound ctc
    "OHHH, OHHHH, OOOOOOHHHH!!!"
    play sound ctc
    "(Ver uma vida humana agonizar e se\ncontorcer no chão de dor é\nextremamente satisfatório...)"
    play sound ctc
    "(Você não consegue parar de olhar\npara essa senna.)"
    play sound ctc
    "(Não importa quem você seja ou o\nque você conquistou na vida...)"
    play sound ctc
    "(Todos somos iguais quando a morte\nchega.)"
    play sound ctc
    "(Você trata este momento como algo\nmuito importante, talvez você não\nvai conseguir ver algo assim de novo.)"
    play sound ctc
    "(O grande momento da Morte, o epílogo\nda sua própria história e\nexistência.)"
    play sound ctc
    "OHHH, OOHHH, OHHHHH!"
    play sound ctc
    "(Ele não consegue se levantar, em mais\nou menos uma hora provavelmente\nele irá morrer de dor no chão.)"
    play sound ctc
    "(Estou muito ansioso para ver este\nmomento chegar.)"
    play sound ctc
    "(Tenho todo o tempo do mundo!\nHAHAHA!)"
    play sound ctc
    "(Yeah Man olha em seus olhos,\ndesesperado.)"
    play sound ctc
    "(Desesperado em pensar sobre como\na humanidade pode ser\ntão perversa e doentia.)"
    play sound ctc
    "AH CARALHO!"
    play sound ctc
    "(Você sente uma vontade urgente\nde rir.)"
    play sound ctc
    "(Rir. Rir sem parar.)"
    play sound ctc
    "(Rir.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Rir.)"
    play sound ctc
    "(Você começa a rir.)"
    play sound ctc
    $ register_ending("R")
    jump game_over

