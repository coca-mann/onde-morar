# Projeto Onde Morar

Sistema em Django para registrar e gerenciar resultados de buscas por imóveis (casas, apartamentos) em diferentes localidades, com foco na avaliação de bairros e cidades para futura moradia. A interface principal para gerenciamento de dados é o Django Admin.

## Funcionalidades Principais (via Django Admin)

* Cadastro e gerenciamento de Cidades.
* Cadastro e gerenciamento de Bairros associados a Cidades.
* Cadastro e gerenciamento de Imóveis (Residências) encontrados, associados a Cidades e Bairros.
* Registro de Pontos Positivos e Negativos para Cidades, Bairros e Imóveis.
* Categorização de aspectos (Urbanos e Residenciais) para os pontos positivos/negativos.
* Categorização de Tipos de Imóveis (Casa, Apartamento, etc.).
* Registro de Opções de Financiamento para imóveis.

## Tecnologias Utilizadas

* **Backend:** Python 3.10+, Django 5.2+
* **Banco de Dados:** PostgreSQL
* **Interface Admin:** Django Admin com tema [Django Jazzmin](https://github.com/farridav/django-jazzmin)
* **Gerenciamento de Configuração:** Arquivo `.env` com [django-environ](https://django-environ.readthedocs.io/)
* **Servidor de Aplicação WSGI (Produção):** Gunicorn
* **Servidor Web/Proxy Reverso (Produção):** Nginx
* **Exposição para Internet (Produção):** Cloudflare Tunnels (`cloudflared`)
* **Hospedagem (Produção):** Container LXC no Proxmox
* **Automação de Deploy (CI/CD):** GitHub Actions

## Estrutura do Projeto (Apps Django)

* `core`: Configurações principais do projeto Django (`settings.py`, `urls.py`, `wsgi.py`).
* `categories`: Modelos para `UrbanAspectCategory`, `ResidentialAspectCategory`, `PropertyType`.
* `points`: Modelos para `PositivePoint` e `NegativePoint` (anteriormente `characteristics`).
* `cities`: Modelo para `City`.
* `neighborhood`: Modelo para `Neighborhood`.
* `property`: Modelo para `Property` (Residência) e `Financing` (anteriormente `financing_options`).

## Configuração do Ambiente de Desenvolvimento

Siga estes passos para configurar o ambiente de desenvolvimento localmente.

### Pré-requisitos

* Python 3.10 ou superior
* Pip (gerenciador de pacotes Python)
* Git
* PostgreSQL instalado e rodando

### Passos

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/coca-mann/onde-morar
    cd onde-morar 
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente:**
    * Copie o arquivo de exemplo `.envexample` para `.env`:
        ```bash
        cp .env.example .env
        ```
    * Edite o arquivo `.env` e preencha com suas configurações locais (especialmente as do banco de dados e `DJANGO_SECRET_KEY`).

    *Exemplo de `.env.example` (e estrutura do seu `.env`):*
    ```ini
    DJANGO_SECRET_KEY=sua_chave_secreta_aqui
    DEBUG=True  # Mudar para False para produção

    # Configurações do Banco de Dados PostgreSQL
    DB_NAME=db_ondemorar
    DB_USER=user_ondemorar
    DB_PASSWORD=sua_senha_do_banco
    DB_HOST=localhost
    DB_PORT=5432
    ```

5.  **Configure o Banco de Dados PostgreSQL:**
    * Crie um usuário e um banco de dados no PostgreSQL com as credenciais que você colocou no arquivo `.env`.
        ```sql
        -- Exemplo de comandos SQL (execute como superusuário do Postgres, ex: psql -U postgres)
        CREATE USER user_ondemorar WITH PASSWORD 'sua_senha_do_banco';
        CREATE DATABASE db_ondemorar OWNER user_ondemorar;
        ```

6.  **Aplique as Migrações:**
    ```bash
    python manage.py migrate
    ```

7.  **Crie um Superusuário** (para acessar o Django Admin):
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir nome de usuário, e-mail e senha.

8.  **Rode o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    Acesse `http://127.0.0.1:8000/admin/` no seu navegador.

## Visão Geral do Deploy em Produção

Este projeto foi configurado para rodar em um container LXC no Proxmox, utilizando a seguinte pilha:

* **Nginx:** Atua como proxy reverso, recebe as requisições e serve arquivos estáticos.
* **Gunicorn:** Servidor de aplicação WSGI que roda o código Django. Comunica-se com o Nginx via Unix socket.
* **Cloudflare Tunnel (`cloudflared`):** Cria um túnel seguro entre o servidor e a rede da Cloudflare, expondo a aplicação para a internet através do subdomínio sem necessidade de abrir portas no roteador.
* **`systemd`:** Gerencia os serviços do Gunicorn e `cloudflared` para que iniciem automaticamente e sejam reiniciados em caso de falha.

**Configurações Chave em Produção:**
* O arquivo `.env` no servidor contém configurações específicas para produção (ex: `DEBUG=False`, `ALLOWED_HOSTS` restrito, senhas de produção).
* O comando `python manage.py collectstatic` é usado para juntar todos os arquivos estáticos na pasta definida por `STATIC_ROOT`.
* O Nginx é configurado para servir arquivos da pasta `STATIC_ROOT` diretamente.

## Uso da Aplicação

1.  Acesse a interface de administração.
2.  Faça login com as credenciais do superusuário.
3.  Utilize as seções do Django Admin para cadastrar e gerenciar Cidades, Bairros, Tipos de Categoria, Pontos Positivos/Negativos, Imóveis e Opções de Financiamento.

## Automação de Deploy (CI/CD)

Este repositório está configurado com GitHub Actions (`.github/workflows/deploy.yml`) para automatizar o processo de deploy para o servidor de produção.
Toda vez que um `push` é feito para a branch `main`:
1.  O GitHub Actions é acionado.
2.  Ele se conecta ao servidor de produção via SSH (usando secrets configurados no repositório).
3.  Executa os seguintes comandos no servidor:
    * `git pull` para atualizar o código.
    * Ativa o ambiente virtual.
    * `pip install -r requirements.txt` para instalar/atualizar dependências.
    * `python manage.py migrate --noinput` para aplicar migrações do banco.
    * `python manage.py collectstatic --noinput` para coletar arquivos estáticos.
    * `sudo systemctl restart gunicorn.service` para reiniciar a aplicação com o novo código.

---