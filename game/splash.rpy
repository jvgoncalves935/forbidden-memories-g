## This splash screen is the first thing that Renpy will show the player
##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    import hashlib
    global melancholic_glitch
    global melancholic_glitch_filename
    
    global racionais_g_count
    global faceless_mode
    global faceless_screen_paranoiascope
    
    faceless_mode = True
    racionais_g_count = 0
    faceless_screen_paranoiascope = 0
    
    melancholic_glitch = False
    #Check for each archive needed
    if renpy.variant("pc"):
        for archive in ['audio','scripts','images','fonts']:
            if archive in config.archives:
                #If one is missing, throw an error and chlose
                renpy.error("O arquivo "+arquive+" de Doki Doki Literature Club NÃO pode ser incluído pasta /game. Por favor, exclua-o e tente novamente.")
        
        dokis_names = ['yuri.chr','sayori.chr','monika.chr','natsuki.chr']
        dokis_hashes = ['b13e8044ac74fc021a4d8a29ac28309519778c5a756071d263fa1288f653a68e',
                        'ae4670655a5381464a62ac92f1572b6dfe4dfca92c0df43075e0aceaf3352fb5',
                        '508cd3fa9bd30caadf05d2def59cfb4d98b3ffbc8b9dec23525eb2f46ab1ec44',
                        '4e0ebef87e52c9f34f1abe68f0bcb34f246f98b363b16bcc18aa3bab41aca3ec']
        i = 0
        for archive in dokis_names:
            try:
                hash_file = hashlib.sha256(renpy.file("../characters/"+archive).read().encode('utf-8')).hexdigest()
                if(hash_file != dokis_hashes[i]):
                    melancholic_glitch = True
                    melancholic_glitch_filename = archive
                    break
                i += 1
            except:
                pass

## First, a disclaimer declaring this is a mod is shown, then there is a
## check for the original DDLC assets in the install folder. If those are
## not found, the player is directed to the developer's site to download.
##
default d27roll = 0
default proll = 0.05
default prollint = 0.05


init python:
    def diceroll(trans, st, at):
        global d27roll
        d27roll = renpy.random.randint(1, 27)
        return None
    def sleeproll(trans, st, at):
        global proll
        if st >= proll:
            proll = renpy.random.random()/520
            return None
        else:
            return 0
    def sleeprollint(trans, st, at):
        global prollint
        if st >= prollint:
            prollint = renpy.random.randint(6, 16)
            return None
        else:
            return 0

    def register_ending(ending):
        persistent.endings[ending] = True
        global current_ending_id
        global current_ending_name
        current_ending_id = ending
        current_ending_name = endings_names[ending]
        
        #print(current_ending_id,current_ending_name)
        

    def is_all_endings_unlocked():
        for key, value in persistent.endings.items():
            if(not value):
                return False
        return True

    def is_all_endings_locked():
        for key, value in persistent.endings.items():
            if(value):
                return False
        return True

    def init_endings():
        if(persistent.endings is None):
            array_aux = [("A",False),
                        ("B",False),
                        ("C",False),
                        ("D",False),
                        ("E",False),
                        ("F",False),
                        ("G",False),
                        ("H",False),
                        ("I",False),
                        ("J",False),
                        ("K",False),
                        ("L",False),
                        ("M",False),
                        ("N",False),
                        ("O",False),
                        ("P",False),
                        ("Q",False),
                        ("R",False),
                        ("S",False),
                        ("T",False),
                        ("U",False),
                        ("V",False),
                        ("W",False),
                        ("X",False),
                        ("Y",False),
                        ("Z",False),
                        ("C1",False),
                        ("C2",False),
                        ("C3",False),
                        ("C4",False),
                        ("C5",False),
                        ("CXX",False),
                        ("CXY",False),
                        ("CYM",False),
                        ("mara",False),
                        ("PRTD",False)]
                        
            persistent.endings = dict(array_aux)

        #Liberar todos os finais (debug)
        for key, value in persistent.endings.items():
            persistent.endings[key] = True
        
        #print(persistent.endings)
    def label_callback(name, abnormal):
        store.current_label = name

    def init_error242424():
        if(persistent.error242424 is None):
            persistent.error242424 = False
        if(persistent.is_error242424_splashscreen is None):
            persistent.is_error242424_splashscreen = False

    config.label_callback = label_callback
    #"--> You are at [current_label]"

    menu_trans_time = 1
    #The default splash message, originally shown in Act 1 and Act 4
    
    #splash_message_default = "'VAI ESPANCA MEU CU, ME ESTUPRA CARALHO' -Alexandre Senna"
    #Optional splash messages, originally chosen at random in Act 2 and Act 3

    init_endings()
    init_error242424()
    
    
    #persistent._character_volume['narrator'] = 1.0

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

