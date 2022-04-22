# spacexAPI-consumer
SpaceX API consumer é um client para extrair informações de lançamentos e responder as seguintes 3 perguntas.

- Qual o ano onde houve mais lançamentos?
- Qual o launch_site onde houve mais lançamentos?
- Qual foi o total de lançamentos entre os anos de 2019-2021?


## Inicialização 
- 1 - Inicie uma venv    
    - Navegue até a pasta que deseja clonar o repositorio e inicie um ambiente virtual
    - ### Para o Windows:
    	- `py -m venv venv`
    - ### Para Linux e Mac:
    	- `python3 -m venv ./venv`

- 2 - na mesma pasta clone o repositorio do git e ative a venv
    	- `git clone  https://github.com/Massakera/spacexAPI-consumer-.git`
    - ### Para o Windows:
    	- `venv/Scripts/activate`
    - ### Para Linux e Mac:
    - `source venv/bin/activate`.

- 3 - entre na pasta spacexConsumer e installe os requirements:
    - `cd spacexConsumer`
    - `pip install --upgrade pip`
    - `pip install -r requirements.txt`
    - se estiver em Linux/Mac use `pip3` ao invés de `pip`.

- 4 - rode o servidor
    - `python3 manage.py runserver` ou `python manage.py runserver` no Windows
    - acesse `127.0.0.1:8000`.