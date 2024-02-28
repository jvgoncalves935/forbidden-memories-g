﻿
## Initialization
################################################################################

init offset = -1

#Forbidden Memories G
transform change_transform(old,new):
    contains:
        old
        alpha 1.0
        linear 0.5 alpha 0.0
    contains:
        new
        alpha 0.0
        linear 0.5 alpha 1.0

################################################################################
## Styles
################################################################################

style default:
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    size gui.text_size
    color gui.text_color
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style arabe_style:
    font "mod_assets/gui/fonts/calibri.ttf"
    size 22
    color gui.text_color
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    line_overlap_split 1
    line_spacing 1
    padding gui.frame_borders.padding
    ypos 120
    xpos 50

style font_creditos_menu:
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    size 16
    color gui.text_color
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style font_creditos_menu_2:
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    size 30
    color "#020202"
    outlines [(2, "#0F0F0F", 2, 2),(1, "#1A1A1A", 2, 2)]
    line_overlap_split 1
    line_spacing 1

style escolha:
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    size gui.text_size
    color gui.text_color
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    line_overlap_split 1
    line_spacing 1
    background "#000000"

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


#style bar:
#    ysize gui.bar_size
#    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

#style vscrollbar:
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"
        vbox:
            key "K_ESCAPE" action [If(current_label != "game_over" and not persistent.config_arabe,ShowMenu("save"),NullAction())]

        vbox:
            xalign 0.96
            yalign 0.96
            
            textbutton _("OPEN BETA 0.1.7 (WIP)"):
                style "page_label_text"
                text_size 12
    
    if renpy.variant("touch") and not persistent.config_arabe:
        vbox:
            xalign 0.0
            yalign 0.0
            
            imagebutton:
                idle "gui/button/android_exit_button.png"
                action [ShowMenu("save")]
                activate_sound gui.activate_sound
                


    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("mod_assets/gui/textbox2.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.96 yalign 0.94 xoffset -5 alpha 1.0 subpixel True
    block:
        "mod_assets/gui/ctc/ctc1.png"
        linear 0.2 alpha 1.0
        "mod_assets/gui/ctc/ctc2.png"
        linear 0.2 alpha 1.0
        "mod_assets/gui/ctc/ctc3.png"
        linear 0.2 alpha 1.0
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid("#070e5c")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

            text prompt style "input_prompt"
            input id "input"
        
            


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    vbox:
        key "K_ESCAPE" action [If(current_label != "game_over" and not persistent.config_arabe,ShowMenu("save"),NullAction())]

    vbox:
        xalign 0.96
        yalign 0.98
        
        textbutton _("OPEN BETA 0.1.7 (WIP)"):
            style "page_label_text"
            text_size 12
    
    if renpy.variant("touch") and not persistent.config_arabe:
        vbox:
            xalign 0.0
            yalign 0.0
            
            imagebutton:
                idle "gui/button/android_exit_button.png"
                action [ShowMenu("save")]
                activate_sound gui.activate_sound


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action
    
    timer 1.0/30.0 repeat True action Function(RigMouse)


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 570
    yanchor 0.5

    spacing 0

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    #font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    #size 22
    color gui.text_color
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    #xalign -2.0

## Simple choice grid ###############################################################
##

screen choicegrid(items):
    style_prefix "choicegrid"

    vpgrid:
        cols 4
        spacing 40
        xalign 0.1
        yalign 0.8
        xsize 500

        for i in items:
            textbutton i.caption action i.action text_size 22

## Text Timer  #######################################################################
##

style texttimer_ok:
    size 72
    color "#FFF"
    italic True
    #kerning -5
    font "gui/fonts/PT_Sans-Web-Regular.ttf"
    outlines [(2, "#000", 0, 0)]

style texttimer_near:
    size 72
    color "#F22"
    italic True
    font "gui/fonts/PT_Sans-Web-Regular.ttf"
    outlines [(2, "#000", 0, 0)]


screen texttimer(**kwargs):

    vbox:
        add DynamicDisplayable(timercountdown, **kwargs)

        textbutton "Parar cronômetro":
            action [Function(renpy.hide_screen, 'texttimer'), Call(kwargs.get('done_label', 'done_label'))]


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = False

#style quick_button is default
#style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init python:
    def FinishEnterName():
        #if not player: return
        #persistent.playername = player
        #renpy.hide_screen("name_input")
        if(not persistent.config_arabe):
            renpy.jump_out_of_context("start")
        else:
            renpy.jump_out_of_context("cap_arabe")

    def FinishEnterNameCapXY():
        renpy.jump_out_of_context("capXY")

    def FinishEnterNameCapYeahMan():
        renpy.jump_out_of_context("capYM")

    def FinishEnterNameCapSenna():
        renpy.jump_out_of_context("capSN")

    def FinishEnterNameCapJailson():
        renpy.jump_out_of_context("capJA")

    def FinishEnterNameChurrasco():
        renpy.jump_out_of_context("churrasco")

    def FinishEnterNameOnlyMen():
        renpy.jump_out_of_context("onlymen")

    def FinishEnterNameBadBoy():
        renpy.jump_out_of_context("badboy")

    def FinishEnterNameError242424():
        renpy.jump_out_of_context("label_error242424_begin")
    
    def FinishStandingHereIRealize():
        renpy.jump_out_of_context("standing_here_i_realize")



screen navigation():

    #vbox:
    #    style_prefix "navigation"

    #    xalign 0.5
    #    yalign 0.5

    #    spacing 20

    if main_menu:
        if persistent.playthrough == 1:
            textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Por favor digite seu nome", ok_action=Function(FinishEnterName)))
        else:
            vbox:
                xalign 0.5
                yalign 0.18
                imagebutton:
                    idle "mod_assets/gui/menu/menu_new_game_idle.png"
                    hover "mod_assets/gui/menu/menu_new_game_selected.png"
                    action [Function(FinishEnterName)]
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound

    else:

        textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

        textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

    if main_menu:
        
        vbox:
            xalign 0.5
            yalign 0.31
            imagebutton:
                idle "mod_assets/gui/menu/menu_load_game_idle.png"
                hover "mod_assets/gui/menu/menu_load_game_selected.png"
                action [If(not persistent.config_arabe,ShowMenu("load"),NullAction()),
                        SensitiveIf(renpy.get_screen("load") == None and not persistent.config_arabe),
                        If(not persistent.config_arabe,Hide("game_menu"),NullAction()),
                        If(not persistent.config_arabe,Play("music",audio.fm_deck),NullAction())]
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

        vbox:
            xalign 0.96
            yalign 0.96
            
            textbutton _("OPEN BETA 0.1.7 (WIP)"):
                style "page_label_text"
                text_size 12

    if _in_replay:

        textbutton _("End Replay") action EndReplay(confirm=True)

    elif not main_menu:
        if persistent.is_yuri_self_aware == True:
            textbutton _("Main Menu") action Show(screen="dialog", message="Isso não é necessário!\nEstou cuidando de tudo!", ok_action=Hide("dialog"))
        else:
            textbutton _("Main Menu") action MainMenu()
    vbox:
        xalign 0.5
        yalign 0.44
        imagebutton: 
            idle "mod_assets/gui/menu/menu_options_idle.png"
            hover "mod_assets/gui/menu/menu_options_selected.png"
            action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None),Play("music", audio.fm_password)]
            hover_sound gui.hover_sound
            activate_sound gui.activate_sound

    #textbutton _("Créditos") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

    if main_menu:
        vbox:
            xalign 0.5
            yalign 0.57
            imagebutton:
                idle "mod_assets/gui/menu/menu_endings_idle.png"
                hover "mod_assets/gui/menu/menu_endings_selected.png"
                action [ShowMenu("endings"), SensitiveIf(renpy.get_screen("endings") == None), Play("music", audio.fm_library),Function(guinodia_init),Function(init_music_channel_stopped)]
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

        vbox:
            xalign 0.5
            yalign 0.70
            
            imagebutton:
                idle "mod_assets/gui/menu/menu_credits_idle.png"
                hover "mod_assets/gui/menu/menu_credits_selected.png"
                action [ShowMenu("creditos"), SensitiveIf(renpy.get_screen("creditos") == None), Play("music", audio.fm_freeduel)]
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            
    
    #textbutton _("About") action ShowMenu("about")

    if renpy.variant("pc"):

        ## Help isn't necessary or relevant to mobile devices.
        #textbutton _("Help") action Help("README.html")

        ## The quit button is banned on iOS and unnecessary on Android.
        vbox:
            xalign 0.5
            yalign 0.83
            imagebutton:
                idle "mod_assets/gui/menu/menu_quit_idle.png"
                hover "mod_assets/gui/menu/menu_quit_selected.png"
                action Quit(confirm=not main_menu)
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

