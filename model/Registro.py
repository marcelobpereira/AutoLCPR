class Registro:
    """
    Representa um lançamento financeiro com informações de identificação, origem e valor.

    Atributos:
        numero (str): Número identificador do registro.
        data (str): Data do registro no formato 'YYYY-MM-DD'.
        descricao (str): Descrição textual do registro.
        origem (str): Origem do registro, como por exemplo 'venda', 'compra', etc.
        valor (float): Valor monetário associado ao registro.

    Métodos:
        numero (property): Retorna ou define o número do registro.
        data (property): Retorna ou define a data do registro.
        descricao (property): Retorna ou define a descrição.
        origem (property): Retorna ou define a origem.
        valor (property): Retorna ou define o valor.
    """
    def __init__(self, numero: str, data: str, descricao: str, origem: str, valor: float):
        self._numero = numero
        self._data = data
        self._descricao = descricao
        self._origem = origem
        self._valor = valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor: str):
        self._numero = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor: str):
        self._data = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor: str):
        self._descricao = valor

    @property
    def origem(self):
        return self._origem

    @origem.setter
    def origem(self, valor: str):
        self._origem = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        self._valor = valor