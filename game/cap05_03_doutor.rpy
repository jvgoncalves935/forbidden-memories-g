label cap05_03_doutor:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
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
    #(0:06 - 0:15 Senna Richtofen)
    "Vai ser muito séria hoje... hoje...\na nossa aula vai ser\nsobre SEXO."
    play sound ctc
    #(0:15 - 0:20 multidão)
    "UUUHUUUUUUUUUUUUUUULLLLL!!!"
    play sound ctc
    "Vai tirar a roupa?"
    play sound ctc
    #(0:20 - 0:29 Senna Richtofen)
    "Não não... e a gente... e hoje\nvocês vão aprender a como\nse utiliza... o preservativo..."
    play sound ctc
    #(0:29 - 0:31 multidão)
    "Você sabe muito bem!"
    play sound ctc
    #(0:34 - 0;42 Senna Richtofen)
    "Coloca o pau pra fora aí... só\ntira aqui, só... aí colocou\nna linguinha assim ó...\nviu?"
    play sound ctc
    #(0:53 - 0:54 Senna Richtofen)
    "Tem que ser com a boca, não\npode utilizar a mão!"
    play sound ctc
    "(Alexandre Senna começou sua carreira\nacadêmica como médico e\npesquisador da UFCP.)"
    play sound ctc
    "\"Não vai ter nenhum médico com o\nCUrrículo à minha altura.\""
    play sound ctc
    "(No futuro, teve uma carreira grande\ne gostosa com um futuro\nbrilhante.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(FIM)"
    play sound ctc
    return


label wrong_end_05_02_1:
    stop music
    $ register_ending("W")
    jump game_over

label wrong_end_05_02_2:
    stop music
    $ register_ending("X")
    jump game_over
