from pydantic import BaseModel
from typing import Optional, List
from model.musicas import Musicas



class MusicasSchema(BaseModel):
    """ Define como uma nova música a ser inserida deve ser representada
    """
    nome: str = "Teto Baixo"
    bpm: int = 130
    escala: str = "D#maj"


class MusicasBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da música.
    """
    nome: str


class ListagemMusicasSchema(BaseModel):
    """ Define como uma listagem de músicas será retornada.
    """
    musicas:List[MusicasSchema]


def apresenta_musicas(musicas: List[Musicas]):
    """ Retorna uma representação da música seguindo o schema definido em
        MusicasViewSchema.
    """
    result = []
    for musica in musicas:
        print("nome", musica.nome)
        result.append({
            "nome": musica.nome,
            "bpm": musica.bpm,
            "escala": musica.escala,
        })
    print(result)
    return {"musicas": result}


class MusicasViewSchema(BaseModel):
    """ Define como uma música será retornada
    """
    id: int = 1
    nome: str = "Teste de música"
    bpm: Optional[int] = 130
    escala: str = "D#maj"


class MusicasDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_musica(musica: Musicas):
    """ Retorna uma representação da música seguindo o schema definido em
        MusicasViewSchema.
    """

    return {
        "id": musica.id,
        "nome": musica.nome,
        "bpm": musica.bpm,
        "escala": musica.escala,
    }
