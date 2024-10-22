label mikael_choice:
    scene bg club_day with fade
    pause 2.0
    "..."
    play music t6
    show monika 5b at hf11
    m "Que bom que você escolheu passar mais tempo comigo!"
    show monika 1b at hf11
    mc "Com certeza, isso vai ser muito bom."

    "A interação com Mikael está se tornando cada vez mais interessante..."

    "Mikael retira da bolsa um livro..."
    "Fico admirando sua beleza e concentração na leitura."

    show monika 5a
    m "[player], gostaria de se juntar a mim nessa leitura?"
    mc "C-claro!"
    
    "Estou começando a ficar com vergonha..."
    "A presença de Mikael é imponente, porém muito boa."
    "Começo a mergulhar na leitura procurando palavras-chave para puxar assunto..."
    call poem from _call_poem_1

    call encontro_mikael from _call_encontro_mikael
