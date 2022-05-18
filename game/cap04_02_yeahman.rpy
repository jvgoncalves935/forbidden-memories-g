label cap04_02_yeahman:
    $ drpc_update("cap04-1")
    scene black
    stop music
    show textbox_black at center
    
    #show intro_001 at top
    stop voice

    $ renpy.movie_cutscene("mod_assets/videos/yeahman.webm")
    play music fm_sebek_neku
    "(...!)"
    play sound ctc
    
    "Machucou, cara?"
    play sound ctc
    
    voice voz_cap04_02_16
    "YEAH MAN!"
    play sound ctc
    
    stop music
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Socorrer Yeah Man>":
            hide textbox_aux
            pass
        "<Deixar ele agonizando no chão>":
            hide textbox_aux
            jump wrong_end_04_02_1
    stop music
    play music fm_modern_shop
    voice voz_cap04_02_01
    "(Como que esse louco conseguiu\nmachucar a perna no saco\nde pancada...?)"
    play sound ctc
    
    "(...)"
    play sound ctc
    
    "Na perna... tá doendo muito?"
    play sound ctc
    
    voice voz_cap04_02_18
    "YEAH MAN! YEAH MAN!"
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
    
    voice voz_cap04_02_19
    stop music
    "OOHH!"
    play sound ctc
    
    "(Yeah Man começa a te encarar,\ncom medo do que você\nirá fazer com ele.)"
    play sound ctc
    
    "(...)"
    play sound ctc
    stop voice
    
    $ renpy.movie_cutscene("mod_assets/videos/yeahman2.webm")

    show img_yeah_man_foca at center
    voice voz_cap04_02_20
    "{p=23.9}{nw}"
    hide img_yeah_man_foca
    stop voice
    return

label wrong_end_04_02_1:
    $ drpc_update("finalR")
    stop music
    play music fm_inside_the_puzzle
    voice voz_cap04_02_01
    "(Você vê a dor e agonia na expressão\naflita de Yeah Man...)"
    play sound ctc
    
    voice voz_cap04_02_02
    "(Isso te enche de DETERMINAÇÃO.)"
    play sound ctc
    
    voice voz_cap04_02_03
    "(Ver uma vida humana agonizar e se\ncontorcer no chão de dor é\nextremamente satisfatório...)"
    play sound ctc
    
    voice voz_cap04_02_04
    "(Você não consegue parar de olhar\npara essa senna.)"
    play sound ctc
    
    voice voz_cap04_02_05
    "(Não importa quem você seja ou o\nque você conquistou na vida...)"
    play sound ctc
    
    voice voz_cap04_02_06
    "(Todos somos iguais quando a morte\nchega.)"
    play sound ctc
    
    voice voz_cap04_02_07
    "(Você trata este momento como algo\nmuito importante, talvez você não\nvai conseguir ver algo assim de novo.)"
    play sound ctc
    
    voice voz_cap04_02_08
    "(O grande momento da Morte, o epílogo\nda sua própria história e\nexistência.)"
    play sound ctc
    
    voice voz_cap04_02_09
    "(Ele não consegue se levantar, em mais\nou menos uma hora provavelmente\nele irá morrer de dor no chão.)"
    play sound ctc
    
    voice voz_cap04_02_10
    "(Estou muito ansioso para ver este\nmomento chegar.)"
    play sound ctc
    
    voice voz_cap04_02_11
    "(Tenho todo o tempo do mundo!\nHAHAHA!)"
    play sound ctc
    
    voice voz_cap04_02_12
    "(Yeah Man olha em seus olhos,\ndesesperado.)"
    play sound ctc
    
    voice voz_cap04_02_13
    "(Desesperado em pensar sobre como\na humanidade pode ser\ntão perversa e doentia.)"
    play sound ctc
    
    voice voz_cap04_02_14
    stop music fadeout 5.0
    "(Você sente uma vontade urgente\nde rir.)"
    play sound ctc
    
    voice voz_cap04_02_15
    "(Rir.)"
    play sound ctc
    
    "(Você começa a rir.)"
    play sound ctc
    
    "{p=0.2}{nw}"
    play sound voz_cap04_02_17
    stop music
    pause 9.0
    $ register_ending("R")
    jump game_over
    return