##Here's where you can change the logo file to whatever you want
image menu_logo:
    subpixel True
    
image menu_bg:
    topleft
    alpha 0.0
    "/mod_assets/images/MainMenu.png"
    easeout 1.0 alpha 1
    

image game_menu_bg:
    topleft
    "white"

image menu_fade:
    "white"
    menu_fadeout

image menu_art:
    "menu_art_y"

image menu_art_y:
    subpixel True
    #"mod_assets/bg/mainmenu/yuri0.png"
    #xcenter 805
    #ycenter 360
    #function sleeprollint
    #glitche

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform basicfade:
    alpha 0.0
    linear 1.0 alpha 1.0

transform glitche:
    subpixel True
    #function sleeprollint
    #parallel:
    #    function diceroll
    #    "mod_assets/bg/mainmenu/yuri[d27roll].png"
    #    function sleeproll
    #    repeat 27
    #"mod_assets/bg/mainmenu/yuri0.png"
    #repeat

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:
    python:
        toggle_fadein_texto(init=True)
        toggle_arabe()
        persistent.guinodia_active = False

    $ quick_menu = False
    $ persistent.faceless_mode = False

    if(melancholic_glitch):
        $ splash_message_default = "'A melancolia é a felicidade de estar triste.' -Victor Hugo"
        show img_melancholic_glitch
        play sound audio.melancholic_glitch2
        pause 2.2
        #hide img_melancholic_glitch
        python:
            global melancholic_glitch_filename
            try:
                raise Exception()    
            except:
                renpy.error("O arquivo "+melancholic_glitch_filename+" foi excluído ou corrompido. Por favor, recupere o arquivo original e reinicie o jogo.")
                pass
        
        $ renpy.quit()

    if(persistent.splash_complete is None or not persistent.splash_complete):
        #jump capXX
        #scene black
        #show black
        #with dissolve
        show splash_image at top_fade
        #with dissolve
        "{p=1.5}{nw}"
        play music fm_nameinput
        "[config.name] é uma Visual Novel\nfeita em Ren'Py a partir de um template\nde um mod de Doki Doki Literature Club.\nEste jogo não é afiliado à Team\nSalvato."
        play sound ctc
        "Este jogo é um CLONE SEM FINS\nLUCRATIVOS de \"Yu-Gi-Oh: Forbidden\nMemories\", desenvolvido pela Konami\nEntertaiment Japan (atual Konami\nCorporation) em 1999. Todos os\ndireitos reservados."
        play sound ctc
        "Este é um jogo de HUMOR, porém\nenvolve TEMAS ADULTOS. Mesmo assim,\nele NÃO POSSUI nenhum conteúdo\nvisualmente explícito. Não é\nrecomendado para menores de 18 anos."
        play sound ctc
        "Este projeto foi inspirado no vídeo\ndo YouTube \"Alexandre Senna rpG\"\ndo canal \"Cena do Senna\". O reupload\npode ser encontrado em seu canal."
        play sound ctc
        "Caso não conheça, esse jogo irá falar\nsobre os personagens do \"Universo do\nPai de Família\", atualmente chamado de\n\"Universo G\"."
        play sound ctc
        "O objetivo do humor deste jogo é\nsatirizar APENAS a atuação dos atores,\nassim como os contextos e narrativas\n\"peculiares\" dos filmes adultos\nbrasileiros de baixo orçamento,tudo\nde forma divertida e saudável."
        play sound ctc
        "Este jogo NÃO possui intenção de\nofender ou difamar os atores da vida\nreal, é apenas um jogo de humor feito\npelos fãs. Incentivamos os jogadores a\nrespeitarem os atores da vida real."
        play sound ctc
        "Nenhum conteúdo particular sobre\nos atores é divulgado neste jogo.\nSão utilizados apenas seus nomes\nfantasia, imagens e áudios de filmes\nautorais publicados na internet."
        play sound ctc
        "Todos os direitos de imagem\npertencem às produtoras dos\nfilmes adultos originais."
        play sound ctc
        "Este jogo NÃO possui intenção de\nofender ou satirizar a orientação\nsexual de nenhuma pessoa. Somos contra\nqualquer tipo de desrespeito e\nsomos a favor das liberdades\nindividuais."
        play sound ctc
        "Este jogo NÃO possui intenção de\nofender ou satirizar grupos\nminoritários, etnias ou nacionalidades\nde nenhuma pessoa. Condenamos o\nescárnio público desses tópicos."
        play sound ctc
        "\"Confirmo que estou ciente que o jogo\npossui HUMOR ADULTO e não possui\nintenção de ofender pessoas, minorias,\netnias, opções sexuais ou\nnacionalidades.\""
        play sound ctc

        show textbox_aux
        menu:
            "Eu COMPACTUO com TODOS estes avisos.":
                hide textbox_aux
                pass
            "Eu NÃO CONCORDO com os avisos e\nNÃO JOGAREI este jogo.":
                $ renpy.quit()

        "Mesmo que este jogo NÃO tenha\nconteúdo visualmente explícito, ainda\nexiste a possibilidade de possuir\nconteúdos não permitidos em\nplataformas como YouTube."
        play sound ctc
        "Por isso, este jogo possui o\n\"Modo Streamer\", onde conteúdos\nconsiderados mais \"perigosos\"\nsão censurados."
        play sound ctc
        "Você deseja ATIVAR ou DESATIVAR\no Modo Streamer?"
        play sound ctc
        $ streamer_mode_choice = True
        show textbox_aux
        menu:
            "Desejo ATIVAR o Modo Streamer.":
                hide textbox_aux
                "Caso você queria jogar o jogo\nSEM CENSURA, vá até o Menu\n\"Opções\" e DESATIVE o\nModo Streamer."
                play sound ctc
            "Desejo DESATIVAR o Modo Streamer.":
                $ streamer_mode_choice = False
                hide textbox_aux
                "Caso você queria jogar o jogo\nCOM CENSURA, vá até o Menu\n\"Opções\" e ATIVE o\nModo Streamer."
                play sound ctc
        "Caso o jogo esteja com BAIXA\nperformance, vá até o Menu\n\"Opções\" e desative a opção\n\"Efeito de Textos\"."
        play sound ctc
        "Este jogo NÃO SALVA automaticamente.\nSALVE e CARREGUE o jogo o\nmáximo que puder!"
        play sound ctc
        hide splash_image
        stop music fadeout 1.5
        #scene black
        #with Dissolve(1.5)
        "{p=1.5}{nw}"
        $ persistent.splash_complete = False
        $ persistent.config_main_menu_music = False
        $ persistent.faceless_games_first_time = True
        $ persistent.should_delete_conehead_files = False
        $ persistent.streamer_mode = streamer_mode_choice

        
        

    #Optional, load a copy of DDLC save data
    #call import_ddlc_persistent


    $ basedir = config.basedir.replace('\\', '/')

    #autoload handling
    #Use persistent.autoload if you want to bypass the splashscreen on startup for some reason
    #if persistent.autoload and not _restart:
    #    jump autoload

    # Start splash logic
    $ config.allow_skipping = False

    #$ renpy.movie_cutscene("mod_assets/videos/operation_senna.webm")
    #$ renpy.movie_cutscene("mod_assets/videos/intro.webm")

    if(not renpy.android and persistent.should_delete_conehead_files):
        $ delete_conehead_files()
        $ persistent.should_delete_conehead_files = False

    if(persistent.is_error242424_splashscreen == True):
        $ drpc_update("error242424")
        play sound conehead_influencia
        show conehead
        pause 0.1
        hide conehead
        pause 2.5
        stop sound

        $ persistent.error242424 = True
        $ persistent.is_error242424_splashscreen = False

        $ renpy.movie_cutscene("mod_assets/videos/erro242424.webm")
        if(not renpy.android):
            $ init_conehead_files()
            $ persistent.should_delete_conehead_files = True
        $ renpy.quit()

    $ drpc_update("menu")

    if(persistent.splash_complete == False): 
        $ persistent.splash_complete = True
    else:
        $ renpy.movie_cutscene("mod_assets/videos/disclaimer.webm")
    
    $ renpy.movie_cutscene("mod_assets/videos/operation_senna.webm")
    $ renpy.movie_cutscene("mod_assets/videos/intro.webm")

    # Splash screen
    show white
    #$ persistent.ghost_menu = False #Handling for easter egg from DDLC
    #$ splash_message = splash_message_default #Default splash message
    $ renpy.music.play(audio.main_menu)
    #show intro with Dissolve(0.5, alpha=True)
    #pause 2.5
    #hide intro with Dissolve(0.5, alpha=True)
    #You can use random splash messages, as well. By default, they are only shown during certain acts.
    #if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
    #    $ splash_message = renpy.random.choice(splash_messages)
    #show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    #pause 2.0
    #hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label before_main_menu:
    $ change_main_menu_music(persistent.config_main_menu_music)
    $ renpy.music.play(audio.main_menu)
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ style.say_dialogue = style.normal
    #Check if the save has been tampered with
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Trapaceiro."
        #Handle however you want, default is to force reset all save data
        $ renpy.utter_restart()
    return



label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()
    #$ drpc_update()
    jump expression persistent.autoload

label quit:
    return

label operation_senna_intro_web:
    return

label forbidden_memories_intro_web:
    return
