label cap03_02_doutora01:
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "Toc! toc! toc! toc! toc! toc!"
    play sound ctc
    #(0:09 - 0:10 doutora rosa)
    "Pode entrar..."
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Entrar na secretaria>":
            pass
        "<Sair correndo igual um louco>":
            jump wrong_end_03_02_1
    hide textbox_aux
    stop music
    #(0:14 - 0:29 Senna)
    "É o seguinte..."
    play sound ctc
    "Fiquei sabendo... Através de um amigo que a clínica de vocês é especializada em reto e eu tô com um com um problema no meu reto..."
    play sound ctc
    #(0:29 - 0:37 Senna)
    "Eu tô tendo algumas dores assim, tô tendo algumas sensações diferentes no meu CU..."
    play sound ctc
    #(0:38 - 0:52 Senna)
    "Então essa sensação ela vai e volta, vai e volta..."
    play sound ctc
    "E como tem uma doutora especialista em CU aqui, eu queria passar com ela pra ver, pra ela resolver o problema do meu CU, entendeu?!"
    #(0:52 - 0:57 Senna)
    play sound ctc
    "Entendeu? As vezes eu sinto calor, as vezes ele coça, não sei, entendeu..."
    #(0:57 - 0:59 doutora rosa)
    play sound ctc
    "Quanto tempo tu vem sentindo isso dai?"
    #(1:00 - 1:01 Senna)
    play sound ctc
    "Ah, tem uns 6 meses já..."
    #(1:15 - 1:15 doutora preto)
    "Pode entrar..."
    play sound ctc
    #(1:22 - 1:29 doutora rosa)
    "Chegou seu paciente, ele tá com problema, aí ele veio ver se consegue alguma coisa pra ajudar ele.."
    play sound ctc
    #(1:30 - 1:32 doutora preto)
    "Ah, fazer uns exames né, seu nome?"
    play sound ctc
    #(1:32 - 1:33 Senna)
    "Alexandre!"
    play sound ctc
    #(1:33 - 1:35 doutora preto)
    "Cê vem comigo Alexandre. Obrigada hein"
    play sound ctc
    #(1:36 - 1:37 Senna)
    "Você quer que eu explique mais ou menos ou não?"
    play sound ctc
    #(1:38 - 1:38 doutora preto)
    "Pode explicar."
    play sound ctc
    #(1:38 - 1:48 Senna)
    " Então tem uns 6 meses aí que... tô com o CU coçando, aí não sei o motivo e tal.."
    play sound ctc
    #(1:48 - 1:49 doutora preto)
    "Tá sentindo alguma dor?"
    play sound ctc
    #(1:49 - 1:52 Senna)
    "Não!, Não!... só uma coceirinha mesmo..."
    play sound ctc
    #(1:59 - 2:01 Senna)
    "Tem mais um pouquinho daquele gel lá? Tem? Coloca um pouquinho dele pra mim."
    play sound ctc
    #(2:02 - 2:04 Senna)
    "AAAAAAAAAAI DOUTORA..."
    play sound ctc
    #(2:05 - 2:05 doutora preto)
    "Isso, tá gostando, tá?"
    play sound ctc
    #(2:07 - 2:12 Senna)
    "AAAAI... AAAAI QUE SENSAÇÃO... DIFERENTE... AAAI..."
    play sound ctc
    #(2:11 - 2:11 doutora preto)
    "Tô pondo o dedinho..."
    play sound ctc
    #(2:15 - 2:15
    "PODE...."
    play sound ctc
    #(2:18 - 2:19 doutora preto)
    "Isso, isso tá gostoso?"
    play sound ctc
    #(2:19 -2:26 Senna)
    "AAAAAAAAI... AAI VOU TRAZER MEU AMIGO AQUI... TÁ COM MESMO PROBLEMA QUE EU..."
    play sound ctc
    #(2:28 - 2:36 Senna)
    "VAI... É O MÁRCIO, MARCINHO MEU PARCEIRO ELE... ELE TEVE CHEGOU A FALAR COMIGO..."
    play sound ctc
    #(2:36 - 2:36 doutora preto)
    "Mas ele é gay?"
    play sound ctc
    #(2:37 - 2:41 Senna)
    "NÃO ELE É CASADO, ELE É NOIVO, ELE NAMORA..."
    play sound ctc
    #(2:41 - 2:42 doutora preto)
    "Trás ele aqui que eu cuido dele também!"
    play sound ctc
    #(2:51 - 3:03 Senna)
    "AAI... AAAAI... AAIIIII... AAAAAAII... AAAII... AAAI..."
    play sound ctc
    #(3:04 - 3:16 Senna)
    "TÁ QUENTE MEU CU, TÁ... TÁ SUA PUTA... UUGH... AI TA ME SOCANDO... TO ME SENTINDO A BICHA LOKA... AAAGH... AAGH..."
    play sound ctc
    #(3:23 - 3:32 Senna)
    "AAGH... AAA... AAA... QUERIA... QUERIA... AAA..."
    play sound ctc
    #(3:42 - 3:43 doutora preto)
    "Queria, né viadinho?"
    play sound ctc
    #(3:43 - 3:44 Senna)
    "Queria..."
    play sound ctc
    return

label wrong_end_03_02_1:
    stop music
    "(Você escuta vozes na sua cabeça\ndizendo para sair dali\ncorrendo!)"
    play sound ctc
    "(Você sai correndo como se não\nhouvesse amanhã.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Você ainda está correndo, quase\nsem fôlego.)"
    play sound ctc
    "(Nesse momento, você olha para\ntrás e vê um homem bombado\ncom roupa de hospital vindo\natrás de você!)"
    play sound ctc
    "(Será que te confundiram com\nalguém?)"
    play sound ctc
    "(Não importa, ele REALMENTE\nquer te pegar!)"
    play sound ctc
    "(Você luta para correr do homem,\nmas você está ficando sem\nforças para correr.)"
    play sound ctc
    "Esse paciente fugiu do hospital,\nalguém pare ele!"
    play sound ctc
    "(O quê...?)"
    play sound ctc
    "(Depois de correr um total de três\nminutos, você cai no chão\nde exaustão.)"
    play sound ctc
    "(O enfermeiro te imobiliza e chama\na ambulância para vir\nte buscar.)"
    play sound ctc
    "(Ele aplica uma injeção no seu\npescoço e você desmaia.)"
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    "Que porra é essa?"
    play sound ctc
    "(Você acorda amarrado em uma\nmaca de hospital.)"
    play sound ctc
    "(Você está preso em um quarto de\nhospital, pelo menos é\no que parece.)"
    play sound ctc
    "(Você consegue ouvir vozes ecoando\npelas paredes...)"
    play sound ctc
    "Mas que lugar é esse?!"
    play sound ctc
    "QUE LUGAR É ESSE?"
    play sound ctc
    "SOCORRO!"
    play sound ctc
    "SOCORRO! ALGUÉM ME SOLTA!"
    play sound ctc
    "ALGUÉM ME SOLTA, POR FAVOR!"
    play sound ctc
    "EU QUERO SAIR!"
    play sound ctc
    $ register_ending("N")
    jump game_over
