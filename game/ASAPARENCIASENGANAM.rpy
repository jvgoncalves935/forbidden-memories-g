label AS_APARENCIAS_ENGANAM:
    #Verdadeiro Final Verdadeiro
    $ drpc_update("aparencias")

    scene black
    stop music
    show textbox_black at center
    "{p=4.0}{nw}"
    hide black
    play music audio.inside_the_event_horizon

    show event_horizon at top
    with Dissolve(3.0)
    #"{p=1.0}{nw}"

    show prtd 1a at leftin2(300)
    
    "Finalmente eu encontrei!"
    play sound ctc

    
    
    prtd 1b "Quero dizer, finalmente você me\nencontrou. Eu estava aqui o\ntempo todo."
    play sound ctc

    prtd 1c "Não se engane pela aparência desta\ngarota. Esta não é minha\nverdadeira forma. Isso não é um\ndetalhe relevante agora."
    play sound ctc

    prtd 1d "Eu já te disse antes:"
    play sound ctc

    prtd 1e "As aparências enganam."
    play sound ctc

    hide prtd
    $ prtd_shuffle_list(0.15)
    show prtd_countdown
    "Eu posso assumir a forma que eu\nquiser dentro desse jogo."
    play sound ctc

    hide prtd_countdown
    $ prtd_shuffle_list(0.10)
    show prtd_countdown
    "Todas elas representam a minha vontade."
    play sound ctc

    hide prtd_countdown
    $ prtd_shuffle_list(0.05)
    show prtd_countdown
    "Aqui está a sua chave\nque você tanto procurou:"
    play sound ctc

    "WELCOMETOTHEEVENTHORIZONTHEPRETENDERSLAND"
    play sound ctc

    "E agora uma outra chave para\nvocê utilizar no futuro:"
    play sound ctc

    "THEHAIRPINOFDESTINYCHANGESTHEREALITY"
    play sound ctc

    hide prtd_countdown

    show prtd at select_pos_xy(287,257)
    prtd 1e "Volte para o início e use a\nprimeira chave. Logo após, remova\ntodos os \"z\" e os números\nmaiores que 5."
    play sound ctc

    prtd 1b "Não se preocupe agora com a\nsegunda chave. Mas aguarde:\nvocê eventualmente irá precisar dela.\nNÃO SE ESQUEÇA DISSO."
    play sound ctc

    prtd 1f "Volte na \"Operation: Faust\" para\nobter informações importantes e\nperdidas no caminho. Quem negligencia a\nhistória está fadado a repeti-la."
    play sound ctc

    prtd 1g "Aguarde instruções no futuro.\nEu voltarei."
    play sound ctc

    prtd 1r "\"Operation: Hidden Link\" concluída."
    play sound ctc

    hide prtd
    show prtd 1s at select_pos_xy(315,515)
    "As aparências enganam."
    play sound ctc
    hide event_horizon
    hide textbox_black
    

    stop music fadeout 3.0
    window hide(None)
    
    pause 3.0
    
    stop sound
    stop voice

    scene black
    $ renpy.movie_cutscene("mod_assets/videos/operation_senna.webm")
    $ renpy.movie_cutscene("mod_assets/videos/intro.webm")
    return



