label cap03_02_doutora01:
    $ drpc_update("cap03-1")
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    voice voz_cap03_02_01
    "(Toc toc toc toc toc toc)"
    play sound ctc
    voice voz_cap03_02_02
    "Pode entrar..."
    play sound ctc
    show textbox_aux
    play music audio.fm_password
    menu:
        "<Entrar na secretaria>":
            hide textbox_aux
            pass
        "<Sair correndo igual um louco>":
            hide textbox_aux
            jump wrong_end_03_02_1
    stop music
    play sound ctc
    voice voz_cap03_02_03
    "É o seguinte... Fiquei sabendo...\nAtravés de um amigo que a\nclínica de vocês é especializada\nno... no reto e eu tô com\num problema no meu reto..."
    play sound ctc
    voice voz_cap03_02_04
    "Eu tô tendo algumas dores assim, tô\ntendo algumas sensações diferentes\nno meu CU..."
    play sound ctc
    voice voz_cap03_02_05
    "Então essa sensação ela vai e volta,\nvai e volta..."
    play sound ctc
    voice voz_cap03_02_06
    "E como tem uma doutora especialista em\nCU aqui, eu queria passar com\nela pra ver, pra resolver o\nproblema do meu CU, entendeu?!"
    play sound ctc
    voice voz_cap03_02_07
    "Entendeu? As vezes eu sinto calor, as\nvezes ele coça, não sei,\nentendeu..."
    play sound ctc
    voice voz_cap03_02_08
    "Quanto tempo tu vem sentindo essas-"
    play sound ctc
    voice voz_cap03_02_09
    "Ah, tem uns 6 meses já..."
    play sound ctc
    voice voz_cap03_02_10
    "Pode entrar..."
    play sound ctc
    voice voz_cap03_02_11
    "Chegou seu paciente, ele tá com\nproblema, aí ele veio ver se\nconsegue fazer alguma coisa\npra ajudar ele..."
    play sound ctc
    voice voz_cap03_02_12
    "Ah, fazer uns exames né, seu nome?"
    play sound ctc
    voice voz_cap03_02_13
    "Alexandre!"
    play sound ctc
    voice voz_cap03_02_14
    "Vem comigo Alexandre.\nObrigada, hein."
    play sound ctc
    voice voz_cap03_02_15
    "Você quer que eu explique\nmais ou menos ou não?"
    play sound ctc
    voice voz_cap03_02_16
    "Pode explicar."
    play sound ctc
    voice voz_cap03_02_17
    "Então tem uns 6 meses aí que... tô\ncom o CU coçando, aí\nnão sei o motivo e tal.."
    play sound ctc
    voice voz_cap03_02_18
    "Tá sentindo alguma dor?"
    play sound ctc
    voice voz_cap03_02_19
    "Não, não... Só uma coceirinha\nmesmo, assim..."
    play sound ctc
    "(...)"
    play sound ctc
    "(...)"
    play sound ctc
    voice voz_cap03_02_20
    "Tem mais um pouquinho daquele gel lá?\nTem? Dá um pouquinho\ndele pra mim, dá..."
    play sound ctc
    voice voz_cap03_02_21
    "AAAAAAAAAAI DOUTORA..."
    play sound ctc
    voice voz_cap03_02_22
    "Isso, tá gostoso, tá?"
    play sound ctc
    voice voz_cap03_02_23
    "AAAAI... AAAAI QUE SENSAÇÃO...\nDEFERENTE... AAAI..."
    play sound ctc
    voice voz_cap03_02_24
    "Tô pondo o dedinho..."
    play sound ctc
    voice voz_cap03_02_25
    "PODE...."
    play sound ctc
    voice voz_cap03_02_26
    "Isso, isso tá gostoso?"
    play sound ctc
    voice voz_cap03_02_27
    "AAI VOU TRAZER MEU\nAMIGO AQUI... VOU... TÁ COM MESMO\nPROBLEMA QUE EU..."
    play sound ctc
    voice voz_cap03_02_28
    "É O MÁRCIO, MARCINHO NÉ? MEU\nPARCEIRO ELE... ELE TEVE...\nCHEGOU A FALAR COMIGO..."
    play sound ctc
    voice voz_cap03_02_29
    "Mas ele é gay?"
    play sound ctc
    voice voz_cap03_02_30
    "NÃO ELE É CASADO, ELE É NOIVO,\nNAMORA..."
    play sound ctc
    voice voz_cap03_02_31
    "Trás ele aqui que eu cuido\ndele também!"
    play sound ctc
    voice voz_cap03_02_32
    "AAHH... AAAAI... AAIIIII...\nAAAAAAII... AAAII..."
    play sound ctc
    voice voz_cap03_02_33
    "AI TÁ QUENTE MEU CU, TÁ? TÁ SUA PUTA!\nUUGH... AI TA ME SOCANDO...\nTO ME SENTINDO A BICHA\nLOKA, SABIA...? AAAGH... AAGH..."
    play sound ctc
    voice voz_cap03_02_34
    "AAGH... AAA... AAA... QUERIA...\nQUERIA... AAA..."
    play sound ctc
    voice voz_cap03_02_35
    "Queria dar, né? Né? Isso..."
    play sound ctc
    voice voz_cap03_02_36
    "Queria..."
    play sound ctc
    "(...)"
    play sound ctc
    return

label wrong_end_03_02_1:
    $ drpc_update("finalN")
    stop music
    "(Você escuta vozes na sua cabeça\ndizendo para sair dali\ncorrendo!)"
    play sound ctc
    play sound_bg running_footsteps fadein 3.0
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
    play sound_bg siren2 fadein 3.0
    "Esse paciente fugiu do hospital,\nalguém pare ele!"
    play sound ctc
    "(O quê...?)"
    play sound ctc
    "(Depois de correr um total de três\nminutos, você cai no chão\nde exaustão.)"
    play sound ctc
    voice voz_cap02_04_39
    "(O enfermeiro te imobiliza e chama\na ambulância para vir\nte buscar.)"
    play sound ctc
    voice voz_cap05_01_02
    stop sound_bg fadeout 4.0
    "(Ele aplica uma injeção no seu\npescoço e você desmaia.)"
    play sound ctc
    "(...)"
    play sound ctc
    play sound_bg voices fadein 5.0
    "(...)"
    play sound ctc
    "Hein...?"
    play sound ctc
    voice voz_cap03_02_37
    "Porra é essa?"
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
    "EU QUERO SAIR...!"
    play sound ctc
    "ME SOLTA!"
    play sound ctc
    "ALGUÉM ME AJUDA!"
    play sound ctc
    "POR FAVOR!"
    play sound ctc

    $ game_over_musica = False
    $ game_over_fadeout_sound = 2.0
    $ game_over_delay_musica = 8.0
    
    $ register_ending("N")
    jump game_over
