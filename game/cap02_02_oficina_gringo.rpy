label cap02_02_oficina_gringo:
    $ drpc_update("cap02-1")
    scene black
    stop music
    show textbox_black at center
    #show intro_001 at top
    "(...)"
    play sound ctc
    "(20 minutos depois)"
    play sound ctc
    "(Você acabou de chegar em frente à\nOficina do Gringo.)"
    play sound_bg heresy fadein 4.0
    play sound ctc
    "(A oficina é bem fudida mas\nesse é o lugar.)"
    play sound ctc
    "(Você escuta uma música tocando em\num rádio do outro\nlado da rua.)"
    play sound ctc
    "Eu conheço essa música de\nalgum lugar..."
    play sound ctc
    stop sound_bg fadeout 1.5
    "Ah, foda-se. Tenho mais o que fazer."
    play sound ctc

    play music audio.fm_password
    show textbox_aux
    menu:
        "<Entrar na oficina>":
            hide textbox_aux
            pass
        "<Dar meia volta e sair gritando>":
            hide textbox_aux
            jump wrong_end_02_02_1
    stop music
    voice voz_cap02_02_01
    "Excuse me?"
    play sound ctc
    voice voz_cap02_02_02
    "Excuse me... hi."
    play sound ctc
    voice voz_cap02_02_03
    "Uhh... What's your name?"
    play sound ctc
    voice voz_cap02_02_04
    "Mai neime is... Alexandre."
    play sound ctc
    voice voz_cap02_02_05
    "Alexandre..."
    play sound ctc
    "(Você tem amnésia, porra?\nOs gringo são bundão mesmo.)"
    play sound ctc
    voice voz_cap02_02_06
    "Uhh... Alexandre. Are you busy...\nor... you can talk a few\nminutes, yeah?"
    play sound ctc
    voice voz_cap02_02_07
    "Yeah."
    play sound ctc
    voice voz_cap02_02_08
    "Okay..."
    play sound ctc
    voice voz_cap02_02_09
    "I have a small problem and maybe\nyou can help me out..."
    play sound ctc
    "(Foda-se o seu problema\nCADÊ MEU CARRO CARALHO)"
    play sound ctc
    voice voz_cap02_02_10
    "Uhh, this is my girlfriend, Anita..."
    play sound ctc
    "(Nuoooossa, minha filhona,\neu não acrediiito...)"
    play sound ctc
    voice voz_cap02_02_11
    "She loves... FUCKING, you understand?"
    play sound ctc
    voice voz_cap02_02_12
    "And... I have been fucking her for\ntwo days now and I cannot\nfuck her anymore."
    play sound ctc
    voice voz_cap02_02_13
    "And she's getting a little 'cause I\ncannot fuck her, you think\nyou can help me out here?"
    play sound ctc
    voice voz_cap02_02_14
    "Ies, okei..."
    play sound ctc
    "(Esse gringo é broxa ou o quê?\nSerá que ele tem algum\nestranho? Devo me preocupar?)"
    voice voz_cap02_02_15
    "You think you can fuck her for me?"
    play sound ctc
    voice voz_cap02_02_16
    "Just... you know, maybe half an hour...\nshe suck your dick, you\nfuck her in the ass..."
    play sound ctc
    voice voz_cap02_02_17
    "And you can go home, grab and have it.\nSo you can do it, yeah?"
    play sound ctc
    voice voz_cap02_02_18
    "Ié, ié, ooouuu ié...!"
    play sound ctc
    "(Caralho vei, deu MUITO\nMUITO bom...)"
    play sound ctc
    voice voz_cap02_02_19
    "He's okay for you, Anita? You\nliked him, yes?"
    play sound ctc
    voice voz_cap02_02_20
    "YAS."
    play sound ctc
    voice voz_cap02_02_21
    "Ok, you know... I'll leave you alone..."
    play sound ctc
    voice voz_cap02_02_22
    "I need you two guys come around\nthe car..."
    play sound ctc
    voice voz_cap02_02_23
    "Now close the gate, that no one\ncan see us, okay?"
    play sound ctc
    voice voz_cap02_02_24
    "Oukei, oukei..."
    play sound ctc
    voice voz_cap02_02_25
    "Okay now, here is the thing, Alexandre,\nwe have a little surprise\nfor you..."
    play sound ctc
    voice voz_cap02_02_26
    "Surprais...?"
    play sound ctc
    voice voz_cap02_02_27
    "A surprise for you, yeah..."
    play sound ctc
    voice voz_cap02_02_28
    "So we have... woman? Stand up for\na second... Huh?"
    play sound ctc
    voice voz_cap02_02_29
    "And maybe you can show him...\nyour surprise..."
    play sound ctc
    "(Do que esse filho da\nputa tá falando?)"
    play sound ctc
    voice voz_cap02_02_30
    "Here my friend, here is a\nextra for you today."
    play sound ctc
    voice voz_cap02_02_31
    "Ouuuu mai góóó...!"
    play sound ctc
    "(É isso que eles chamam de\nMulher do Futuro?)"
    play sound ctc
    "(Talvez seja um fenômeno da\nnatureza, olha o tamanho\ndo fenômeno...)"
    play sound ctc
    voice voz_cap02_02_32
    "Huh? It is not incredible?"
    play sound ctc
    voice voz_cap02_02_33
    "Does not look fantastic with\nthose big fucking tits,\nget home with it!"
    play sound ctc
    "(dois minutos depois)"
    play sound ctc
    "(Anita te deu uma chuopadinha\nmuito boa.)"
    play sound ctc
    "(Foi muito bom, mas e agora? O que\nserá que vai acontecer? Você\npensa inquieto sobre isso...)"
    play sound ctc
    voice voz_cap02_02_34
    "In fact... she sucked your dick\ngood, yeah?"
    play sound ctc
    voice voz_cap02_02_35
    "Ié, ié."
    play sound ctc
    voice voz_cap02_02_36
    "You wanna give her a little, huh..."
    play sound ctc
    

    play sound ctc
    play music audio.fm_password
    show textbox_aux
    menu:
        "<Sair do local o mais rápido possível>":
            hide textbox_aux
            jump wrong_end_02_02_2
        "<\"No problem.\">":
            hide textbox_aux
            pass
    stop music

    voice voz_cap02_02_37
    "No problem."
    play sound ctc
    voice voz_cap02_02_38
    "You do it? That's my boy!"
    play sound ctc
    voice voz_cap02_02_39
    "Okay... alright..."
    play sound ctc
    voice voz_cap02_02_40
    "God, you beautiful in here...\nYou're SO fucking beautiful!"
    play sound ctc
    voice voz_cap02_02_41
    "Plis... plis fuck mai és..."
    play sound ctc
    voice voz_cap02_02_42
    "Plis fuck me..."
    play sound ctc
    voice voz_cap02_02_43
    "OU IEEE!"
    play sound ctc
    voice voz_cap02_02_44
    "OU VERI, VERI, VERI... VERI GUD!"
    play sound ctc
    voice voz_cap02_02_45
    "OU FOCK ME, IE FOCK ME!"
    play sound ctc
    voice voz_cap02_02_46
    "(palmada na bunda) FOCK ME!"
    play sound ctc
    voice voz_cap02_02_47
    "OU IE... OU FOCK ME..."
    play sound ctc
    voice voz_cap02_02_48
    "FOCK ME PLIS...!"
    play sound ctc
    voice voz_cap02_02_49
    "OU...!"
    play sound ctc
    voice voz_cap02_02_50
    "FOCK ME! FOCK ME..."
    play sound ctc

    return


