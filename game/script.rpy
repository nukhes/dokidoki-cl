label start:
    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0
    $ score = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Indiano"
    $ m_name = "Mikael"
    $ chosen = "just yuri porra"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    call game

    # if persistent.example_seen:
    #     call tutorial_selection
    # else:
    #     call example_chapter from _call_example_chapter

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length

    call credits_custom

    $ quick_menu = True
    $ renpy.full_restart()

label credits_custom:
    "Obrigado por jogar Doki Doki Chemistry Lab! Este mod de DDLC não seria possível sem a Team Salvato e a nossa equipe."
    "Pedro H. (Desenvolvimento, Programação e Roteiro)"
    "Matheus M. (Roteiro)"
    "Rafael Tavares (Design de personagem)"
    "Rafael Garcia (Design de personagem e desenho digital)"
    "OBS: Esse jogo possui múltiplos finais, fique a vontade para testar."
    "Feira de Cursos 2024 - ETEC 2DS"
    return