style navigation_button is gui_button
style navigation_button_2 is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    xalign 0.5
    yalign 0.5

style navigation_button_2:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound audio.fm_error
    xalign 0.5
    yalign 0.5

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(2, "#070e5c", 5, 5), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]
    xalign 0.5
    yalign 0.5

style navigation_button_text_endings:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    size 18
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(2, "#070e5c", 5, 5), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]
    xalign 0.5
    yalign 0.5

style navigation_button_text_endings_2:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    size 12
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(2, "#070e5c", 5, 5), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]
    xalign 0.5
    yalign 0.5
    


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

#Just add Monika art now!
    
    #   if persistent.ghost_menu:
    #      add "white"
    #     add "menu_art_y_ghost"
    #    add "menu_art_n_ghost"
    #    else:
    add "menu_bg" alpha 0.5
        #add "menu_art_y"
        #add "menu_art_n"
    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:

    #    vbox:
    #        text "[config.name!t]":
    #            style "main_menu_title"

    #        text "[config.version]":
    #            style "main_menu_version"

#    if not persistent.ghost_menu:
#    add "menu_particles"
#    add "menu_particles"
#    add "menu_particles"
    add "menu_logo"
#    if persistent.ghost_menu:
#        add "menu_art_s_ghost"
#        add "menu_art_m_ghost"
#    else:
#        if persistent.playthrough == 1 or persistent.playthrough == 2:
#            add "menu_art_s_glitch"
#        else:
#            add "menu_art_s"
#    add "menu_particles"
#        if persistent.playthrough != 4:
    #add "menu_art_m"
    #add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

#style main_menu_frame:
#    xsize 310
#    yfill True
#
#    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):
    # Add the backgrounds.
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        hbox:

            # Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_2 is navigation_button_2
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

#    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style return_button_2:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    #use game_menu(_("About"), scroll="viewport"):

    style_prefix "about"

    vbox:

        label "[config.name!t]"
        text _("Version [config.version!t]\n")

        ## gui.about is usually set in options.rpy.
        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Endings screen #######################################################
##
screen side_menuart:
    add "menu_art"

screen side_img_right(img,ending):
    vbox:
        xalign 0.87
        yalign 0.275
        
        add "mod_assets/images/deck/" + img:
            zoom 0.78

    vbox:
        xalign 0.94
        yalign 0.96

        textbutton _("\""+endings_names[ending]+"\""):
            style "page_label_text"
            text_size 16

        textbutton _(endings_descriptions[ending]):
            style "page_label_text"
            text_size 10
    
    


screen side_img_left(img,card):

    vbox:
        xalign 0.105
        yalign 0.275
        
        add "mod_assets/images/deck/" + img:
            zoom 0.78

    vbox:
        xalign 0.92
        yalign 0.945

        textbutton _("\""+deck_g_names[card]+"\""):
            style "page_label_text"
            text_size 16



screen side_img_right_2(img,card):
    #Pagina 2 cartas 
    vbox:
        xalign 0.87
        yalign 0.275
        
        add "mod_assets/images/deck/" + img:
            zoom 0.78

    vbox:
        xalign 0.92
        yalign 0.945

        textbutton _("\""+deck_g_names[card]+"\""):
            style "page_label_text"
            text_size 16
    


screen side_img_left_video(img,card,video):

    vbox:
        xalign 0.105
        yalign 0.275
        
        add "mod_assets/images/deck/" + img:
            zoom 0.78
    
    vbox:
        xalign 0.145
        yalign 0.33

        add video:
            zoom 0.78

    vbox:
        xalign 0.94
        yalign 0.945

        textbutton _("\""+deck_g_names[card]+"\""):
            style "page_label_text"
            text_size 16
    #$ guinodia(guinodia_toggle,guinodia_pos)

    #on "show" action Play("sound", "audio/se/SE_シスてム_タイとル_ルーぷ.wav")
    #on "hide" action Stop("sound", fadeout=1.0)

screen default_menu_aux():

    tag menu

    style_prefix "default_menu_aux"

    add "menu_bg"

    textbutton _("Return"):
        xalign 0.05
        ypos 0.95
        style "return_button"
        action [Return(), Hide("side_menuart")]

