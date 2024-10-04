label minigame:
    scene bg class_day with dissolve
    play music t7
    $ renpy.call_screen("dialog", "[Prova de Química, sua pontuação aqui poderá determinar o rumo do enredo, boa sorte :)]", ok_action=return()) 

    "Devo ler e responder as questões da melhor forma possível..."
    "Isso aqui vai afetar diretamente minha relação com... Esquece, vou parar de pensar bobagem."

    "A chuva ácida é causada principalmente por:"

    menu:
        "a) Evaporação de água limpa":
            $ pass
        "b) Gases liberados pela queima de combustíveis fósseis":
            $ score += 1
        "c) Fertilizantes naturais das plantas":
            $ pass

    "O nome do ácido HCl (dissolvido em água) é:"

    menu:
        "a) Ácido nítrico":
            $ pass
        "b) Ácido sulfúrico":
            $ pass
        "c) Ácido clorídrico":
            $ score += 1

    "Qual destes compostos é considerado um hidrocarboneto?"

    menu:
        "a) H2O (água)":
            $ pass
        "b) NaCl (sal de cozinha)":
            $ pass
        "c) CH4 (metano)":
            $ score += 1

    "Qual é a principal fonte de poluição dos rios?"

    menu:
        "a) Raios solares":
            $ pass
        "b) Despejo de esgoto e produtos químicos":
            $ score += 1
        "c) Vento forte":
            $ pass

    "O nome do ácido H2SO4 é:"

    menu:
        "a) Ácido sulfúrico":
            $ score += 1
        "b) Ácido clorídrico":
            $ pass
        "c) Ácido carbônico":
            $ pass

    "Qual destas opções é um efeito da poluição atmosférica?"

    menu:
        "a) Aumento da camada de ozônio":
            $ pass
        "b) Melhora na qualidade do ar":
            $ pass
        "c) Problemas respiratórios nas pessoas":
            $ score += 1

    "O ácido presente no vinagre é:"

    menu:
        "a) Ácido fosfórico":
            $ pass
        "b) Ácido acético":
            $ score += 1
        "c) Ácido nítrico":
            $ pass

    "O nome do ácido HNO3 é:"

    menu:
        "a) Ácido acético":
            $ pass
        "b) Ácido nítrico":
            $ score += 1
        "c) Ácido carbônico":
            $ pass

    "Qual dos seguintes é um efeito da chuva ácida?"

    menu:
        "a) Crescimento acelerado das plantas":
            $ pass
        "b) Destruição de florestas e prédios":
            $ score += 1
        "c) Formação de rios mais limpos":
            $ pass

    "Um hidrocarboneto é composto por quais elementos?"

    menu:
        "a) Carbono e oxigênio":
            $ pass
        "b) Hidrogênio e oxigênio":
            $ pass
        "c) Carbono e hidrogênio":
            $ score += 1

    "Qual destes ácidos é mais usado em baterias de carro?"

    menu:
        "a) Ácido nítrico":
            $ pass
        "b) Ácido fosfórico":
            $ pass
        "c) Ácido sulfúrico":
            $ score += 1

    "Qual destes compostos é um exemplo de um composto orgânico?"

    menu:
        "a) H2O (água)":
            $ pass
        "b) NaCl (sal de cozinha)":
            $ pass
        "c) C2H6 (etano)":
            $ score += 1


    if score < 3:
        call badendgame
    return