label wrong_end_02_02_1:
    $ drpc_update("finalH")
    stop music
    "(Sua consciência diz para você sair da\noficina o mais rápido que\nvocê puder!)"
    play sound ctc
    "(...)"
    play sound ctc
    play sound_bg audio.city_01 fadein 2.0
    "(...)"
    play sound ctc
    "(Você decide sair correndo na rua\nimitando o Quico.)"
    play sound ctc
    voice voz_cap02_02_51
    "OH, OH, OH, OH, OH, OH!"
    play sound ctc
    "(Por algum motivo, parece ser\nengraçado...)"
    play sound ctc
    "(Você está bem no centro da rua\nda Avenida PrinciPAL...)"
    play sound ctc
    voice voz_cap02_02_52
    "OH, OH, OH, OH, OH, OH!"
    play sound ctc
    "(Uma criança com a mãe que estavam\natravessando a rua decidem\nvoltar e fugir correndo\nde você.)"
    play sound ctc
    voice voz_cap02_02_51
    "OH, OH, OH, OH, OH, OH!"
    play sound ctc
    "(Você está bem no meio da rua e...)"
    play sound ctc
    stop music
    play sound_bg audio.car_crash noloop
    "{p=1.5}{nw}"
    voice voz_cap02_02_53
    "OOOOOOIIIIHHHH, OOOOOOHHHH!!!"
    play sound ctc
    play sound_bg audio.ambulance_01 noloop
    "(Todos na rua ficam assustados com o\nacidente, algumas pessoas vêm\nte ajudar.)"
    play sound ctc
    play sound_bg audio.ambulance_02
    "(Sua perna doi muito, ela está\njorrando muito sangue!)"
    play sound ctc
    voice voz_cap02_02_54
    "AAAAIIIIHHHH, AIIIII...! UUGHH!!"
    play sound ctc
    "(A ambulância chega 5 minutos depois\ne te socorre.)"
    play sound ctc
    
    "(Você começa a ficar fraco devido a\nperda excessiva de sangue\ne desmaia...)"
    play sound ctc
    "(A última coisa que você ouve\nsOCOrrista dizer é:)"
    play sound ctc
    "\"Vamos ter que levá-lo para\na Doutora de Plantão!\""
    play sound ctc
    stop sound_bg fadeout 3.0
    $ register_ending("H")
    jump game_over

