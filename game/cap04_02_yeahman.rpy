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
            pass
        "<Deixar ele agonizando no chão>":
            jump wrong_end_04_02_1
    hide textbox_aux
    "(Como que esse louco conseguiu machucar a perna no saco de pancada...?)"
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
    "Tenho o remédio certinho pra você, beleza?"
    play sound ctc
    "Fica tranquilo aí..."
    play sound ctc
    $ play_video("mod_assets/videos/yeahman2.webm","yeahman_01_web")
    #$ renpy.movie_cutscene("mod_assets/videos/yeahman.webm")
    return

label wrong_end_04_02_1:
    stop music
    "(Você vê a dor e agonia na expressão aflita de Yeah Man...)"
    play sound ctc
    "(Isso te enche de DETERMINAÇÃO.)"
    play sound ctc
    "OHHH, OHHHH, OOOOOOHHHH!!!"
    play sound ctc
    "(Ver uma vida humana agonizar e se contorcer no chão de dor é extremamente satisfatório...)"
    play sound ctc
    "(Você não consegue parar de olhar para essa senna.)"
    play sound ctc
    "(Não importa quem você seja ou o que você conquistou na vida...)"
    play sound ctc
    "(Todos somos iguais quando a morte chega.)"
    play sound ctc
    "(Você trata este momento como algo muito importante, talvez você não vai conseguir ver algo assim de novo.)"
    play sound ctc
    "(O grande momento da Morte, o epílogo da sua própria história e existência.)"
    play sound ctc
    "OHHH, OOHHH, OHHHHH!"
    play sound ctc
    "(Ele não consegue se levantar, em mais ou menos uma hora provavelmente ele irá morrer de dor no chão.)"
    play sound ctc
    "(Estou muito ansioso para ver este momento chegar.)"
    play sound ctc
    "(Tenho todo o tempo do mundo! HAHAHA!)"
    play sound ctc
    "(Yeah Man olha em seus olhos, desesperado.)"
    play sound ctc
    "(Em como a humanidade pode ser tão perversa e doentia.)"
    play sound ctc
    "AH CARALHO!"
    play sound ctc
    "(Você sente uma vontade urgente de rir.)"
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

label yeahman_01_web:
    return