screen operation_senna_scr():
    tag menu

    style_prefix "operation_senna_scr"

    add "black"
    
    textbutton _(glitchtext(renpy.random.randint(12,50))):
        xalign 0.5
        yalign 0.5
        style "return_button"
        action [Show(screen="name_input", message=glitchtext(renpy.random.randint(12,50)), ok_action=Function(set_input_operation_senna))]

    hbox:
        align (0.10,1.015)
        textbutton _("Voltar?"):
            style "return_button_2"
            text_style "navigation_button_text"
            action [NullAction()]

screen converting_minds_scr():
    tag menu

    style_prefix "converting_minds_scr"

    add "black"

    if(is_all_endings_unlocked()):
        textbutton _("?v=pXFuqH4AXTU"):
            xalign 0.5
            yalign 0.5
            
            action [NullAction()]
            text_style "font_creditos_menu_2"
    else:
        textbutton _("??????????????"):
            xalign 0.5
            yalign 0.5
            
            action [NullAction()]
            text_style "font_creditos_menu_2"


    textbutton _("Voltar?"):
        xalign 0.05
        ypos 0.975
        style "return_button_2"
        text_style "navigation_button_text"
        action [NullAction()]

screen guinodia_scr():
    add "guinodia_movie"
    timer 60 action Function(renpy.quit)
    key "dismiss" action [[]]

#screen texttimer(**kwargs):
#    vbox:
#        add DynamicDisplayable(timercountdown, **kwargs)


