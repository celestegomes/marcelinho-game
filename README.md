# Little Marcelo - O JOGO
Trabalho de conclusão da cadeira de Programação 1 para o curso de Sistemas de Informação da UFPE. Um jogo em pixel de infinite runner escrito em python utilizando a biblioteca pygames com foco em POO.

# RELATÓRIO DO PROJETO

Nome do projeto: LITTLE MARCELO<br />Integrantes do grupo: Beatriz Helena, Larissa Gomes, Maria Antônia e Williams Andrade

ORGANIZAÇÃO DO CÓDIGO

Etapas de criação:
  - Criamos primeiro a parte jogável do game (criamos o personagem e adicionamos os coletáveis);
  - A segunda etapa foi usada para fazer os movimentos do player e coletáveis e também para adicionar um antagonista (guardinha);
  - Após os elementos principais serem adicionados, começamos a trabalhar na adição das ações “coletar” e “gerenciar”;
  - Concluído todos os requisitos obrigatórios, o grupo iniciou a inclusão de background, ícones no gerenciador de coletas, música, tela inicial e tela final.

Organização do código:

  Utilizamos as primeiras linhas do código para chamar as bibliotecas necessárias e armazenar as mídias que foram utilizadas no jogo. Após isso, usamos as seguintes, para escrever funções que seriam utilizadas para tela inicial, tela final, reiniciar o game e escrever textos. As classes dos objetos foram escritas após as funções e o nosso loop no final do código, após as listas.

Finalidade das funções, classes e listas:

- As funções pressionar_espaço( ) e exibe_mensagem( ) foram criadas com o objetivo de serem usadas em diversas partes do código repetidas vezes, ou seja, para poupar o retrabalho de reescrever algo feito anteriormente.
- As funções de telas (inicial e final) foram criadas para deixar o código mais “limpo” e organizado, pode-se notar que se escrevêssemos os textos da tela inicial e final fora da função o código ficaria “pesado” para ler e mais complexo de entender.
- As listas foram usadas para identificar as colisões entre o player e o antagonista/coletáveis.
- As classes deram vida ao player, antagonista e comidas (os coletáveis) do jogo, o que faz o jogo funcionar. Ela permite a movimentação de todos os elementos principais do projeto.
- O loop é o jogo, a parte que integra todas as funções e classes e utiliza as listas e mídias adicionadas.
	
FERRAMENTAS, BIBLIOTECAS E FRAMEWORKS

  Utilizamos as bibliotecas PYGAME e OS. O Pygame nos permitiu modelar quase o jogo inteiro, ele possibilitou o upload de mídias, modelagem das imagens, criação de textos em tela e também funcionalidades como: movimentação do player (pulo), reconhecimento de colisão, movimentação dos objetos coletáveis, aplicação de background e outras. A biblioteca OS ajudou muito na automatização de processos como o upload de imagens.

DIVISÃO DO TRABALHO
Código:

  Código base - As movimentações do player e dos elementos coletáveis foram escritas por Beatriz Helena e Williams Andrade (Larissa Gomes e Maria Antônia participaram de algumas soluções, como: tornar o elemento coletável assim que houvesse uma colisão).
  Parte gráfica - As sprites do jogo foram adquiridas em sites que disponibilizam artes de graça para pequenos desenvolvedores e algumas foram criadas por um amigo da equipe. No código, a aplicação dessas sprites foi feita por todos os membros (sprites de player e coletáveis - Beatriz e Williams -, sprites de tela inicial e background - Larissa e Maria.
  Funções do código - Sempre que surgia a necessidade de uma nova função o membro que estava “codando” a criava e os outros utilizavam-na em outra parte do código.
  Gerenciamento de tarefas - Não foram definidas tarefas propriamente ditas, cada membro teve autonomia de escolher o que fazer e todos ajudaram na criação de cada bloco de código, seja com pesquisa ou realmente escrevendo.
  Relatório:
O relatório foi escrito por Maria Antônia e revisado pelos outros membros da equipe.

CONCEITOS DA DISCIPLINA

  Utilizamos bastantes os conteúdos aprendidos ao longo da disciplina, como por exemplo: Funções, condicionais e Laços.
  Os mais utilizados foram: Funções e Laços. O código do projeto depende muito desses dois recursos de Python, a estrutura dele é inteiramente baseada no conceito de loops e utiliza diversas funções. No geral, o loop utilizado integra os outros assuntos, ele é a estrutura base e as funções e condições são auxiliares.

DESAFIOS E ERROS

1. Qual foi o maior erro cometido? Como lidaram com ele?

  Falta de organização no início do projeto, isso gerou uma divisão desigual do trabalho e atrasou um pouco. Por falta de tempo, alguns membros demoraram a focar no planejamento do jogo, porém os outros iniciaram o código e com o tempo tudo se organizou de forma espontânea.

2. Qual foi o maior desafio? Como lidaram com ele?

  Se adaptar à biblioteca (Pygame). A falta de experiência no desenvolvimento de jogos e de conhecimento da biblioteca foram os maiores desafios para todos da equipe, muitas das funcionalidades que queríamos e poderíamos implementar acabaram se perdendo por conta desse obstáculo. Nós demos o nosso máximo no aprendizado para entregar o projeto cumprindo todos os requisitos obrigatórios e da melhor forma possível, quando um integrante não sabia como executar tal ideia os outros ajudavam a procurar sobre ou até mesmo dando formas práticas para implementar essa ideia.

3. Quais lições aprenderam?

  Uma das lições foi: primeiro aprender a lidar com a biblioteca, depois programar com ela. Os bugs que vêm depois quando você altera algo mínimo, acabam sendo os maiores desafios para lidar, então é melhor programar sabendo o que está fazendo e não apenas repetir blocos de códigos.
  Aprendemos que o planejamento pode ser considerado como 50% de um projeto, fazê-lo de qualquer jeito ou ignorá-lo pode ser um empecilho ao longo da criação de um jogo, por exemplo.
  Também entendemos a importância do trabalho em equipe, ter e ser o suporte de alguém pode ser um fator muito importante no desenvolvimento de uma aplicação, não iríamos prosseguir em algumas etapas sem a ajuda um do outro.
  Em resumo, tivemos muitas complicações (problemas com o tamanho da sprite, problemas com a coleta dos objetos, problemas com  a falta de tempo de alguns integrantes, problemas com a parte de reinicialização do game, etc) ao longo do projeto, porém conseguimos ser resilientes o suficiente para não desistir e continuar tentando até acertar.