label wrong_end_02_02_2:
    $ drpc_update("finalI")
    stop music
    "(Inicialmente, você pensa em sair\ncorrendo o máximo que puder\nda Oficina do Gringo...)"
    play sound ctc
    "(Mas uma onda emergente de maldade\nconsome o seu coração!)"
    play sound ctc
    "OW SEU FILHO DA PUTA!"
    play sound ctc
    "{p=0.2}{nw}"
    play sound punch01
    "(Indignado com a armadilha que o Gringo\narmou, você dá um soco na\ncara dele e sai tranquilamente\nda oficina.)"
    play sound ctc
    "FALA PORTUGUÊS, CARALHO!"
    play sound ctc
    "(Anita, ainda com o pezão pra fora,\nfica chocada.)"
    play sound ctc
    "(Ela acabou de te dar uma chuopadinha,\nmas você decide não\nretribuir o favor.)"
    play sound ctc
    "(\"Eu tenho cara de comunista pra\ncompartilhar as coisas?\",\nvocê pensa.)"
    play sound ctc
    "(Revoltado com a humilhação que passou,\nvocê decide tacar o foda-se e\nvai para a casa lotérica\nmais próxima.)"
    play sound ctc
    play sound_bg audio.tele_sena
    "(Você decide tentar a sorte\nna Tele Senna.)"
    play sound ctc
    "(Você preenche o bilhete puto e entrega\npara a atendente, ainda puto.)"
    play sound ctc
    "(Você vai para a casa puto, com a\nsensação de que se esqueceu de\nalguma coisa... mas continua puto.)"
    play sound ctc
    stop sound_bg fadeout 2.0
    "(cinco dias depois)"
    play sound ctc
    "\"E o ganhador do Chevromete Blazer\npreto é...\""
    play sound ctc
    play sound_bg audio.tele_sena_metaleiro
    "\"...Alexandre Senna de Cupiqueno!\",\nvocê ouve na TV."
    play sound ctc
    "(Ainda puto, você vai para a casa\nlotérica resgatar seu prêmio.)"
    play sound ctc
    "\"Meu sonho foi sempre viajar pra\numa cachoeira...\", você ainda diz."
    play sound ctc
    "(Puto.)"
    play sound ctc
    stop sound_bg fadeout 2.0
    "(uma semana depois)"
    play sound ctc
    "(...)"
    play sound ctc
    "(Não mais puto, você curte a viagem\ncom o carro novo na\nCachoeira de Pau Grande.)"
    play sound ctc
    "(A sensação de aventura e liberdade\né muito gostosa...)"
    play sound ctc
    $ register_ending("I")
    jump game_over