screen endings():

    tag menu

    add "mod_assets/images/EndingsMenu.png"
    
    textbutton _("Finais (Deck G)"):
        xalign 0.5
        yalign 0.005
        style "page_label_text"
        text_size 28

    if(is_all_endings_locked()):
        textbutton _("Nenhum final desbloqueado."):
            xalign 0.5
            yalign 0.5
            style "page_label_text"
            text_size 22

    if(persistent.endings["A"]):
        vbox:
            xalign 0.09
            yalign 0.11
            textbutton _("Final A"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="alexandre_senna.png",ending="A"),Function(reset_jumpscare_senna,False,2)]
                unhovered [Hide("side_img_right"),Function(reset_jumpscare_senna,False,0)]
                action [Function(jumpscare_senna_count,False,0)]

    if(persistent.endings["B"]):
        vbox:
            xalign 0.09
            yalign 0.16
            textbutton _("Final B"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="goleiro_de_familia.png",ending="B"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["C"]):
        vbox:
            xalign 0.09
            yalign 0.21
            textbutton _("Final C"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="james_matarazzo.png",ending="C"),Function(sfx_carta,audio.james_matarazzo_01,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]
    
    if(persistent.endings["D"]):
        vbox:
            xalign 0.09
            yalign 0.26
            textbutton _("Final D"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="indio.png",ending="D"),Function(sfx_carta,audio.indio01,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["E"]):
        vbox:
            xalign 0.09
            yalign 0.31
            textbutton _("Final E"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="vaimeti.png",ending="E"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]
    
    if(persistent.endings["F"]):
        vbox:
            xalign 0.09
            yalign 0.36
            textbutton _("Final F"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="alexandre_senna_policial.png",ending="F"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["G"]):
        vbox:
            xalign 0.09
            yalign 0.41
            textbutton _("Final G"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="jailson_mendes.png",ending="G"),Function(sfx_carta,audio.jailson_ainn,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["H"]):
        vbox:
            xalign 0.09
            yalign 0.46
            textbutton _("Final H"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="os_carros.png",ending="H"),Function(sfx_carta,audio.os_carros_sao,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["I"]):
        vbox:
            xalign 0.09
            yalign 0.51
            textbutton _("Final I"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="tele_senna.png",ending="I"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [Function(FinishEnterNameOnlyMen)]

    if(persistent.endings["J"]):
        vbox:
            xalign 0.09
            yalign 0.56
            textbutton _("Final J"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="guinnass_book.png",ending="J"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["K"]):
        vbox:
            xalign 0.09
            yalign 0.61
            textbutton _("Final K"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="yeah_man_bandido.png",ending="K"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["L"]):
        vbox:
            xalign 0.09
            yalign 0.66
            textbutton _("Final L"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="posso_imaginar.png",ending="L"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["M"]):
        vbox:
            xalign 0.09
            yalign 0.71
            textbutton _("Final M"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="alexandre_senna_carrasco.png",ending="M"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]
    

    if(persistent.endings["N"]):
        vbox:
            xalign 0.29
            yalign 0.11
            textbutton _("Final N"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="doutoras_hospital.png",ending="N"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["O"]):
        vbox:
            xalign 0.29
            yalign 0.16
            textbutton _("Final O"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="hetero.png",ending="O"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["P"]):
        vbox:
            xalign 0.29
            yalign 0.21
            textbutton _("Final P"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="doutora.png",ending="P"),Function(sfx_carta,audio.doutora02,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["Q"]):
        vbox:
            xalign 0.29
            yalign 0.26
            textbutton _("Final Q"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="chorao.png",ending="Q"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["R"]):
        vbox:
            xalign 0.29
            yalign 0.31
            textbutton _("Final R"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="yeah_man.png",ending="R"),Function(sfx_carta,audio.yeahman_02,False,0)]
                unhovered [Hide("side_img_right")]
                action [Function(FinishEnterNameCapYeahMan)]

    if(persistent.endings["S"]):
        vbox:
            xalign 0.29
            yalign 0.36
            textbutton _("Final S"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="mangueira_evil.png",ending="S"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["T"]):
        vbox:
            xalign 0.29
            yalign 0.41
            textbutton _("Final T"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="kid_bengala.png",ending="T"),Function(sfx_carta,audio.kid_bengala2,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["U"]):
        vbox:
            xalign 0.29
            yalign 0.46
            textbutton _("Final U"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="paulo_gino_professor.png",ending="U"),Function(sfx_carta,audio.gino_professor,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["V"]):
        vbox:
            xalign 0.29
            yalign 0.51
            textbutton _("Final V"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="harpica.png",ending="V"),Function(guinodia,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["W"]):
        vbox:
            xalign 0.29
            yalign 0.56
            textbutton _("Final W"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="princesa_demacol.png",ending="W"),Function(sfx_carta,audio.princesa_demacol2,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]
    
    if(persistent.endings["X"]):
        vbox:
            xalign 0.29
            yalign 0.61
            textbutton _("Final X"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="bob.png",ending="X"),Function(sfx_carta,voz_cap05_02_032,False,0)]
                unhovered [Hide("side_img_right")]
                action [NullAction()]

    if(persistent.endings["Y"]):
        vbox:
            xalign 0.29
            yalign 0.66
            textbutton _("Final Y"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="paulo_gino_arabe.png",ending="Y"),Function(sfx_carta,voz_gino_arabe,False,0)]
                unhovered [Hide("side_img_right")]
                action [Function(FinishEnterNameCapJailson)]

    if(persistent.endings["Z"]):
        vbox:
            xalign 0.29
            yalign 0.71
            textbutton _("Final Z"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings"
                hovered [ShowTransient("side_img_right", img="darkilson.png",ending="Z"),Function(sfx_carta,audio.vcs_broxaram,False,1),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_right"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [NullAction()]


















    if(persistent.endings["A"]):
        vbox:
            xalign 0.66
            yalign 0.09
            textbutton _("Carta 27"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="minha_mulher.png",card=27),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["B"]):
        vbox:
            xalign 0.795
            yalign 0.09
            textbutton _("Carta 28"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_perna_direita.png",card=28),Function(guinodia,True,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["C"]):
        vbox:
            xalign 0.93
            yalign 0.09
            textbutton _("Carta 29"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="paulo_gino_piscineiro.png",card=29),Function(sfx_carta,audio.gino_piscineiro,False,1),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [NullAction()]

    if(persistent.endings["D"]):
        vbox:
            xalign 0.66
            yalign 0.14
            textbutton _("Carta 30"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_braco_direito.png",card=30),Function(guinodia,True,1)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["E"]):
        vbox:
            xalign 0.795
            yalign 0.14
            textbutton _("Carta 31"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="paulo_gino_bombeiro.png",card=31),Function(sfx_carta,audio.mangueira,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["F"]):
        vbox:
            xalign 0.93
            yalign 0.14
            textbutton _("Carta 32"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="renzo.png",card=32),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["G"]):
        vbox:
            xalign 0.66
            yalign 0.19
            textbutton _("Carta 33"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="paulo_gino.png",card=33),Function(sfx_carta,audio.gino_supremo,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["H"]):
        vbox:
            xalign 0.795
            yalign 0.19
            textbutton _("Carta 34"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="cabacao.png",card=34),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [Function(FinishEnterNameChurrasco)]

    if(persistent.endings["I"]):
        vbox:
            xalign 0.93
            yalign 0.19
            textbutton _("Carta 35"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="anita.png",card=35),Function(sfx_carta,voz_cap02_02_20,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["J"]):
        vbox:
            xalign 0.66
            yalign 0.24
            textbutton _("Carta 36"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="lily_santos.png",card=36),Function(sfx_carta,audio.lily_santos2,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["K"]):
        vbox:
            xalign 0.795
            yalign 0.24
            textbutton _("Carta 37"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="boy_stronda.png",card=37),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [Function(FinishEnterNameBadBoy)]

    if(persistent.endings["L"]):
        vbox:
            xalign 0.93
            yalign 0.24
            textbutton _("Carta 38"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="mangueira_boy.png",card=38),Function(sfx_carta,audio.mangueira_boy_01,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["M"]):
        vbox:
            xalign 0.66
            yalign 0.29
            textbutton _("Carta 39"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="dansa_gatinho.png",card=39),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["N"]):
        vbox:
            xalign 0.795
            yalign 0.29
            textbutton _("Carta 40"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="felipinho.png",card=40),Function(sfx_carta,audio.felipinho_01,False,0),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [NullAction()]

    if(persistent.endings["O"]):
        vbox:
            xalign 0.93
            yalign 0.29
            textbutton _("Carta 41"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="cj_de_familia.png",card=41),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["P"]):
        vbox:
            xalign 0.66
            yalign 0.34
            textbutton _("Carta 42"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_braco_esquerdo.png",card=42),Function(guinodia,True,2)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["Q"]):
        vbox:
            xalign 0.795
            yalign 0.34
            textbutton _("Carta 43"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="kawan.png",card=43),Function(sfx_carta,audio.kawan2,True,1)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["R"]):
        vbox:
            xalign 0.93
            yalign 0.34
            textbutton _("Carta 44"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="oh_man.png",card=44),Function(sfx_carta,"<from 0.833 loop 0.833>mod_assets/music/fm_kaiba_faceoff.ogg",False,1),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [Function(FinishEnterNameCapXY)]
                

    if(persistent.endings["S"]):
        vbox:
            xalign 0.66
            yalign 0.39
            textbutton _("Carta 45"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left_video", img="tom_chines.png",card=45,video="img_tom_chines"),Function(racionais_g_audio,audio.tom_chines,False,1),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left_video"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [NullAction()]

    if(persistent.endings["T"]):
        vbox:
            xalign 0.795
            yalign 0.39
            textbutton _("Carta 46"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guilhotina_g.png",card=46),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["U"]):
        vbox:
            xalign 0.93
            yalign 0.39
            textbutton _("Carta 47"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="sandro_lima.png",card=47),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["V"]):
        vbox:
            xalign 0.66
            yalign 0.44
            textbutton _("Carta 48"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="paulo_gino_matrix.png",card=48),Function(sfx_carta,audio.gino_seguranca,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["W"]):
        vbox:
            xalign 0.795
            yalign 0.44
            textbutton _("Carta 49"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="vegeta.png",card=49),Function(sfx_carta,audio.vegeta_de_familia,False,0),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(renpy.music.stop,"sound"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg")]
                action [NullAction()]

    if(persistent.endings["X"]):
        vbox:
            xalign 0.93
            yalign 0.44
            textbutton _("Carta 50"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="alemao.png",card=50),Function(sfx_carta,audio.alemao_01,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["Y"]):
        vbox:
            xalign 0.66
            yalign 0.49
            textbutton _("Carta 51"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_perna_esquerda.png",card=51),Function(guinodia,True,3)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["Z"]):
        vbox:
            xalign 0.795
            yalign 0.49
            textbutton _("Carta 52"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="ricco_puentes.png",card=52),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["CYM"]):
        vbox:
            xalign 0.93
            yalign 0.49
            textbutton _("Carta 53"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="sarcofago.png",card=53),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["CYM"]):
        vbox:
            xalign 0.66
            yalign 0.54
            textbutton _("Carta 54"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="pote_da_delicia.png",card=54),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["CXY"]):
        vbox:
            xalign 0.795
            yalign 0.54
            textbutton _("Carta 55"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="noku_tijolao.png",card=55),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.93
            yalign 0.54
            textbutton _("Carta 56"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_terceira_perna.png",card=56),Function(guinodia,True,4)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]






    if(persistent.endings["C1"]):
        vbox:
            xalign 0.66
            yalign 0.59
            textbutton _("Carta 57"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="monstro_que_relaxa.png",card=57),Function(sfx_carta,audio.jailson_ainn2,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["C2"]):
        vbox:
            xalign 0.795
            yalign 0.59
            textbutton _("Carta 58"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="filhona.png",card=58),Function(sfx_carta,audio.filhona2,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    

    if(persistent.endings["C3"]):
        vbox:
            xalign 0.93
            yalign 0.59
            textbutton _("Carta 59"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="dragao_baiano.png",card=59),Function(sfx_carta,audio.dragao_baiano2,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["C4"]):
        vbox:
            xalign 0.66
            yalign 0.64
            textbutton _("Carta 60"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="coringa_dano.png",card=60),Function(sfx_carta,audio.coringa_dano2,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["C5"]):
        vbox:
            xalign 0.795
            yalign 0.64
            textbutton _("Carta 61"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="polimerizacao.png",card=61),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(persistent.endings["CXX"]):
        vbox:
            xalign 0.93
            yalign 0.64
            textbutton _("Carta 62"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="guinodia_o_proibido.png",card=62),Function(guinodia,True,5)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]










    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.66
            yalign 0.69
            textbutton _("Carta 63"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="glob.png",card=63),Function(sfx_carta,audio.globglogabgalab,False,0),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(renpy.music.stop,"sound"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.795
            yalign 0.69
            textbutton _("Carta 64"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="taeyeon.png",card=64),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.93
            yalign 0.69
            textbutton _("Carta 65"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="mark.png",card=65),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.66
            yalign 0.74
            textbutton _("Carta 66"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="decode_paxcii.png",card=66),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.795
            yalign 0.74
            textbutton _("Carta 67"):
                style "confirm_button_3"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="feminista.png",card=67),Function(guinodia,False,0)]
                unhovered [Hide("side_img_left")]
                action [NullAction()]

    if(is_all_endings_unlocked()):
        vbox:
            xalign 0.93
            yalign 0.74
            textbutton _("Carta 68"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings_2"
                hovered [ShowTransient("side_img_left", img="calvo_supremo.png",card=68),Function(sfx_carta,audio.calvoooo,False,0),Function(music_channel_stop,"music")]
                unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
                action [Function(renpy.music.stop,"sound"),Function(FinishStandingHereIRealize)]
    


    if(persistent.endings["PRTD"]):
        vbox:
            xalign 0.66
            yalign 0.79
            textbutton _("Página 1"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings_2"
                hovered [Function(guinodia,False,0),Function(guinodia,False,0)]
                action None

    if(persistent.endings["PRTD"]):
        vbox:
            xalign 0.93
            yalign 0.79
            textbutton _("Página 2"):
                style "confirm_button_4"
                text_style "navigation_button_text_endings_2"
                hovered [Function(guinodia,False,0),Function(guinodia,False,0)]
                action [ShowMenu("endings_pag_2")]

    textbutton _("Voltar"):
        xalign 0.05
        ypos 0.99
        style "return_button"
        hovered [Function(guinodia,False,0),Function(guinodia,False,0)]
        action [Return(), Play("music", audio.main_menu),Function(guinodia_init)]




screen endings_pag_2():

    tag menu

    add "mod_assets/images/EndingsMenu.png"
    
    textbutton _("Finais (Deck G)"):
        xalign 0.5
        yalign 0.005
        style "page_label_text"
        text_size 28

    vbox:
        xalign 0.09
        yalign 0.12
        textbutton _("Carta 69"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="conehead.png",card=69)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]
    
    vbox:
        xalign 0.29
        yalign 0.12
        textbutton _("Carta 70"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="jailson_mendes_primeiro.png",card=70)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.17
        textbutton _("Carta 71"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="the_boys_do_ano.png",card=71)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.17
        textbutton _("Carta 72"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="omacho.png",card=72),Function(sfx_carta,audio.pingu,False,1),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_right_2"),Function(music_channel_play,"music",0.00,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.22
        textbutton _("Carta 73"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="rocky_gaucho.png",card=73)]
            unhovered [Hide("side_img_right_2"),Function(reset_jumpscare_senna,False,0)]
            action [Function(jumpscare_senna_count,False,0)]

    vbox:
        xalign 0.29
        yalign 0.22
        textbutton _("Carta 74"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="indios_papacu.png",card=74)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]
    
    vbox:
        xalign 0.09
        yalign 0.27
        textbutton _("Carta 75"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="xaropinho.png",card=75)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.27
        textbutton _("Carta 76"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="ucraniano.png",card=76)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.32
        textbutton _("Carta 77"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="senhor_dos_anais.png",card=77)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.32
        textbutton _("Carta 78"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="jo_abdul.png",card=78),Function(sfx_carta,audio.jo_abdul2,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [Function(FinishEnterNameCapYeahMan)]
    
    vbox:
        xalign 0.09
        yalign 0.37
        textbutton _("Carta 79"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="vaca_no_ku.png",card=79)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.37
        textbutton _("Carta 80"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="gemidao.png",card=80)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.42
        textbutton _("Carta 81"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="bizarro.png",card=81)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.42
        textbutton _("Carta 82"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="ricardo_milos.png",card=82)]
            unhovered [Hide("side_img_right_2")]
            action [Function(FinishEnterNameBadBoy)]

    vbox:
        xalign 0.09
        yalign 0.47
        textbutton _("Carta 83"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="saci.png",card=83)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.47
        textbutton _("Carta 84"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="indiana_torres.png",card=84),Function(sfx_carta,audio.pingu,False,1),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_right_2"),Function(music_channel_play,"music",0.00,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.52
        textbutton _("Carta 85"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="papai_noel.png",card=85)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.52
        textbutton _("Carta 86"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="zeh.png",card=86),Function(sfx_carta,voz_cap02_02_20,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.57
        textbutton _("Carta 87"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="entregador_de_pizza.png",card=87)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.29
        yalign 0.57
        textbutton _("Carta 88"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="papaco.png",card=88)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]

    vbox:
        xalign 0.09
        yalign 0.62
        textbutton _("Carta 89"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="ed_hector.png",card=89)]
            unhovered [Hide("side_img_right_2")]
            action [Function(FinishEnterNameOnlyMen)]

    vbox:
        xalign 0.29
        yalign 0.62
        textbutton _("Carta 90"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="dolph_ziggler.png",card=90),Function(sfx_carta,audio.mangueira_boy_01,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]
    
    vbox:
        xalign 0.09
        yalign 0.67
        textbutton _("Carta 91"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="akuma.png",card=91),Function(sfx_carta,voz_cap05_02_032,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]
    
    vbox:
        xalign 0.29
        yalign 0.67
        textbutton _("Carta 92"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="demacol.png",card=92),Function(sfx_carta,audio.alemao_01,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [NullAction()]
    
    vbox:
        xalign 0.09
        yalign 0.72
        textbutton _("Carta 93"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="ursos_lolitos.png",card=93),Function(sfx_carta,audio.jailson01,False,0)]
            unhovered [Hide("side_img_right_2")]
            action [Function(FinishEnterNameCapJailson)]

    vbox:
        xalign 0.29
        yalign 0.72
        textbutton _("Carta 94"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings"
            hovered [ShowTransient("side_img_right_2", img="vin_diesel.png",card=94),Function(sfx_carta,audio.vcs_broxaram,False,1),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_right_2"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    

    

    

    

    

    













    

    

    

    

    vbox:
        xalign 0.64
        yalign 0.12
        textbutton _("Carta 95"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="magrinhu.png",card=95),Function(sfx_carta,audio.jailson_ainn,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.12
        textbutton _("Carta 96"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="ursos.png",card=96)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.12
        textbutton _("Carta 97"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="kakapo.png",card=97)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.17
        textbutton _("Carta 98"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="leo_lins.png",card=98),Function(sfx_carta,audio.kid_bengala2,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.17
        textbutton _("Carta 99"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="everson_zoio.png",card=99)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.17
        textbutton _("Carta 100"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="mc_gorila.png",card=100)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.22
        textbutton _("Carta 101"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="gil_brother.png",card=101),Function(sfx_carta,audio.gino_piscineiro,False,1),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.22
        textbutton _("Carta 102"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="mc_vv.png",card=102)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.22
        textbutton _("Carta 103"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="nego_bam.png",card=103)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.27
        textbutton _("Carta 104"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="pegasus.png",card=104),Function(sfx_carta,audio.pau_brilhante,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.27
        textbutton _("Carta 105"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="fome.png",card=105),Function(sfx_carta,audio.fomehahaha,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.27
        textbutton _("Carta 106"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="barra_de_metal.png",card=106)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.32
        textbutton _("Carta 107"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="entra_que_eu_te_explico.png",card=107)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.32
        textbutton _("Carta 108"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="super_choque.png",card=108),Function(sfx_carta,audio.jo_abdul2,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.32
        textbutton _("Carta 109"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="dragao_comunista.png",card=109)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.37
        textbutton _("Carta 110"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="chessus.png",card=110),Function(sfx_carta,audio.jesuis,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.37
        textbutton _("Carta 111"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="crow.png",card=111)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.37
        textbutton _("Carta 112"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="pica_pau.png",card=112)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.42
        textbutton _("Carta 113"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="manto_azul.png",card=113),Function(sfx_carta,audio.computador_gino,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.42
        textbutton _("Carta 114"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="nicole.png",card=114),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.42
        textbutton _("Carta 115"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="nibonetti.png",card=115)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.47
        textbutton _("Carta 116"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="danger_gilson.png",card=116),Function(sfx_carta,voz_capXX_019,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(renpy.music.stop,"sound"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.47
        textbutton _("Carta 117"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="12_do_gugu.png",card=117),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.47
        textbutton _("Carta 118"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="reneral.png",card=118)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.52
        textbutton _("Carta 119"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="MARCELO.png",card=119),Function(sfx_carta,audio.fomehahaha,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.52
        textbutton _("Carta 120"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="lain.png",card=120),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.52
        textbutton _("Carta 121"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="miyuki.png",card=121)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.57
        textbutton _("Carta 122"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="yuri.png",card=122),Function(sfx_carta,audio.fomehahaha,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.57
        textbutton _("Carta 123"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="mara.png",card=123),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.57
        textbutton _("Carta 124"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="yami_senna.png",card=124)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.64
        yalign 0.67
        textbutton _("Token 01"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="revista_g.png",card=125),Function(sfx_carta,audio.fomehahaha,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.795
        yalign 0.67
        textbutton _("Token 02"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="pedra_g.png",card=126),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.67
        textbutton _("Token 03"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="mara_mara.png",card=127),Function(sfx_carta,audio.fomehahaha,False,0)]
            unhovered [Hide("side_img_left")]
            action [NullAction()]

    vbox:
        xalign 0.95
        yalign 0.72
        textbutton _("vtnc kkkk"):
            style "confirm_button_3"
            text_style "navigation_button_text_endings_2"
            hovered [ShowTransient("side_img_left", img="noir.png",card=128),Function(sfx_carta,voz_gino_arabe,False,0),Function(music_channel_stop,"music")]
            unhovered [Hide("side_img_left"),Function(music_channel_play,"music",0.70,"mod_assets/music/fm_library.ogg"),Function(renpy.music.stop,"sound")]
            action [NullAction()]









    


    

    vbox:
        xalign 0.665
        yalign 0.79
        textbutton _("Página 1"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings_2"
            action [ShowMenu("endings")]

    vbox:
        xalign 0.94
        yalign 0.79
        textbutton _("Página 2"):
            style "confirm_button_4"
            text_style "navigation_button_text_endings_2"
            action None

    textbutton _("Voltar"):
        xalign 0.04
        ypos 0.99
        style "return_button"
        action [Return(), Play("music", audio.main_menu),Function(guinodia_init)]




screen creditos():

    tag menu

    style_prefix "creditos"

    add "black"

    vbox:
        xalign 0.475
        yalign 0.22
        imagebutton:
            idle "mod_assets/images/operation_senna.png"
            hover "mod_assets/images/operation_senna_hover.png"
            action [ShowMenu("operation_senna_scr"), SensitiveIf(renpy.get_screen("operation_senna_scr") == None), [init_input_operation_senna(),Function(drpc_update,"finalZ")],Play("music", audio.m_converting_minds)]
            hover_sound audio.fm_arrow_select
            activate_sound audio.fm_back

    vbox:
        xalign 0.475
        yalign 0.89
        imagebutton:
            idle "mod_assets/images/converting_minds.png"
            hover "mod_assets/images/converting_minds_hover.png"
            action [ShowMenu("converting_minds_scr"), SensitiveIf(renpy.get_screen("converting_minds_scr") == None),[Play("music", audio.m_converting_minds),Function(drpc_update,"aparencias"),Function(is_error242424)]]
            hover_sound audio.fm_arrow_select
            activate_sound audio.fm_back

    if(is_main_chapters_unlocked()):
        vbox:
            xalign 0.925
            yalign 0.9
            imagebutton:
                idle "FACELESSGAMES_COM_BR"
                action [ShowMenu("creditos"), SensitiveIf(renpy.get_screen("converting_minds_scr") == None),[Play("music", audio.fm_freeduel),Function(renpy.call_in_new_context,"capFACELESSGAMES")]]
                hover_sound audio.fm_arrow_select
                activate_sound audio.fm_back
            #image "FACELESSGAMES_COM_BR"

    vbox:
        xalign 0.5
        yalign 0.05
        
        text "Forbidden Memories G" style "font_creditos_menu":
            size 22
    
    vbox:
        xalign 0.5
        yalign 0.10
        
        text "Desenvolvido por: \"Operation: Senna\"" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.13
        
        text "Publicado por: \"Operation: Hidden Link\"" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.34
        
        text "Programação, Game Design, Fonte, Roteiro," style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.37
        
        text "Scripts, Sound Design, Design Gráfico:" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.40
        
        text "\"Macho\"" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.49
        
        text "Transcripts:" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.52
        
        text "\"Taeyeon\", \"Mark\"" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.61
        
        text "\"Operation: Senna\" é a" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.64
        
        text "equipe criada para o desenvolvimento de" style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.67
        
        text "Forbidden Memories G." style "font_creditos_menu"

    vbox:
        xalign 0.5
        yalign 0.975
        
        text "Operation: Rabbithole, 2024" style "font_creditos_menu"
            

    #        text "[config.version]":
    #            style "main_menu_version"

    #1996 Kazuki Takahashi

    textbutton _("Voltar"):
        xalign 0.05
        ypos 1.015
        style "return_button"
        action [Return(), Play("music", audio.main_menu)]




## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Salvar"))


screen load():

    tag menu

    use file_slots(_("Carregar"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.is_yuri_self_aware == True and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="Não se preocupe!\nEu estou salvando o jogo para você!", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern="Página {}")

    #use game_menu(title):
    
    #on 'show' action toggle_current_music_player(True)
    
    add "mod_assets/images/logo02.png" #alpha 0.5
    on 'show' action [PauseAudio('sound_bg', True),PauseAudio('sound', True),PauseAudio('movie', True)]

    textbutton _(title):
        xalign 0.5
        yalign 0.025
        style "page_label_text"
        
        if(title == "Salvar"):
            text_style "font_menu_save"
        else:
            text_style "font_menu_load"
            

    hbox:
        box_wrap True
        xalign 0.5
        yalign 0.92
        if(not main_menu and renpy.current_screen().screen_name[0] == "save"):
            textbutton _("Carregar"):
                #xalign 0.05
                
                style "return_button"
                action [Show("load")]

        if(not main_menu and renpy.current_screen().screen_name[0] == "load"):
            textbutton _("Salvar"):
                #xalign 0.05
                style "return_button"
                action [Show("save")]

        if(not main_menu):
            textbutton _("Menu"):
                style "return_button"
                action [MainMenu(),Function(drpc_update,"menu")]

        textbutton _("Voltar"):
            yalign 0.975
            style "return_button"
            action [Return(),If(main_menu,Play("music",audio.main_menu),NullAction())]

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        # The page name, which can be edited by clicking on a button.

        button:
            style "page_label"

            #key_events True
            xalign 0.5
            yalign 0.1
            #action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileActionMod(slot)
                    hover_sound audio.fm_arrow_select
                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("slot vazio")):
                        #style "slot_time_text"
                        align (0.5,0.5)
                        if(title == "Salvar"):
                            style "page_label_text_red"
                        else:
                            style "page_label_text_blue"

                    text FileSaveName(slot):
                        align (0.5,0.5)
                        if(title == "Salvar"):
                            style "page_label_text_red"
                        else:
                            style "page_label_text_blue"
                        #style "slot_name_text"
                    
                    

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

            #textbutton _("{#auto_page}A") action FilePage("auto")

            #textbutton _("{#quick_page}Q") action FilePage("quick")

            # range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton _("[page]"):
                    action FilePage(page)
                    hover_sound audio.fm_arrow_select
                    activate_sound gui.activate_sound

            #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#fff"
    text_align 0.5
    layout "subtitle"
    xmaximum 760
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_color "#070e5c"

style page_label_text_red:
    color "#fff"
    text_align 0.5
    size 14
    #layout "subtitle"
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(4, "#5c0707", 0, 0), (1, "#9e9e9eaa", 0, 0)]

style page_label_text_blue:
    color "#fff"
    text_align 0.5
    size 14
    layout "subtitle"
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(4, "#070e5c", 0, 0), (1, "#9e9e9eaa", 0, 0)]
     

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_color "#070e5c"
    color "#fff"

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#fff"
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    #use game_menu(_("Settings"), scroll="viewport"):
    add "options_menu_bg" alpha 0.3

    vbox:
        xalign 1.0
        yalign 0.7
        xmaximum 900
        hbox:
            box_wrap True
            xmaximum 900
            if renpy.variant("pc"):

                vbox:
                    xmaximum 500
                    style_prefix "radio"
                    label _("Modo de Exibicão")
                    textbutton _("Modo Janela") action Preference("display", "window")
                    textbutton _("Tela Cheia") action Preference("display", "fullscreen")
            #if config.developer:
            #    vbox:
            #        style_prefix "radio"
            #        label _("Rollback Side")
            #        textbutton _("Disable") action Preference("rollback side", "disable")
            #        textbutton _("Left") action Preference("rollback side", "left")
            #        textbutton _("Right") action Preference("rollback side", "right")
            null width (12 * gui.pref_spacing)
            vbox:
                xmaximum 400
                style_prefix "radio"
                label _("Efeito Texto")
                
                textbutton _("Ativado") action [SetField(persistent, "config_fadein_texto", True)] #, toggle_fadein_texto(flag=True)
                textbutton _("Desativado") action [SetField(persistent, "config_fadein_texto", False)] #, toggle_fadein_texto(flag=False)
                #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height (7 * gui.pref_spacing)

        hbox:
            xmaximum 900
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("Velocidade do Texto")

                #bar value Preference("text speed")
                bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=True, style="slider", step=10)

            vbox:

                if config.has_music:
                    label _("Volume de Música")

                    hbox:
                        #bar value SteppedMixerValue('music', step=0.01)
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Volume de Som")

                    hbox:
                        bar value Preference("sound volume")


                if config.has_voice:
                    label _("Volume de Voz")

                    hbox:
                        bar value Preference("voice volume")


                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mutar Tudo"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"
        
        null height (1 * gui.pref_spacing)

        hbox:
            box_wrap True
            xmaximum 900
            vbox:
                hbox:
                    style_prefix "radio"
                    label _("Idioma")
                hbox:
                    style_prefix "radio"
                    textbutton _("Português") action [SetField(persistent, "config_arabe", False)] #, toggle_fadein_texto(flag=True)
                    textbutton _("Árabe") action [SetField(persistent, "config_arabe", True)] #, toggle_fadein_texto(flag=False)
    
    if(persistent.endings["G"]):
        vbox:
            xalign 0.1
            yalign 0.7
            ymaximum 500
            vbox:
                xmaximum 900
                style_prefix "radio"
                label _("Música Menu Principal")
            vbox:
                xmaximum 900
                style_prefix "radio"
                textbutton _("Forbidden Memories Main Menu") action [SetField(persistent, "config_main_menu_music", False), Function(change_main_menu_music,False)] #, toggle_fadein_texto(flag=True)
                textbutton _("Duelista de Família") action [SetField(persistent, "config_main_menu_music", True), Function(change_main_menu_music,True)] #, toggle_fadein_texto(flag=False)

    textbutton _("Voltar"):
        xalign 0.95
        ypos 0.95
        style "return_button"
        action [Return(), Play("music", audio.main_menu),toggle_fadein_texto(),toggle_arabe()]

    #text "v[config.version]":
    #            xalign 1.0 yalign 1.0
    #            xoffset -10 yoffset -10
    #            style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    size 20
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(5, "#070e5c", 2, 2), (1, "#9e9e9eaa", 0, 0)]
    size 14

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(5, "#070e5c", 2, 2), (1, "#9e9e9eaa", 0, 0)]
    size 14

style slider_slider:
    xsize 350
    color "#fff"

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Help"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
#
#            if device == "keyboard":
#                use keyboard_help
#            elif device == "mouse":
#                use mouse_help
#            elif device == "gamepad":
#                use gamepad_help
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Space")
#        text _("Advances dialogue without selecting choices.")
#
#    hbox:
#        label _("Arrow Keys")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Escape")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Skips dialogue while held down.")
#
#    hbox:
#        label _("Tab")
#        text _("Toggles dialogue skipping.")
#
#    hbox:
#        label _("Page Up")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Page Down")
#        text _("Rolls forward to later dialogue.")
#
#    hbox:
#        label "H"
#        text _("Hides the user interface.")
#
#    hbox:
#        label "S"
#        text _("Takes a screenshot.")
#
#    hbox:
#        label "V"
#        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Left Click")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Middle Click")
#        text _("Hides the user interface.")
#
#    hbox:
#        label _("Right Click")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Mouse Wheel Up\nClick Rollback Side")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Mouse Wheel Down")
#        text _("Rolls forward to later dialogue.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Right Trigger\nA/Bottom Button")
#        text _("Advance dialogue and activates the interface.")
#
#    hbox:
#        label ("Left Trigger\nLeft Shoulder")
#        text _("Roll back to earlier dialogue.")
#
#    hbox:
#        label _("Right Shoulder")
#        text _("Roll forward to later dialogue.")
#
#    hbox:
#        label _("D-Pad, Sticks")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Start, Guide")
#        text _("Access the game menu.")
#
#    hbox:
#        label _("Y/Top Button")
#        text _("Hides the user interface.")
#
#    textbutton _("Calibrate") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen name_input(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action,set_flag_input_operation_senna(False)]

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("player") length 1000 allow string.printable

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen dialog(message, ok_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch" xalign 0.5

            else:
                #label _(message):
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Sim") action yes_action
                textbutton _("Não") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_2 is gui_medium_button
style confirm_button_3 is gui_medium_button
style confirm_button_4 is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#fff"
    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_2:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound audio.fm_error
    xalign 0.5
    yalign 0.5

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(5, "#070e5c", 2, 2), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]

style font_menu_save:
    #size_group "navigation"
    xalign 0.5
    yalign 0.5
    size 28

    outlines [(6, "#5c0707", 0, 0),(1, "#9e9e9eaa", 0, 0)]

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"

style font_menu_load:
    #size_group "navigation"
    xalign 0.5
    yalign 0.5
    size 28

    outlines [(6, "#070e5c", 0, 0),(1, "#9e9e9eaa", 0, 0)]

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"

style confirm_button_3:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound audio.fm_arrow_select
    activate_sound audio.fm_error
    xalign 0.5
    yalign 0.5

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(5, "#070e5c", 2, 2), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]

style confirm_button_4:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound audio.fm_arrow_select
    activate_sound gui.activate_sound
    xalign 0.5
    yalign 0.5

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0)]
    hover_outlines [(5, "#070e5c", 2, 2), (1, "#9e9e9eaa", 0, 0)]
    insensitive_outlines [(5, "#070e5c", 0, 0), (2, "#9e9e9eaa", 0, 0)]

style credits_text:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound audio.fm_arrow_select
    activate_sound audio.fm_error
    xalign 0.5
    yalign 0.5

    font "mod_assets/gui/fonts/ForbiddenMemories.ttf"
    color "#fff"
    outlines [(4, "#000000aa", 0, 0),(1, "#9e9e9eaa", 0, 0),(5, "#070e5c", 2, 2)]

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size


#Texto Game Over
screen texto_game_over:
    vbox:
        xalign 0.94
        yalign 0.96

        textbutton _("Final "+current_ending_id+": \""+endings_names[current_ending_id]+"\""):
            style "page_label_text"
            text_size 16

screen texto_final_mara:
    vbox:
        xalign 0.94
        yalign 0.96

        textbutton _("final mara"):
            style "page_label_text"
            text_size 16

        
    