# Doki Doki - Chemistry Lab
Jogo para a Feira de Cursos ETEC 2024, se passa em universo alternativo em que você será imerso em uma experiência envolvendo encontros e Estudos de Química, conquiste sua garota balanceando moléculas C6H12O6.

# Instrução de Desenvolvimento (apenas para devs, caso queira baixar o jogo vá em "releases")
O jogo está sendo desenvolvido com o [Ren'py](https://www.renpy.org/), com o [DDLCModTemplate](https://github.com/Monika-After-Story/DDLCModTemplate), adotamos alguns padrões internos de construção para o código e organização do projeto.

## Caminhos
- `./characters`: contém os personagens originais do jogo para fins de arquivamento e compatibilidade.
- `./game`: estrutura do jogo, contém código em .rpy (python com a sintaxe do Ren'py).
- `./game/_example`: material usado como exemplo de sintaxe para trabalhar no código.
- `./game/_routes`: diretório que contém todos os diálogos do jogo.
- `./game/advanced_scripts`: funções internas do jogo (lógica e minigames).
- `./game/gui`: alguns arquivos para compor a UI do jogo.
- `./game/mod_assets`: assets modificados.
- `./game/submods`: gerencia os saves e garanti que nenhum outro jogo entre em conflito (exemplo: outro mod de DDLC).
- `./script.rpy`: configura o ambiente e invoca o jogo.

Para os desenvolvedores do projeto (ou qualquer um que queira modifica-lo) recomendo construir o jogo APENAS no caminho `./game/_routes`, ele é reservado para trabalhar com toda a história.

## Código
Devemos seguir as regras de sintaxe do Ren'py, quando indentar certifique-se de usar QUATRO ESPAÇOS no lugar de tabulações visto que os códigos `.rpy` não aceitam TAB; além disto manter o código limpo e legível é muito importante, respeitando os padrões adotados durante o projeto como:

- labels: devem ter um nome que descreva bem o que ela faz e todo em `lower_case`, palavras separadas por `_`.
Exemplo: `monika_festival_day`, `sayori_birthday`, `natsuki_teaching_chemistry`.

## Observação
Os Assets originais (audio.rpa, images.rpa, fonts.rpa) devem ser copiados para o diretório `./game`, pois os mesmos são pré-compilados e inserir-los neste repositório é ilegal, [Clique Aqui](https://ddlc.moe/) para ser redirecionado ao site oficial do DDLC e instalar uma cópia completa que contém os assets.