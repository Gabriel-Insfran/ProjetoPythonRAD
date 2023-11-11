# ProjetoPythonRAD
Projeto da matéria Aplicações Rápidas em Python (Gerenciador de Tarefas)

Membros do grupo:
Gabriel Insfran da Silva: 202204000059
Erick Lohan Lee Souza: 202203193571
Kayo Bappstista de Araujo da Silva: 202203422979
Erick Barradas da Silva Santos: 202002605961
Bernardo de Oliveira da Cruz: 202202177172

Bibliotecas utilizadas:
tkinter, biblioteca para criação de interfaces gráficas, utilizada para criar as telas de login e do gerenciador. Utilizamos funções como “messagebox” para a criação de mensagens de aviso, como por exemplo, uma mensagem que avisa quando uma das entradas do gerenciador está em branco. Também foi utilizada “StringVar” para acessar os dados mais dinamicamente ao invés de conseguir o dado diretamente do widget (entry).
sqlite3, foi utilizada para criar o banco de dados.
re, utilizada para aplicar regex, para verificar-se o formato do registro e-mail.
os, utilizada para abrir o arquivo "view_manager" (janela do gerenciador), a partir da função "system()".

Como iniciar o programa:
Execute o arquivo “view_login.py”.

Idealização do Projeto: 
A ideal inicial do projeto era ser um gerenciador de tarefas, porém decidimos criar um gerenciador de jogos.

Como utilizar:
Primeiramente é necessário realizar um cadastro para fazer login no programa, preenchendo os campos "Endereço de -email" e "senha", após isso clique no botão “cadastrar”, clique no botão “entrar” ou digite seu e-mail e senha e depois clique em “entrar” para fazer login e abrir a tela do gerenciador.
Na tela do Gerenciador de tarefas, preencha todos os campos para cadastrar o jogo e insira no banco através do botão “Salvar”, após inserir o cadastro no banco, clique duas vezes na linha desejada para seleciona-la, após isso podemos deletar ou atualizar um cadastro.
Modifique os registros que foram carregados nas entradas e clique em “Atualizar”, para que assim as informações sejam atualizadas no banco.
Para apagar um registro, clique na linha desejada e depois clique no botão “Excluir”, após isso aparecerá uma janela perguntando se deseja mesmo excluir o registro, se desejar excluir o arquivo do banco, clique em “Sim”, caso não queira, clique em “Não”.





