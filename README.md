# gerenciador de tarefas
Este projeto servirá para aprimorarmos nossa lógica de programação ao mesmo tempo em que exploramos conceitos  e tecnicas de programação back-end e fullstack. Vamosultilizar e desenvolver o conceito de MVC (Model-View-Controller), algumas particularidades da Progrmação Orientada a Objetos, Programação funcional, persistencia de dados (MySQL), microframework Flask e gerenciador de pacotes do python (Astral uv).

Alguns passos iniciais para preparar o projeto:
1. Caso não esteja instalado, prepare o uv no seu OS: Você encontra o script de instalação no site <https://docs.astral.sh/uv/#installation>
```bash
powershell -ExecutationPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
2. Faça a inicialização do projeto com o comando
```bash
    uv init
    ```
    Até então ultilizavámos um Layout de Pacote (Package Layout) denominado *flat-layout*. O uv adota um estruturação mais moderna chanada src-layout, que previne eros de importação cimuns chamados `import shadowing` (importação mascaradas).

3. Crie um ambiente virtual do python:
```bash 
uv venv
```
Ative o ambiente virtual, se necessário:
```bash
.\.venv/Scripts/Activate.ps1 # no Powershell do Windows
source.venv/Scripts/activate # no Git Bash do Windows
source .venv/bin/activitate # no Bash do Linux
```

4. Instale o Flask
```bash
uv add flask 
```

Será criado um arquivo `uv.lock` contendo as dependências (requerimentos) e versões dos pacotes do seu projeto.

5. Crie um arquivo `app.py` contendo o código inicial do projeto 
```python
from flask import Flask 

app = Flask(__name__)

@app.route('/test')
def test ():
    return 'Servidor online!'
``` 

6. Teste a aplicação iniciando o servidor do Flask 
``bash
uv run flask run 
```