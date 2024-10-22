label marquinhosbadendgame_indiano(pause_length=4.0):
    $ quick_menu = False
    play music m1
    scene black
    s "Você..."
    s "Você conseguiu estragar tudo..."
    s "Por que escolheu o Mikael?"
    s "Achou que era um carbono secundário, podendo manter duas relações, acontece que você não passa de um..."
    s "Hidrogênio, você só poderia se relacionar com uma molécul-, quero dizer, pessoa"
    show sayori 2u at hf11
    pause 1
    show sayori 2v at hf11
    pause 1
    show sayori 2w at hf11
    pause 4
    with dissolve_scene_full
    pause pause_length
    call mikael_choice from _call_mikael_choice
    $ quick_menu = True

label marquinhosbadendgame_mikael(pause_length=4.0):
    $ quick_menu = False
    play music m1
    scene black
    m "Você..."
    m "Você conseguiu estragar tudo..."
    m "Por que escolheu o Indiano?"
    m "Achou que era um carbono secundário, podendo manter duas relações, acontece que você não passa de um..."
    m "Hidrogênio, você só poderia se relacionar com uma molécul-, quero dizer, pessoa"
    show monika 2p at hf11
    pause 1
    show monika 2q at hf11
    pause 1
    show monika 2r at hf11
    pause 4
    with dissolve_scene_full
    pause pause_length
    call indiano_choice from _call_indiano_choice
    $ quick_menu = True
