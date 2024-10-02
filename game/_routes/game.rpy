label game:
    scene bg residential_day with fade

    "É um dia calmo como qualquer outro no qual eu estou indo para a escola. Bem, seria se não fossem meus dois amigos que vêm todos os dias comigo. Espero que seja um dia divertido como todos os outros."

    show sayori 1e at left
    show monika 1c at right

    s "Ei! [player], esse dia está bonito, não é? Cheio de gás carbônico no ar, né? Hehe."

    m "Eu também faço parte da turma, sua boba. Aliás, está preparado para a aula de hoje? O professor disse que vai ter exercícios envolvendo hidrogênio."

    mc "Ah, sim! Estou ansioso para a aula... e quem sabe aprender algo novo. O que vocês acham que vamos fazer?"

    show sayori 1f
    s "Eu espero que seja algo explosivo! Sabe, algo que realmente nos faça sentir a química... em todos os sentidos."

    show monika 1h
    m "Indiano, você e suas piadas. Mas, seria maneiro! Talvez uma reação ácido-base? Gosto de ver as cores mudarem."

    "Sara e Mikael são tão... Qual delas será que eu deveria me aproximar?"

    # Transição para a escola
    scene bg class_day with dissolve

    "Vocês chegam à escola e se reúnem na sala de aula."

    show sayori 1g at left
    s "Perfeito! Mal posso esperar para ver as cores mudarem. [player], quer ser meu parceiro nesse experimento?"

    show monika 1c at right
    m "Ou pode vir comigo, acho que podemos aprender muito juntos. O que acha?"

    "Quem eu escolho para trabalhar hoje? Indiano é bem animada, mas Mikael parece bem focado."

    menu:
        "Escolher Indiano":
            call indiano_lab

        "Escolher Mikael":
            call mikael_lab


# Dia 2 - Segunda Escolha
label dia_2_intro:
    scene bg residential_day with fade
    "A cara, ontem foi divertido demais, queria mais momentos assim!"

    show sayori 1e at left
    s "[player] deveriamos nos apress..."

    show monika 1c at right
    m "VAMOS PRA ESCOLA, ESTAMOS ATRASADOS!"

    scene black with fade
    "Todos correm para a escola."

    scene bg class_day with fade

    show sayori 1e at left
    s "Ei, [player]! Quer se juntar a mim hoje?"

    show monika 1c at right
    m "Oi! Acho que vamos continuar com mais experimentos práticos hoje... Se quiser, podemos fazer algo."

    "Quem será que me ajudará melhor hoje? Será mais divertido com caio ou mais interessante com mikael?"

    menu:
        "Escolher Mikael":
            call mikael_choice

        "Escolher Indiano":
            call indiano_choice

# A Partir daqui a histório termina em alguns dos encontros