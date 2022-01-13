label cap01_02_casa:
    play music celular
    show textbox_aux
    menu:
        "<Escapar o mais rápido possível>":
            "então chuopa"
            jump game_over
        "<\"No problem.\">":
            "então cuome"
    hide textbox_aux
    stop music
    return