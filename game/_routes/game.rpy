label game:
    play music t2
    scene bg residential_day with fade

    "É um dia calmo como qualquer outro no qual eu estou indo para a escola. Bem, seria se não fossem meus dois amigos que vêm todos os dias comigo. Espero que seja um dia divertido como todos os outros."

    show monika 1a at t22

    show sayori 4x at f21
    s "Ei! [player], esse dia está bonito, não é? Cheio de gás carbônico no ar, né? Hehe."

    show monika 3l at f22
    m "Eu também faço parte da turma, sua boba. Aliás, está preparado para a aula de hoje? O professor disse que vai ter exercícios envolvendo hidrogênio."

    show monika 2j at f22

    mc "Ah, sim! Estou ansioso para a aula... e quem sabe aprender algo novo. O que vocês acham que vamos fazer?"

    show sayori 3s at f21
    s "Eu espero que seja algo explosivo! Sabe, algo que realmente nos faça sentir a química... em todos os sentidos."

    show monika 1k at f22
    m "Indiano, você e suas piadas. Mas, seria maneiro! Talvez uma reação ácido-base? Gosto de ver as cores mudarem."

    "Indiano e Mikael são tão... Qual delas será que eu deveria me aproximar?"

    # Transição para a escola
    scene bg class_day with dissolve
    "Vocês chegam à escola e se reúnem na sala de aula."

    show sayori 1r at f11
    s "Perfeito! Mal posso esperar para ver as cores mudarem. [player], quer ser meu parceiro nesse experimento?"

    show sayori 1b at t21
    show monika 3b at f22
    m "Ou pode vir comigo, acho que podemos aprender muito juntos. O que acha?"
    show monika 3m at t22
    "Quem eu escolho hoje? Indiano é bem animado, mas Mikael parece mais focado."

    menu:
        "Escolher Indiano":
            $ chosen = "s"
            call indiano_lab

        "Escolher Mikael":
            $ chosen = "m"
            call mikael_lab


# Dia 2 - Segunda Escolha
label dia_2:
    scene bg residential_day with fade
    "A cara, ontem foi divertido demais, queria mais momentos assim!"

    show sayori 4p at f11
    s "[player] deveriamos nos apress..."
    hide sayori

    show monika 5b at f11
    m "VAMOS PRA ESCOLA, ESTAMOS ATRASADOS!"

    scene black with fade
    "Todos correm para a escola."

    scene bg class_day with fade

    show sayori 5b at f11
    s "Ei, [player]! Quer se juntar a mim hoje?"
    show sayori 5c at t22

    show monika 4b at t21
    m "Oi! Acho que vamos continuar com mais experimentos práticos hoje... Se quiser, podemos fazer algo."

    "Quem será que me ajudará melhor hoje? Será mais divertido com caio ou mais interessante com mikael?"

    menu:
        "Escolher Mikael":
            if chosen != "m":
                call marquinhosbadendgame_indiano
            else:
                call mikael_choice

        "Escolher Indiano":
            if chosen != "s":
                call marquinhosbadendgame_mikael
            else:
                call indiano_choice

# A Partir daqui a histório termina em alguns dos encontros