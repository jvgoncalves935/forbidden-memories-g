label epilogo:
    $ drpc_update("epilogo")
    
    scene black
    stop music
    
    play music fm_credits
    show textbox_black at center
    #show intro_001 at top

    show img_epilogo_01 at top_fade
    "(...)"
    play sound ctc
    
    "(Haha, isso aqui é muito bom!)"
    play sound ctc

    hide img_epilogo_01
    show img_epilogo_02 at top_fade
    "{p=1.2}{nw}"

    hide img_epilogo_02
    show img_epilogo_01 at top_fade
    "{p=1.2}{nw}"

    hide img_epilogo_01
    show img_epilogo_03 at top_fade
    "{p=2.2}{nw}"

    hide img_epilogo_03
    show img_epilogo_04 at top_fade
    "{p=1.2}{nw}"

    hide img_epilogo_04
    show img_epilogo_05 at top_fade
    "{p=1.2}{nw}"
    
    hide img_epilogo_05
    show img_epilogo_06 at top_fade
    voice voz_epilogo_01
    "AAAAHH! Então é aí que você tava?"
    play sound ctc

    hide img_epilogo_06
    show img_epilogo_07 at top_fade
    voice voz_epilogo_02
    "O que você está fazendo com isso aí?"
    play sound ctc
    
    hide img_epilogo_07
    show img_epilogo_08 at top_fade
    voice voz_epilogo_03
    "O que você tem aí atrás?"
    play sound ctc
    
    voice voz_epilogo_04
    "Nada..."
    play sound ctc
    
    hide img_epilogo_08
    show img_epilogo_09 at top_fade
    voice voz_epilogo_05
    "Nada?"
    play sound ctc
    
    hide img_epilogo_09
    show img_epilogo_10 at top_fade
    voice voz_epilogo_06
    "Porque você tá com medo...? Tá fazendo\no quê?"
    play sound ctc
    
    voice voz_epilogo_07
    "Tô fazendo nada não...!"
    play sound ctc
    
    voice voz_epilogo_08
    "O que você tem aí atrás?"
    play sound ctc
    
    voice voz_epilogo_09
    "Tem nada não..."
    play sound ctc
    
    hide img_epilogo_10
    show img_epilogo_11 at top_fade
    voice voz_epilogo_10
    "Deixa eu ver!"
    play sound ctc
    
    voice voz_epilogo_11
    "Tem nada não..."
    play sound ctc
    
    hide img_epilogo_11
    show img_epilogo_12 at top_fade
    voice voz_epilogo_12
    "Isso aqui é o quê...?"
    play sound ctc
    
    voice voz_epilogo_13
    "Olha, vendo revista de homem pelado,\ntá vendo pau é?"
    play sound ctc
    
    hide img_epilogo_12
    show img_epilogo_13 at top_fade
    voice voz_epilogo_14
    "Tava não, tava aí-"
    play sound ctc
    
    hide img_epilogo_13
    show img_epilogo_14 at top_fade
    voice voz_epilogo_15
    "E isso aqui é o quê...?"
    play sound ctc
    
    hide img_epilogo_14
    show img_epilogo_15 at top_fade
    voice voz_epilogo_16
    "Tá vendo pau em revista...? PEGA NUM\nORIGINAL, NUM DE VERDADE!"
    play sound ctc
    
    hide img_epilogo_15
    show img_epilogo_16 at top_fade
    voice voz_epilogo_17
    "Vem aqui, você não quer ver um pau...?\nPega aí!"
    play sound ctc
    
    hide img_epilogo_16
    show img_epilogo_17 at top_fade
    voice voz_epilogo_18
    "Isso, pega no pau do professor!"
    play sound ctc
    
    hide img_epilogo_17
    show img_epilogo_19 at top_fade
    voice voz_epilogo_19
    "Não é isso que você quer, pau?\nTô te dando pau, aqui oh."
    play sound ctc
    
    hide img_epilogo_19
    show img_epilogo_21 at top_fade
    voice voz_epilogo_20
    "Cai de boca, dá um beijinho nele..."
    play sound ctc
    
    hide img_epilogo_21
    show img_epilogo_22 at top_fade

    voice voz_epilogo_21
    "Tá com medo do quê? Se abaixa\naí, chupa meu pau aí!"
    play sound ctc

    hide img_epilogo_22
    show img_epilogo_23 at top_fade
    "{p=1.2}{nw}"

    stop music fadeout 4.0
    hide img_epilogo_23
    "{p=4.0}{nw}"

    stop voice
    stop music

    $ register_ending("G")
    return