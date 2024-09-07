#  CalculadoraGUIOO.py

 Esta é uma simples aplicação de calculadora com interface gráfica desenvolvida em Python, utilizando a biblioteca Tkinter. A calculadora permite realizar as operações básicas de soma, subtração, multiplicação e divisão entre dois números.

 # Como Executar
Pré-requisitos:

Certifique-se de ter o Python instalado na sua máquina. A versão 3.6 ou superior é recomendada.
A biblioteca Tkinter é parte da biblioteca padrão do Python, então não é necessário instalar nada adicional

# Clonando o Repositório:

git clone https://github.com/seu-usuario/calculadora-tkinter.git
cd calculadora-tkinter

# Executando o Programa:

python calculadora.py

Uma janela da interface gráfica aparecerá, onde você poderá inserir os valores e selecionar a operação desejada.

# Funcionalidades
Operações disponíveis:

Soma: Adiciona dois números.

Subtração: Subtrai o segundo número do primeiro.

Multiplicação: Multiplica dois números.

Divisão: Divide o primeiro número pelo segundo. Caso o segundo número seja zero, retorna uma mensagem de erro.

# Decisões de Design

Encapsulamento das Operações:  As operações matemáticas são encapsuladas em métodos dentro da classe Calculadora. Isso facilita a manutenção e a possível extensão do código, caso novas operações sejam adicionadas no futuro.


Interface Gráfica com Tkinter:  A interface foi desenvolvida utilizando a biblioteca Tkinter, que é parte da biblioteca padrão do Python. Tkinter foi escolhido por ser simples de usar e suficiente para a proposta desta calculadora básica.


Validação de Entradas:  O programa inclui uma simples verificação de erros para garantir que os valores inseridos são números válidos. Em caso de entrada inválida, uma mensagem de erro é exibida na interface.


Modularidade:  A classe Calculadora é responsável por todas as operações matemáticas, enquanto o código da interface gráfica está separado em funções distintas. Isso promove uma melhor organização e facilita a compreensão e o teste do código.
