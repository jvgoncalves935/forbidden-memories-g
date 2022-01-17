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

        

    
    

############################################################################################################
############################################################################################################
#######Assets Forbidden Memories G

#Variaveis
define input_operation_senna = ""
define flag_input_operation_senna = False
define hash_operation_senna = "DA05114A91FFC80DE0C2E579754AF46FCFEA573041BD4C885B6A7FD44BC3E43DE825B8F6D7C20F812C2E43E3D0B1C5B6B119BC1691E3287F737F195868B9DBB0"

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
define seto = DynamicCharacter('seto', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image seto 1a = "mod_assets/characters/seto/1a.png"
image seto 1b = "mod_assets/characters/seto/1b.png"

image senna 1a = "mod_assets/characters/senna/1a.png"

image guina 1a = "mod_assets/characters/guina/1a.png"

image yuri 3xd = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xd.png")
image yuri 3xe = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xe.png")


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

image corredor_ddlc = "mod_assets/images/capXX/corridor.png"
image escadas_ddlc = "mod_assets/images/capXX/stairs.png"

#Musicas 
define audio.fm_nameinput = "<loop 9.00>mod_assets/music/fm_nameinput.ogg"
define audio.fm_intro = "mod_assets/music/fm_intro.ogg"
define audio.fm_preliminary_faceoff = "<loop 1.333>mod_assets/music/fm_preliminary_faceoff.ogg"
define audio.fm_plazatown = "<loop 26.033>mod_assets/music/fm_plazatown.ogg"
define audio.fm_gameover = "mod_assets/music/fm_gameover.ogg"
define audio.m_converting_minds = "mod_assets/music/m_converting_minds.ogg"
define audio.fm_freeduel = "<loop 0.933>mod_assets/music/fm_freeduel.ogg"
define audio.fm_deck = "<loop 0.60>mod_assets/music/fm_deck.ogg"
define audio.fm_password = "<loop 1.833>mod_assets/music/fm_password.ogg"

#Vozes
define voz_teste = "mod_assets/voices/teste.ogg"

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

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

# UI

#-endings
###############################################################
# Vertices
# -
# Maiden
image Maiden_Vertice:
    "mod_assets/bg/endings/Maiden/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Maiden/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Maiden/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/Maiden/Vertice_frame_2.png"
    0.1
    repeat

image Maiden_Vertice_a = Composite(
    (202, 48),
    (-11, -6), "Maiden_Vertice",
    (0, 0), "mod_assets/bg/endings/Maiden/The Maiden Mystery_hovered.png")

image Maiden_Vertice_s = Composite(
    (202, 48),
    (-11, -6), "mod_assets/bg/endings/Maiden/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Maiden/The Maiden Mystery.png")

# Prologue
image Prologue_Vertice:
    "mod_assets/bg/endings/Prologue/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Prologue/Vertice_frame_2.png"
    0.3
    "mod_assets/bg/endings/Prologue/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/Prologue/Vertice_frame_2.png"
    0.1
    repeat

image Prologue_Vertice_a = Composite(
    (183, 50),
    (-9, -8), "Prologue_Vertice",
    (0, 0), "mod_assets/bg/endings/Prologue/The Bad Prologue_hovered.png")

image Prologue_Vertice_s = Composite(
    (183, 50),
    (-9, -8), "mod_assets/bg/endings/Prologue/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Prologue/The Bad Prologue.png")

# Awake
image Awake_Vertice:
    "mod_assets/bg/endings/Awake/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Awake/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Awake/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/Awake/Vertice_frame_2.png"
    0.3
    repeat

image Awake_Vertice_a = Composite(
    (219, 51),
    (-7, -10), "Awake_Vertice",
    (0, 0), "mod_assets/bg/endings/Awake/The Awful Awakening_hovered.png")

image Awake_Vertice_s = Composite(
    (219, 51),
    (-7, -10), "mod_assets/bg/endings/Awake/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Awake/The Awful Awakening.png")

# World
image World_Vertice:
    "mod_assets/bg/endings/World/Vertice_frame_1.png"
    0.3
    "mod_assets/bg/endings/World/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/World/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/World/Vertice_frame_2.png"
    0.1
    repeat

image World_Vertice_a = Composite(
    (124, 39),
    (-12, -11), "World_Vertice",
    (0, 0), "mod_assets/bg/endings/World/Yuri's World_hovered.png")

image World_Vertice_s = Composite(
    (124, 39),
    (-12, -11), "mod_assets/bg/endings/World/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/World/Yuri's World.png")

# X1
image X1_Vertice:
    "mod_assets/bg/endings/X1/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/X1/Vertice_frame_2.png"
    0.3
    "mod_assets/bg/endings/X1/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/X1/Vertice_frame_2.png"
    0.1
    repeat

image X1_Vertice_a = Composite(
    (42, 48),
    (-15, -18), "X1_Vertice",
    (0, 0), "mod_assets/bg/endings/X1/x_hovered.png")

image X1_Vertice_s = Composite(
    (42, 48),
    (-15, -18), "mod_assets/bg/endings/X1/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/X1/x.png")

# X2
image X2_Vertice:
    "mod_assets/bg/endings/X2/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/X2/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/X2/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/X2/Vertice_frame_2.png"
    0.3
    repeat

image X2_Vertice_a = Composite(
    (42, 55),
    (-14, -10), "X2_Vertice",
    (0, 0), "mod_assets/bg/endings/X2/x_hovered.png")

image X2_Vertice_s = Composite(
    (42, 55),
    (-14, -10), "mod_assets/bg/endings/X2/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/X2/x.png")

# X3
image X3_Vertice:
    "mod_assets/bg/endings/X3/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/X3/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/X3/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/X3/Vertice_frame_2.png"
    0.1
    repeat

image X3_Vertice_a = Composite(
    (37, 41),
    (-13, -14), "X3_Vertice",
    (0, 0), "mod_assets/bg/endings/X3/x_hovered.png")

image X3_Vertice_s = Composite(
    (37, 41),
    (-13, -14), "mod_assets/bg/endings/X3/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/X3/x.png")

# X4
image X4_Vertice:
    "mod_assets/bg/endings/X4/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/X4/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/X4/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/X4/Vertice_frame_2.png"
    0.1
    repeat

image X4_Vertice_a = Composite(
    (41, 47),
    (-17, -12), "X4_Vertice",
    (0, 0), "mod_assets/bg/endings/X4/x_hovered.png")

image X4_Vertice_s = Composite(
    (41, 47),
    (-17, -12), "mod_assets/bg/endings/X4/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/X4/x.png")

# X5
image X5_Vertice:
    "mod_assets/bg/endings/X5/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/X5/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/X5/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/X5/Vertice_frame_2.png"
    0.1
    repeat

image X5_Vertice_a = Composite(
    (47, 52),
    (-13, -12), "X5_Vertice",
    (0, 0), "mod_assets/bg/endings/X5/x_hovered.png")

image X5_Vertice_s = Composite(
    (47, 52),
    (-13, -12), "mod_assets/bg/endings/X5/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/X5/x.png")

# Violation
image Violation_Vertice:
    "mod_assets/bg/endings/Violation/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Violation/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Violation/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/Violation/Vertice_frame_2.png"
    0.1
    repeat

image Violation_Vertice_a = Composite(
    (195, 37),
    (-8, -14), "Violation_Vertice",
    (0, 0), "mod_assets/bg/endings/Violation/The Vile Violation_hovered.png")

image Violation_Vertice_s = Composite(
    (195, 37),
    (-8, -14), "mod_assets/bg/endings/Violation/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Violation/The Vile Violation.png")

# Visions
image Visions_Vertice:
    "mod_assets/bg/endings/Visions/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Visions/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Visions/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/Visions/Vertice_frame_2.png"
    0.1
    repeat

image Visions_Vertice_a = Composite(
    (223, 37),
    (-6, -15), "Visions_Vertice",
    (0, 0), "mod_assets/bg/endings/Visions/The Vivacious Visions_hovered.png")

image Visions_Vertice_s = Composite(
    (223, 37),
    (-6, -15), "mod_assets/bg/endings/Visions/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Visions/The Vivacious Visions.png")

# Gordian
image Gordian_Vertice:
    "mod_assets/bg/endings/Gordian/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Gordian/Vertice_frame_2.png"
    0.3
    "mod_assets/bg/endings/Gordian/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/Gordian/Vertice_frame_2.png"
    0.1
    repeat

image Gordian_Vertice_a = Composite(
    (134, 39),
    (-10, -11), "Gordian_Vertice",
    (0, 0), "mod_assets/bg/endings/Gordian/Gordian Knot_hovered.png")

image Gordian_Vertice_s = Composite(
    (134, 39),
    (-10, -11), "mod_assets/bg/endings/Gordian/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Gordian/Gordian Knot.png")

# Decision
image Decision_Vertice:
    "mod_assets/bg/endings/Decision/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Decision/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Decision/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/Decision/Vertice_frame_2.png"
    0.1
    repeat

image Decision_Vertice_a = Composite(
    (241, 37),
    (-9, -9), "Decision_Vertice",
    (0, 0), "mod_assets/bg/endings/Decision/The Disastrous Decision_hovered.png")

image Decision_Vertice_s = Composite(
    (241, 37),
    (-9, -9), "mod_assets/bg/endings/Decision/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Decision/The Disastrous Decision.png")

# Sunset
image Sunset_Vertice:
    "mod_assets/bg/endings/Sunset/Vertice_frame_1.png"
    0.1
    "mod_assets/bg/endings/Sunset/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Sunset/Vertice_frame_3.png"
    0.3
    "mod_assets/bg/endings/Sunset/Vertice_frame_2.png"
    0.1
    repeat

image Sunset_Vertice_a = Composite(
    (204, 39),
    (-12, -11), "Sunset_Vertice",
    (0, 0), "mod_assets/bg/endings/Sunset/The Crimson Sunset_hovered.png")

image Sunset_Vertice_s = Composite(
    (204, 39),
    (-12, -11), "mod_assets/bg/endings/Sunset/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Sunset/The Crimson Sunset.png")

# Manipulator
image Manipulator_Vertice:
    "mod_assets/bg/endings/Manipulator/Vertice_frame_1.png"
    0.3
    "mod_assets/bg/endings/Manipulator/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Manipulator/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/Manipulator/Vertice_frame_2.png"
    0.1
    repeat

image Manipulator_Vertice_a = Composite(
    (223, 50),
    (-12, -18), "Manipulator_Vertice",
    (0, 0), "mod_assets/bg/endings/Manipulator/The Mild Manipulator_hovered.png")

image Manipulator_Vertice_s = Composite(
    (223, 50),
    (-12, -18), "mod_assets/bg/endings/Manipulator/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Manipulator/The Mild Manipulator.png")

# Guardian
image Guardian_Vertice:
    "mod_assets/bg/endings/Guardian/Vertice_frame_1.png"
    0.3
    "mod_assets/bg/endings/Guardian/Vertice_frame_2.png"
    0.1
    "mod_assets/bg/endings/Guardian/Vertice_frame_3.png"
    0.1
    "mod_assets/bg/endings/Guardian/Vertice_frame_2.png"
    0.1
    repeat

image Guardian_Vertice_a = Composite(
    (193, 39),
    (-12, -11), "Guardian_Vertice",
    (0, 0), "mod_assets/bg/endings/Guardian/The Gate Guardian_hovered.png")

image Guardian_Vertice_s = Composite(
    (193, 39),
    (-12, -11), "mod_assets/bg/endings/Guardian/Vertice_frame_1.png",
    (0, 0), "mod_assets/bg/endings/Guardian/The Gate Guardian.png")

image Guardian_X1:
    xpos 244
    ypos 633
    "mod_assets/bg/endings/Guardian/x/x1.png"

image Guardian_X2:
    "mod_assets/bg/endings/Guardian/x/x2.png"
    xpos 270
    ypos 632

image Guardian_X3:
    xpos 297
    ypos 632
    "mod_assets/bg/endings/Guardian/x/x3.png"

image Guardian_X4:
    xpos 323
    ypos 633
    "mod_assets/bg/endings/Guardian/x/x4.png"

image Guardian_X5:
    xpos 348
    ypos 631
    "mod_assets/bg/endings/Guardian/x/x5.png"

###############################################################
# Arestas
image Prologue_Aresta:
    xpos 301
    ypos 56
    "mod_assets/bg/endings/Prologue/Aresta_frame_1_Maiden.png"
    #0.1
    #"mod_assets/bg/endings/Prologue/Aresta_frame_2_Maiden.png"
    #0.1
    #"mod_assets/bg/endings/Prologue/Aresta_frame_3_Maiden.png"
    #0.1
    #"mod_assets/bg/endings/Prologue/Aresta_frame_2_Maiden.png"
    #0.1
    #repeat

image Awake_Aresta:
    xpos 335
    ypos 123
    "mod_assets/bg/endings/Awake/Aresta_frame_1_Prologue.png"
    #0.1
    #"mod_assets/bg/endings/Awake/Aresta_frame_2_Prologue.png"
    #0.1
    #"mod_assets/bg/endings/Awake/Aresta_frame_3_Prologue.png"
    #0.1
    #"mod_assets/bg/endings/Awake/Aresta_frame_2_Prologue.png"
    #0.1
    #repeat

image World_Aresta:
    xpos 331
    ypos 206
    "mod_assets/bg/endings/World/Aresta_frame_1_Awake.png"
    #0.1
    #"mod_assets/bg/endings/World/Aresta_frame_2_Awake.png"
    #0.1
    #"mod_assets/bg/endings/World/Aresta_frame_3_Awake.png"
    #0.1
    #"mod_assets/bg/endings/World/Aresta_frame_2_Awake.png"
    #0.1
    #repeat

image X1_Aresta:
    xpos 165
    ypos 266
    "mod_assets/bg/endings/X1/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/X1/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/X1/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/X1/Aresta_frame_2_World.png"
    #0.1
    #repeat

image X2_Aresta:
    xpos 93
    ypos 167
    "mod_assets/bg/endings/X2/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/X2/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/X2/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/X2/Aresta_frame_2_World.png"
    #0.1
    #repeat

image X3_Aresta:
    xpos 446
    ypos 132
    "mod_assets/bg/endings/X3/Aresta_frame_1_Awake.png"
    #0.1
    #"mod_assets/bg/endings/X3/Aresta_frame_2_Awake.png"
    #0.1
    #"mod_assets/bg/endings/X3/Aresta_frame_3_Awake.png"
    #0.1
    #"mod_assets/bg/endings/X3/Aresta_frame_2_Awake.png"
    #0.1
    #repeat

image X4_Aresta:
    xpos 395
    ypos 240
    "mod_assets/bg/endings/X4/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/X4/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/X4/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/X4/Aresta_frame_2_World.png"
    #0.1
    #repeat

image X5_Aresta:
    xpos 432
    ypos 30
    "mod_assets/bg/endings/X5/Aresta_Maiden.png"
    #repeat

image Violation_Aresta:
    xpos 390
    ypos 291
    "mod_assets/bg/endings/Violation/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/Violation/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/Violation/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/Violation/Aresta_frame_2_World.png"
    #0.1
    #repeat

image Visions_Aresta:
    xpos 227
    ypos 286
    "mod_assets/bg/endings/Visions/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/Visions/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/Visions/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/Visions/Aresta_frame_2_World.png"
    #0.1
    #repeat

image Gordian_Aresta:
    xpos 316
    ypos 293
    "mod_assets/bg/endings/Gordian/Aresta_frame_1_World.png"
    #0.1
    #"mod_assets/bg/endings/Gordian/Aresta_frame_2_World.png"
    #0.1
    #"mod_assets/bg/endings/Gordian/Aresta_frame_3_World.png"
    #0.1
    #"mod_assets/bg/endings/Gordian/Aresta_frame_2_World.png"
    #0.1
    #repeat

image Decision_Aresta:
    xpos 393
    ypos 438
    "mod_assets/bg/endings/Decision/Aresta_frame_1_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Decision/Aresta_frame_2_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Decision/Aresta_frame_3_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Decision/Aresta_frame_2_Gordian.png"
    #0.1
    #repeat

image Sunset_Aresta_Gordian:
    xpos 339
    ypos 447
    "mod_assets/bg/endings/Sunset/Aresta_frame_1_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_2_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_3_Gordian.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_2_Gordian.png"
    #0.1
    #repeat

image Sunset_Aresta_X4:
    xpos 562
    ypos 248
    "mod_assets/bg/endings/Sunset/Aresta_frame_1_X4.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_2_X4.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_3_X4.png"
    #0.1
    #"mod_assets/bg/endings/Sunset/Aresta_frame_2_X4.png"
    #0.1
    #repeat

image Manipulator_Aresta:
    xpos 186
    ypos 437
    "mod_assets/bg/endings/Manipulator/Aresta_frame_1_Gordian.png"
    ##0.1
    ##"mod_assets/bg/endings/Manipulator/Aresta_frame_2_Gordian.png"
    ##0.1
    ##"mod_assets/bg/endings/Manipulator/Aresta_frame_3_Gordian.png"
    ##0.1
    ##"mod_assets/bg/endings/Manipulator/Aresta_frame_2_Gordian.png"
    ##0.1
    ##repeat

image Guardian_Aresta_Decision:
    xpos 437
    ypos 508
    "mod_assets/bg/endings/Guardian/Aresta_frame_1_Decision.png"
    ##0.1
    ##"mod_assets/bg/endings/Guardian/Aresta_frame_2_Decision.png"
    ##0.1
    ##"mod_assets/bg/endings/Guardian/Aresta_frame_3_Decision.png"
    ##0.1
    ##"mod_assets/bg/endings/Guardian/Aresta_frame_2_Decision.png"
    ##0.1
    ##repeat

image Guardian_Aresta_Manipulator:
    xpos 202
    ypos 600
    "mod_assets/bg/endings/Guardian/Aresta_frame_1_Manipulator.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Manipulator.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_3_Manipulator.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Manipulator.png"
    #0.1
    #repeat

image Guardian_Aresta_Sunset:
    xpos 375
    ypos 606
    "mod_assets/bg/endings/Guardian/Aresta_frame_1_Sunset.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Sunset.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_3_Sunset.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Sunset.png"
    #0.1
    #repeat

image Guardian_Aresta_Violation:
    xpos 438
    ypos 361
    "mod_assets/bg/endings/Guardian/Aresta_frame_1_Violation.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Violation.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_3_Violation.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Violation.png"
    #0.1
    #repeat

image Guardian_Aresta_Visions:
    xpos 17
    ypos 367
    "mod_assets/bg/endings/Guardian/Aresta_frame_1_Visions.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Visions.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_3_Visions.png"
    #0.1
    #"mod_assets/bg/endings/Guardian/Aresta_frame_2_Visions.png"
    #0.1
    #repeat

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

###### Definições do Yuri's Melancholy ######
#Audios
define audio.insector_sun = "<loop 0.00>mod_assets/ost/insector_sun.ogg"
define audio.vassoura = "<loop 0.00>mod_assets/ost/vassoura.ogg"
define audio.suspence01 = "<loop 0.00>mod_assets/ost/its_you_its_me.ogg"
define audio.suspence02 = "<loop 0.00>mod_assets/ost/soe.ogg"
define audio.happy = "<loop 0.00>mod_assets/ost/happy.ogg"
define audio.null_exception = "<loop 0.00>mod_assets/sound/exception.ogg"
define creditos_sam_20dB = "mod_assets/sound/creditos_sam_20dB.ogg"

#Backgrounds
image bg psycho_club = "mod_assets/bg/psycho_club.png"
image bg happy_club = "mod_assets/bg/happy_club.png"
image bg lab = "mod_assets/bg/lab.png"
image bg bonoro = "mod_assets/bg/bonoro.png"
image bg bonoro2 = "mod_assets/bg/bonoro2.png"
image bg eyes00 = "mod_assets/bg/eyes/eyes00.png"
image bg eyes01 = "mod_assets/bg/eyes/eyes01.png"
image bg eyes02 = "mod_assets/bg/eyes/eyes02.png"
image bg eyes03 = "mod_assets/bg/eyes/eyes03.png"
image bg eyes04 = "mod_assets/bg/eyes/eyes04.png"
image bg eyes05 = "mod_assets/bg/eyes/eyes05.png"
image bg eyes06 = "mod_assets/bg/eyes/eyes06.png"
image nego_bam movie = Movie(play="mod_assets/bg/nego_bam.webm")
#image nego_bam movie = Movie(play="mod_assets/bg/nego_bam.webm", mask="mod_assets/bg/nego_bam.webm")

#Monika
image monika 6 = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/3c.png")

#Melancholic Yuri
image yuri 1xa = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/1l.png", (0, 0), "mod_assets/characters/yuri/1r.png", (0, 0), "mod_assets/characters/yuri/xa.png")
image yuri 2xa = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/2l.png", (0, 0), "mod_assets/characters/yuri/2r.png", (0, 0), "mod_assets/characters/yuri/xa.png")
image yuri my1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri my1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri my1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri my1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri my1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri my1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri my1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri my1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri my1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri my1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri my1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri my1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri my1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri my1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri my1o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri my1p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri my1q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri my1r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri my1s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri my1t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri my1u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri my1v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri my1w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/w.png")
image yuri my1xa = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/xa.png")
image yuri my1xb = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/xb.png")
image yuri my1xc = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/xc.png")
image yuri my1xd = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/xd.png")
image yuri my2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri my2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri my2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri my2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri my2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri my2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri my2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri my2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri my2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri my2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri my2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri my2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri my2m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri my2n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri my2o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri my2p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri my2q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri my2r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri my2s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri my2t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri my2u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri my2v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri my2w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/w.png")
image yuri my2xa = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/xa.png")
image yuri my2xb = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/xb.png")
image yuri my2xc = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri/xc.png")
image yuri my3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/a.png")
image yuri my3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/b.png")
image yuri my3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/c.png")
image yuri my3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/d.png")
image yuri my3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/e.png")
image yuri my3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/f.png")
image yuri my3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/g.png")
image yuri my3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/h.png")
image yuri my3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/i.png")
image yuri my3j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/j.png")
image yuri my3k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/k.png")
image yuri my3l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/l.png")
image yuri my3m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/m.png")
image yuri my3n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/n.png")
image yuri my3o = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/o.png")
image yuri my3p = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/p.png")
image yuri my3q = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/q.png")
image yuri my3r = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/r.png")
image yuri my3s = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/s.png")
image yuri my3t = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/t.png")
image yuri my3u = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/u.png")
image yuri my3v = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/v.png")
image yuri my3w = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/w.png")
image yuri my3xa = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/xa.png")
image yuri my3xb = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/xb.png")
image yuri my3xc = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/xc.png")
image yuri my4a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my4.png", (0, 0), "mod_assets/characters/yuri/a2.png")
image yuri my4b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my4.png", (0, 0), "mod_assets/characters/yuri/b2.png")
image yuri my4c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my4.png", (0, 0), "mod_assets/characters/yuri/c2.png")
image yuri my4d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my4.png", (0, 0), "mod_assets/characters/yuri/d2.png")
image yuri my4e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my4.png", (0, 0), "mod_assets/characters/yuri/e2.png")

image yuri esp01 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/esp01.png")
image yuri esp02 = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri/esp02.png")


#Insane Yuri

image yuri_y iy1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y iy1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y iy1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y iy1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y iy1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y iy1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y iy1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y iy1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y iy1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y iy1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y iy1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y iy1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y iy1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y iy1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")
image yuri_y iy2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y iy2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y iy2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y iy2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y iy2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y iy2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y iy2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y iy2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y iy2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y iy2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y iy2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y iy2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y iy2m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y iy2n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my2.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")
image yuri_y iy3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y iy3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y iy3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y iy3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y iy3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y iy3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y iy3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y iy3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y iy3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y iy3j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y iy3k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y iy3l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y iy3m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y iy3n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my3.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")
image yuri_y 1ya = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y 1yb = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y 1yc = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y 1yd = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y 1ye = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y 1yf = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y 1yg = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y 1yh = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y 1yi = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y 1yj = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y 1yk = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y 1yl = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y 1ym = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y 1yn = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/1l.png", (0, 0), "mod_assets/characters/yuri_y/1r.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")
image yuri_y 2ya = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y 2yb = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y 2yc = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y 2yd = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y 2ye = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y 2yf = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y 2yg = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y 2yh = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y 2yi = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y 2yj = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y 2yk = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y 2yl = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y 2ym = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y 2yn = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/2l.png", (0, 0), "mod_assets/characters/yuri_y/2r.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")

image yuri_y fake1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri_y fakemy1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri/my1.png", (0, 0), "mod_assets/characters/yuri/a.png")

image yuri_y vio1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/ya.png")
image yuri_y vio1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yb.png")
image yuri_y vio1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yc.png")
image yuri_y vio1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yd.png")
image yuri_y vio1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/ye.png")
image yuri_y vio1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yf.png")
image yuri_y vio1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yg.png")
image yuri_y vio1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yh.png")
image yuri_y vio1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yi.png")
image yuri_y vio1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yj.png")
image yuri_y vio1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yk.png")
image yuri_y vio1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yl.png")
image yuri_y vio1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/ym.png")
image yuri_y vio1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/yuri_y/vio1.png", (0, 0), "mod_assets/characters/yuri_y/yn.png")

#Kurisu
image kurisu 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/b.png")
image kurisu 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/c.png")
image kurisu 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/d.png")
image kurisu 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/e.png")
image kurisu 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/f.png")
image kurisu 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/g.png")
image kurisu 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/h.png")
image kurisu 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/i.png")
image kurisu 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/j.png")
image kurisu 1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/k.png")
image kurisu 1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/l.png")
image kurisu 1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/m.png")
image kurisu 1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/n.png")
image kurisu 1o = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1a.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/o.png")

image kurisu 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/a.png")
image kurisu 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/b.png")
image kurisu 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/c.png")
image kurisu 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/d.png")
image kurisu 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/e.png")
image kurisu 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/f.png")
image kurisu 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/g.png")
image kurisu 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/h.png")
image kurisu 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/i.png")
image kurisu 2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/j.png")
image kurisu 2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/k.png")
image kurisu 2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/l.png")
image kurisu 2m = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/m.png")
image kurisu 2n = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/n.png")
image kurisu 2o = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASA/1b.png", (0, 0), "mod_assets/characters/cris/CRS_ASA/o.png")

image kurisu 3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/a.png")
image kurisu 3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/b.png")
image kurisu 3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/c.png")
image kurisu 3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/d.png")
image kurisu 3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/e.png")
image kurisu 3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/f.png")
image kurisu 3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/g.png")
image kurisu 3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/h.png")
image kurisu 3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/i.png")
image kurisu 3j = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/j.png")
image kurisu 3k = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/k.png")
image kurisu 3l = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/l.png")
image kurisu 3m = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/m.png")
image kurisu 3n = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/n.png")
image kurisu 3o = im.Composite((960, 960), (0, 0), "mod_assets/characters/cris/CRS_ASC/1c.png", (0, 0), "mod_assets/characters/cris/CRS_ASC/o.png")

#Faris
image nya 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/a.png")
image nya 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/b.png")
image nya 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/c.png")
image nya 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/d.png")
image nya 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/e.png")
image nya 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/f.png")
image nya 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/g.png")
image nya 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSA/1a.png", (0, 0), "mod_assets/characters/feiris/FEI_DSA/h.png")

image nya 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/a.png")
image nya 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/b.png")
image nya 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/c.png")
image nya 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/d.png")
image nya 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/e.png")
image nya 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/f.png")
image nya 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/g.png")
image nya 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSB/1b.png", (0, 0), "mod_assets/characters/feiris/FEI_DSB/h.png")

image nya 3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/a.png")
image nya 3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/b.png")
image nya 3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/c.png")
image nya 3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/d.png")
image nya 3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/e.png")
image nya 3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/f.png")
image nya 3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/g.png")
image nya 3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/h.png")
image nya 3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/i.png")
image nya 3j = im.Composite((960, 960), (0, 0), "mod_assets/characters/feiris/FEI_DSC/1c.png", (0, 0), "mod_assets/characters/feiris/FEI_DSC/j.png")

#Mayuri
image mayuri 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/a.png")
image mayuri 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/b.png")
image mayuri 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/c.png")
image mayuri 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/d.png")
image mayuri 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/e.png")
image mayuri 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/f.png")
image mayuri 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/g.png")
image mayuri 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/h.png")
image mayuri 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/i.png")
image mayuri 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASA/1a.png", (0, 0), "mod_assets/characters/may/MAY_ASA/j.png")

image mayuri 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/a.png")
image mayuri 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/b.png")
image mayuri 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/c.png")
image mayuri 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/d.png")
image mayuri 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/e.png")
image mayuri 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/f.png")
image mayuri 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/g.png")
image mayuri 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/h.png")
image mayuri 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASB/1b.png", (0, 0), "mod_assets/characters/may/MAY_ASB/i.png")

image mayuri 3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/a.png")
image mayuri 3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/b.png")
image mayuri 3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/c.png")
image mayuri 3d = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/d.png")
image mayuri 3e = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/e.png")
image mayuri 3f = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/f.png")
image mayuri 3g = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/g.png")
image mayuri 3h = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/h.png")
image mayuri 3i = im.Composite((960, 960), (0, 0), "mod_assets/characters/may/MAY_ASC/1c.png", (0, 0), "mod_assets/characters/may/MAY_ASC/i.png")

#Luka
image lucas 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/a.png")
image lucas 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/b.png")
image lucas 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/c.png")
image lucas 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/d.png")
image lucas 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/e.png")
image lucas 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/f.png")
image lucas 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/g.png")
image lucas 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/h.png")
image lucas 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/i.png")
image lucas 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/j.png")
image lucas 1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/k.png")
image lucas 1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/l.png")
image lucas 1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSA/1a.png", (0, 0), "mod_assets/characters/luka/RUK_CSA/m.png")

image lucas 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/a.png")
image lucas 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/b.png")
image lucas 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/c.png")
image lucas 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/d.png")
image lucas 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/e.png")
image lucas 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/f.png")
image lucas 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/g.png")
image lucas 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/h.png")
image lucas 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/i.png")
image lucas 2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/luka/RUK_CSB/1b.png", (0, 0), "mod_assets/characters/luka/RUK_CSB/j.png")

#Daru
image daru 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/a.png")
image daru 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/b.png")
image daru 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/c.png")
image daru 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/d.png")
image daru 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/e.png")
image daru 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/f.png")
image daru 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/g.png")
image daru 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/h.png")
image daru 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/i.png")
image daru 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/j.png")
image daru 1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/k.png")
image daru 1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1a.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/l.png")

image daru 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/a.png")
image daru 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/b.png")
image daru 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/c.png")
image daru 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/d.png")
image daru 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/e.png")
image daru 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/f.png")
image daru 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/g.png")
image daru 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/h.png")
image daru 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/i.png")
image daru 2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/j.png")
image daru 2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/k.png")
image daru 2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/daru/DAR_ASB/1b.png", (0, 0), "mod_assets/characters/daru/DAR_ASB/l.png")

#King Dice
image king_dice 1a = "mod_assets/characters/king_dice/1a.png"
image king_dice 1b = "mod_assets/characters/king_dice/1b.png"
image king_dice 1c = "mod_assets/characters/king_dice/1c.png"

#Pedro Bial
image pedro 1a = "mod_assets/characters/king_dice/1a.png"

#Supervisor
image supervisor 1a = "mod_assets/characters/supervisor/1a.png"

#Sayori
image sayori happy1 = "mod_assets/characters/sayori/s_kill.png"
image sayori happy2 = "mod_assets/characters/sayori/s_kill2.png"

#MC
#mc art character by Sir French Fries and Childish-N, xd
image main_c 1a = "mod_assets/characters/main_c/1a.png"
image main_c 1a = "mod_assets/characters/main_c/2a.png"
image main_c 1b = "mod_assets/characters/main_c/2b.png"
image main_c 1c = "mod_assets/characters/main_c/2c.png"
image main_c 1d = "mod_assets/characters/main_c/2d.png"
image main_c 1e = "mod_assets/characters/main_c/2e.png"
image main_c 1f = "mod_assets/characters/main_c/2f.png"
image main_c 1g = "mod_assets/characters/main_c/2g.png"
image main_c 1h = "mod_assets/characters/main_c/2h.png"
image main_c 1i = "mod_assets/characters/main_c/2i.png"
image main_c 1j = "mod_assets/characters/main_c/2j.png"
image main_c 1k = "mod_assets/characters/main_c/2k.png"
######                                 ######

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
#define narrator = Character(ctc="ctc", ctc_position="fixed", voice_tag="narrator",what_prefix='{fi=50-0.3-50}',what_suffix='{/fi}')
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kd = DynamicCharacter('kd_name', image='king_dice', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nya = DynamicCharacter('nya_name', image='nya', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kurisu = DynamicCharacter('crs_name', image='kurisu', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define iy = DynamicCharacter('iy_name', image='yuri_y', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define may = DynamicCharacter('may_name', image='mayuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define lucas = DynamicCharacter('lucas_name', image='lucas', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define daru = DynamicCharacter('daru_name', image='daru', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define pedro = DynamicCharacter('pedro_name', image='pedro', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define supervisor = DynamicCharacter('supervisor_name', image='pedro', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

#$ kd = "King Dice"
#$ crs = "Kurisu"
#$ iy = "Insane Yuri"
#$ may = "Mayuri"
#$ lucas = "Luka"
#$ daru = "Daru"

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
