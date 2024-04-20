from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Musicas
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
musica_tag = Tag(name="Musica", description="Adição, visualização e remoção de músicas à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/musica', tags=[musica_tag],
          responses={"200": MusicasViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_musica(form: MusicasSchema):
    """Adiciona uma nova Música à base de dados

    Retorna uma representação das músicas adicionadas.
    """

    musica = Musicas(
        nome=form.nome,
        bpm=form.bpm,
        escala=form.escala)
    logger.debug(f"Adicionando música de nome: '{musica.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando música
        session.add(musica)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_musica(musica), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Música de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar música '{musica.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar música '{musica.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/musicas', tags=[musica_tag],
         responses={"200": ListagemMusicasSchema, "404": ErrorSchema})
def get_musicas():
    """Faz a busca por todas as Músicas cadastradas

    Retorna uma representação da listagem de músicas.
    """
    logger.debug(f"Coletando músicas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    musicas = session.query(Musicas).all()

    if not musicas:
        # se não há músicas cadastrados
        return {"musicas": []}, 200
    else:
        logger.debug(f"%d musicas econtrados" % len(musicas))
        # retorna a representação de música
        print(musicas)
        return apresenta_musicas(musicas), 200


@app.get('/musica', tags=[musica_tag],
         responses={"200": MusicasViewSchema, "404": ErrorSchema})
def get_musica(query: MusicasBuscaSchema):
    """Faz a busca por uma Música a partir do nome da música

    Retorna uma representação das músicas associadas.
    """
    musica_nome = query.nome
    print(query.nome)
    logger.debug(f"Coletando dados sobre música #{musica_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    musica = session.query(Musicas).filter(Musicas.nome == musica_nome).first()

    if not musica:
        # se a música não foi encontrada
        error_msg = "Música não encontrada na base :/"
        logger.warning(f"Erro ao buscar música '{musica_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Música econtrado: '{musica.nome}'")
        # retorna a representação de música
        return apresenta_musica(musica), 200


@app.delete('/musica', tags=[musica_tag],
            responses={"200": MusicasDelSchema, "404": ErrorSchema})
def del_musica(query: MusicasBuscaSchema):
    """Deleta uma Música a partir do nome de música informada

    Retorna uma mensagem de confirmação da remoção.
    """
    musica_nome = unquote(unquote(query.nome))
    print(musica_nome)
    logger.debug(f"Deletando dados sobre música #{musica_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Musicas).filter(Musicas.nome == musica_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado música #{musica_nome}")
        return {"mesage": "Música removida", "id": musica_nome}
    else:
        # se a música não foi encontrada
        error_msg = "Música não encontrada na base :/"
        logger.warning(f"Erro ao deletar música #'{musica_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
