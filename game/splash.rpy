## splash screen is first thing that gets shown to player
init -100 python:
    # archive check for mods
    for archive in ['audio','images','fonts']:
        if archive not in config.archives:
            renpy.error("Instalação defeituosa, contate o desenvolvedor para mais informações")

# disclaimers
init python:
    menu_trans_time = 1

    splash_message_default = "Este é um mod de Doki Doki Literature Club, sem filiação com a equipe do Team Salvato. Feira de Cursos ETEC 2024."

    splash_messages = [
        "Feira de Cursos ETEC 2024.",
        "Bom Jogo <3",
        "Lembre-se que este jogo possui múltiplos finais, de o seu melhor!"
    ]


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)


image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 210
    ycenter 200
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.9
    menu_art_move(0.68, 510, 0.68)

# Dummy
image menu_art_n:
    pass

image menu_art_y:
    pass

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.8
    menu_art_move(1.00, 1000, 1.00)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0.2, numParticles=60, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

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


init python:
    if not persistent.do_not_delete:

        import os
        try:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")

            if persistent.playthrough <= 2:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 0 or persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

        except:
            pass


label splashscreen:


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "Um save anterior foi detectado, gostaria de deletar ele e recomeçar?"
                "Sim, delete meu save":
                    "Removendo seu save...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "Não, continue de onde eu estava":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()


    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0

        "[config.name] Este é um mod de Doki Doki Literature Club, sem filiação com a equipe do Team Salvato."
        "Uma recriação sem conexão com o universo do DDLC..."

        scene tos2
        with Dissolve(1.5)
        pause 1.0


        scene white
        with Dissolve(1.5)

        $ persistent.first_run = True

    python:
        basedir = config.basedir.replace('\\', '/')

    if persistent.autoload and not _restart:
        jump autoload

    $ config.allow_skipping = False

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)

    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "Não foi possível carregar este save."
        "Você está tentando burlar o jogo?"


        $ renpy.utter_restart()
    return


label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None



    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:

    # stuff that happens when the game closes

    return
