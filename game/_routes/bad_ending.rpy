label badendgame(pause_length=4.0):
    $ quick_menu = False
    play music m1
    scene black
    "Você..."
    "Você conseguiu estragar tudo..."
    "Por quê? COMO VOCÊ PODE ERRAR TANTAS QUESTÕES????"
    "Enfim, isso é só um jogo, pode tentar denovo :)"
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    $ renpy.full_restart()