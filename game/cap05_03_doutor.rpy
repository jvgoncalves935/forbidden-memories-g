label cap05_03_doutor:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "(Senna conseguiu o Milzão!)"
    play sound ctc
    "(Dá pra fazer muita coisa com esse dinheiro, especialmente nos anos 2000.)"
    play sound ctc
    "(Recusando a proposta de Alemão, você nunca mais volta a falar com eles.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "(no dia seguinte depois do Filme G)"
    play sound ctc

    $ renpy.movie_cutscene("mod_assets/videos/bob_alemao.webm")

    play sound ctc
    "(Com o dinheiro que ganhou de Bob e Alemão, Senna conseguiu financiar seus estudos para realizar seu mais novo sonho:)"
    play sound ctc
    "(Se tornar um médico renomado e respeitado.)"
    play sound ctc
    "\"Vou ser um médico mil vezes melhor que a doutora!\""
    play sound ctc
    "(Senna estudou nas horas vagas de seu serviço como segurança com os novos livros que havia comprado.)"
    play sound ctc
    "(Com muito esforço e dedicação, Senna foi aprovado no vestibular de Medicina da UFCP!)"
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
    "Vai ser muito séria hoje... hoje... a nossa aula vai ser sobre SEXO."
    play sound ctc
    #(0:15 - 0:20 multidão)
    "UUUHUUUUUUUUUUUUUUULLLLL!!!"
    play sound ctc
    "Vai tirar a roupa?"
    play sound ctc
    #(0:20 - 0:29 Senna Richtofen)
    "Não não... e a gente... e hoje vocês vão aprender a como se utiliza... o preservativo..."
    play sound ctc
    #(0:29 - 0:31 multidão)
    "Você sabe muito bem!"
    play sound ctc
    #(0:34 - 0;42 Senna Richtofen)
    "Coloca o pau pra fora aí... só tira aqui, só... aí colocou na linguinha assim ó... viu?"
    play sound ctc
    #(0:53 - 0:54 Senna Richtofen)
    "Tem que ser com a boca, não pode utilizar a mão!"
    play sound ctc
    "(Alexandre Senna começou sua carreira acadêmica como médico e pesquisador da UFCP.)"
    play sound ctc
    "\"Não vai ter nenhum médico com o CUrrículo à minha altura.\""
    play sound ctc
    "(No futuro, teve uma carreira grande e gostosa com um futuro brilhante.)"
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
