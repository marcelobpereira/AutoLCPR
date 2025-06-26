from model.Rebanho import Rebanho
from model.Registro import Registro

class Produtor:
    """
    Representa um produtor rural, englobando informações pessoais, o rebanho sob sua responsabilidade
    e os registros financeiros (receitas e despesas).

    Attributes:
        _id (int): Identificador único do produtor.
        _nome (str): Nome do produtor.
        _rebanho (Rebanho): Instância(S) da classe Rebanho associada(S) ao produtor. (um produtor pode ter vários rebanhos).
        _receitas (list[Registro]): Lista de registros financeiros referentes às receitas (entradas de recursos).
        _despesas (list[Registro]): Lista de registros financeiros referentes às despesas (saídas de recursos).

    Methods:
        id: Propriedade para obter ou definir o identificador do produtor.
        nome: Propriedade para obter ou definir o nome do produtor.
        rebanho: Propriedade para obter ou definir o rebanho associado.
        receitas: Propriedade para obter ou definir a lista de receitas.
        despesas: Propriedade para obter ou definir a lista de despesas.
    """

    def __init__(self, id: int, nome: str, rebanho: list[Rebanho], receitas: list[Registro], despesas: list[Registro]):
        self._id = id
        self._nome = nome
        self._rebanho = [Rebanho]  # Um produtor pode ter vários rebanhos, iniciando com uma lista
        self._receitas = [Registro] #Lista de registros financeiros referentes às receitas
        self._despesas = [Registro]    #Lista de registros financeiros referentes às despesas

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def rebanho(self):
        return self._rebanho

    @rebanho.setter
    def rebanho(self, valor: Rebanho):
        self._rebanho = valor

    @property
    def receitas(self):
        return self._receitas

    @receitas.setter
    def receitas(self, valor: list):
        self._receitas = valor

    @property
    def despesas(self):
        return self._despesas

    @despesas.setter
    def despesas(self, valor: list):
        self._despesas = valor