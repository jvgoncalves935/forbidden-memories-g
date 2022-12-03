label label_error242424_begin:
    
    $ drpc_update("error242424")
    $ persistent.is_error242424_splashscreen = True

    stop music
    stop sound_bg
    stop voice

    $ play_video("mod_assets/videos/error242424.webm","forbidden_memories_intro_web")

    $ renpy.quit()
    
    return



