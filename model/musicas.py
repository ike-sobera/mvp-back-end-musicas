from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Musicas(Base):
    __tablename__ = 'musicas'

    id = Column("pk_musicas", Integer, primary_key=True, autoincrement=True)
    nome = Column(String(140), unique=True)
    bpm = Column(Integer)
    escala = Column(String(25))


    def __init__(self, nome:str, bpm:int, escala:str):
        """
        Cria um uma Música

        Arguments:
            nome: nome da música.
            bpm: informação de batidas por minuto da música
            escala: escala em que a musica foi composta
        """
        self.nome = nome
        self.bpm = bpm
        self.escala = escala