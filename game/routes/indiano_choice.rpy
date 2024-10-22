label indiano_choice:
    scene bg club_day with fade
    pause 2.0
    "..."
    play music t6
    show sayori 4p at hf11
    s "Isso pode dar errado... Mas não se preocupe, eu sei o que estou fazendo."
    show sayori 1k at f11

    mc "Confio em você. Parece que essa reação está ficando bem..."
    mc "estável."

    show sayori 5b at hf11
    s "Está falando da reação ou de nós dois?"
    show sayori 5c at f11

    "Ela está flertando de novo? Isso está ficando interessante."
    hide sayori

    "Indiano retira da bolsa um livro..."
    "Fico admirando sua beleza e concentração na leitura."

    show sayori 5d
    s "[player], gostaria de se juntar a mim nessa leitura?"
    mc "C-claro!"
    
    "Estou começando a ficar com vergonha..."
    "A presença de Indiano é doce."
    "Começo a mergulhar na leitura procurando palavras-chave para puxar assunto..."
    call poem from _call_poem

    call encontro_indiano from _call_encontro_indiano