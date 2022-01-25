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
    #config.keymap['game_menu'].remove('mouseup_3')
    #config.keymap['hide_windows'].append('mouseup_3')
    #config.rollback_enabled = False
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['game_menu'] = ['K_ESCAPE']
    renpy.music.register_channel("music_poem", mixer="music", tight=True)

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


        

    
    

############################################################################################################
############################################################################################################
#######Assets Forbidden Memories G

#Variaveis
define input_operation_senna = ""
define flag_input_operation_senna = False
define hash_operation_senna = "DA05114A91FFC80DE0C2E579754AF46FCFEA573041BD4C885B6A7FD44BC3E43DE825B8F6D7C20F812C2E43E3D0B1C5B6B119BC1691E3287F737F195868B9DBB0"


define endings_names = {
    "A":"Melancolia do Toque de Celular Irritante",
    "B":"Sem Tempo Para Brincadeiras",
    "C":"Você É Real Mesmo?",
    "D":"Assassino G",
    "E":"Extinção Humana",
    "F":"Policial de Família",
    "G":"As Crônicas de Alexandre Senna",
    "H":"Teste",
    "I":"Teste",
    "J":"Teste",
    "K":"Teste",
    "L":"Teste",
    "M":"Teste",
    "N":"Teste",
    "O":"Teste",
    "P":"Teste",
    "Q":"Teste",
    "R":"Teste",
    "S":"Teste",
    "T":"Teste",
    "U":"Teste",
    "V":"Teste",
    "W":"Teste",
    "X":"Teste",
    "Y":"Árabe de Família",
    "Z":"As Aparências Enganam"
}

define endings_descriptions = {
    "A":"Perdeu seu jogo de futebol e o celular para ir jogar Palavras-Cruzadas.",
    "B":"Virou o melhor goleiro de Cupiqueno e foi escalado para a Seleção.",
    "C":"Questionou sua existência na Metrix e perdeu o Campeonato G.",
    "D":"Transformou Índio em um monstro e perdeu o Campeonato G.",
    "E":"Causou a destruição da Terra e perdeu o Campeonato G.",
    "F":"Foi aprovado na Polícia Militar de Cupiqueno.",
    "G":"Desvendou todo o Códex G.",
    "H":"Teste",
    "I":"Teste",
    "J":"Teste",
    "K":"Teste",
    "L":"Teste",
    "M":"Teste",
    "N":"Teste",
    "O":"Teste",
    "P":"Teste",
    "Q":"Teste",
    "R":"Teste",
    "S":"Teste",
    "T":"Teste",
    "U":"Teste",
    "V":"Teste",
    "W":"Teste",
    "X":"Teste",
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

#Transform
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

#Personagens
define narrator = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='',what_suffix='')
define narrator_arabe = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='',what_suffix='',what_style="arabe_style")
define seto = DynamicCharacter('seto', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image seto 1a = "mod_assets/characters/seto/1a.png"
image seto 1b = "mod_assets/characters/seto/1b.png"

image senna 1a = "mod_assets/characters/senna/1a.png"

image guina 1a = "mod_assets/characters/guina/1a.png"

image yuri 3xd = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xd.png")
image yuri 3xe = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xe.png")


#Imagens
image testeee = "mod_assets/images/teste.png"
image logo01 = "mod_assets/images/logo01.png"
image game_over_bg = "mod_assets/images/GameOver.png"
image options_menu_bg = "mod_assets/images/OptionsMenu.png"
image textbox_black = "mod_assets/gui/textbox_black.png"

image textbox_aux:
    "mod_assets/gui/textbox2.png"
    xalign 0.5
    yalign 1.0

image seto_s = "mod_assets/characters/side/seto_s.png"
image yuri_s1 = "mod_assets/characters/side/yuri_s1.png"
image yuri_s2 = "mod_assets/characters/side/yuri_s2.png"
image guina_s = "mod_assets/characters/side/guina_s.png"
image senna_s1 = "mod_assets/characters/side/senna_s1.png"

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

#Musicas 
define audio.nao_venha_me_dizer = "<loop 0.0>mod_assets/music/nao_venha_me_dizer.ogg"
define audio.guina_piscineiro = "<loop 0.0>mod_assets/music/paulo_guina_piscineiro.ogg"
define audio.senna_theme = "<loop 0.0>mod_assets/music/senna_theme.ogg"


define audio.fm_nameinput = "<loop 9.00>mod_assets/music/fm_nameinput.ogg"
define audio.fm_intro = "mod_assets/music/fm_intro.ogg"
define audio.fm_preliminary_faceoff = "<loop 1.333>mod_assets/music/fm_preliminary_faceoff.ogg"
define audio.fm_plazatown = "<loop 26.033>mod_assets/music/fm_plazatown.ogg"
define audio.fm_gameover = "mod_assets/music/fm_gameover.ogg"
define audio.m_converting_minds = "mod_assets/music/m_converting_minds.ogg"
define audio.fm_freeduel = "<loop 0.933>mod_assets/music/fm_freeduel.ogg"
define audio.fm_deck = "<loop 0.60>mod_assets/music/fm_deck.ogg"
define audio.fm_password = "<loop 1.833>mod_assets/music/fm_password.ogg"
define audio.fm_library = "<loop 0.70>mod_assets/music/fm_library.ogg"

#Vozes
define voz_teste = "mod_assets/voices/teste.ogg"
define voz_jailson_arabe = "mod_assets/voices/jailson_arabe.ogg"
define voz_guina_arabe = "mod_assets/voices/guina_arabe.ogg"

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

#Audios
define audio.menu_start = "mod_assets/sounds/menu_start.ogg"
define audio.ctc = "mod_assets/sounds/ctc.ogg"
define audio.footsteps = "mod_assets/sounds/footsteps.ogg"
define audio.celular = "<loop 0.00>mod_assets/sounds/celular.ogg"
define audio.fm_back = "mod_assets/sounds/back.ogg"
define audio.fm_error = "mod_assets/sounds/error.ogg"
define audio.fm_arrow_select = "mod_assets/sounds/arrow_select.ogg"
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
    client_id = '466702541732839462' 
    start_time = int(time.time())
    large_text = 'Você acredita em tudo o que vê?'
    large_image = 'ymel_large'
    try: drpc = drpc.DiscordIpcClient.for_platform(client_id)
    except:
        # Discord's IPC wasn't found
        pass

    def drpc_update():
        drpc_details = persistent.current_chapter_head
        drpc_state = persistent.current_chapter_title
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
