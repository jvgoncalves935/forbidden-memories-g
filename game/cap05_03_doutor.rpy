label cap05_03_doutor:
    $ drpc_update("finalG")

    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    play sound audio.millenniumitem
    "(Senna conseguiu o Milzão!)"
    play sound ctc
    "(Dá pra fazer muita coisa com esse\ndinheiro, especialmente\nnos anos 2000.)"
    play sound ctc
    "(Recusando a proposta de Alemão,\nvocê nunca mais volta a\nfalar com eles.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(no dia seguinte depois\ndo Filme G)"
    play sound ctc
    stop voice

    $ renpy.movie_cutscene("mod_assets/videos/bob_alemao.webm")

    "(Com o dinheiro que ganhou de Bob\ne Alemão, Senna conseguiu financiar\nseus estudos para realizar\nseu mais novo sonho:)"
    play sound ctc
    "(Se tornar um médico renomado e\nrespeitado.)"
    play sound ctc
    "\"Vou ser um médico mil vezes\nmelhor que a doutora!\""
    play sound ctc
    "(Senna estudou nas horas vagas de\nseu serviço como segurança\ncom os novos livros que\nhavia comprado.)"
    play sound ctc
    "(Com muito esforço e dedicação,\nSenna foi aprovado no\nvestibular de Medicina\nda UFCP!)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Universidade Federal de Cupiqueno.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(6 anos depois)"
    play sound ctc
    "(...)"
    voice voz_cap05_03_01
    "A coisa vai ser... vai ser muito\nséria hoje... tá certo?\nHoje... a nossa aula... vai ser\nsobre SEXO..."
    play sound ctc
    voice voz_cap05_03_02
    "UUUHUUUUUUUUUUUUUUULLLLL!!!"
    play sound ctc
    voice voz_cap05_03_03
    "Vai tirar a roupa?\nQuero ver nu!"
    play sound ctc
    voice voz_cap05_03_04
    "E a gente... e hoje\nvocês vão aprender como\nque se utiliza... o preservativo..."
    play sound ctc
    voice voz_cap05_03_05
    "Você sabe muito bem!"
    play sound ctc
    voice voz_cap05_03_06
    "Coloca o pau pra fora aí..."
    play sound ctc
    voice voz_cap05_03_07
    "Tem que ser com a boca, não\npode utilizar a mão!"
    play sound ctc
    "(Alexandre Senna começou sua carreira\nacadêmica como médico e\npesquisador da UFCP.)"
    play sound ctc
    "\"Não vai ter nenhum médico com o\nCUrrículo à minha altura.\""
    play sound ctc
    "(...)"
    play sound ctc
    "(Certo dia, Doutor Senna encontra\ncom um rosto familiar na\nacademia...)"
    play sound ctc
    "James...?"
    play sound ctc

    voice voz_cap05_03_08
    "E aí, tudo bemmmm??"
    play sound ctc
    "Fala aí, meu camarada!\nQuanto tempo!"
    voice voz_cap05_03_09
    "Meu nome é James Matarazzo..."
    play sound ctc
    "Eu sei, mermão. Nossa, que saudade\ndos velhos tempos..."
    play sound ctc
    
    voice voz_cap05_03_10
    "Meu nome é James, James Matarazzo...\nsou cirurgião plástico..."
    play sound ctc
    voice voz_cap05_03_11
    "Nas horas vagas eu gosto de fazer\nuns esportes sexuais..."
    play sound ctc
    voice voz_cap05_03_12
    "Esse aqui é meu amigo..."
    play sound ctc
    voice voz_cap05_03_13
    "Tudo bom? Meu nome é\nAlexandre Senna..."
    play sound ctc
    voice voz_cap05_03_14
    "E... tô aí, com meu amigo, meu\ncamarada aqui que a gente\nse conheceu no parque aí\nfazendo exercício, não é,\nJames?"
    play sound ctc

    "(No futuro, Senna teve uma carreira\ngrande e gostosa com um\nfuturo brilhante.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Estas são as Memórias Proibídas\nde Alexandre Senna.)"
    play sound ctc
    "FIM"
    play sound ctc
    stop voice


    $ backup_game_menu_keymap = config.keymap['game_menu']
    $ backup_game_hide_windows = config.keymap['hide_windows']
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()  


    $ register_ending("C5")
    play music fm_youwin
    scene black

    show capitulo_concluido
    pause 1.0
    play sound voz_cap05_03_15
    pause 3.7
    play sound voz_cap05_03_16
    pause 4.26
    hide capitulo_concluido
    
    show voce_desbloqueou
    show carta_img_cap_05
    show carta_desc_cap_05
    pause 1.5
    play sound voz_cap05_03_17
    pause 5.0

    stop music fadeout 3.0
    pause 1.0
    stop sound fadeout 3.0
    pause 4.0

    hide voce_desbloqueou
    hide carta_img_cap_05
    hide carta_desc_cap_05

    $ config.keymap['game_menu'] = backup_game_menu_keymap
    $ config.keymap['hide_windows'] = backup_game_hide_windows
    $ renpy.display.behavior.clear_keymap_cache()

    return


label wrong_end_05_02_1:
    stop music
    $ register_ending("W")
    jump game_over

label wrong_end_05_02_2:
    stop music
    $ register_ending("X")
    jump game_over
