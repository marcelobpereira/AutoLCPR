class Rebanho:
    """
    Representa um rebanho de animais sob responsabilidade de um produtor rural.

    Atributos:
        inscricao (str): Número de inscrição estadual da prorpiedade em que está rebanho o formato é xx.xxx.xxx-x.
        nome (str): Nome identificador do rebanho.
        entradas (int): Quantidade de animais que entraram no rebanho.
        saidas (int): Quantidade de animais que saíram do rebanho (venda, doação, etc.).
        consumo_mortes (int): Número de animais mortos ou consumidos.
        nascimentos (int): Número de nascimentos no rebanho.

    Métodos:
        inscricao (property): Obtém ou define o número de inscrição do rebanho.
        nome (property): Obtém ou define o nome do rebanho.
        entradas (property): Obtém ou define a quantidade de entradas.
        saidas (property): Obtém ou define a quantidade de saídas.
        consumo_mortes (property): Obtém ou define o número de mortes e consumo.
        nascimentos (property): Obtém ou define a quantidade de nascimentos.
    """

    def __init__(self, inscricao: str, nome: str, entradas: int, saidas: int, consumo_mortes: int, nascimentos: int):
        self._inscricao = inscricao
        self._nome = nome
        self._entradas = entradas
        self._saidas = saidas
        self._consumo_mortes = consumo_mortes
        self._nascimentos = nascimentos

    @property
    def inscricao(self):
        return self._inscricao

    @inscricao.setter
    def inscricao(self, valor: str):
        self._inscricao = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def entradas(self):
        return self._entradas

    @entradas.setter
    def entradas(self, valor: int):
        self._entradas = valor

    @property
    def saidas(self):
        return self._saidas

    @saidas.setter
    def saidas(self, valor: int):
        self._saidas = valor

    @property
    def consumo_mortes(self):
        return self._consumo_mortes

    @consumo_mortes.setter
    def consumo_mortes(self, valor: int):
        self._consumo_mortes = valor

    @property
    def nascimentos(self):
        return self._nascimentos

    @nascimentos.setter
    def nascimentos(self, valor: int):
        self._nascimentos = valor