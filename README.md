# API FLASK para fazer download dos vídeos de uma playlist

## Objetivo:

A ideia é ser possível fazer download dos vídeos de uma playlist para ter como usar no carro 
em algum local offline.

## Funcionamento:

Instalar os pacotes necessários
pip3 install -r requirements.txt

Iniciar o projeto
python3 main.py

Efetuar a verificação de funcionamento da api requisitando o status

Efetuar requests simples get para a contagem de vídeos de uma playlist passando a url da playlist

Efetuar o download dos vídeos de uma playlist passado a url da playlist

Exemplos abaixo.

## Exemplo:

#### Status da API
http://0.0.0.0:8085/api/status <br>

{"message": "Api respondendo com sucesso."}

#### Contagem dos vídeos

http://0.0.0.0:8085/playlist/count  <br>
Body_json = { "url": "https://www.youtube.com/playlist?list=sdfafweweawefwf "}

http://0.0.0.0:8085/playlist/download  <br>

Body_json = { "url": "https://www.youtube.com/playlist?list=sdfafweweawefwf "}