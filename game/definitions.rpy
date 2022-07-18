#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = True #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    import hashlib
    def print_debug(var):
        print("teste",var)

    #config.keymap['game_menu'].remove('mouseup_3')
    #config.keymap['hide_windows'].append('mouseup_3')
    #config.rollback_enabled = False

    config.keymap['self_voicing'] = []
    config.keymap['performance'] = []
    config.keymap['screenshot'] = []
    config.keymap['accessibility'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['game_menu'] = ['K_ESCAPE']
    renpy.music.register_channel("sound_bg", mixer="sfx",loop=True, tight=True)


    #config.preferences['prefs_left'].append(
    #            _Preference(
    #                "FadeIn",
    #                "fadein",
    #                [ ("Ativado", True, "True"),
    #                ("Desativado", False, "True") ],
    #                base=persistent))

    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)
    
    
    def timercountdown(st, at, duration = 20.0, done_label = 'done_label', end_label = 'end_label', screen = 'texttimer', ok_style = 'texttimer_ok', near_style = 'texttimer_near', style_swap = 30.0, tformat = "{minutes:02d}:{seconds:02d}:{microseconds:02d}"):
        remaining = duration - st
        parts_dict = {
            'minutes' : int(remaining // 60),
            'seconds' : int(remaining % 60),
            'microseconds' : int((remaining % 1) * 100)
        }
        if remaining <= 0.0:
            renpy.hide_screen(screen)
            renpy.call(end_label)
        return Text(tformat.format(**parts_dict), 
                    style = ok_style if remaining > style_swap else near_style), .1


    def init_input_operation_senna():
        global flag_input_operation_senna
        flag_input_operation_senna =False
    
    def set_input_operation_senna():
        #print(player)
        set_flag_input_operation_senna(True)
        register_ending("Z")
        hash_aux = hashlib.sha512(str(player).upper().encode("utf-8")).hexdigest().upper()
        
        #print(hash_aux)
        global hash_operation_senna
        if(hash_aux == hash_operation_senna):
            renpy.quit()
            return
        
        renpy.hide_screen("name_input")
        renpy.show_screen("creditos")
        drpc_update("menu")
        renpy.music.play(audio.fm_freeduel)

        

    
    #def is_input_operation_senna():
    #    global flag_input_operation_senna
    #    (player,"aaaaa")
    #    if(player == "" or not flag_input_operation_senna):
    #        print("input_op")
    #        renpy.show_screen("operation_senna_scr")
    #        ShowMenu("operation_senna_scr")
    #        SensitiveIf(renpy.get_screen("operation_senna_scr") == None)
    #    else:
    #        print("return")
            
    
    def set_flag_input_operation_senna(flag):
        #print("set",flag)
        global flag_input_operation_senna
        if(flag_input_operation_senna):
            return
        flag_input_operation_senna = flag

    def texto_arabe():
        string_arabe = ""
        for i in range (0,10):
            string_arabe += arabe_wordlist[renpy.random.randint(0,len(arabe_wordlist)-1)]
            string_arabe += "  "
        return string_arabe

    def toggle_arabe():
        global config_arabe

        flag = persistent.config_arabe

        if(flag is None):
            persistent.config_arabe = False
            flag = False

        config_arabe = flag

    
    def toggle_fadein_texto(init=False):
        global config_fadein_texto
        global narrator_what_prefix
        global narrator_what_suffix
        global narrator
        
        flag = persistent.config_fadein_texto
        
        if(flag is None):
            persistent.config_fadein_texto = True
            flag = True

        if(flag):
            narrator.what_prefix = narrator_what_prefix
            narrator.what_suffix = narrator_what_suffix
        else:
            narrator.what_prefix = ""
            narrator.what_suffix = ""
        
        config_fadein_texto = flag

    def change_current_music(current_music=None,next_music=None,play_next=False):
        global main_menu
        global music_player_active
        print("main menu",main_menu,"music_player",music_player_active,"current_screen",renpy.current_screen().screen_name[0])

        if not music_player_active:
            return
        if(next_music is not None):
            persistent.next_music = next_music

        if(play_next):
            if(persistent.next_music is None):
                music = config.main_menu_music
            else:
                music = persistent.next_music
        else:
            if(current_music is None):
                music = config.main_menu_music
            else:
                music = current_music 
            
        persistent.current_music = music
        print(current_music,next_music,play_next,music)
        renpy.music.play(music)
        toggle_current_music_player(False)

    def toggle_current_music_player(flag):
        print("toggle_current_music_player",flag)
        global music_player_active
        music_player_active = flag

    def current_screen():
        print("current screen: ",renpy.current_screen().screen_name[0])

    def change_channel_volume(volume,channel):
        _preferences.set_volume(channel, volume)
        renpy.restart_interaction()


    def set_half_volume():
        channel = renpy.audio.audio.get_channel("music")
        channel_volume = channel.context.secondary_volume

        half_volume = channel_volume

        if(channel_volume > 0):
            half_volume = half_volume / 2

        change_channel_volume(half_volume,'music')

        return half_volume

    def set_double_volume(half_volume):
        double_volume = half_volume

        if(double_volume * 2 < 1):
            double_volume *= 2
        else:
            double_volume = 1

        change_channel_volume(double_volume,'music')
        return

    def play_video(video,alt_label=None):
        if(not renpy.emscripten):
            renpy.movie_cutscene(video)
        else:
            renpy.call_in_new_context(alt_label)

    def guinodia_init():
        global guinodia_array
        guinodia_array = [False,False,False,False,False,False]
        #print(guinodia_array)

    def guinodia(toggle,pos):
        global guinodia_array

        if(not toggle or guinodia_array[pos]):
            guinodia_init()
            return
        
        guinodia_array[pos] = True
        renpy.music.play(audio.oco,"sound")
        #print(guinodia_array)

        if(is_guinodia_available()):
            drpc_update("guinodia")
            renpy.jump_out_of_context("guinodia_label")
        
    def is_guinodia_available():
        global guinodia_array
        for pos in guinodia_array:
            if(not pos):
                return False
        return True

    def check_overwrite_menu(message):
        if(message == "Tem certeza de que deseja sobrescrever seu Save?"):
            return True
        return False
    

############################################################################################################
############################################################################################################
#######Assets Forbidden Memories G

#Variaveis
define input_operation_senna = ""
define flag_input_operation_senna = False
define hash_operation_senna = "DA05114A91FFC80DE0C2E579754AF46FCFEA573041BD4C885B6A7FD44BC3E43DE825B8F6D7C20F812C2E43E3D0B1C5B6B119BC1691E3287F737F195868B9DBB0"
define guinarnia_null = [False,False,False,False,False,False]

define endings_names = {
    "A":"Melancolia do Toque de Celular Irritante",
    "B":"Sem Tempo Para Brincadeiras",
    "C":"Você É Real Mesmo?",
    "D":"Assassino G",
    "E":"Extinção Humana",
    "F":"Policial de Família",
    "G":"As Crônicas de Alexandre Senna",
    "H":"Os Carros São Como As Lanchas",
    "I":"Tele Senna",
    "J":"Recordista do Guinnass Book",
    "K":"Nunca Abra A Porta Para Estranhos",
    "L":"Hétero com G",
    "M":"Contra-Trote Mortal",
    "N":"Tratamento de Choque",
    "O":"O Acidente de Cupiqueno",
    "P":"Dois Dias Na Fila, Um Ano Na Rua",
    "Q":"Só os Skates Sabem",
    "R":"Sádico e Calculista",
    "S":"Gosto Buocólico",
    "T":"Viagem para Pau Grande",
    "U":"Teoria do Kenoverso",
    "V":"Watashi wa Arekusando desu",
    "W":"Casamento-Surpresa",
    "X":"El Gángster de Familia",
    "Y":"Árabe de Família",
    "Z":"As Aparências Enganam",
    "C1":"Capítulo 1",
    "C2":"Capítulo 2",
    "C3":"Capítulo 3",
    "C4":"Capítulo 4",
    "C5":"Capítulo 5",
    "CXX":"Capítulo XX"
}

define deck_g_names = [
    "Pote da Delícia",
    "Kawan Desu, O Mecânico",
    "Braço Direito do Proibido",
    "Jô Abdul",
    "Minha Mu;lher",
    "Braço Esquerdo do Proibido",
    "Cabação",
    "Pegasus do PAU BRILHANTE",
    "Grito Ensurdecedor de Lily Santos",
    "Perna Direita do Proibido",
    "Paulo Guina Piscineiro",
    "Paulo Guina Bombeiro",
    "Paulo Guina Professor",
    "Paulo Guina Árabe",
    "Paulo Guina Matrix",
    "Paulo Guina, O Deixador de Ocos",
    "Pica-Pau Biruta",
    "Perna Esquerda do Proibido",
    "Kid Bengala, O Grande",
    "CJ de Família",
    "Demacol (Morpheus Form)",
    "Terceira Perna do Proibido",
    "FOME.",
    "Princesa Demacol",
    "É JESUUUUIIIISSSSSSSSSS",
    "Sarcófago da Ícaro Studios",
    "Guinodia, O Proibido",
    "Monstro Que Relaxa",
    "Filhona",
    "Dragão BAIANO",
    "Coringa Dano",
    "Polimerização G",
    "Sandro Lima, O Arquiteto do Universo G",
    "Vegeta de Família",
    "Danger?! Gilson?",
    "Globglogabgalab, A Traça Melancólica",
    "Mark_77Souls, O Esquizofrêncio",
    "Taeyeon115, O Amigo de Sangue",
    "Master Exploder, O Calvo Supremo"
]

define endings_descriptions = {
    "A":"Perdeu seu jogo de futebol e o celular para ir jogar Palavras-Cruzadas.",
    "B":"Virou o melhor goleiro de Cupiqueno e foi escalado para a Seleção.",
    "C":"Questionou sua existência na Metrix e perdeu o Campeonato G.",
    "D":"Transformou Índio em um monstro e perdeu o Campeonato G.",
    "E":"Causou a destruição da Terra e perdeu o Campeonato G.",
    "F":"Foi aprovado na Polícia Militar de Cupiqueno.",
    "G":"Desvendou todo o Códex G.",
    "H":"As motos são como os Jet-Skis.",
    "I":"Visitou a Cachoeira de Pau Grande com sua nova Blazer preta.",
    "J":"Bateu o recorde mundial no Jogo da Cobrinha.",
    "K":"Teve a casa assaltada por um vigarista e perdeu tudo.",
    "L":"Confundido com um bandido e levado ao Ary Fontoura. Mas você é hétero.",
    "M":"Não mexe com quem tá quieto.",
    "N":"Foi confundido com um louco e foi internado no Sanatório de Cupiqueno.",
    "O":"Ganhou super poderes.",
    "P":"Foi processado pelo Consultório Santa Mônica e entrou em falência.",
    "Q":"Virou um skatista profissional de Cupiqueno.",
    "R":"Deixou Yeah Man agonizar até a morte.",
    "S":"Foi viver uma vida no campo.",
    "T":"Foi visitar a Praia de Pau Grande.",
    "U":"Foi procurar o arrombamento em outra dimensão do Kenoverso.",
    "V":"Aprendeu mais sobre as coisas exóticas da cultura japonesa.",
    "W":"Se casou com uma estrangeira avantajada.",
    "X":"Fugiu para Madrid e virou gangster.",
    "Y":"Aprendeu um novo idioma.",
    "Z":"¡¢£¤¥¦§¨©ª&«¬ÂÃíÄÅ+ÆÇÈâěçĜĝĞğĠġĢģôĤĥ#ĦħĨĩĪīĬĭĮÍįİıĲĳĴĵĶķÂĸĹĺĻļĽľž"
}

define arabe_wordlist = [
    "البرتقالي",
    "عصير",
    "قطعة",
    "ميكانيكي",
    "كرة القدم",
    "حمام السباحة",
    "الأسرة",
    "بابا",
    "ارتياح",
    "طبيبة",
    "بطولة",
    "قدم",
    "بهجة",
    "لذيذ",
    "السيارات",
    "للعمل",
    "شاويش",
    "امتحان",
    "ملاكمة",
    "يقتحم",
    "للراحة",
    "جوامع",
    "السجن",
    "القليل",
    "مضمون",
    "حارس مرمى",
    "الممثل",
    "اختبار",
    "عيادة",
    "شلال",
    "مدرب رياضي",
    "الأكاديمية",
    "رجل الاطفاء",
    "خرطوم",
    "موقد",
    "مشكلة",
    "غاز",
    "بنت",
    "قارب",
    "القرصان",
    "قاطع طريق",
    "الشرطي",
    "مصور فوتوغرافي",
    "جندي",
    "صديق قديم",
    "ابنة كبيرة",
    "السنوكر",
    "زواج",
    "أنا لم أفهم",
    "كذاب"
]

define config_fadein_texto = True
define narrator_what_prefix = "{fi=33-0.16-33}"
define narrator_what_suffix = "{/fi}"

define music_player_active = False
#define flag_input_operation_senna_concluido = False

###################Transform
transform select_slot_pos(x=0.5,y=0.5):
    align (x,y) alpha 1.0

transform rightin(x=640, z=0.80,time=0.25):
    xcenter 1300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein time xcenter x

transform rhide(time=0.25,position=1300):
    subpixel True
    on hide:
        easeout time xcenter position

transform lhide2(time=0.25,position=-300):
    subpixel True
    on hide:
        easeout time xcenter position

transform side_image_in:
    subpixel True
    alpha 0.0
    align (0.92, 0.9)
    size (0,218)
    linear 0.6 ypos 0.60 size (200,145) xanchor 0.70 alpha 1.0
    
transform side_image_out:
    subpixel True
    alpha 1.0
    #align (0.92, 0.9)
    linear 0.6 ypos 0.92 size (0,218) xanchor 0.70 alpha 0.0

transform credits_11():
    align (0.5,0.5) alpha 1.0

transform intro_cap:
    subpixel True
    alpha 0.0
    linear 1.5 alpha 1.0
    linear 1.5
    linear 2.5 alpha 0.0

transform top_fade:
    on show:
        align (0,0)
        alpha 0.0
        easein 0.5 alpha 1.0
    on hide:
        easeout 0.5 alpha 0

###################Personagens
define narrator = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='',what_suffix='')
define narrator_arabe = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='',what_suffix='',what_style="arabe_style")
define seto = DynamicCharacter('seto', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image seto 1a = "mod_assets/characters/seto/1a.png"
image seto 1b = "mod_assets/characters/seto/1b.png"

image senna 1a = "mod_assets/characters/senna/1a.png"

image guina 1a = "mod_assets/characters/guina/1a.png"

image yuri 3xd = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xd.png")
image yuri 3xe = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xe.png")

image gilson 1a = "mod_assets/characters/gilson/1a.png"


###################Videos
image guinodia_movie = Movie(play="mod_assets/videos/guinodia.webm",size=(960,720))
image pelada_james_02 = Movie(play="mod_assets/videos/pelada_james_02.webm",size=(960,720))
image pelada_james_03 = Movie(play="mod_assets/videos/pelada_james_03.webm",size=(960,720))
image pelada_james_04 = Movie(play="mod_assets/videos/pelada_james_04.webm",size=(960,720))
image pelada_james_05 = Movie(play="mod_assets/videos/pelada_james_05.webm",size=(960,720))
image pelada_james_06 = Movie(play="mod_assets/videos/pelada_james_06.webm",size=(960,720))
image pelada_james_07 = Movie(play="mod_assets/videos/pelada_james_07.webm",size=(960,720))
image senna_danca = Movie(play="mod_assets/videos/senna_danca.webm",size=(960,720))







###################Imagens
image testeee = "mod_assets/images/teste.png"
image logo01 = "mod_assets/images/logo01.png"
image game_over_bg = "mod_assets/images/GameOver.png"
image options_menu_bg = "mod_assets/images/OptionsMenu.png"
image textbox_black = "mod_assets/gui/textbox_black.png"
image white_bg = "mod_assets/images/white.png"




#01_02
image img_01_02_01 = "mod_assets/images/01_02/01_02_01.png"


image img_01_03_01 = "mod_assets/images/01_03/01_03_01.png"
image img_01_03_02 = "mod_assets/images/01_03/01_03_02.png"
image img_01_03_03 = "mod_assets/images/01_03/01_03_03.png"
image img_01_03_04 = "mod_assets/images/01_03/01_03_04.png"
image img_01_03_05 = "mod_assets/images/01_03/01_03_05.png"
image img_01_03_06 = "mod_assets/images/01_03/01_03_06.png"
image img_01_03_07 = "mod_assets/images/01_03/01_03_07.png"
image img_01_03_08 = "mod_assets/images/01_03/01_03_08.png"
image img_01_03_09 = "mod_assets/images/01_03/01_03_09.png"
image img_01_03_10 = "mod_assets/images/01_03/01_03_10.png"
image img_01_03_11 = "mod_assets/images/01_03/01_03_11.png"
image img_01_03_12 = "mod_assets/images/01_03/01_03_12.png"
image img_01_03_13 = "mod_assets/images/01_03/01_03_13.png"
image img_01_03_14 = "mod_assets/images/01_03/01_03_14.png"
image img_01_03_15 = "mod_assets/images/01_03/01_03_15.png"
image img_01_03_16 = "mod_assets/images/01_03/01_03_16.png"
image img_01_03_17 = "mod_assets/images/01_03/01_03_17.png"
image img_01_03_18 = "mod_assets/images/01_03/01_03_18.png"
image img_01_03_19 = "mod_assets/images/01_03/01_03_19.png"
image img_01_03_20 = "mod_assets/images/01_03/01_03_20.png"
image img_01_03_21 = "mod_assets/images/01_03/01_03_21.png"
image img_01_03_22 = "mod_assets/images/01_03/01_03_22.png"
image img_01_03_23 = "mod_assets/images/01_03/01_03_23.png"
image img_01_03_24 = "mod_assets/images/01_03/01_03_24.png"
image img_01_03_25 = "mod_assets/images/01_03/01_03_25.png"
image img_01_03_26 = "mod_assets/images/01_03/01_03_26.png"
image img_01_03_27 = "mod_assets/images/01_03/01_03_27.png"
image img_01_03_28 = "mod_assets/images/01_03/01_03_28.png"
image img_01_03_29 = "mod_assets/images/01_03/01_03_29.png"
image img_01_03_30 = "mod_assets/images/01_03/01_03_30.png"
image img_01_03_31 = "mod_assets/images/01_03/01_03_31.png"
image img_01_03_32 = "mod_assets/images/01_03/01_03_32.png"
image img_01_03_33 = "mod_assets/images/01_03/01_03_33.png"
image img_01_03_34 = "mod_assets/images/01_03/01_03_34.png"
image img_01_03_35 = "mod_assets/images/01_03/01_03_35.png"
image img_01_03_36 = "mod_assets/images/01_03/01_03_36.png"
image img_01_03_37 = "mod_assets/images/01_03/01_03_37.png"
image img_indio_cavalo = "mod_assets/images/01_03/indio_cavalo.png"


image img_01_04_01 = "mod_assets/images/01_04/01_04_01.png"
image img_01_04_02 = "mod_assets/images/01_04/01_04_02.png"
image img_01_04_03 = "mod_assets/images/01_04/01_04_03.png"
image img_01_04_04 = "mod_assets/images/01_04/01_04_04.png"
image img_01_04_05 = "mod_assets/images/01_04/01_04_05.png"
image img_01_04_06 = "mod_assets/images/01_04/01_04_06.png"
image img_01_04_07 = "mod_assets/images/01_04/01_04_07.png"
image img_01_04_08 = "mod_assets/images/01_04/01_04_08.png"
image img_01_04_09 = "mod_assets/images/01_04/01_04_09.png"
image img_01_04_10 = "mod_assets/images/01_04/01_04_10.png"
image img_01_04_11 = "mod_assets/images/01_04/01_04_11.png"
image img_01_04_12 = "mod_assets/images/01_04/01_04_12.png"
image img_01_04_13 = "mod_assets/images/01_04/01_04_13.png"
image img_01_04_14 = "mod_assets/images/01_04/01_04_14.png"
image img_01_04_15 = "mod_assets/images/01_04/01_04_15.png"
image img_01_04_16 = "mod_assets/images/01_04/01_04_16.png"
image img_01_04_17 = "mod_assets/images/01_04/01_04_17.png"
image img_01_04_18 = "mod_assets/images/01_04/01_04_18.png"
image img_01_04_19 = "mod_assets/images/01_04/01_04_19.png"
image img_01_04_20 = "mod_assets/images/01_04/01_04_20.png"
image img_01_04_21 = "mod_assets/images/01_04/01_04_21.png"
image img_01_04_22 = "mod_assets/images/01_04/01_04_22.png"
image img_01_04_23 = "mod_assets/images/01_04/01_04_23.png"
image img_01_04_24 = "mod_assets/images/01_04/01_04_24.png"
image img_01_04_25 = "mod_assets/images/01_04/01_04_25.png"
image img_01_04_26 = "mod_assets/images/01_04/01_04_26.png"
image img_01_04_27 = "mod_assets/images/01_04/01_04_27.png"
image img_01_04_28 = "mod_assets/images/01_04/01_04_28.png"
image img_01_04_29 = "mod_assets/images/01_04/01_04_29.png"
image img_01_04_30 = "mod_assets/images/01_04/01_04_30.png"
image img_01_04_31 = "mod_assets/images/01_04/01_04_31.png"
image img_01_04_32 = "mod_assets/images/01_04/01_04_32.png"
image img_01_04_33 = "mod_assets/images/01_04/01_04_33.png"
image img_01_04_34 = "mod_assets/images/01_04/01_04_34.png"
image img_01_04_35 = "mod_assets/images/01_04/01_04_35.png"
image img_01_04_36 = "mod_assets/images/01_04/01_04_36.png"
image img_01_04_37 = "mod_assets/images/01_04/01_04_37.png"
image img_01_04_38 = "mod_assets/images/01_04/01_04_38.png"
image img_01_04_39 = "mod_assets/images/01_04/01_04_39.png"
image img_01_04_40 = "mod_assets/images/01_04/01_04_40.png"
image img_01_04_41 = "mod_assets/images/01_04/01_04_41.png"
image img_01_04_42 = "mod_assets/images/01_04/01_04_42.png"
image img_01_04_43 = "mod_assets/images/01_04/01_04_43.png"
image img_01_04_44 = "mod_assets/images/01_04/01_04_44.png"
image img_01_04_45 = "mod_assets/images/01_04/01_04_45.png"
image img_01_04_46 = "mod_assets/images/01_04/01_04_46.png"
image img_01_04_47 = "mod_assets/images/01_04/01_04_47.png"
image img_01_04_48 = "mod_assets/images/01_04/01_04_48.png"
image img_01_04_49 = "mod_assets/images/01_04/01_04_49.png"
image img_01_04_50 = "mod_assets/images/01_04/01_04_50.png"
image img_01_04_51 = "mod_assets/images/01_04/01_04_51.png"
image img_01_04_52 = "mod_assets/images/01_04/01_04_52.png"
image img_01_04_53 = "mod_assets/images/01_04/01_04_53.png"
image img_01_04_54 = "mod_assets/images/01_04/01_04_54.png"
image img_01_04_55 = "mod_assets/images/01_04/01_04_55.png"
image img_01_04_56 = "mod_assets/images/01_04/01_04_56.png"
image img_01_04_57 = "mod_assets/images/01_04/01_04_57.png"
image img_01_04_58 = "mod_assets/images/01_04/01_04_58.png"
image img_01_04_59 = "mod_assets/images/01_04/01_04_59.png"
image img_01_04_60 = "mod_assets/images/01_04/01_04_60.png"
image img_01_04_61 = "mod_assets/images/01_04/01_04_61.png"
image img_01_04_62 = "mod_assets/images/01_04/01_04_62.png"
image img_01_04_63 = "mod_assets/images/01_04/01_04_63.png"


#02_01
image img_02_01_01 = "mod_assets/images/02_01/02_01_01.png"


#02_02
image img_02_02_01 = "mod_assets/images/02_02/02_02_01.png"
image img_02_02_02 = "mod_assets/images/02_02/02_02_02.png"
image img_02_02_03 = "mod_assets/images/02_02/02_02_03.png"
image img_02_02_04 = "mod_assets/images/02_02/02_02_04.png"
image img_02_02_05 = "mod_assets/images/02_02/02_02_05.png"
image img_02_02_06 = "mod_assets/images/02_02/02_02_06.png"
image img_02_02_07 = "mod_assets/images/02_02/02_02_07.png"
image img_02_02_08 = "mod_assets/images/02_02/02_02_08.png"
image img_02_02_09 = "mod_assets/images/02_02/02_02_09.png"
image img_02_02_10 = "mod_assets/images/02_02/02_02_10.png"
image img_02_02_11 = "mod_assets/images/02_02/02_02_11.png"
image img_02_02_12 = "mod_assets/images/02_02/02_02_12.png"
image img_02_02_13 = "mod_assets/images/02_02/02_02_13.png"
image img_02_02_14 = "mod_assets/images/02_02/02_02_14.png"
image img_02_02_15 = "mod_assets/images/02_02/02_02_15.png"
image img_02_02_16 = "mod_assets/images/02_02/02_02_16.png"
image img_02_02_17 = "mod_assets/images/02_02/02_02_17.png"
image img_02_02_18 = "mod_assets/images/02_02/02_02_18.png"
image img_02_02_19 = "mod_assets/images/02_02/02_02_19.png"
image img_02_02_20 = "mod_assets/images/02_02/02_02_20.png"
image img_02_02_21 = "mod_assets/images/02_02/02_02_21.png"
image img_02_02_22 = "mod_assets/images/02_02/02_02_22.png"
image img_02_02_23 = "mod_assets/images/02_02/02_02_23.png"
image img_02_02_24 = "mod_assets/images/02_02/02_02_24.png"
image img_02_02_25 = "mod_assets/images/02_02/02_02_25.png"
image img_02_02_26 = "mod_assets/images/02_02/02_02_26.png"
image img_02_02_27 = "mod_assets/images/02_02/02_02_27.png"
image img_02_02_28 = "mod_assets/images/02_02/02_02_28.png"
image img_02_02_29 = "mod_assets/images/02_02/02_02_29.png"
image img_02_02_30 = "mod_assets/images/02_02/02_02_30.png"
image img_02_02_31 = "mod_assets/images/02_02/02_02_31.png"
image img_02_02_32 = "mod_assets/images/02_02/02_02_32.png"
image img_02_02_33 = "mod_assets/images/02_02/02_02_33.png"
image img_02_02_34 = "mod_assets/images/02_02/02_02_34.png"
image img_02_02_35 = "mod_assets/images/02_02/02_02_35.png"
image img_02_02_36 = "mod_assets/images/02_02/02_02_36.png"
image img_02_02_37 = "mod_assets/images/02_02/02_02_37.png"
image img_02_02_38 = "mod_assets/images/02_02/02_02_38.png"
image img_02_02_39 = "mod_assets/images/02_02/02_02_39.png"
image img_02_02_40 = "mod_assets/images/02_02/02_02_40.png"
image img_02_02_41 = "mod_assets/images/02_02/02_02_41.png"
image img_02_02_42 = "mod_assets/images/02_02/02_02_42.png"
image img_02_02_43 = "mod_assets/images/02_02/02_02_43.png"
image img_senna_foca = "mod_assets/images/02_02/senna_foca.png" 
image img_senna_paraquedas = "mod_assets/images/02_02/senna_paraquedas.png"

#02_03
image img_02_03_01 = "mod_assets/images/02_03/02_03_01.png"


#02_04
image img_02_04_01 = "mod_assets/images/02_04/02_04_01.png"
image img_02_04_02 = "mod_assets/images/02_04/02_04_02.png"
image img_02_04_03 = "mod_assets/images/02_04/02_04_03.png"
image img_02_04_04 = "mod_assets/images/02_04/02_04_04.png"
image img_02_04_05 = "mod_assets/images/02_04/02_04_05.png"
image img_02_04_06 = "mod_assets/images/02_04/02_04_06.png"
image img_02_04_07 = "mod_assets/images/02_04/02_04_07.png"
image img_02_04_08 = "mod_assets/images/02_04/02_04_08.png"
image img_02_04_09 = "mod_assets/images/02_04/02_04_09.png"
image img_02_04_10 = "mod_assets/images/02_04/02_04_10.png"
image img_02_04_11 = "mod_assets/images/02_04/02_04_11.png"
image img_02_04_12 = "mod_assets/images/02_04/02_04_12.png"
image img_02_04_13 = "mod_assets/images/02_04/02_04_13.png"
image img_02_04_14 = "mod_assets/images/02_04/02_04_14.png"
image img_02_04_15 = "mod_assets/images/02_04/02_04_15.png"
image img_02_04_16 = "mod_assets/images/02_04/02_04_16.png"
image img_02_04_17 = "mod_assets/images/02_04/02_04_17.png"
image img_02_04_18 = "mod_assets/images/02_04/02_04_18.png"
image img_02_04_19 = "mod_assets/images/02_04/02_04_19.png"
image img_02_04_20 = "mod_assets/images/02_04/02_04_20.png"
image img_02_04_21 = "mod_assets/images/02_04/02_04_21.png"
image img_02_04_22 = "mod_assets/images/02_04/02_04_22.png"
image img_02_04_23 = "mod_assets/images/02_04/02_04_23.png"
image img_02_04_24 = "mod_assets/images/02_04/02_04_24.png"
image img_02_04_25 = "mod_assets/images/02_04/02_04_25.png"
image img_02_04_26 = "mod_assets/images/02_04/02_04_26.png"
image img_02_04_27 = "mod_assets/images/02_04/02_04_27.png"
image img_02_04_28 = "mod_assets/images/02_04/02_04_28.png"
image img_02_04_29 = "mod_assets/images/02_04/02_04_29.png"
image img_02_04_30 = "mod_assets/images/02_04/02_04_30.png"
image img_02_04_31 = "mod_assets/images/02_04/02_04_31.png"
image img_02_04_32 = "mod_assets/images/02_04/02_04_32.png"
image img_02_04_33 = "mod_assets/images/02_04/02_04_33.png"
image img_02_04_34 = "mod_assets/images/02_04/02_04_34.png"
image img_02_04_35 = "mod_assets/images/02_04/02_04_35.png"
image img_02_04_36 = "mod_assets/images/02_04/02_04_36.png"
image img_02_04_37 = "mod_assets/images/02_04/02_04_37.png"
image img_02_04_38 = "mod_assets/images/02_04/02_04_38.png"
image imgs_senna_egito:
    block:
        "mod_assets/images/02_04/senna_egito01.png"
        0.3
        "mod_assets/images/02_04/senna_egito02.png"
        0.3
        "mod_assets/images/02_04/senna_egito03.png"
        0.3
        "mod_assets/images/02_04/senna_egito04.png"
        0.3
        "mod_assets/images/02_04/senna_egito05.png"
        0.3
        "mod_assets/images/02_04/senna_egito06.png"
        0.3
        "mod_assets/images/02_04/senna_egito07.png"
        0.3
        "mod_assets/images/02_04/senna_egito08.png"
        0.3
        "mod_assets/images/02_04/senna_egito09.png"
        0.3
        "mod_assets/images/02_04/senna_egito10.png"
        0.3
        "mod_assets/images/02_04/senna_egito11.png"
        0.3
        "mod_assets/images/02_04/senna_egito12.png"
        0.3
        "mod_assets/images/02_04/senna_egito13.png"
        0.3
        "mod_assets/images/02_04/senna_egito14.png"
        0.3
        "mod_assets/images/02_04/senna_egito15.png"
        0.3
        "mod_assets/images/02_04/senna_egito16.png"
        0.3
        "mod_assets/images/02_04/senna_egito17.png"
        0.3
        "mod_assets/images/02_04/senna_egito18.png"
        0.3
        "mod_assets/images/02_04/senna_egito19.png"
        0.3
        "mod_assets/images/02_04/senna_egito20.png"
        0.3
    block:
        choice:
            "mod_assets/images/02_04/senna_egito01.png"
        choice:
            "mod_assets/images/02_04/senna_egito02.png"
        choice:
            "mod_assets/images/02_04/senna_egito03.png"
        choice:
            "mod_assets/images/02_04/senna_egito04.png"
        choice:
            "mod_assets/images/02_04/senna_egito05.png"
        choice:
            "mod_assets/images/02_04/senna_egito06.png"
        choice:
            "mod_assets/images/02_04/senna_egito07.png"
        choice:
            "mod_assets/images/02_04/senna_egito08.png"
        choice:
            "mod_assets/images/02_04/senna_egito09.png"
        choice:
            "mod_assets/images/02_04/senna_egito10.png"
        choice:
            "mod_assets/images/02_04/senna_egito11.png"
        choice:
            "mod_assets/images/02_04/senna_egito12.png"
        choice:
            "mod_assets/images/02_04/senna_egito13.png"
        choice:
            "mod_assets/images/02_04/senna_egito14.png"
        choice:
            "mod_assets/images/02_04/senna_egito15.png"
        choice:
            "mod_assets/images/02_04/senna_egito16.png"
        choice:
            "mod_assets/images/02_04/senna_egito17.png"
        choice:
            "mod_assets/images/02_04/senna_egito18.png"
        choice:
            "mod_assets/images/02_04/senna_egito19.png"
        choice:
            "mod_assets/images/02_04/senna_egito20.png"
        0.3
        repeat


#03_01
image img_03_01_01 = "mod_assets/images/03_01/03_01_01.png"


#03_02
image img_03_02_01 = "mod_assets/images/03_02/03_02_01.png"
image img_03_02_02 = "mod_assets/images/03_02/03_02_02.png"
image img_03_02_03 = "mod_assets/images/03_02/03_02_03.png"
image img_03_02_04 = "mod_assets/images/03_02/03_02_04.png"
image img_03_02_05 = "mod_assets/images/03_02/03_02_05.png"
image img_03_02_06 = "mod_assets/images/03_02/03_02_06.png"
image img_03_02_07 = "mod_assets/images/03_02/03_02_07.png"
image img_03_02_08 = "mod_assets/images/03_02/03_02_08.png"
image img_03_02_09 = "mod_assets/images/03_02/03_02_09.png"
image img_03_02_10 = "mod_assets/images/03_02/03_02_10.png"
image img_03_02_11 = "mod_assets/images/03_02/03_02_11.png"
image img_03_02_12 = "mod_assets/images/03_02/03_02_12.png"
image img_03_02_13 = "mod_assets/images/03_02/03_02_13.png"
image img_03_02_14 = "mod_assets/images/03_02/03_02_14.png"
image img_03_02_15 = "mod_assets/images/03_02/03_02_15.png"
image img_03_02_16 = "mod_assets/images/03_02/03_02_16.png"
image img_03_02_17 = "mod_assets/images/03_02/03_02_17.png"
image img_03_02_18 = "mod_assets/images/03_02/03_02_18.png"
image img_03_02_19 = "mod_assets/images/03_02/03_02_19.png"
image img_03_02_20 = "mod_assets/images/03_02/03_02_20.png"
image img_03_02_21 = "mod_assets/images/03_02/03_02_21.png"
image img_03_02_22 = "mod_assets/images/03_02/03_02_22.png"
image img_03_02_23 = "mod_assets/images/03_02/03_02_23.png"
image img_03_02_24 = "mod_assets/images/03_02/03_02_24.png"
image img_03_02_25 = "mod_assets/images/03_02/03_02_25.png"
image img_03_02_26 = "mod_assets/images/03_02/03_02_26.png"
image img_03_02_27 = "mod_assets/images/03_02/03_02_27.png"
image img_03_02_28 = "mod_assets/images/03_02/03_02_28.png"
image img_03_02_29 = "mod_assets/images/03_02/03_02_29.png"
image img_senna_estatua = "mod_assets/images/03_02/senna_estatua.png"


#03_03
image img_03_03_01 = "mod_assets/images/03_03/03_03_01.png"
image img_03_03_02 = "mod_assets/images/03_03/03_03_02.png"
image img_03_03_03 = "mod_assets/images/03_03/03_03_03.png"
image img_03_03_04 = "mod_assets/images/03_03/03_03_04.png"
image img_03_03_05 = "mod_assets/images/03_03/03_03_05.png"
image img_03_03_06 = "mod_assets/images/03_03/03_03_06.png"
image img_03_03_07 = "mod_assets/images/03_03/03_03_07.png"
image img_03_03_08 = "mod_assets/images/03_03/03_03_08.png"
image img_03_03_09 = "mod_assets/images/03_03/03_03_09.png"
image img_03_03_10 = "mod_assets/images/03_03/03_03_10.png"
image img_03_03_11 = "mod_assets/images/03_03/03_03_11.png"
image img_03_03_12 = "mod_assets/images/03_03/03_03_12.png"
image img_03_03_13 = "mod_assets/images/03_03/03_03_13.png"
image img_03_03_14 = "mod_assets/images/03_03/03_03_14.png"
image img_03_03_15 = "mod_assets/images/03_03/03_03_15.png"
image img_03_03_16 = "mod_assets/images/03_03/03_03_16.png"
image img_03_03_17 = "mod_assets/images/03_03/03_03_17.png"
image img_03_03_18 = "mod_assets/images/03_03/03_03_18.png"
image img_03_03_19 = "mod_assets/images/03_03/03_03_19.png"
image img_03_03_20 = "mod_assets/images/03_03/03_03_20.png"
image img_03_03_21 = "mod_assets/images/03_03/03_03_21.png"
image img_03_03_22 = "mod_assets/images/03_03/03_03_22.png"
image img_03_03_23 = "mod_assets/images/03_03/03_03_23.png"
image img_03_03_24 = "mod_assets/images/03_03/03_03_24.png"
image img_03_03_25 = "mod_assets/images/03_03/03_03_25.png"
image img_03_03_26 = "mod_assets/images/03_03/03_03_26.png"
image img_03_03_27 = "mod_assets/images/03_03/03_03_27.png"
image img_03_03_28 = "mod_assets/images/03_03/03_03_28.png"
image img_03_03_29 = "mod_assets/images/03_03/03_03_29.png"
image img_03_03_30 = "mod_assets/images/03_03/03_03_30.png"
image img_03_03_31 = "mod_assets/images/03_03/03_03_31.png"
image img_03_03_32 = "mod_assets/images/03_03/03_03_32.png"
image img_03_03_33 = "mod_assets/images/03_03/03_03_33.png"
image img_03_03_34 = "mod_assets/images/03_03/03_03_34.png"
image img_senna_doutora_01 = "mod_assets/images/03_03/senna_doutora_01.png"
image img_senna_doutora_02 = "mod_assets/images/03_03/senna_doutora_02.png"
image img_senna_doutora_03 = "mod_assets/images/03_03/senna_doutora_03.png"
image img_senna_doutora_04 = "mod_assets/images/03_03/senna_doutora_04.png"


#04_01
image img_04_01_01 = "mod_assets/images/04_01/04_01_01.png"
image img_04_01_02 = "mod_assets/images/04_01/04_01_02.png"
image img_04_01_03 = "mod_assets/images/04_01/04_01_03.png"
image img_04_01_04 = "mod_assets/images/04_01/04_01_04.png"
image img_04_01_05 = "mod_assets/images/04_01/04_01_05.png"
image img_04_01_06 = "mod_assets/images/04_01/04_01_06.png"
image img_04_01_07 = "mod_assets/images/04_01/04_01_07.png"
image img_04_01_08 = "mod_assets/images/04_01/04_01_08.png"
image img_04_01_09 = "mod_assets/images/04_01/04_01_09.png"


#04_02
image img_04_02_01 = "mod_assets/images/04_02/04_02_01.png"
image img_04_02_02 = "mod_assets/images/04_02/04_02_02.png"
image img_04_02_03 = "mod_assets/images/04_02/04_02_03.png"
image img_04_02_04 = "mod_assets/images/04_02/04_02_04.png"
image img_04_02_05 = "mod_assets/images/04_02/04_02_05.png"
image img_04_02_06 = "mod_assets/images/04_02/04_02_06.png"
image img_04_02_07 = "mod_assets/images/04_02/04_02_07.png"
image img_04_02_08 = "mod_assets/images/04_02/04_02_08.png"
image img_04_02_09 = "mod_assets/images/04_02/04_02_09.png"
image img_04_02_10 = "mod_assets/images/04_02/04_02_10.png"
image img_04_02_11 = "mod_assets/images/04_02/04_02_11.png"
image img_04_02_12 = "mod_assets/images/04_02/04_02_12.png"
image img_04_02_13 = "mod_assets/images/04_02/04_02_13.png"
image img_04_02_14 = "mod_assets/images/04_02/04_02_14.png"
image img_04_02_15 = "mod_assets/images/04_02/04_02_15.png"
image img_04_02_16 = "mod_assets/images/04_02/04_02_16.png"
image img_04_02_17 = "mod_assets/images/04_02/04_02_17.png"
image img_04_02_18 = "mod_assets/images/04_02/04_02_18.png"
image img_04_02_19 = "mod_assets/images/04_02/04_02_19.png"

image img_yeah_man_foca:
    "mod_assets/images/04_02/yeah_man_foca.png"
    linear 23.9 zoom 2.8 xoffset -500 yoffset -200



#04_03
image img_04_03_01 = "mod_assets/images/04_03/04_03_01.png"


#04_04
image img_04_04_01 = "mod_assets/images/04_04/04_04_01.png"
image img_04_04_02 = "mod_assets/images/04_04/04_04_02.png"
image img_04_04_03 = "mod_assets/images/04_04/04_04_03.png"
image img_04_04_04 = "mod_assets/images/04_04/04_04_04.png"
image img_04_04_05 = "mod_assets/images/04_04/04_04_05.png"
image img_04_04_06 = "mod_assets/images/04_04/04_04_06.png"
image img_04_04_07 = "mod_assets/images/04_04/04_04_07.png"
image img_04_04_08 = "mod_assets/images/04_04/04_04_08.png"
image img_04_04_09 = "mod_assets/images/04_04/04_04_09.png"
image img_04_04_10 = "mod_assets/images/04_04/04_04_10.png"
image img_04_04_11 = "mod_assets/images/04_04/04_04_11.png"
image img_04_04_12 = "mod_assets/images/04_04/04_04_12.png"
image img_04_04_13 = "mod_assets/images/04_04/04_04_13.png"
image img_04_04_14 = "mod_assets/images/04_04/04_04_14.png"
image img_04_04_15 = "mod_assets/images/04_04/04_04_15.png"
image img_04_04_16 = "mod_assets/images/04_04/04_04_16.png"
image img_04_04_17 = "mod_assets/images/04_04/04_04_17.png"
image img_04_04_18 = "mod_assets/images/04_04/04_04_18.png"
image img_04_04_19 = "mod_assets/images/04_04/04_04_19.png"
image img_04_04_20 = "mod_assets/images/04_04/04_04_20.png"
image img_04_04_21 = "mod_assets/images/04_04/04_04_21.png"
image img_04_04_22 = "mod_assets/images/04_04/04_04_22.png"
image img_04_04_23 = "mod_assets/images/04_04/04_04_23.png"
image img_04_04_24 = "mod_assets/images/04_04/04_04_24.png"
image img_04_04_25 = "mod_assets/images/04_04/04_04_25.png"
image img_04_04_26 = "mod_assets/images/04_04/04_04_26.png"
image img_04_04_27 = "mod_assets/images/04_04/04_04_27.png"
image img_04_04_28 = "mod_assets/images/04_04/04_04_28.png"
image img_04_04_29 = "mod_assets/images/04_04/04_04_29.png"
image img_04_04_30 = "mod_assets/images/04_04/04_04_30.png"
image img_04_04_31 = "mod_assets/images/04_04/04_04_31.png"
image img_04_04_32 = "mod_assets/images/04_04/04_04_32.png"
image img_04_04_33 = "mod_assets/images/04_04/04_04_33.png"
image img_04_04_34 = "mod_assets/images/04_04/04_04_34.png"
image img_senna_cavalo = "mod_assets/images/04_04/senna_cavalo.png"

#05_01
image img_05_01_01 = "mod_assets/images/05_01/05_01_01.png"


#05_02
image img_05_02_01 = "mod_assets/images/05_02/05_02_01.png"
image img_05_02_02 = "mod_assets/images/05_02/05_02_02.png"
image img_05_02_03 = "mod_assets/images/05_02/05_02_03.png"
image img_05_02_04 = "mod_assets/images/05_02/05_02_04.png"
image img_05_02_05 = "mod_assets/images/05_02/05_02_05.png"
image img_05_02_06 = "mod_assets/images/05_02/05_02_06.png"
image img_05_02_07 = "mod_assets/images/05_02/05_02_07.png"
image img_05_02_08 = "mod_assets/images/05_02/05_02_08.png"
image img_05_02_09 = "mod_assets/images/05_02/05_02_09.png"
image img_05_02_10 = "mod_assets/images/05_02/05_02_10.png"
image img_05_02_11 = "mod_assets/images/05_02/05_02_11.png"
image img_05_02_12 = "mod_assets/images/05_02/05_02_12.png"
image img_05_02_13 = "mod_assets/images/05_02/05_02_13.png"
image img_05_02_14 = "mod_assets/images/05_02/05_02_14.png"
image img_05_02_15 = "mod_assets/images/05_02/05_02_15.png"
image img_05_02_16 = "mod_assets/images/05_02/05_02_16.png"
image img_05_02_17 = "mod_assets/images/05_02/05_02_17.png"
image img_05_02_18 = "mod_assets/images/05_02/05_02_18.png"
image img_05_02_19 = "mod_assets/images/05_02/05_02_19.png"
image img_05_02_20 = "mod_assets/images/05_02/05_02_20.png"
image img_05_02_21 = "mod_assets/images/05_02/05_02_21.png"
image img_05_02_22 = "mod_assets/images/05_02/05_02_22.png"
image img_05_02_23 = "mod_assets/images/05_02/05_02_23.png"
image img_05_02_24 = "mod_assets/images/05_02/05_02_24.png"
image img_05_02_25 = "mod_assets/images/05_02/05_02_25.png"
image img_05_02_26 = "mod_assets/images/05_02/05_02_26.png"
image img_05_02_27 = "mod_assets/images/05_02/05_02_27.png"
image img_05_02_28 = "mod_assets/images/05_02/05_02_28.png"
image img_05_02_29 = "mod_assets/images/05_02/05_02_29.png"
image img_05_02_30 = "mod_assets/images/05_02/05_02_30.png"
image img_05_02_31 = "mod_assets/images/05_02/05_02_31.png"
image img_05_02_32 = "mod_assets/images/05_02/05_02_32.png"
image img_05_02_33 = "mod_assets/images/05_02/05_02_33.png"
image img_05_02_34 = "mod_assets/images/05_02/05_02_34.png"
image img_05_02_35 = "mod_assets/images/05_02/05_02_35.png"
image img_05_02_36 = "mod_assets/images/05_02/05_02_36.png"
image img_05_02_37 = "mod_assets/images/05_02/05_02_37.png"
image img_05_02_38 = "mod_assets/images/05_02/05_02_38.png"
image img_05_02_39 = "mod_assets/images/05_02/05_02_39.png"
image img_05_02_40 = "mod_assets/images/05_02/05_02_40.png"
image img_05_02_41 = "mod_assets/images/05_02/05_02_41.png"
image img_05_02_42 = "mod_assets/images/05_02/05_02_42.png"
image img_05_02_43 = "mod_assets/images/05_02/05_02_43.png"
image img_05_02_44 = "mod_assets/images/05_02/05_02_44.png"
image img_05_02_45 = "mod_assets/images/05_02/05_02_45.png"
image img_05_02_46 = "mod_assets/images/05_02/05_02_46.png"
image img_05_02_47 = "mod_assets/images/05_02/05_02_47.png"
image img_05_02_48 = "mod_assets/images/05_02/05_02_48.png"
image img_05_02_49 = "mod_assets/images/05_02/05_02_49.png"
image img_05_02_50 = "mod_assets/images/05_02/05_02_50.png"
image img_05_02_51 = "mod_assets/images/05_02/05_02_51.png"
image img_05_02_52 = "mod_assets/images/05_02/05_02_52.png"
image img_05_02_53 = "mod_assets/images/05_02/05_02_53.png"
image img_05_02_54 = "mod_assets/images/05_02/05_02_54.png"
image img_05_02_55 = "mod_assets/images/05_02/05_02_55.png"
image img_05_02_56 = "mod_assets/images/05_02/05_02_56.png"
image img_05_02_57 = "mod_assets/images/05_02/05_02_57.png"
image img_05_02_58 = "mod_assets/images/05_02/05_02_58.png"
image img_05_02_59 = "mod_assets/images/05_02/05_02_59.png"
image img_05_02_60 = "mod_assets/images/05_02/05_02_60.png"
image img_05_02_61 = "mod_assets/images/05_02/05_02_61.png"
image img_05_02_62 = "mod_assets/images/05_02/05_02_62.png"
image img_05_02_63 = "mod_assets/images/05_02/05_02_63.png"
image img_05_02_64 = "mod_assets/images/05_02/05_02_64.png"
image img_05_02_65 = "mod_assets/images/05_02/05_02_65.png"
image img_05_02_66 = "mod_assets/images/05_02/05_02_66.png"
image img_05_02_67 = "mod_assets/images/05_02/05_02_67.png"
image img_05_02_68 = "mod_assets/images/05_02/05_02_68.png"
image img_05_02_69 = "mod_assets/images/05_02/05_02_69.png"
image img_05_02_70 = "mod_assets/images/05_02/05_02_70.png"
image img_05_02_71 = "mod_assets/images/05_02/05_02_71.png"
image img_05_02_72 = "mod_assets/images/05_02/05_02_72.png"
image img_05_02_73 = "mod_assets/images/05_02/05_02_73.png"
image img_05_02_74 = "mod_assets/images/05_02/05_02_74.png"
image img_05_02_75 = "mod_assets/images/05_02/05_02_75.png"
image img_05_02_76 = "mod_assets/images/05_02/05_02_76.png"
image img_05_02_77 = "mod_assets/images/05_02/05_02_77.png"
image img_05_02_78 = "mod_assets/images/05_02/05_02_78.png"
image img_05_02_79 = "mod_assets/images/05_02/05_02_79.png"
image img_05_02_80 = "mod_assets/images/05_02/05_02_80.png"
image img_05_02_81 = "mod_assets/images/05_02/05_02_81.png"
image img_05_02_82 = "mod_assets/images/05_02/05_02_82.png"
image img_05_02_83 = "mod_assets/images/05_02/05_02_83.png"
image img_05_02_84 = "mod_assets/images/05_02/05_02_84.png"
image img_05_02_85 = "mod_assets/images/05_02/05_02_85.png"
image img_05_02_86 = "mod_assets/images/05_02/05_02_86.png"
image img_05_02_87 = "mod_assets/images/05_02/05_02_87.png"
image img_05_02_88 = "mod_assets/images/05_02/05_02_88.png"
image img_05_02_89 = "mod_assets/images/05_02/05_02_89.png"
image img_05_02_90 = "mod_assets/images/05_02/05_02_90.png"
image img_05_02_91 = "mod_assets/images/05_02/05_02_91.png"
image img_05_02_92 = "mod_assets/images/05_02/05_02_92.png"
image img_05_02_93 = "mod_assets/images/05_02/05_02_93.png"
image img_05_02_94 = "mod_assets/images/05_02/05_02_94.png"
image img_05_02_95 = "mod_assets/images/05_02/05_02_95.png"
image img_05_02_96 = "mod_assets/images/05_02/05_02_96.png"
image img_05_02_97 = "mod_assets/images/05_02/05_02_97.png"
image img_05_02_98 = "mod_assets/images/05_02/05_02_98.png"
image img_05_02_99 = "mod_assets/images/05_02/05_02_99.png"
image img_05_02_100 = "mod_assets/images/05_02/05_02_100.png"
image img_05_02_101 = "mod_assets/images/05_02/05_02_101.png"
image img_05_02_102 = "mod_assets/images/05_02/05_02_102.png"
image img_05_02_103 = "mod_assets/images/05_02/05_02_103.png"
image img_05_02_104 = "mod_assets/images/05_02/05_02_104.png"
image img_05_02_105 = "mod_assets/images/05_02/05_02_105.png"
image img_05_02_106 = "mod_assets/images/05_02/05_02_106.png"
image img_05_02_107 = "mod_assets/images/05_02/05_02_107.png"
image img_05_02_108 = "mod_assets/images/05_02/05_02_108.png"
image img_05_02_109 = "mod_assets/images/05_02/05_02_109.png"
image img_05_02_110 = "mod_assets/images/05_02/05_02_110.png"
image img_05_02_111 = "mod_assets/images/05_02/05_02_111.png"
image img_05_02_112 = "mod_assets/images/05_02/05_02_112.png"
image img_05_02_113 = "mod_assets/images/05_02/05_02_113.png"
image img_05_02_114 = "mod_assets/images/05_02/05_02_114.png"
image img_05_02_115 = "mod_assets/images/05_02/05_02_115.png"
image img_05_02_116 = "mod_assets/images/05_02/05_02_116.png"
image img_05_02_117 = "mod_assets/images/05_02/05_02_117.png"
image img_05_02_118 = "mod_assets/images/05_02/05_02_118.png"
image img_05_02_119 = "mod_assets/images/05_02/05_02_119.png"
image img_05_02_120 = "mod_assets/images/05_02/05_02_120.png"
image img_05_02_121 = "mod_assets/images/05_02/05_02_121.png"
image img_05_02_122 = "mod_assets/images/05_02/05_02_122.png"
image img_05_02_123 = "mod_assets/images/05_02/05_02_123.png"
image img_05_02_124 = "mod_assets/images/05_02/05_02_124.png"
image img_05_02_125 = "mod_assets/images/05_02/05_02_125.png"
image img_05_02_126 = "mod_assets/images/05_02/05_02_126.png"
image img_05_02_127 = "mod_assets/images/05_02/05_02_127.png"
image img_05_02_128 = "mod_assets/images/05_02/05_02_128.png"
image img_05_02_129 = "mod_assets/images/05_02/05_02_129.png"
image img_05_02_130 = "mod_assets/images/05_02/05_02_130.png"
image img_05_02_131 = "mod_assets/images/05_02/05_02_131.png"
image img_05_02_132 = "mod_assets/images/05_02/05_02_132.png"
image img_05_02_133 = "mod_assets/images/05_02/05_02_133.png"
image img_05_02_134 = "mod_assets/images/05_02/05_02_134.png"
image img_05_02_135 = "mod_assets/images/05_02/05_02_135.png"
image img_05_02_136 = "mod_assets/images/05_02/05_02_136.png"
image img_05_02_137 = "mod_assets/images/05_02/05_02_137.png"
image img_05_02_138 = "mod_assets/images/05_02/05_02_138.png"
image img_05_02_139 = "mod_assets/images/05_02/05_02_139.png"
image img_05_02_140 = "mod_assets/images/05_02/05_02_140.png"
image img_05_02_141 = "mod_assets/images/05_02/05_02_141.png"
image img_05_02_142 = "mod_assets/images/05_02/05_02_142.png"
image img_05_02_143 = "mod_assets/images/05_02/05_02_143.png"
image img_05_02_144 = "mod_assets/images/05_02/05_02_144.png"
image img_05_02_145 = "mod_assets/images/05_02/05_02_145.png"
image img_05_02_146 = "mod_assets/images/05_02/05_02_146.png"
image img_05_02_147 = "mod_assets/images/05_02/05_02_147.png"
image img_05_02_148 = "mod_assets/images/05_02/05_02_148.png"
image img_05_02_149 = "mod_assets/images/05_02/05_02_149.png"
image img_05_02_150 = "mod_assets/images/05_02/05_02_150.png"
image img_05_02_151 = "mod_assets/images/05_02/05_02_151.png"
image img_05_02_152 = "mod_assets/images/05_02/05_02_152.png"
image img_05_02_153 = "mod_assets/images/05_02/05_02_153.png"
image img_05_02_154 = "mod_assets/images/05_02/05_02_154.png"
image img_05_02_155 = "mod_assets/images/05_02/05_02_155.png"
image img_05_02_156 = "mod_assets/images/05_02/05_02_156.png"
image img_05_02_157 = "mod_assets/images/05_02/05_02_157.png"
image img_05_02_158 = "mod_assets/images/05_02/05_02_158.png"
image img_05_02_159 = "mod_assets/images/05_02/05_02_159.png"
image img_05_02_160 = "mod_assets/images/05_02/05_02_160.png"
image img_05_02_161 = "mod_assets/images/05_02/05_02_161.png"
image img_05_02_162 = "mod_assets/images/05_02/05_02_162.png"
image img_05_02_163 = "mod_assets/images/05_02/05_02_163.png"
image img_05_02_164 = "mod_assets/images/05_02/05_02_164.png"
image img_05_02_165 = "mod_assets/images/05_02/05_02_165.png"
image img_05_02_166 = "mod_assets/images/05_02/05_02_166.png"
image img_05_02_167 = "mod_assets/images/05_02/05_02_167.png"
image img_05_02_168 = "mod_assets/images/05_02/05_02_168.png"
image img_05_02_169 = "mod_assets/images/05_02/05_02_169.png"
image img_05_02_170 = "mod_assets/images/05_02/05_02_170.png"
image img_05_02_171 = "mod_assets/images/05_02/05_02_171.png"
image img_05_02_172 = "mod_assets/images/05_02/05_02_172.png"
image img_05_02_173 = "mod_assets/images/05_02/05_02_173.png"
image img_05_02_174 = "mod_assets/images/05_02/05_02_174.png"
image img_05_02_175 = "mod_assets/images/05_02/05_02_175.png"
image img_05_02_176 = "mod_assets/images/05_02/05_02_176.png"
image img_05_02_177 = "mod_assets/images/05_02/05_02_177.png"
image img_05_02_178 = "mod_assets/images/05_02/05_02_178.png"
image img_05_02_179 = "mod_assets/images/05_02/05_02_179.png"
image img_05_02_180 = "mod_assets/images/05_02/05_02_180.png"
image img_05_02_181 = "mod_assets/images/05_02/05_02_181.png"
image img_05_02_182 = "mod_assets/images/05_02/05_02_182.png"
image img_milzao = "mod_assets/images/05_02/milzao.png"


#05_03
image img_05_03_01 = "mod_assets/images/05_03/05_03_01.png"
image img_05_03_02 = "mod_assets/images/05_03/05_03_02.png"
image img_05_03_03 = "mod_assets/images/05_03/05_03_03.png"
image img_05_03_04 = "mod_assets/images/05_03/05_03_04.png"
image img_05_03_05 = "mod_assets/images/05_03/05_03_05.png"
image img_05_03_06 = "mod_assets/images/05_03/05_03_06.png"
image img_05_03_07 = "mod_assets/images/05_03/05_03_07.png"
image img_05_03_08 = "mod_assets/images/05_03/05_03_08.png"
image img_05_03_09 = "mod_assets/images/05_03/05_03_09.png"
image img_05_03_10 = "mod_assets/images/05_03/05_03_10.png"
image img_05_03_11 = "mod_assets/images/05_03/05_03_11.png"
image img_05_03_12 = "mod_assets/images/05_03/05_03_12.png"
image img_05_03_13 = "mod_assets/images/05_03/05_03_13.png"
image img_05_03_14 = "mod_assets/images/05_03/05_03_14.png"
image img_05_03_15 = "mod_assets/images/05_03/05_03_15.png"
image img_05_03_16 = "mod_assets/images/05_03/05_03_16.png"
image img_05_03_17 = "mod_assets/images/05_03/05_03_17.png"
image img_05_03_18 = "mod_assets/images/05_03/05_03_18.png"
image img_05_03_19 = "mod_assets/images/05_03/05_03_19.png"
image img_05_03_20 = "mod_assets/images/05_03/05_03_20.png"
image img_05_03_21 = "mod_assets/images/05_03/05_03_21.png"
image img_05_03_22 = "mod_assets/images/05_03/05_03_22.png"


#Epilogo
image img_epilogo_01 = "mod_assets/images/epilogo/epilogo_01.png"
image img_epilogo_02 = "mod_assets/images/epilogo/epilogo_02.png"
image img_epilogo_03 = "mod_assets/images/epilogo/epilogo_03.png"
image img_epilogo_04 = "mod_assets/images/epilogo/epilogo_04.png"
image img_epilogo_05 = "mod_assets/images/epilogo/epilogo_05.png"
image img_epilogo_06 = "mod_assets/images/epilogo/epilogo_06.png"
image img_epilogo_07 = "mod_assets/images/epilogo/epilogo_07.png"
image img_epilogo_08 = "mod_assets/images/epilogo/epilogo_08.png"
image img_epilogo_09 = "mod_assets/images/epilogo/epilogo_09.png"
image img_epilogo_10 = "mod_assets/images/epilogo/epilogo_10.png"
image img_epilogo_11 = "mod_assets/images/epilogo/epilogo_11.png"
image img_epilogo_12 = "mod_assets/images/epilogo/epilogo_12.png"
image img_epilogo_13 = "mod_assets/images/epilogo/epilogo_13.png"
image img_epilogo_14 = "mod_assets/images/epilogo/epilogo_14.png"
image img_epilogo_15 = "mod_assets/images/epilogo/epilogo_15.png"
image img_epilogo_16 = "mod_assets/images/epilogo/epilogo_16.png"
image img_epilogo_17 = "mod_assets/images/epilogo/epilogo_17.png"
image img_epilogo_18 = "mod_assets/images/epilogo/epilogo_18.png"
image img_epilogo_19 = "mod_assets/images/epilogo/epilogo_19.png"
image img_epilogo_20 = "mod_assets/images/epilogo/epilogo_20.png"
image img_epilogo_21 = "mod_assets/images/epilogo/epilogo_21.png"
image img_epilogo_22 = "mod_assets/images/epilogo/epilogo_22.png"
image img_epilogo_23 = "mod_assets/images/epilogo/epilogo_23.png"





image yami_senna:
    "mod_assets/images/yami_senna.png"
    alpha 0.0
    linear 0.5
    linear 4.0 alpha 1.0
    linear 1.0
    linear 0.5 alpha 0.2

image yami_senna_bg:
    "mod_assets/images/yami_senna.png"
    alpha 0.2

image yami_senna_bg_end:
    "mod_assets/images/yami_senna.png"
    alpha 0.2
    linear 4.0 alpha 0.0

image capitulo_concluido:
    "mod_assets/images/capitulo_concluido.png"
    align (0.5,0.5)
    block:
        alpha 1.0
        0.25
        alpha 0.0
        0.25 
        repeat 11
    block:
        alpha 1.0
        0.03
    
        alpha 0.0
        0.03 
        repeat 24
    
image voce_desbloqueou:
    "mod_assets/images/voce_desbloqueou.png"
    align (0.5,0.10)
    alpha 0.0
    linear 0.8 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_01:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/monstro_que_relaxa.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_01:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Monstro Que\nRelaxa\n\n\n\nReviva um\nmacho do seu\ncemitério vain", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_02:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/filhona.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_02:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Filhona\n\n\n\nNUOOOSSA MINHA\nFILHONA EU\nNA CREDITO", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_03:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/dragao_baiano.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_03:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Dragão BAIANO\n\n\n\nUma criatura vinda\nda Bahia, lá de\nCupiqueno.", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_04:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/coringa_dano.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_04:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Coringa Dano\n\n\n\nO CORINGA DANO MAS\nVAI VER HOJE O\nCORINGA DANO", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_05:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/polimerizacao.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_05:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Polimerização G\n\n\n\nFaça uma fusão\ngrande e gostosa de\ndois machos peludos.", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_img_cap_06:
    align (0.15,0.75)
    zoom 0.75
    alpha 0.0
    time 1.5
    "mod_assets/images/deck/sandro_lima.png"
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0

image carta_desc_cap_06:
    align (0.85,0.65)
    alpha 0.0
    time 1.5
    Text("Sandro Lima,\no Arquiteto\nda Delícia\n\n\n\nDeus onipotente\nda criação do\nUniverso G.", style="credits_text")
    linear 1.0 alpha 1.0
    time 6.5
    linear 3.0 alpha 0.0


image header_cap_01 = "mod_assets/images/cap01.png"
image header_cap_02 = "mod_assets/images/cap02.png"
image header_cap_03 = "mod_assets/images/cap03.png"
image header_cap_04 = "mod_assets/images/cap04.png"
image header_cap_05 = "mod_assets/images/cap05.png"
image header_cap_XX = "mod_assets/images/capXX.png"

image textbox_aux:
    "mod_assets/gui/textbox2.png"
    xalign 0.5
    yalign 1.0

image alemao_s1 = "mod_assets/characters/side/alemao_s1.png"
image anita_s1 = "mod_assets/characters/side/anita_s1.png"
image bob_s1 = "mod_assets/characters/side/bob_s1.png"
image bob_s2 = "mod_assets/characters/side/bob_s2.png"
image doutora_s1 = "mod_assets/characters/side/doutora_s1.png"
image goleiro_s1 = "mod_assets/characters/side/goleiro_s1.png"
image guina_s = "mod_assets/characters/side/guina_s.png"
image indio_s1 = "mod_assets/characters/side/indio_s1.png"
image indio_s2 = "mod_assets/characters/side/indio_s2.png"
image james_s1 = "mod_assets/characters/side/james_s1.png"
image james_s2 = "mod_assets/characters/side/james_s2.png"
image mangueiraboy_s1 = "mod_assets/characters/side/mangueiraboy_s1.png"
image mangueiraevil_s1 = "mod_assets/characters/side/mangueiraevil_s1.png"
image secretaria_s1 = "mod_assets/characters/side/secretaria_s1.png"
image senna_s1 = "mod_assets/characters/side/senna_s1.png"
image senna_s2 = "mod_assets/characters/side/senna_s2.png"
image senna_s3 = "mod_assets/characters/side/senna_s3.png"
image senna_s4 = "mod_assets/characters/side/senna_s4.png"
image senna_s5 = "mod_assets/characters/side/senna_s5.png"
image senna_s6 = "mod_assets/characters/side/senna_s6.png"
image senna_s7 = "mod_assets/characters/side/senna_s7.png"
image senna_s8 = "mod_assets/characters/side/senna_s8.png"
image seto_s = "mod_assets/characters/side/seto_s.png"
image yeahman_s1 = "mod_assets/characters/side/yeahman_s1.png"
image yuri_s1 = "mod_assets/characters/side/yuri_s1.png"
image yuri_s2 = "mod_assets/characters/side/yuri_s2.png"


image splash_image = "mod_assets/images/splash_image.png"
image intro_001 = "mod_assets/images/intro/intro_001.png"
image intro_002 = "mod_assets/images/intro/intro_002.png"
image intro_003 = "mod_assets/images/intro/intro_003.png"
image intro_004 = "mod_assets/images/intro/intro_004.png"

image cap_arabe_img = "mod_assets/images/cap_arabe.png"
image cap_arabe_img2 = "mod_assets/images/cap_arabe2.png"

image club = "mod_assets/images/capXX/club.png"
image corredor_ddlc = "mod_assets/images/capXX/corridor.png"
image escadas_ddlc = "mod_assets/images/capXX/stairs.png"

###################Musicas 
define audio.guina_piscineiro = "<loop 0.0>mod_assets/music/paulo_guina_piscineiro.ogg"
define audio.senna_theme = "<loop 0.0>mod_assets/music/senna_theme.ogg"
define audio.yugioco = "<loop 0.0>mod_assets/music/yugioco.ogg"
define audio.farao_amet = "<loop 0.0>mod_assets/music/farao_amet.ogg"
define audio.sh4_resting_comfortably = "<loop 1.966>mod_assets/music/sh4_resting_comfortably.ogg"

define audio.indio_policia = "<loop 0.0>mod_assets/music/indio_policia.ogg"
define audio.tv_001 = "mod_assets/music/tv_001.ogg"
define audio.tv_002 = "mod_assets/music/tv_002.ogg"
define audio.tv_003 = "mod_assets/music/tv_003.ogg"
define audio.tv_004 = "mod_assets/music/tv_004.ogg"
define audio.tv_005 = "mod_assets/music/tv_005.ogg"
define audio.siren = "mod_assets/music/siren.ogg"
define audio.siren2 = "<loop 0.433>mod_assets/music/siren2.ogg"
define audio.ambulance_01 = "<loop 0.00>mod_assets/music/ambulance_01.ogg"
define audio.ambulance_02 = "<loop 0.00>mod_assets/music/ambulance_02.ogg"
define audio.city_01 = "<loop 0.00>mod_assets/music/city_01.ogg"
define audio.cicadas = "<loop 0.00>mod_assets/music/cicadas.ogg"
define audio.tele_sena = "<loop 0.00>mod_assets/music/tele_sena.ogg"
define audio.tele_sena_metaleiro = "<loop 0.00>mod_assets/music/tele_sena_metaleiro.ogg"
define audio.despacito_nokia = "<loop 0.00>mod_assets/music/despacito_nokia.ogg"

define audio.fm_nameinput = "<loop 9.00>mod_assets/music/fm_nameinput.ogg"
define audio.fm_intro = "mod_assets/music/fm_intro.ogg"
define audio.fm_preliminary_faceoff = "<loop 1.333>mod_assets/music/fm_preliminary_faceoff.ogg"
define audio.fm_plazatown = "<loop 26.033>mod_assets/music/fm_plazatown.ogg"
define audio.fm_gameover = "mod_assets/music/fm_gameover.ogg"
define audio.fm_gameover2 = "mod_assets/music/fm_gameover2.ogg"
define audio.m_converting_minds = "mod_assets/music/m_converting_minds.ogg"
define audio.fm_freeduel = "<loop 0.933>mod_assets/music/fm_freeduel.ogg"
define audio.fm_deck = "<loop 0.60>mod_assets/music/fm_deck.ogg"
define audio.fm_password = "<loop 1.833>mod_assets/music/fm_password.ogg"
define audio.fm_library = "<loop 0.70>mod_assets/music/fm_library.ogg"
define audio.fm_credits = "<loop 0.00>mod_assets/music/fm_credits.ogg"
define audio.fm_sebek_neku = "<loop 0.00>mod_assets/music/fm_sebek_neku.ogg"
define audio.fm_finals = "<loop 21.066>mod_assets/music/fm_finals.ogg"
define audio.fm_finals_faceoff = "<loop 2.233>mod_assets/music/fm_finals_faceoff.ogg"
define audio.fm_youlose = "mod_assets/music/fm_youlose.ogg"
define audio.fm_youwin = "<loop 9.2>mod_assets/music/fm_youwin.ogg"
define audio.fm_modern_times = "<loop 1.633>mod_assets/music/fm_modern_times.ogg"
define audio.fm_modern_shop = "<loop 2.058>mod_assets/music/fm_modern_shop.ogg"
define audio.fm_tournament = "<loop 10.366>mod_assets/music/fm_tournament.ogg"
define audio.fm_preliminary_duel = "<loop 0.933>mod_assets/music/fm_preliminary_duel.ogg"
define audio.fm_inside_the_puzzle = "<loop 3.433>mod_assets/music/fm_inside_the_puzzle.ogg"
define audio.fm_heishin_encounter = "<loop 8.6>mod_assets/music/fm_heishin_encounter.ogg"
define audio.fm_heishin_theme = "<loop 0.5>mod_assets/music/fm_heishin_theme.ogg"
define audio.fm_seto_encounter = "<loop 5.2>mod_assets/music/fm_seto_encounter.ogg"
define audio.fm_temple_ruins = "<loop 0.0>mod_assets/music/fm_temple_ruins.ogg"
define audio.fm_map_select_2 = "<loop 0.0>mod_assets/music/fm_map_select_2.ogg"
define audio.fm_shadi_egypt = "<loop 2.4>mod_assets/music/fm_shadi_egypt.ogg"
define audio.fm_simon_muran = "<loop 14.766>mod_assets/music/fm_simon_muran.ogg"
define audio.fm_map_select_1 = "<loop 0.0>mod_assets/music/fm_map_select_1.ogg"
define audio.fm_seto_theme = "<loop 3.266>mod_assets/music/fm_seto_theme.ogg"
define audio.fm_duel_grounds = "<loop 6.933>mod_assets/music/fm_duel_grounds.ogg"
define audio.fm_mages_duel = "<loop 9.2>mod_assets/music/fm_mages_duel.ogg"
define audio.fm_3d_duel = "<loop 10.333>mod_assets/music/fm_3d_duel.ogg"
define audio.fm_free_duel_theme = "<loop 1.766>mod_assets/music/fm_free_duel_theme.ogg"
define audio.fm_shadi_future = "<loop 0.0>mod_assets/music/fm_shadi_future.ogg"
define audio.fm_kaiba_faceoff = "<loop 0.833>mod_assets/music/fm_kaiba_faceoff.ogg"
define audio.fm_kaiba_theme = "<loop 0.0>mod_assets/music/fm_kaiba_theme.ogg"
define audio.fm_forest_shrine = "<loop 0.0>mod_assets/music/fm_forest_shrine.ogg"
define audio.fm_vast_shrine = "<loop 38.3>mod_assets/music/fm_vast_shrine.ogg"
define audio.fm_egyptian_duel = "<loop 0.666>mod_assets/music/fm_egyptian_duel.ogg"
define audio.fm_high_mages_duel = "<loop 16.666>mod_assets/music/fm_high_mages_duel.ogg"
define audio.fm_darknite_encounter = "<loop 17.266>mod_assets/music/fm_darknite_encounter.ogg"
define audio.fm_darknite_theme = "<loop 6.6>mod_assets/music/fm_darknite_theme.ogg"
define audio.fm_pharaoh = "<loop 0.0>mod_assets/music/fm_pharaoh.ogg"
define audio.fm_3d_duel_finals = "<loop 9.933>mod_assets/music/fm_3d_duel_finals.ogg"
define audio.fm_forbidden_ruins = "<loop 16.8>mod_assets/music/fm_forbidden_ruins.ogg"

###################Vozes
define voz_teste = "mod_assets/voices/teste.ogg"
define voz_jailson_arabe = "mod_assets/voices/jailson_arabe.ogg"
define voz_guina_arabe = "mod_assets/voices/guina_arabe.ogg"

#01_01



#01_02
define voz_cap01_02_01 = "mod_assets/voices/01_02/01_02_01.ogg"
define voz_cap01_02_02 = "mod_assets/voices/01_02/01_02_02.ogg"


#01_03
define voz_cap01_03_01 = "mod_assets/voices/01_03/01_03_01.ogg"
define voz_cap01_03_02 = "mod_assets/voices/01_03/01_03_02.ogg"
define voz_cap01_03_03 = "mod_assets/voices/01_03/01_03_03.ogg"
define voz_cap01_03_04 = "mod_assets/voices/01_03/01_03_04.ogg"
define voz_cap01_03_05 = "mod_assets/voices/01_03/01_03_05.ogg"
define voz_cap01_03_06 = "mod_assets/voices/01_03/01_03_06.ogg"
define voz_cap01_03_07 = "mod_assets/voices/01_03/01_03_07.ogg"
define voz_cap01_03_08 = "mod_assets/voices/01_03/01_03_08.ogg"
define voz_cap01_03_09 = "mod_assets/voices/01_03/01_03_09.ogg"
define voz_cap01_03_10 = "mod_assets/voices/01_03/01_03_10.ogg"
define voz_cap01_03_11 = "mod_assets/voices/01_03/01_03_11.ogg"
define voz_cap01_03_12 = "mod_assets/voices/01_03/01_03_12.ogg"
define voz_cap01_03_13 = "mod_assets/voices/01_03/01_03_13.ogg"
define voz_cap01_03_14 = "mod_assets/voices/01_03/01_03_14.ogg"
define voz_cap01_03_15 = "mod_assets/voices/01_03/01_03_15.ogg"
define voz_cap01_03_16 = "mod_assets/voices/01_03/01_03_16.ogg"
define voz_cap01_03_17 = "mod_assets/voices/01_03/01_03_17.ogg"
define voz_cap01_03_18 = "mod_assets/voices/01_03/01_03_18.ogg"
define voz_cap01_03_19 = "mod_assets/voices/01_03/01_03_19.ogg"
define voz_cap01_03_20 = "mod_assets/voices/01_03/01_03_20.ogg"
define voz_cap01_03_21 = "mod_assets/voices/01_03/01_03_21.ogg"
define voz_cap01_03_22 = "mod_assets/voices/01_03/01_03_22.ogg"
define voz_cap01_03_23 = "mod_assets/voices/01_03/01_03_23.ogg"
define voz_cap01_03_24 = "mod_assets/voices/01_03/01_03_24.ogg"
define voz_cap01_03_25 = "mod_assets/voices/01_03/01_03_25.ogg"
define voz_cap01_03_26 = "mod_assets/voices/01_03/01_03_26.ogg"
define voz_cap01_03_27 = "mod_assets/voices/01_03/01_03_27.ogg"
define voz_cap01_03_28 = "mod_assets/voices/01_03/01_03_28.ogg"
define voz_cap01_03_29 = "mod_assets/voices/01_03/01_03_29.ogg"
define voz_cap01_03_30 = "mod_assets/voices/01_03/01_03_30.ogg"


#01_04
define voz_cap01_04_01 = "mod_assets/voices/01_04/01_04_01.ogg"
define voz_cap01_04_02 = "mod_assets/voices/01_04/01_04_02.ogg"
define voz_cap01_04_03 = "mod_assets/voices/01_04/01_04_03.ogg"
define voz_cap01_04_04 = "mod_assets/voices/01_04/01_04_04.ogg"
define voz_cap01_04_05 = "mod_assets/voices/01_04/01_04_05.ogg"
define voz_cap01_04_06 = "mod_assets/voices/01_04/01_04_06.ogg"
define voz_cap01_04_07 = "mod_assets/voices/01_04/01_04_07.ogg"
define voz_cap01_04_08 = "mod_assets/voices/01_04/01_04_08.ogg"
define voz_cap01_04_09 = "mod_assets/voices/01_04/01_04_09.ogg"
define voz_cap01_04_10 = "mod_assets/voices/01_04/01_04_10.ogg"
define voz_cap01_04_11 = "mod_assets/voices/01_04/01_04_11.ogg"
define voz_cap01_04_12 = "mod_assets/voices/01_04/01_04_12.ogg"
define voz_cap01_04_13 = "mod_assets/voices/01_04/01_04_13.ogg"
define voz_cap01_04_14 = "mod_assets/voices/01_04/01_04_14.ogg"
define voz_cap01_04_15 = "mod_assets/voices/01_04/01_04_15.ogg"
define voz_cap01_04_16 = "mod_assets/voices/01_04/01_04_16.ogg"
define voz_cap01_04_17 = "mod_assets/voices/01_04/01_04_17.ogg"
define voz_cap01_04_18 = "mod_assets/voices/01_04/01_04_18.ogg"
define voz_cap01_04_19 = "mod_assets/voices/01_04/01_04_19.ogg"
define voz_cap01_04_20 = "mod_assets/voices/01_04/01_04_20.ogg"
define voz_cap01_04_21 = "mod_assets/voices/01_04/01_04_21.ogg"
define voz_cap01_04_22 = "mod_assets/voices/01_04/01_04_22.ogg"
define voz_cap01_04_23 = "mod_assets/voices/01_04/01_04_23.ogg"
define voz_cap01_04_24 = "mod_assets/voices/01_04/01_04_24.ogg"
define voz_cap01_04_25 = "mod_assets/voices/01_04/01_04_25.ogg"
define voz_cap01_04_26 = "mod_assets/voices/01_04/01_04_26.ogg"
define voz_cap01_04_27 = "mod_assets/voices/01_04/01_04_27.ogg"
define voz_cap01_04_28 = "mod_assets/voices/01_04/01_04_28.ogg"
define voz_cap01_04_29 = "mod_assets/voices/01_04/01_04_29.ogg"
define voz_cap01_04_30 = "mod_assets/voices/01_04/01_04_30.ogg"
define voz_cap01_04_31 = "mod_assets/voices/01_04/01_04_31.ogg"
define voz_cap01_04_32 = "mod_assets/voices/01_04/01_04_32.ogg"
define voz_cap01_04_33 = "mod_assets/voices/01_04/01_04_33.ogg"
define voz_cap01_04_34 = "mod_assets/voices/01_04/01_04_34.ogg"
define voz_cap01_04_35 = "mod_assets/voices/01_04/01_04_35.ogg"
define voz_cap01_04_36 = "mod_assets/voices/01_04/01_04_36.ogg"
define voz_cap01_04_37 = "mod_assets/voices/01_04/01_04_37.ogg"
define voz_cap01_04_38 = "mod_assets/voices/01_04/01_04_38.ogg"
define voz_cap01_04_39 = "mod_assets/voices/01_04/01_04_39.ogg"
define voz_cap01_04_40 = "mod_assets/voices/01_04/01_04_40.ogg"
define voz_cap01_04_41 = "mod_assets/voices/01_04/01_04_41.ogg"
define voz_cap01_04_42 = "mod_assets/voices/01_04/01_04_42.ogg"
define voz_cap01_04_43 = "mod_assets/voices/01_04/01_04_43.ogg"
define voz_cap01_04_44 = "mod_assets/voices/01_04/01_04_44.ogg"
define voz_cap01_04_45 = "mod_assets/voices/01_04/01_04_45.ogg"
define voz_cap01_04_46 = "mod_assets/voices/01_04/01_04_46.ogg"
define voz_cap01_04_47 = "mod_assets/voices/01_04/01_04_47.ogg"
define voz_cap01_04_48 = "mod_assets/voices/01_04/01_04_48.ogg"
define voz_cap01_04_49 = "mod_assets/voices/01_04/01_04_49.ogg"
define voz_cap01_04_50 = "mod_assets/voices/01_04/01_04_50.ogg"
define voz_cap01_04_51 = "mod_assets/voices/01_04/01_04_51.ogg"
define voz_cap01_04_52 = "mod_assets/voices/01_04/01_04_52.ogg"
define voz_cap01_04_53 = "mod_assets/voices/01_04/01_04_53.ogg"
define voz_cap01_04_54 = "mod_assets/voices/01_04/01_04_54.ogg"
define voz_cap01_04_55 = "mod_assets/voices/01_04/01_04_55.ogg"
define voz_cap01_04_56 = "mod_assets/voices/01_04/01_04_56.ogg"
define voz_cap01_04_57 = "mod_assets/voices/01_04/01_04_57.ogg"
define voz_cap01_04_58 = "mod_assets/voices/01_04/01_04_58.ogg"
define voz_cap01_04_59 = "mod_assets/voices/01_04/01_04_59.ogg"
define voz_cap01_04_60 = "mod_assets/voices/01_04/01_04_60.ogg"
define voz_cap01_04_61 = "mod_assets/voices/01_04/01_04_61.ogg"
define voz_cap01_04_62 = "mod_assets/voices/01_04/01_04_62.ogg"
define voz_cap01_04_63 = "mod_assets/voices/01_04/01_04_63.ogg"
define voz_cap01_04_64 = "mod_assets/voices/01_04/01_04_64.ogg"
define voz_cap01_04_65 = "mod_assets/voices/01_04/01_04_65.ogg"


#02_01
define voz_cap02_01_01 = "mod_assets/voices/02_01/02_01_01.ogg"


#02_02
define voz_cap02_02_01 = "mod_assets/voices/02_02/02_02_01.ogg"
define voz_cap02_02_02 = "mod_assets/voices/02_02/02_02_02.ogg"
define voz_cap02_02_03 = "mod_assets/voices/02_02/02_02_03.ogg"
define voz_cap02_02_04 = "mod_assets/voices/02_02/02_02_04.ogg"
define voz_cap02_02_05 = "mod_assets/voices/02_02/02_02_05.ogg"
define voz_cap02_02_06 = "mod_assets/voices/02_02/02_02_06.ogg"
define voz_cap02_02_07 = "mod_assets/voices/02_02/02_02_07.ogg"
define voz_cap02_02_08 = "mod_assets/voices/02_02/02_02_08.ogg"
define voz_cap02_02_09 = "mod_assets/voices/02_02/02_02_09.ogg"
define voz_cap02_02_10 = "mod_assets/voices/02_02/02_02_10.ogg"
define voz_cap02_02_11 = "mod_assets/voices/02_02/02_02_11.ogg"
define voz_cap02_02_12 = "mod_assets/voices/02_02/02_02_12.ogg"
define voz_cap02_02_13 = "mod_assets/voices/02_02/02_02_13.ogg"
define voz_cap02_02_14 = "mod_assets/voices/02_02/02_02_14.ogg"
define voz_cap02_02_15 = "mod_assets/voices/02_02/02_02_15.ogg"
define voz_cap02_02_16 = "mod_assets/voices/02_02/02_02_16.ogg"
define voz_cap02_02_17 = "mod_assets/voices/02_02/02_02_17.ogg"
define voz_cap02_02_18 = "mod_assets/voices/02_02/02_02_18.ogg"
define voz_cap02_02_19 = "mod_assets/voices/02_02/02_02_19.ogg"
define voz_cap02_02_20 = "mod_assets/voices/02_02/02_02_20.ogg"
define voz_cap02_02_21 = "mod_assets/voices/02_02/02_02_21.ogg"
define voz_cap02_02_22 = "mod_assets/voices/02_02/02_02_22.ogg"
define voz_cap02_02_23 = "mod_assets/voices/02_02/02_02_23.ogg"
define voz_cap02_02_24 = "mod_assets/voices/02_02/02_02_24.ogg"
define voz_cap02_02_25 = "mod_assets/voices/02_02/02_02_25.ogg"
define voz_cap02_02_26 = "mod_assets/voices/02_02/02_02_26.ogg"
define voz_cap02_02_27 = "mod_assets/voices/02_02/02_02_27.ogg"
define voz_cap02_02_28 = "mod_assets/voices/02_02/02_02_28.ogg"
define voz_cap02_02_29 = "mod_assets/voices/02_02/02_02_29.ogg"
define voz_cap02_02_30 = "mod_assets/voices/02_02/02_02_30.ogg"
define voz_cap02_02_31 = "mod_assets/voices/02_02/02_02_31.ogg"
define voz_cap02_02_32 = "mod_assets/voices/02_02/02_02_32.ogg"
define voz_cap02_02_33 = "mod_assets/voices/02_02/02_02_33.ogg"
define voz_cap02_02_34 = "mod_assets/voices/02_02/02_02_34.ogg"
define voz_cap02_02_35 = "mod_assets/voices/02_02/02_02_35.ogg"
define voz_cap02_02_36 = "mod_assets/voices/02_02/02_02_36.ogg"
define voz_cap02_02_37 = "mod_assets/voices/02_02/02_02_37.ogg"
define voz_cap02_02_38 = "mod_assets/voices/02_02/02_02_38.ogg"
define voz_cap02_02_39 = "mod_assets/voices/02_02/02_02_39.ogg"
define voz_cap02_02_40 = "mod_assets/voices/02_02/02_02_40.ogg"
define voz_cap02_02_41 = "mod_assets/voices/02_02/02_02_41.ogg"
define voz_cap02_02_42 = "mod_assets/voices/02_02/02_02_42.ogg"
define voz_cap02_02_43 = "mod_assets/voices/02_02/02_02_43.ogg"
define voz_cap02_02_44 = "mod_assets/voices/02_02/02_02_44.ogg"
define voz_cap02_02_45 = "mod_assets/voices/02_02/02_02_45.ogg"
define voz_cap02_02_46 = "mod_assets/voices/02_02/02_02_46.ogg"
define voz_cap02_02_47 = "mod_assets/voices/02_02/02_02_47.ogg"
define voz_cap02_02_48 = "mod_assets/voices/02_02/02_02_48.ogg"
define voz_cap02_02_49 = "mod_assets/voices/02_02/02_02_49.ogg"
define voz_cap02_02_50 = "mod_assets/voices/02_02/02_02_50.ogg"
define voz_cap02_02_51 = "mod_assets/voices/02_02/02_02_51.ogg"
define voz_cap02_02_52 = "mod_assets/voices/02_02/02_02_52.ogg"
define voz_cap02_02_53 = "mod_assets/voices/02_02/02_02_53.ogg"
define voz_cap02_02_54 = "mod_assets/voices/02_02/02_02_54.ogg"
define voz_cap02_02_55 = "mod_assets/voices/02_02/02_02_55.ogg"
define voz_cap02_02_56 = "mod_assets/voices/02_02/02_02_56.ogg"


#02_03
define voz_cap02_03_01 = "mod_assets/voices/02_03/02_03_01.ogg"
define voz_cap02_03_02 = "mod_assets/voices/02_03/02_03_02.ogg"
define voz_cap02_03_03 = "mod_assets/voices/02_03/02_03_03.ogg"
define voz_cap02_03_04 = "mod_assets/voices/02_03/02_03_04.ogg"
define voz_cap02_03_05 = "mod_assets/voices/02_03/02_03_05.ogg"
define voz_cap02_03_06 = "mod_assets/voices/02_03/02_03_06.ogg"
define voz_cap02_03_07 = "mod_assets/voices/02_03/02_03_07.ogg"
define voz_cap02_03_08 = "mod_assets/voices/02_03/02_03_08.ogg"


#02_04
define voz_cap02_04_01 = "mod_assets/voices/02_04/02_04_01.ogg"
define voz_cap02_04_02 = "mod_assets/voices/02_04/02_04_02.ogg"
define voz_cap02_04_03 = "mod_assets/voices/02_04/02_04_03.ogg"
define voz_cap02_04_04 = "mod_assets/voices/02_04/02_04_04.ogg"
define voz_cap02_04_05 = "mod_assets/voices/02_04/02_04_05.ogg"
define voz_cap02_04_06 = "mod_assets/voices/02_04/02_04_06.ogg"
define voz_cap02_04_07 = "mod_assets/voices/02_04/02_04_07.ogg"
define voz_cap02_04_08 = "mod_assets/voices/02_04/02_04_08.ogg"
define voz_cap02_04_09 = "mod_assets/voices/02_04/02_04_09.ogg"
define voz_cap02_04_10 = "mod_assets/voices/02_04/02_04_10.ogg"
define voz_cap02_04_11 = "mod_assets/voices/02_04/02_04_11.ogg"
define voz_cap02_04_12 = "mod_assets/voices/02_04/02_04_12.ogg"
define voz_cap02_04_13 = "mod_assets/voices/02_04/02_04_13.ogg"
define voz_cap02_04_14 = "mod_assets/voices/02_04/02_04_14.ogg"
define voz_cap02_04_15 = "mod_assets/voices/02_04/02_04_15.ogg"
define voz_cap02_04_16 = "mod_assets/voices/02_04/02_04_16.ogg"
define voz_cap02_04_17 = "mod_assets/voices/02_04/02_04_17.ogg"
define voz_cap02_04_18 = "mod_assets/voices/02_04/02_04_18.ogg"
define voz_cap02_04_19 = "mod_assets/voices/02_04/02_04_19.ogg"
define voz_cap02_04_20 = "mod_assets/voices/02_04/02_04_20.ogg"
define voz_cap02_04_21 = "mod_assets/voices/02_04/02_04_21.ogg"
define voz_cap02_04_22 = "mod_assets/voices/02_04/02_04_22.ogg"
define voz_cap02_04_23 = "mod_assets/voices/02_04/02_04_23.ogg"
define voz_cap02_04_24 = "mod_assets/voices/02_04/02_04_24.ogg"
define voz_cap02_04_25 = "mod_assets/voices/02_04/02_04_25.ogg"
define voz_cap02_04_26 = "mod_assets/voices/02_04/02_04_26.ogg"
define voz_cap02_04_27 = "mod_assets/voices/02_04/02_04_27.ogg"
define voz_cap02_04_28 = "mod_assets/voices/02_04/02_04_28.ogg"
define voz_cap02_04_29 = "mod_assets/voices/02_04/02_04_29.ogg"
define voz_cap02_04_30 = "mod_assets/voices/02_04/02_04_30.ogg"
define voz_cap02_04_31 = "mod_assets/voices/02_04/02_04_31.ogg"
define voz_cap02_04_32 = "mod_assets/voices/02_04/02_04_32.ogg"
define voz_cap02_04_33 = "mod_assets/voices/02_04/02_04_33.ogg"
define voz_cap02_04_34 = "mod_assets/voices/02_04/02_04_34.ogg"
define voz_cap02_04_35 = "mod_assets/voices/02_04/02_04_35.ogg"
define voz_cap02_04_36 = "mod_assets/voices/02_04/02_04_36.ogg"
define voz_cap02_04_37 = "mod_assets/voices/02_04/02_04_37.ogg"
define voz_cap02_04_38 = "mod_assets/voices/02_04/02_04_38.ogg"
define voz_cap02_04_39 = "mod_assets/voices/02_04/02_04_39.ogg"
define voz_cap02_04_40 = "mod_assets/voices/02_04/02_04_40.ogg"
define voz_cap02_04_41 = "mod_assets/voices/02_04/02_04_41.ogg"
define voz_cap02_04_42 = "mod_assets/voices/02_04/02_04_42.ogg"
define voz_cap02_04_43 = "mod_assets/voices/02_04/02_04_43.ogg"
define voz_cap02_04_44 = "mod_assets/voices/02_04/02_04_44.ogg"
define voz_cap02_04_45 = "mod_assets/voices/02_04/02_04_45.ogg"
define voz_cap02_04_46 = "mod_assets/voices/02_04/02_04_46.ogg"


#03_01
define voz_cap03_01_01 = "mod_assets/voices/03_01/03_01_01.ogg"
define voz_cap03_01_02 = "mod_assets/voices/03_01/03_01_02.ogg"
define voz_cap03_01_03 = "mod_assets/voices/03_01/03_01_03.ogg"
define voz_cap03_01_04 = "mod_assets/voices/03_01/03_01_04.ogg"
define voz_cap03_01_05 = "mod_assets/voices/03_01/03_01_05.ogg"
define voz_cap03_01_06 = "mod_assets/voices/03_01/03_01_06.ogg"
define voz_cap03_01_07 = "mod_assets/voices/03_01/03_01_07.ogg"
define voz_cap03_01_08 = "mod_assets/voices/03_01/03_01_08.ogg"
define voz_cap03_01_09 = "mod_assets/voices/03_01/03_01_09.ogg"
define voz_cap03_01_10 = "mod_assets/voices/03_01/03_01_10.ogg"
define voz_cap03_01_11 = "mod_assets/voices/03_01/03_01_11.ogg"
define voz_cap03_01_12 = "mod_assets/voices/03_01/03_01_12.ogg"


#03_02
define voz_cap03_02_01 = "mod_assets/voices/03_02/03_02_01.ogg"
define voz_cap03_02_02 = "mod_assets/voices/03_02/03_02_02.ogg"
define voz_cap03_02_03 = "mod_assets/voices/03_02/03_02_03.ogg"
define voz_cap03_02_04 = "mod_assets/voices/03_02/03_02_04.ogg"
define voz_cap03_02_05 = "mod_assets/voices/03_02/03_02_05.ogg"
define voz_cap03_02_06 = "mod_assets/voices/03_02/03_02_06.ogg"
define voz_cap03_02_07 = "mod_assets/voices/03_02/03_02_07.ogg"
define voz_cap03_02_08 = "mod_assets/voices/03_02/03_02_08.ogg"
define voz_cap03_02_09 = "mod_assets/voices/03_02/03_02_09.ogg"
define voz_cap03_02_10 = "mod_assets/voices/03_02/03_02_10.ogg"
define voz_cap03_02_11 = "mod_assets/voices/03_02/03_02_11.ogg"
define voz_cap03_02_12 = "mod_assets/voices/03_02/03_02_12.ogg"
define voz_cap03_02_13 = "mod_assets/voices/03_02/03_02_13.ogg"
define voz_cap03_02_14 = "mod_assets/voices/03_02/03_02_14.ogg"
define voz_cap03_02_15 = "mod_assets/voices/03_02/03_02_15.ogg"
define voz_cap03_02_16 = "mod_assets/voices/03_02/03_02_16.ogg"
define voz_cap03_02_17 = "mod_assets/voices/03_02/03_02_17.ogg"
define voz_cap03_02_18 = "mod_assets/voices/03_02/03_02_18.ogg"
define voz_cap03_02_19 = "mod_assets/voices/03_02/03_02_19.ogg"
define voz_cap03_02_20 = "mod_assets/voices/03_02/03_02_20.ogg"
define voz_cap03_02_21 = "mod_assets/voices/03_02/03_02_21.ogg"
define voz_cap03_02_22 = "mod_assets/voices/03_02/03_02_22.ogg"
define voz_cap03_02_23 = "mod_assets/voices/03_02/03_02_23.ogg"
define voz_cap03_02_24 = "mod_assets/voices/03_02/03_02_24.ogg"
define voz_cap03_02_25 = "mod_assets/voices/03_02/03_02_25.ogg"
define voz_cap03_02_26 = "mod_assets/voices/03_02/03_02_26.ogg"
define voz_cap03_02_27 = "mod_assets/voices/03_02/03_02_27.ogg"
define voz_cap03_02_28 = "mod_assets/voices/03_02/03_02_28.ogg"
define voz_cap03_02_29 = "mod_assets/voices/03_02/03_02_29.ogg"
define voz_cap03_02_30 = "mod_assets/voices/03_02/03_02_30.ogg"
define voz_cap03_02_31 = "mod_assets/voices/03_02/03_02_31.ogg"
define voz_cap03_02_32 = "mod_assets/voices/03_02/03_02_32.ogg"
define voz_cap03_02_33 = "mod_assets/voices/03_02/03_02_33.ogg"
define voz_cap03_02_34 = "mod_assets/voices/03_02/03_02_34.ogg"
define voz_cap03_02_35 = "mod_assets/voices/03_02/03_02_35.ogg"
define voz_cap03_02_36 = "mod_assets/voices/03_02/03_02_36.ogg"
define voz_cap03_02_37 = "mod_assets/voices/03_02/03_02_37.ogg"


#03_03
define voz_cap03_03_01 = "mod_assets/voices/03_03/03_03_01.ogg"
define voz_cap03_03_02 = "mod_assets/voices/03_03/03_03_02.ogg"
define voz_cap03_03_03 = "mod_assets/voices/03_03/03_03_03.ogg"
define voz_cap03_03_04 = "mod_assets/voices/03_03/03_03_04.ogg"
define voz_cap03_03_05 = "mod_assets/voices/03_03/03_03_05.ogg"
define voz_cap03_03_06 = "mod_assets/voices/03_03/03_03_06.ogg"
define voz_cap03_03_07 = "mod_assets/voices/03_03/03_03_07.ogg"
define voz_cap03_03_08 = "mod_assets/voices/03_03/03_03_08.ogg"
define voz_cap03_03_09 = "mod_assets/voices/03_03/03_03_09.ogg"
define voz_cap03_03_10 = "mod_assets/voices/03_03/03_03_10.ogg"
define voz_cap03_03_11 = "mod_assets/voices/03_03/03_03_11.ogg"
define voz_cap03_03_12 = "mod_assets/voices/03_03/03_03_12.ogg"
define voz_cap03_03_13 = "mod_assets/voices/03_03/03_03_13.ogg"
define voz_cap03_03_14 = "mod_assets/voices/03_03/03_03_14.ogg"
define voz_cap03_03_15 = "mod_assets/voices/03_03/03_03_15.ogg"
define voz_cap03_03_16 = "mod_assets/voices/03_03/03_03_16.ogg"
define voz_cap03_03_17 = "mod_assets/voices/03_03/03_03_17.ogg"
define voz_cap03_03_18 = "mod_assets/voices/03_03/03_03_18.ogg"
define voz_cap03_03_19 = "mod_assets/voices/03_03/03_03_19.ogg"
define voz_cap03_03_20 = "mod_assets/voices/03_03/03_03_20.ogg"
define voz_cap03_03_21 = "mod_assets/voices/03_03/03_03_21.ogg"
define voz_cap03_03_22 = "mod_assets/voices/03_03/03_03_22.ogg"
define voz_cap03_03_23 = "mod_assets/voices/03_03/03_03_23.ogg"
define voz_cap03_03_24 = "mod_assets/voices/03_03/03_03_24.ogg"
define voz_cap03_03_25 = "mod_assets/voices/03_03/03_03_25.ogg"
define voz_cap03_03_26 = "mod_assets/voices/03_03/03_03_26.ogg"
define voz_cap03_03_27 = "mod_assets/voices/03_03/03_03_27.ogg"
define voz_cap03_03_28 = "mod_assets/voices/03_03/03_03_28.ogg"
define voz_cap03_03_29 = "mod_assets/voices/03_03/03_03_29.ogg"
define voz_cap03_03_30 = "mod_assets/voices/03_03/03_03_30.ogg"
define voz_cap03_03_31 = "mod_assets/voices/03_03/03_03_31.ogg"
define voz_cap03_03_32 = "mod_assets/voices/03_03/03_03_32.ogg"
define voz_cap03_03_33 = "mod_assets/voices/03_03/03_03_33.ogg"
define voz_cap03_03_34 = "mod_assets/voices/03_03/03_03_34.ogg"
define voz_cap03_03_35 = "mod_assets/voices/03_03/03_03_35.ogg"
define voz_cap03_03_36 = "mod_assets/voices/03_03/03_03_36.ogg"
define voz_cap03_03_37 = "mod_assets/voices/03_03/03_03_37.ogg"


#04_01
define voz_cap04_01_01 = "mod_assets/voices/04_01/04_01_01.ogg"
define voz_cap04_01_02 = "mod_assets/voices/04_01/04_01_02.ogg"
define voz_cap04_01_03 = "mod_assets/voices/04_01/04_01_03.ogg"
define voz_cap04_01_04 = "mod_assets/voices/04_01/04_01_04.ogg"
define voz_cap04_01_05 = "mod_assets/voices/04_01/04_01_05.ogg"
define voz_cap04_01_06 = "mod_assets/voices/04_01/04_01_06.ogg"
define voz_cap04_01_07 = "mod_assets/voices/04_01/04_01_07.ogg"
define voz_cap04_01_08 = "mod_assets/voices/04_01/04_01_08.ogg"
define voz_cap04_01_09 = "mod_assets/voices/04_01/04_01_09.ogg"
define voz_cap04_01_10 = "mod_assets/voices/04_01/04_01_10.ogg"


#04_02
define voz_cap04_02_01 = "mod_assets/voices/04_02/04_02_01.ogg"
define voz_cap04_02_02 = "mod_assets/voices/04_02/04_02_02.ogg"
define voz_cap04_02_03 = "mod_assets/voices/04_02/04_02_03.ogg"
define voz_cap04_02_04 = "mod_assets/voices/04_02/04_02_04.ogg"
define voz_cap04_02_05 = "mod_assets/voices/04_02/04_02_05.ogg"
define voz_cap04_02_06 = "mod_assets/voices/04_02/04_02_06.ogg"
define voz_cap04_02_07 = "mod_assets/voices/04_02/04_02_07.ogg"
define voz_cap04_02_08 = "mod_assets/voices/04_02/04_02_08.ogg"
define voz_cap04_02_09 = "mod_assets/voices/04_02/04_02_09.ogg"
define voz_cap04_02_10 = "mod_assets/voices/04_02/04_02_10.ogg"
define voz_cap04_02_11 = "mod_assets/voices/04_02/04_02_11.ogg"
define voz_cap04_02_12 = "mod_assets/voices/04_02/04_02_12.ogg"
define voz_cap04_02_13 = "mod_assets/voices/04_02/04_02_13.ogg"
define voz_cap04_02_14 = "mod_assets/voices/04_02/04_02_14.ogg"
define voz_cap04_02_15 = "mod_assets/voices/04_02/04_02_15.ogg"
define voz_cap04_02_16 = "mod_assets/voices/04_02/04_02_16.ogg"
define voz_cap04_02_17 = "mod_assets/voices/04_02/04_02_17.ogg"
define voz_cap04_02_18 = "mod_assets/voices/04_02/04_02_18.ogg"
define voz_cap04_02_19 = "mod_assets/voices/04_02/04_02_19.ogg"
define voz_cap04_02_20 = "mod_assets/voices/04_02/04_02_20.ogg"
define voz_cap04_02_21 = "mod_assets/voices/04_02/04_02_21.ogg"
define voz_cap04_02_22 = "mod_assets/voices/04_02/04_02_22.ogg"
define voz_cap04_02_23 = "mod_assets/voices/04_02/04_02_23.ogg"


#04_03
define voz_cap04_03_01 = "mod_assets/voices/04_03/04_03_01.ogg"
define voz_cap04_03_02 = "mod_assets/voices/04_03/04_03_02.ogg"
define voz_cap04_03_03 = "mod_assets/voices/04_03/04_03_03.ogg"
define voz_cap04_03_04 = "mod_assets/voices/04_03/04_03_04.ogg"
define voz_cap04_03_05 = "mod_assets/voices/04_03/04_03_05.ogg"
define voz_cap04_03_06 = "mod_assets/voices/04_03/04_03_06.ogg"
define voz_cap04_03_07 = "mod_assets/voices/04_03/04_03_07.ogg"


#04_04
define voz_cap04_04_01 = "mod_assets/voices/04_04/04_04_01.ogg"
define voz_cap04_04_02 = "mod_assets/voices/04_04/04_04_02.ogg"
define voz_cap04_04_03 = "mod_assets/voices/04_04/04_04_03.ogg"
define voz_cap04_04_04 = "mod_assets/voices/04_04/04_04_04.ogg"
define voz_cap04_04_05 = "mod_assets/voices/04_04/04_04_05.ogg"
define voz_cap04_04_06 = "mod_assets/voices/04_04/04_04_06.ogg"
define voz_cap04_04_07 = "mod_assets/voices/04_04/04_04_07.ogg"
define voz_cap04_04_08 = "mod_assets/voices/04_04/04_04_08.ogg"
define voz_cap04_04_09 = "mod_assets/voices/04_04/04_04_09.ogg"
define voz_cap04_04_10 = "mod_assets/voices/04_04/04_04_10.ogg"
define voz_cap04_04_11 = "mod_assets/voices/04_04/04_04_11.ogg"
define voz_cap04_04_12 = "mod_assets/voices/04_04/04_04_12.ogg"
define voz_cap04_04_13 = "mod_assets/voices/04_04/04_04_13.ogg"
define voz_cap04_04_14 = "mod_assets/voices/04_04/04_04_14.ogg"
define voz_cap04_04_15 = "mod_assets/voices/04_04/04_04_15.ogg"
define voz_cap04_04_16 = "mod_assets/voices/04_04/04_04_16.ogg"
define voz_cap04_04_17 = "mod_assets/voices/04_04/04_04_17.ogg"
define voz_cap04_04_18 = "mod_assets/voices/04_04/04_04_18.ogg"
define voz_cap04_04_19 = "mod_assets/voices/04_04/04_04_19.ogg"
define voz_cap04_04_20 = "mod_assets/voices/04_04/04_04_20.ogg"
define voz_cap04_04_21 = "mod_assets/voices/04_04/04_04_21.ogg"
define voz_cap04_04_22 = "mod_assets/voices/04_04/04_04_22.ogg"
define voz_cap04_04_23 = "mod_assets/voices/04_04/04_04_23.ogg"
define voz_cap04_04_24 = "mod_assets/voices/04_04/04_04_24.ogg"
define voz_cap04_04_25 = "mod_assets/voices/04_04/04_04_25.ogg"
define voz_cap04_04_26 = "mod_assets/voices/04_04/04_04_26.ogg"
define voz_cap04_04_27 = "mod_assets/voices/04_04/04_04_27.ogg"
define voz_cap04_04_28 = "mod_assets/voices/04_04/04_04_28.ogg"
define voz_cap04_04_29 = "mod_assets/voices/04_04/04_04_29.ogg"
define voz_cap04_04_30 = "mod_assets/voices/04_04/04_04_30.ogg"
define voz_cap04_04_31 = "mod_assets/voices/04_04/04_04_31.ogg"
define voz_cap04_04_32 = "mod_assets/voices/04_04/04_04_32.ogg"
define voz_cap04_04_33 = "mod_assets/voices/04_04/04_04_33.ogg"
define voz_cap04_04_34 = "mod_assets/voices/04_04/04_04_34.ogg"
define voz_cap04_04_35 = "mod_assets/voices/04_04/04_04_35.ogg"
define voz_cap04_04_36 = "mod_assets/voices/04_04/04_04_36.ogg"
define voz_cap04_04_37 = "mod_assets/voices/04_04/04_04_37.ogg"
define voz_cap04_04_38 = "mod_assets/voices/04_04/04_04_38.ogg"
define voz_cap04_04_39 = "mod_assets/voices/04_04/04_04_39.ogg"
define voz_cap04_04_40 = "mod_assets/voices/04_04/04_04_40.ogg"
define voz_cap04_04_41 = "mod_assets/voices/04_04/04_04_41.ogg"
 


#05_01
define voz_cap05_01_01 = "mod_assets/voices/05_01/05_01_01.ogg"
define voz_cap05_01_02 = "mod_assets/voices/05_01/05_01_02.ogg"
define voz_cap05_01_03 = "mod_assets/voices/05_01/05_01_03.ogg"
define voz_cap05_01_04 = "mod_assets/voices/05_01/05_01_04.ogg"
define voz_cap05_01_05 = "mod_assets/voices/05_01/05_01_05.ogg"
define voz_cap05_01_06 = "mod_assets/voices/05_01/05_01_06.ogg"
define voz_cap05_01_07 = "mod_assets/voices/05_01/05_01_07.ogg"
define voz_cap05_01_08 = "mod_assets/voices/05_01/05_01_08.ogg"
define voz_cap05_01_09 = "mod_assets/voices/05_01/05_01_09.ogg"
define voz_cap05_01_10 = "mod_assets/voices/05_01/05_01_10.ogg"
define voz_cap05_01_11 = "mod_assets/voices/05_01/05_01_11.ogg"
define voz_cap05_01_12 = "mod_assets/voices/05_01/05_01_12.ogg"
define voz_cap05_01_13 = "mod_assets/voices/05_01/05_01_13.ogg"
define voz_cap05_01_14 = "mod_assets/voices/05_01/05_01_14.ogg"
define voz_cap05_01_15 = "mod_assets/voices/05_01/05_01_15.ogg"
define voz_cap05_01_16 = "mod_assets/voices/05_01/05_01_16.ogg"
define voz_cap05_01_17 = "mod_assets/voices/05_01/05_01_17.ogg"
define voz_cap05_01_18 = "mod_assets/voices/05_01/05_01_18.ogg"
define voz_cap05_01_19 = "mod_assets/voices/05_01/05_01_19.ogg"
define voz_cap05_01_20 = "mod_assets/voices/05_01/05_01_20.ogg"
define voz_cap05_01_21 = "mod_assets/voices/05_01/05_01_21.ogg"
define voz_cap05_01_22 = "mod_assets/voices/05_01/05_01_22.ogg"
define voz_cap05_01_23 = "mod_assets/voices/05_01/05_01_23.ogg"



#05_02
define voz_cap05_02_001 = "mod_assets/voices/05_02/05_02_001.ogg"
define voz_cap05_02_002 = "mod_assets/voices/05_02/05_02_002.ogg"
define voz_cap05_02_003 = "mod_assets/voices/05_02/05_02_003.ogg"
define voz_cap05_02_004 = "mod_assets/voices/05_02/05_02_004.ogg"
define voz_cap05_02_005 = "mod_assets/voices/05_02/05_02_005.ogg"
define voz_cap05_02_006 = "mod_assets/voices/05_02/05_02_006.ogg"
define voz_cap05_02_007 = "mod_assets/voices/05_02/05_02_007.ogg"
define voz_cap05_02_008 = "mod_assets/voices/05_02/05_02_008.ogg"
define voz_cap05_02_009 = "mod_assets/voices/05_02/05_02_009.ogg"
define voz_cap05_02_010 = "mod_assets/voices/05_02/05_02_010.ogg"
define voz_cap05_02_011 = "mod_assets/voices/05_02/05_02_011.ogg"
define voz_cap05_02_012 = "mod_assets/voices/05_02/05_02_012.ogg"
define voz_cap05_02_013 = "mod_assets/voices/05_02/05_02_013.ogg"
define voz_cap05_02_014 = "mod_assets/voices/05_02/05_02_014.ogg"
define voz_cap05_02_015 = "mod_assets/voices/05_02/05_02_015.ogg"
define voz_cap05_02_016 = "mod_assets/voices/05_02/05_02_016.ogg"
define voz_cap05_02_017 = "mod_assets/voices/05_02/05_02_017.ogg"
define voz_cap05_02_018 = "mod_assets/voices/05_02/05_02_018.ogg"
define voz_cap05_02_019 = "mod_assets/voices/05_02/05_02_019.ogg"
define voz_cap05_02_020 = "mod_assets/voices/05_02/05_02_020.ogg"
define voz_cap05_02_021 = "mod_assets/voices/05_02/05_02_021.ogg"
define voz_cap05_02_022 = "mod_assets/voices/05_02/05_02_022.ogg"
define voz_cap05_02_023 = "mod_assets/voices/05_02/05_02_023.ogg"
define voz_cap05_02_024 = "mod_assets/voices/05_02/05_02_024.ogg"
define voz_cap05_02_025 = "mod_assets/voices/05_02/05_02_025.ogg"
define voz_cap05_02_026 = "mod_assets/voices/05_02/05_02_026.ogg"
define voz_cap05_02_027 = "mod_assets/voices/05_02/05_02_027.ogg"
define voz_cap05_02_028 = "mod_assets/voices/05_02/05_02_028.ogg"
define voz_cap05_02_029 = "mod_assets/voices/05_02/05_02_029.ogg"
define voz_cap05_02_030 = "mod_assets/voices/05_02/05_02_030.ogg"
define voz_cap05_02_031 = "mod_assets/voices/05_02/05_02_031.ogg"
define voz_cap05_02_032 = "mod_assets/voices/05_02/05_02_032.ogg"
define voz_cap05_02_033 = "mod_assets/voices/05_02/05_02_033.ogg"
define voz_cap05_02_034 = "mod_assets/voices/05_02/05_02_034.ogg"
define voz_cap05_02_035 = "mod_assets/voices/05_02/05_02_035.ogg"
define voz_cap05_02_036 = "mod_assets/voices/05_02/05_02_036.ogg"
define voz_cap05_02_037 = "mod_assets/voices/05_02/05_02_037.ogg"
define voz_cap05_02_038 = "mod_assets/voices/05_02/05_02_038.ogg"
define voz_cap05_02_039 = "mod_assets/voices/05_02/05_02_039.ogg"
define voz_cap05_02_040 = "mod_assets/voices/05_02/05_02_040.ogg"
define voz_cap05_02_041 = "mod_assets/voices/05_02/05_02_041.ogg"
define voz_cap05_02_042 = "mod_assets/voices/05_02/05_02_042.ogg"
define voz_cap05_02_043 = "mod_assets/voices/05_02/05_02_043.ogg"
define voz_cap05_02_044 = "mod_assets/voices/05_02/05_02_044.ogg"
define voz_cap05_02_045 = "mod_assets/voices/05_02/05_02_045.ogg"
define voz_cap05_02_046 = "mod_assets/voices/05_02/05_02_046.ogg"
define voz_cap05_02_047 = "mod_assets/voices/05_02/05_02_047.ogg"
define voz_cap05_02_048 = "mod_assets/voices/05_02/05_02_048.ogg"
define voz_cap05_02_049 = "mod_assets/voices/05_02/05_02_049.ogg"
define voz_cap05_02_050 = "mod_assets/voices/05_02/05_02_050.ogg"
define voz_cap05_02_051 = "mod_assets/voices/05_02/05_02_051.ogg"
define voz_cap05_02_052 = "mod_assets/voices/05_02/05_02_052.ogg"
define voz_cap05_02_053 = "mod_assets/voices/05_02/05_02_053.ogg"
define voz_cap05_02_054 = "mod_assets/voices/05_02/05_02_054.ogg"
define voz_cap05_02_055 = "mod_assets/voices/05_02/05_02_055.ogg"
define voz_cap05_02_056 = "mod_assets/voices/05_02/05_02_056.ogg"
define voz_cap05_02_057 = "mod_assets/voices/05_02/05_02_057.ogg"
define voz_cap05_02_058 = "mod_assets/voices/05_02/05_02_058.ogg"
define voz_cap05_02_059 = "mod_assets/voices/05_02/05_02_059.ogg"
define voz_cap05_02_060 = "mod_assets/voices/05_02/05_02_060.ogg"
define voz_cap05_02_061 = "mod_assets/voices/05_02/05_02_061.ogg"
define voz_cap05_02_062 = "mod_assets/voices/05_02/05_02_062.ogg"
define voz_cap05_02_063 = "mod_assets/voices/05_02/05_02_063.ogg"
define voz_cap05_02_064 = "mod_assets/voices/05_02/05_02_064.ogg"
define voz_cap05_02_065 = "mod_assets/voices/05_02/05_02_065.ogg"
define voz_cap05_02_066 = "mod_assets/voices/05_02/05_02_066.ogg"
define voz_cap05_02_067 = "mod_assets/voices/05_02/05_02_067.ogg"
define voz_cap05_02_068 = "mod_assets/voices/05_02/05_02_068.ogg"
define voz_cap05_02_069 = "mod_assets/voices/05_02/05_02_069.ogg"
define voz_cap05_02_070 = "mod_assets/voices/05_02/05_02_070.ogg"
define voz_cap05_02_071 = "mod_assets/voices/05_02/05_02_071.ogg"
define voz_cap05_02_072 = "mod_assets/voices/05_02/05_02_072.ogg"
define voz_cap05_02_073 = "mod_assets/voices/05_02/05_02_073.ogg"
define voz_cap05_02_074 = "mod_assets/voices/05_02/05_02_074.ogg"
define voz_cap05_02_075 = "mod_assets/voices/05_02/05_02_075.ogg"
define voz_cap05_02_076 = "mod_assets/voices/05_02/05_02_076.ogg"
define voz_cap05_02_077 = "mod_assets/voices/05_02/05_02_077.ogg"
define voz_cap05_02_078 = "mod_assets/voices/05_02/05_02_078.ogg"
define voz_cap05_02_079 = "mod_assets/voices/05_02/05_02_079.ogg"
define voz_cap05_02_080 = "mod_assets/voices/05_02/05_02_080.ogg"
define voz_cap05_02_081 = "mod_assets/voices/05_02/05_02_081.ogg"
define voz_cap05_02_082 = "mod_assets/voices/05_02/05_02_082.ogg"
define voz_cap05_02_083 = "mod_assets/voices/05_02/05_02_083.ogg"
define voz_cap05_02_084 = "mod_assets/voices/05_02/05_02_084.ogg"
define voz_cap05_02_085 = "mod_assets/voices/05_02/05_02_085.ogg"
define voz_cap05_02_086 = "mod_assets/voices/05_02/05_02_086.ogg"
define voz_cap05_02_087 = "mod_assets/voices/05_02/05_02_087.ogg"
define voz_cap05_02_088 = "mod_assets/voices/05_02/05_02_088.ogg"
define voz_cap05_02_089 = "mod_assets/voices/05_02/05_02_089.ogg"
define voz_cap05_02_090 = "mod_assets/voices/05_02/05_02_090.ogg"
define voz_cap05_02_091 = "mod_assets/voices/05_02/05_02_091.ogg"
define voz_cap05_02_092 = "mod_assets/voices/05_02/05_02_092.ogg"
define voz_cap05_02_093 = "mod_assets/voices/05_02/05_02_093.ogg"
define voz_cap05_02_094 = "mod_assets/voices/05_02/05_02_094.ogg"
define voz_cap05_02_095 = "mod_assets/voices/05_02/05_02_095.ogg"
define voz_cap05_02_096 = "mod_assets/voices/05_02/05_02_096.ogg"
define voz_cap05_02_097 = "mod_assets/voices/05_02/05_02_097.ogg"
define voz_cap05_02_098 = "mod_assets/voices/05_02/05_02_098.ogg"
define voz_cap05_02_099 = "mod_assets/voices/05_02/05_02_099.ogg"
define voz_cap05_02_100 = "mod_assets/voices/05_02/05_02_100.ogg"
define voz_cap05_02_101 = "mod_assets/voices/05_02/05_02_101.ogg"
define voz_cap05_02_102 = "mod_assets/voices/05_02/05_02_102.ogg"
define voz_cap05_02_103 = "mod_assets/voices/05_02/05_02_103.ogg"
define voz_cap05_02_104 = "mod_assets/voices/05_02/05_02_104.ogg"
define voz_cap05_02_105 = "mod_assets/voices/05_02/05_02_105.ogg"
define voz_cap05_02_106 = "mod_assets/voices/05_02/05_02_106.ogg"
define voz_cap05_02_107 = "mod_assets/voices/05_02/05_02_107.ogg"
define voz_cap05_02_108 = "mod_assets/voices/05_02/05_02_108.ogg"
define voz_cap05_02_109 = "mod_assets/voices/05_02/05_02_109.ogg"
define voz_cap05_02_110 = "mod_assets/voices/05_02/05_02_110.ogg"
define voz_cap05_02_111 = "mod_assets/voices/05_02/05_02_111.ogg"
define voz_cap05_02_112 = "mod_assets/voices/05_02/05_02_112.ogg"
define voz_cap05_02_113 = "mod_assets/voices/05_02/05_02_113.ogg"
define voz_cap05_02_114 = "mod_assets/voices/05_02/05_02_114.ogg"
define voz_cap05_02_115 = "mod_assets/voices/05_02/05_02_115.ogg"
define voz_cap05_02_116 = "mod_assets/voices/05_02/05_02_116.ogg"
define voz_cap05_02_117 = "mod_assets/voices/05_02/05_02_117.ogg"
define voz_cap05_02_118 = "mod_assets/voices/05_02/05_02_118.ogg"
define voz_cap05_02_119 = "mod_assets/voices/05_02/05_02_119.ogg"
define voz_cap05_02_120 = "mod_assets/voices/05_02/05_02_120.ogg"
define voz_cap05_02_121 = "mod_assets/voices/05_02/05_02_121.ogg"
define voz_cap05_02_122 = "mod_assets/voices/05_02/05_02_122.ogg"
define voz_cap05_02_123 = "mod_assets/voices/05_02/05_02_123.ogg"
define voz_cap05_02_124 = "mod_assets/voices/05_02/05_02_124.ogg"
define voz_cap05_02_125 = "mod_assets/voices/05_02/05_02_125.ogg"
define voz_cap05_02_126 = "mod_assets/voices/05_02/05_02_126.ogg"


#05_03
define voz_cap05_03_01 = "mod_assets/voices/05_03/05_03_01.ogg"
define voz_cap05_03_02 = "mod_assets/voices/05_03/05_03_02.ogg"
define voz_cap05_03_03 = "mod_assets/voices/05_03/05_03_03.ogg"
define voz_cap05_03_04 = "mod_assets/voices/05_03/05_03_04.ogg"
define voz_cap05_03_05 = "mod_assets/voices/05_03/05_03_05.ogg"
define voz_cap05_03_06 = "mod_assets/voices/05_03/05_03_06.ogg"
define voz_cap05_03_07 = "mod_assets/voices/05_03/05_03_07.ogg"
define voz_cap05_03_08 = "mod_assets/voices/05_03/05_03_08.ogg"
define voz_cap05_03_09 = "mod_assets/voices/05_03/05_03_09.ogg"
define voz_cap05_03_10 = "mod_assets/voices/05_03/05_03_10.ogg"
define voz_cap05_03_11 = "mod_assets/voices/05_03/05_03_11.ogg"
define voz_cap05_03_12 = "mod_assets/voices/05_03/05_03_12.ogg"
define voz_cap05_03_13 = "mod_assets/voices/05_03/05_03_13.ogg"
define voz_cap05_03_14 = "mod_assets/voices/05_03/05_03_14.ogg"
define voz_cap05_03_15 = "mod_assets/voices/05_03/05_03_15.ogg"
define voz_cap05_03_16 = "mod_assets/voices/05_03/05_03_16.ogg"
define voz_cap05_03_17 = "mod_assets/voices/05_03/05_03_17.ogg"
define voz_cap05_03_18 = "mod_assets/voices/05_03/05_03_18.ogg"

#Epilogo
define voz_epilogo_01 = "mod_assets/voices/epilogo/epilogo_01.ogg"
define voz_epilogo_02 = "mod_assets/voices/epilogo/epilogo_02.ogg"
define voz_epilogo_03 = "mod_assets/voices/epilogo/epilogo_03.ogg"
define voz_epilogo_04 = "mod_assets/voices/epilogo/epilogo_04.ogg"
define voz_epilogo_05 = "mod_assets/voices/epilogo/epilogo_05.ogg"
define voz_epilogo_06 = "mod_assets/voices/epilogo/epilogo_06.ogg"
define voz_epilogo_07 = "mod_assets/voices/epilogo/epilogo_07.ogg"
define voz_epilogo_08 = "mod_assets/voices/epilogo/epilogo_08.ogg"
define voz_epilogo_09 = "mod_assets/voices/epilogo/epilogo_09.ogg"
define voz_epilogo_10 = "mod_assets/voices/epilogo/epilogo_10.ogg"
define voz_epilogo_11 = "mod_assets/voices/epilogo/epilogo_11.ogg"
define voz_epilogo_12 = "mod_assets/voices/epilogo/epilogo_12.ogg"
define voz_epilogo_13 = "mod_assets/voices/epilogo/epilogo_13.ogg"
define voz_epilogo_14 = "mod_assets/voices/epilogo/epilogo_14.ogg"
define voz_epilogo_15 = "mod_assets/voices/epilogo/epilogo_15.ogg"
define voz_epilogo_16 = "mod_assets/voices/epilogo/epilogo_16.ogg"
define voz_epilogo_17 = "mod_assets/voices/epilogo/epilogo_17.ogg"
define voz_epilogo_18 = "mod_assets/voices/epilogo/epilogo_18.ogg"
define voz_epilogo_19 = "mod_assets/voices/epilogo/epilogo_19.ogg"
define voz_epilogo_20 = "mod_assets/voices/epilogo/epilogo_20.ogg"
define voz_epilogo_21 = "mod_assets/voices/epilogo/epilogo_21.ogg"
define voz_epilogo_22 = "mod_assets/voices/epilogo/epilogo_22.ogg"


#Capitulo XX
define voz_capXX_001 = "mod_assets/voices/capXX/capxx_001.ogg"
define voz_capXX_002 = "mod_assets/voices/capXX/capxx_002.ogg"
define voz_capXX_003 = "mod_assets/voices/capXX/capxx_003.ogg"
define voz_capXX_004 = "mod_assets/voices/capXX/capxx_004.ogg"
define voz_capXX_005 = "mod_assets/voices/capXX/capxx_005.ogg"
define voz_capXX_006 = "mod_assets/voices/capXX/capxx_006.ogg"
define voz_capXX_007 = "mod_assets/voices/capXX/capxx_007.ogg"
define voz_capXX_008 = "mod_assets/voices/capXX/capxx_008.ogg"
define voz_capXX_009 = "mod_assets/voices/capXX/capxx_009.ogg"
define voz_capXX_010 = "mod_assets/voices/capXX/capxx_010.ogg"
define voz_capXX_011 = "mod_assets/voices/capXX/capxx_011.ogg"
define voz_capXX_012 = "mod_assets/voices/capXX/capxx_012.ogg"
define voz_capXX_013 = "mod_assets/voices/capXX/capxx_013.ogg"
define voz_capXX_014 = "mod_assets/voices/capXX/capxx_014.ogg"
define voz_capXX_015 = "mod_assets/voices/capXX/capxx_015.ogg"
define voz_capXX_016 = "mod_assets/voices/capXX/capxx_016.ogg"
define voz_capXX_017 = "mod_assets/voices/capXX/capxx_017.ogg"
define voz_capXX_018 = "mod_assets/voices/capXX/capxx_018.ogg"
define voz_capXX_019 = "mod_assets/voices/capXX/capxx_019.ogg"
define voz_capXX_020 = "mod_assets/voices/capXX/capxx_020.ogg"
define voz_capXX_021 = "mod_assets/voices/capXX/capxx_021.ogg"
define voz_capXX_022 = "mod_assets/voices/capXX/capxx_022.ogg"
define voz_capXX_023 = "mod_assets/voices/capXX/capxx_023.ogg"


###################Audios

define audio.menu_start = "mod_assets/sounds/menu_start.ogg"
define audio.ctc = "mod_assets/sounds/ctc.ogg"
define audio.footsteps = "mod_assets/sounds/footsteps.ogg"
define audio.celular = "<loop 0.00>mod_assets/sounds/celular.ogg"
define audio.fm_back = "mod_assets/sounds/back.ogg"
define audio.fm_error = "mod_assets/sounds/error.ogg"
define audio.fm_arrow_select = "mod_assets/sounds/arrow_select.ogg"
define audio.oco = "mod_assets/sounds/oco.ogg"
define audio.millenniumitem = "mod_assets/sounds/millenniumitem.ogg"
define audio.phone_click = "mod_assets/sounds/phone_click.ogg"
define audio.phone_end_call = "mod_assets/sounds/phone_end_call.ogg"
define audio.radio_chatter = "<loop 0.00>mod_assets/sounds/radio_chatter.ogg"
define audio.car_crash = "<loop 0.00>mod_assets/sounds/car_crash.ogg"
define audio.door_bell = "<loop 0.00>mod_assets/sounds/door_bell.ogg"
define audio.chaves_punch = "<loop 0.00>mod_assets/sounds/chaves_punch.ogg"
define audio.punch01 = "<loop 0.00>mod_assets/sounds/punch01.ogg"
define audio.door_slam = "<loop 0.00>mod_assets/sounds/door_slam.ogg"
define audio.toaster_ding = "<loop 0.00>mod_assets/sounds/toaster_ding.ogg"
define audio.plates_dropping = "<loop 0.00>mod_assets/sounds/plates_dropping.ogg"
define audio.door_kick = "<loop 0.00>mod_assets/sounds/door_kick.ogg"
define audio.gun_shots = "<loop 0.00>mod_assets/sounds/gun_shots.ogg"
define audio.gun_cocking = "<loop 0.00>mod_assets/sounds/gun_cocking.ogg"
define audio.door_creaking = "<loop 0.00>mod_assets/sounds/door_creaking.ogg"
define audio.voices = "<loop 0.00>mod_assets/sounds/voices.ogg"
define audio.handcuffs = "<loop 0.00>mod_assets/sounds/handcuffs.ogg"
define audio.running_footsteps = "<loop 0.00>mod_assets/sounds/running_footsteps.ogg"
define audio.bell = "<loop 0.00>mod_assets/sounds/bell.ogg"
define audio.energy_source = "<loop 0.00>mod_assets/sounds/energy_source.ogg"
define audio.running_window_breaking = "<loop 0.00>mod_assets/sounds/running_window_breaking.ogg"
define audio.city_02 = "<loop 0.00>mod_assets/sounds/city_02.ogg"
define audio.heresy = "<loop 0.00>mod_assets/sounds/heresy.ogg"
define audio.floor_slam = "<loop 0.00>mod_assets/sounds/floor_slam.ogg"
define audio.black_hole = "<loop 0.00>mod_assets/sounds/black_hole.ogg"
define audio.park = "<loop 0.00>mod_assets/sounds/park.ogg"
define audio.spray = "<loop 0.00>mod_assets/sounds/spray.ogg"
define audio.kabuki = "<loop 0.00>mod_assets/sounds/kabuki.ogg"
define audio.kick_alemao = "<loop 0.00>mod_assets/sounds/kick_alemao.ogg"
define audio.table_rolling = "<loop 0.00>mod_assets/sounds/table_rolling.ogg"
define audio.carrinho = "<loop 0.00>mod_assets/sounds/carrinho.ogg"
define audio.slam = "<loop 0.00>mod_assets/sounds/slam.ogg"
define audio.church_bell = "<loop 0.00>mod_assets/sounds/church_bell.ogg"
define audio.hospital = "<loop 0.00>mod_assets/sounds/hospital.ogg"
define audio.airplane = "<loop 0.00>mod_assets/sounds/airplane.ogg"
define audio.running_breaking_glasses = "<loop 0.00>mod_assets/sounds/running_breaking_glasses.ogg"
define audio.police_background = "<loop 0.00>mod_assets/sounds/police_background.ogg"

#define audio.confirm = "mod_assets/sounds/confirm.ogg"

############################################################################################################
############################################################################################################

#Discord Rich Presence
#ALTERAR FORBIDDEN MEMORIES G
init python:
    import time
    import drpc
    global drpc_details
    global drpc_state
    client_id = '960873947803549776' 
    start_time = int(time.time())
    large_text = 'Forbidden Memories G'
    large_image = 'fmg_logo'

    chapters_head = {
        "menu": "Menu Principal",
        "intro": "Introdução",
        "cap01": "Capítulo 1",
        "cap02-1": "Capítulo 2",
        "cap02-2": "Capítulo 2",
        "cap03-1": "Capítulo 3",
        "cap03-2": "Capítulo 3",
        "cap04-1": "Capítulo 4",
        "cap04-2": "Capítulo 4",
        "cap05": "Capítulo 5",
        "finalG": "Final G",
        "epilogo": "Final G - Epílogo",
        "creditos": "Créditos",
        "capXX": "Capítulo Extra",
        "guinodia": "Guinódia, O Proibido",
        "finalA": "Final A",
        "finalB": "Final B",
        "finalC": "Final C",
        "finalD": "Final D",
        "finalE": "Final E",
        "finalF": "Final F",
        "finalH": "Final H",
        "finalI": "Final I",
        "finalJ": "Final J",
        "finalK": "Final K",
        "finalL": "Final L",
        "finalM": "Final M",
        "finalN": "Final N",
        "finalO": "Final O",
        "finalP": "Final P",
        "finalQ": "Final Q",
        "finalR": "Final R",
        "finalS": "Final S",
        "finalT": "Final T",
        "finalU": "Final U",
        "finalV": "Final V",
        "finalW": "Final W",
        "finalX": "Final X",
        "finalY": "Final Y",
        "finalZ": "Final Z",
        "aparencias": "As aparencias enganam."
    }

    chapters_details = {
        "menu": "Explorando o Menu",
        "intro": "Desvendando o Códex G",
        "cap01": "Pelada do James",
        "cap02-1": "Alexandre Senna Gringo",
        "cap02-2": "Roda de Amigos",
        "cap03-1": "Alexandre Senna no Hospital",
        "cap03-2": "Exame do Senna",
        "cap04-1": "Alexandre Senna e Yeah Man",
        "cap04-2": "Cadê o Arrombamento?",
        "cap05": "Teste do Senna",
        "finalG": "As Crônicas de Alexandre Senna",
        "epilogo": "As Crônicas de Alexandre Senna",
        "creditos": "Criado por Operation Senna",
        "capXX": "Clube de Literatura",
        "guinodia": "Invocando Guinódia",
        "finalA": "Melancolia do Toque de Celular Irritante",
        "finalB": "Sem Tempo Para Brincadeiras",
        "finalC": "Você É Real Mesmo?",
        "finalD": "Assassino G",
        "finalE": "Extinção Humana",
        "finalF": "Policial de Família",
        "finalH": "Os Carros São Como As Lanchas",
        "finalI": "Tele Senna",
        "finalJ": "Recordista do Guinnass Book",
        "finalK": "Nunca Abra A Porta Para Estranhos",
        "finalL": "Hétero com G",
        "finalM": "Contra-Trote Mortal",
        "finalN": "Tratamento de Choque",
        "finalO": "O Acidente de Cupiqueno",
        "finalP": "Dois Dias Na Fila, Um Ano Na Rua",
        "finalQ": "Só os Skates Sabem",
        "finalR": "Sádico e Calculista",
        "finalS": "Gosto Buocólico",
        "finalT": "Viagem para Pau Grande",
        "finalU": "Teoria do Kenoverso",
        "finalV": "Watashi wa Arekusando desu",
        "finalW": "Casamento-Surpresa",
        "finalX": "El Gángster de Familia",
        "finalY": "Árabe de Família",
        "finalZ": "As Aparências Enganam",
        "aparencias": "??????"
    }

    try: 
        if(not renpy.variant("touch")):
            drpc = drpc.DiscordIpcClient.for_platform(client_id)
    except:
        #Discord's IPC wasn't found
        pass

    def drpc_update(capitulo):
        if(renpy.variant("touch")):
            return

        drcp_infos = drcp_info(capitulo)

        drpc_state = drcp_infos[0]
        drpc_details = drcp_infos[1]
        
        try: drpc.set_activity({
            "state": drpc_state,
            "details": drpc_details,
            "timestamps": {
                "start": start_time
            },
            "assets": {
                #"small_text": small_text,
                #"small_image": small_text,
                "large_text": large_text,
                "large_image": large_image }
            })
        except:
            # rip
            pass
        return

    def drcp_info(capitulo):

        global current_chapter
        current_chapter = capitulo

        #print("drcp",current_chapter)

        return chapters_head[capitulo],chapters_details[capitulo]

# Hashwatch

image hashwatch_img:
    Solid("#b26")
    size (25,25) subpixel True
    function hashwatch
    pause 1.0
    repeat

init python:
    import hashlib
    import shutil
    import time
    import singleton
    import os


#Music
#The Music section is where you can reference existing DDLC audio

define audio.t3 = "<loop 4.618>mod_assets/music/ddlc_3.ogg"   #Main theme (in-game)

# UI

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/3.png", (0, 0), "mod_assets/characters/yuri/e2.png")

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
#define narrator = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='{fi=50-0.3-50}',what_suffix='{/fi}')
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.guinodia_active = False

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default kd_name = "King Dice"
default crs_name = "Kurisu"
default iy_name = "Insane Yuri"
default may_name = "Mayuri"
default lucas_name = "Luka"
default nya_name = "Faris"
default daru_name = "Daru"
default pedro_name = "Pedro Bial"
default supervisor_name = "Supervisor"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None
