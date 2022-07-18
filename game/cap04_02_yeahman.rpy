label cap04_02_yeahman:
    $ drpc_update("cap04-1")
    scene black
    stop music
    show textbox_black at center
    
    #show intro_001 at top
    stop voice

    $ renpy.movie_cutscene("mod_assets/videos/yeahman.webm")
    
    show img_04_02_01 at top_fade
    play music fm_sebek_neku
    "(...!)"
    play sound ctc
    
    hide img_04_02_01
    show img_04_02_02 at top_fade

    show senna_s8 at side_image_in zorder 3
    "{p=0.6}{nw}"

    "Machucou, cara?"
    play sound ctc

    show senna_s8 at side_image_out
    "{p=0.6}{nw}"
    hide senna_s8
    
    hide img_04_02_02
    show img_04_02_03 at top_fade

    show yeahman_s1 at side_image_in zorder 3
    "{p=0.6}{nw}"

    voice voz_cap04_02_16
    "YEAH MAN!"
    play sound ctc

    show yeahman_s1 at side_image_out
    "{p=0.6}{nw}"
    hide yeahman_s1
    
    stop music
    
    hide img_04_02_03
    show img_04_02_04 at top_fade
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

    hide img_04_02_04
    show img_04_02_05 at top_fade
    play music fm_modern_shop
    
    "(Como que esse louco conseguiu\nmachucar a perna no saco\nde pancada...?)"
    play sound ctc
    
    hide img_04_02_05
    show img_04_02_06 at top_fade

    show yeahman_s1 at side_image_in zorder 3
    "{p=0.6}{nw}"

    voice voz_cap04_02_01
    "OHH..."
    play sound ctc

    show yeahman_s1 at side_image_out
    "{p=0.6}{nw}"
    hide yeahman_s1
    
    hide img_04_02_06
    show img_04_02_07 at top_fade

    show senna_s8 at side_image_in zorder 3
    "{p=0.6}{nw}"

    "Na perna... tá doendo muito?"
    play sound ctc

    show senna_s8 at side_image_out
    "{p=0.6}{nw}"
    hide senna_s8
    
    hide img_04_02_07
    show img_04_02_08 at top_fade

    show yeahman_s1 at side_image_in zorder 3
    "{p=0.6}{nw}"

    voice voz_cap04_02_18
    "YEAH MAN! YEAH MAN!"
    play sound ctc

    show yeahman_s1 at side_image_out
    "{p=0.6}{nw}"
    hide yeahman_s1
    
    hide img_04_02_08
    show img_04_02_09 at top_fade

    show senna_s8 at side_image_in zorder 3
    "{p=0.6}{nw}"

    "Pera aí, deixa eu dar uma olhada..."
    play sound ctc

    show senna_s8 at side_image_out
    "{p=0.6}{nw}"
    hide senna_s8
    
    hide img_04_02_09
    show img_04_02_10 at top_fade
    "{p=1.5}{nw}"

    hide img_04_02_10
    show img_04_02_11 at top_fade
    "{p=1.5}{nw}"

    hide img_04_02_11
    show img_04_02_12 at top_fade
    "(...)"
    play sound ctc

    hide img_04_02_12
    show img_04_02_13 at top_fade
    "{p=1.5}{nw}"

    hide img_04_02_13
    show img_04_02_14 at top_fade
    "(...)"
    play sound ctc
    
    hide img_04_02_14
    show img_04_02_15 at top_fade
    "{p=1.5}{nw}"

    hide img_04_02_15
    show img_04_02_16 at top_fade
    "{p=1.5}{nw}"

    hide img_04_02_16
    show img_04_02_17 at top_fade
    voice voz_cap04_02_21
    "Isso aqui não é muito grave não."
    play sound ctc
    
    hide img_04_02_17
    show img_04_02_18 at top_fade
    voice voz_cap04_02_22
    "Eu tenho o remédio certinho\npra você, beleza?"
    play sound ctc
    
    hide img_04_02_18
    show img_04_02_19 at top_fade
    voice voz_cap04_02_23
    "Fica tranquilo aí, só\nrelaxar..."
    play sound ctc
    
    show yeahman_s1 at side_image_in zorder 3
    "{p=0.6}{nw}"

    voice voz_cap04_02_19
    stop music
    "OOHH!"
    play sound ctc

    show yeahman_s1 at side_image_out
    "{p=0.6}{nw}"
    hide yeahman_s1
    
    "(Yeah Man começa a te encarar,\ncom medo do que você\nirá fazer com ele.)"
    play sound ctc
    
    hide img_04_02_19
    "(Ele se levanta para fugir\nde você, mas você segura\nbem firme.)"
    play sound ctc
    stop voice

    "{p=1.0}{nw}"

    $ renpy.movie_cutscene("mod_assets/videos/yeahman2.webm")

    show img_yeah_man_foca at top
    voice voz_cap04_02_20
    "{p=23.9}{nw}"

    hide img_yeah_man_foca
    "{p=2.0}{nw}"

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