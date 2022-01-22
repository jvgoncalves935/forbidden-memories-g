## This splash screen is the first thing that Renpy will show the player
##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    #Check for each archive needed
    for archive in ['audio','images','fonts']:
        if not archive in config.archives:
            #If one is missing, throw an error and chlose
            renpy.error("Os arquivos de Doki Doki Literature Club não foram encontrados na pasta /game. Confira a instalação e tente novamente.")

        if 'scripts' in config.archives:
            #If one is missing, throw an error and chlose
            renpy.error("O arquivo 'scripts.rpa' de Doki Doki Literature Club NÃO pode ser incluído pasta /game. Por favor, exclua-o e tente novamente.")

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
        

    def is_all_endings_unlocked():
        for key, value in persistent.endings.items():
            if(not value):
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
                        ("Z",False)]
                        
            persistent.endings = dict(array_aux)

        #teste
        for key, value in persistent.endings.items():
            persistent.endings[key] = True
        
        #print(persistent.endings)
    def label_callback(name, abnormal):
        store.current_label = name

    config.label_callback = label_callback
    #"--> You are at [current_label]"

    menu_trans_time = 1
    #The default splash message, originally shown in Act 1 and Act 4
    splash_message_default = "'A melancolia é a felicidade de se ser triste.' -Victor Hugo"
    #Optional splash messages, originally chosen at random in Act 2 and Act 3

    init_endings()
    
    
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

    $ quick_menu = False

    if(persistent.splash_complete is None or not persistent.splash_complete):
        #jump capXX
        scene black
        show black
        with dissolve
        show splash_image at top
        with dissolve
        "{p=1.5}{nw}"
        play music fm_nameinput
        "[config.name] é um jogo feito\nem Ren'Py a partir de um template de\num mod de Doki Doki Literature Club.\nEste jogo não é afiliado à Team\nSalvato."
        play sound ctc
        "Este jogo é um CLONE sem fins\nlucrativos de \"Yu-Gi-Oh: Forbidden\nMemories\", desenvolvido pela Konami\nEntertaiment Japan (atual Konami\nCorporation) em 1999. Todos os\ndireitos reservados."
        play sound ctc
        "Este é um jogo de humor, porém\nenvolve temas adultos. Mesmo assim,\nele NÃO possui nenhum conteúdo\nexplícito. Não é recomendado para\nmenores de 18 anos."
        play sound ctc
        "Caso não conheça, esse jogo fala\nsobre os personagens do universo do\nPai de Família, atualmente chamado de \"Universo G\"."
        play sound ctc
        "Este jogo não possui intenção de\nofender ou difamar os atores da vida\nreal, é apenas um jogo de humor feito por fãs. Incentivamos os jogadores a\nrespeitarem os atores da vida real."
        play sound ctc
        "Caso o jogo esteja com baixa\nperformance, vá até o Menu de\nConfigurações e desative a opção\n\"Efeito Texto\"."
        play sound ctc
        scene black
        with Dissolve(1.5)
        $ persistent.splash_complete = True
        pause 1.0
        stop music

    #Optional, load a copy of DDLC save data
    #call import_ddlc_persistent


    $ basedir = config.basedir.replace('\\', '/')

    #autoload handling
    #Use persistent.autoload if you want to bypass the splashscreen on startup for some reason
    if persistent.autoload and not _restart:
        jump autoload

    # Start splash logic
    $ config.allow_skipping = False

    $ renpy.movie_cutscene("mod_assets/videos/operation_senna.webm")
    $ renpy.movie_cutscene("mod_assets/videos/intro.webm")

    # Splash screen
    show white
    #$ persistent.ghost_menu = False #Handling for easter egg from DDLC
    #$ splash_message = splash_message_default #Default splash message
    $ renpy.music.play(config.main_menu_music)
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
    $ drpc_update()
    jump expression persistent.autoload

label quit:
    return
