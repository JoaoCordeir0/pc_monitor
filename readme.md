# PC monitor

Scripts para obter informações do computador do usuário

&nbsp;
## Como rodar o projeto no vscode

Obs: Substitua joao.cordeiro pelo seu usuário do windows

1. Instale o python 3.11 - https://www.python.org/downloads/

2. Certifique-se de adicionar o python nas variaveis de ambiente: 
    * C:\Users\joao.cordeiro\AppData\Local\Programs\Python\Python311\Scripts\
    * C:\Users\joao.cordeiro\AppData\Local\Programs\Python\Python311\

3. Instale a extensão do Code Runner e Python no vscode

4. Aplique as seguintes configurações no settings.json do vscode:    
    ```
    "code-runner.runInTerminal": true,
    "code-runner.clearPreviousOutput": true,
    "code-runner.executorMap": {                      
        "python": "cls ; python -u",        
    },
    "code-runner.ignoreSelection": true,
    "python.defaultInterpreterPath": "C:\\Users\\joao.cordeiro\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
    ```

5. Crie o ambiente virtual para baixar as dependências do python, para criar siga os seguintes passos:
    1. No terminal, rode os comandos:
        * pip install virtualenv (Caso o pip não seja instalado juntamente ao python, instale manualmente "https://pip.pypa.io/en/stable/installation/")
        * virtualenv venv
        * .\venv\Scripts\activate
    2. Feito isso seu ambiente virtual estará ativo.
        * Para desativar utilize o comando: deactivate        

6. Após criar e estar dentro do ambiente virtual rode o comando:
    1. pip install -r requirements.txt
    2. Feito isso todas as dependências serão instaladas.

7. Após tudo feito, basta utilizar o botão de executar que será adicionado no canto superior direito do vscode ou escrever "python ./scriptname.py" no terminal.

&nbsp;
## Como compilar o projeto e gerar um executável

Após realizar as alterações e testar, utilize o seguinte comando para gerar o executável:
```
pyinstaller --noconsole --onefile .\scriptname.py
```

Após gerar, exclua a pasta build