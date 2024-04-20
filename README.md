# Musicas-API

## Que projeto é esse?

Esse projeto desenvolvido para o MVP visa atender as necessidades de produtores musicais e DJs. Sempre que um produtor quer fazer algum remix de certa música, ou um DJ quer adicionar essa música ao seu set list algumas informações são necessárias e em alguns casos difíceis de achar.

Por isso desenvolvi esse projeto, onde é possível adicionar o **Nome** de uma música com outras informações cruciais, como por exemplo: **BPM** e **Escala**, depois de adicionar as músicas no banco de dados, é possível pesquisar o nome da música desejada e todas as informações digitadas vão aparecer novamente.


## Como instalar

É necessário ter todas as libs python listadas no `requirements.txt`. 

Para instalar utlize o comando

```
pip install -r requirements.txt
```
**É recomendada a instalação em um ambiente virtual!**

Para executar a API no windows basta executar o comando:

```
flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000](http://localhost:5000) no navegador para verificar o status da API em execução.
