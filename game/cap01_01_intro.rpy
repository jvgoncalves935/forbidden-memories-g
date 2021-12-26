label cap01_01_intro:
    scene black
    stop music
    "{p=4.0}{nw}"
    hide black
    play sound footsteps
    show intro_001 at top
    with dissolve
    #scene bg intro_001 at top
    "{p=1.0}{nw}"
    hide intro_001
    show black
    with dissolve
    hide black
    show intro_002 at top
    with dissolve
    "{p=2.0}{nw}"
    hide intro_002
    show black
    with dissolve
    hide black
    show intro_003 at top
    with dissolve
    "{p=1.0}{nw}"
    "{outlinecolor=#000000}Finalmente eu encontrei!{/outlinecolor}\nFinalmente eu encontrei!"
    play sound ctc
    "O Códex G, a História do Alexandre Senna!"
    play sound ctc
    hide intro_003
    show black
    with dissolve
    hide black
    show intro_004 at top
    with Dissolve(1.5)
    "{p=1.0}{nw}"
    "Hahahahaha!"
    play sound ctc
    "Hahahahaha...\nHahahahaha!!!"
    play sound ctc
    return



