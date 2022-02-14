label guinodia_label:
    #$ guinodia_lock()
    stop music
    $ persistent.guinodia_active = True
    call screen guinodia_scr
    #$ renpy.movie_cutscene("mod_assets/videos/guinodia.webm",delay=None,stop_music=True)
    #show white

    #$ guinodia_unlock()