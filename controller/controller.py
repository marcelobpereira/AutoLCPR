from model import Produtor
from model import Rebanho
from model import Registro

class Controller:
    """
    Controlador para gerenciamento de produtores, registros financeiros e rebanhos.

    Esta classe atua como intermediária entre o modelo e a view (arquitetura MVC) e fornece métodos
    para adicionar, buscar, remover e atualizar dados relacionados aos produtores, seus registros
    financeiros (receitas e despesas) e rebanhos.

    Attributes:
        produtores (list[Produtor]): Lista estática que armazena os produtores registrados.
    """

    produtores = []

    def __init__(self, model, view):
        """
        Inicializa uma nova instância do Controller.

        Args:
            model: Instância do modelo associado.
            view: Instância da view associada.
        """
        self.model = model
        self.view = view

    # Gestão de Produtores

    def buscar_produtor(self, id):
        """
        Busca um produtor na lista de produtores com base no seu identificador.

        Args:
            id (int): O identificador do produtor a ser buscado.

        Returns:
            Produtor: O produtor encontrado ou None se não houver correspondência.
        """
        for produtor in self.produtores:
            if produtor.id == id:
                return produtor
        return None

    def adicionar_produtor(self, produtor):
        """
        Adiciona um produtor à lista de produtores registrados.

        Verifica se o objeto informado é uma instância da classe Produtor e, caso seja,
        adiciona-o à lista. (Nota: aqui é possível adicionar lógica para verificar se o produtor
        já existe com base em seus dados, exceto o id.)

        Args:
            produtor (Produtor): O produtor a ser adicionado.

        Raises:
            ValueError: Se o objeto não for uma instância da classe Produtor.
        """
        if not isinstance(produtor, Produtor):
            raise ValueError("O objeto deve ser uma instância da classe Produtor.")
        self.produtores.append(produtor)

    def remover_produtor(self, id):
        """
        Remove um produtor da lista com base no seu identificador.

        Args:
            id (int): O identificador do produtor a ser removido.

        Raises:
            ValueError: Se o produtor não for encontrado.
        """
        produtor = self.buscar_produtor(id)
        if produtor:
            self.produtores.remove(produtor)
        else:
            raise ValueError("Produtor não encontrado.")

    def atualizar_produtor(self, id, nome=None, rebanho=None, receitas=None, despesas=None):
        """
        Atualiza os atributos de um produtor registrado.

        Apenas os atributos não nulos (não None) serão atualizados.

        Args:
            id (int): O identificador do produtor a ser atualizado.
            nome (str, optional): Novo nome para o produtor.
            rebanho (Rebanho ou list[Rebanho], optional): Novo rebanho ou lista de rebanhos.
            receitas (list[Registro], optional): Nova lista de registros de receitas.
            despesas (list[Registro], optional): Nova lista de registros de despesas.

        Raises:
            ValueError: Se o produtor não for encontrado.
        """
        produtor = self.buscar_produtor(id)
        if not produtor:
            raise ValueError("Produtor não encontrado.")
        if nome is not None:
            produtor.nome = nome
        if rebanho is not None:
            produtor.rebanho = rebanho
        if receitas is not None:
            produtor.receitas = receitas
        if despesas is not None:
            produtor.despesas = despesas

    def listar_produtores(self):
        """
        Retorna a lista de todos os produtores registrados.

        Returns:
            list[Produtor]: Lista dos produtores cadastrados.
        """
        return self.produtores

    # Gestão de Registros

    def buscar_registro(self, produtor, tipo, numero):
        """
        Busca um registro financeiro associado a um produtor com base no tipo e no número do registro.

        Args:
            produtor (Produtor): O produtor onde o registro será buscado.
            tipo (int): Define a categoria do registro. Se for maior que 0, procura em receitas;
                        caso contrário, procura em despesas.
            numero (str): Número identificador do registro.

        Returns:
            Registro: O registro encontrado ou None se não houver correspondência.
        """
        registros = produtor.receitas if tipo > 0 else produtor.despesas
        for registro in registros:
            if registro.numero == numero:
                return registro
        return None

    def adicionar_registro(self, produtor, tipo, registro):
        """
        Adiciona um registro financeiro a um produtor.

        O registro é adicionado à lista de receitas (se tipo > 0) ou à lista de despesas
        (caso contrário).

        Args:
            produtor (Produtor): O produtor que receberá o registro.
            tipo (int): Tipo do registro (positivo para receitas, zero ou negativo para despesas).
            registro (Registro): O registro a ser adicionado.

        Raises:
            ValueError: Se o objeto não for uma instância da classe Registro.
        """
        if not isinstance(registro, Registro):
            raise ValueError("O objeto deve ser uma instância da classe Registro.")
        if tipo > 0:
            produtor.receitas.append(registro)
        else:
            produtor.despesas.append(registro)

    def remover_registro(self, produtor, tipo, numero):
        """
        Remove um registro financeiro de um produtor com base no tipo e no número do registro.

        Args:
            produtor (Produtor): O produtor do qual o registro será removido.
            tipo (int): Tipo do registro (positivo para receitas, zero ou negativo para despesas).
            numero (str): Número do registro a ser removido.

        Raises:
            ValueError: Se o registro não for encontrado.
        """
        registro = self.buscar_registro(produtor, tipo, numero)
        if registro:
            registros = produtor.receitas if tipo > 0 else produtor.despesas
            registros.remove(registro)
        else:
            raise ValueError("Registro não encontrado.")

    def atualizar_registro(self, produtor, tipo, numero, data=None, descricao=None, origem=None, valor=None):
        """
        Atualiza os atributos de um registro financeiro associado a um produtor.

        Apenas os atributos cuja atualização não seja None serão modificados.

        Args:
            produtor (Produtor): O produtor cujo registro será atualizado.
            tipo (int): Tipo do registro (positivo para receitas, zero ou negativo para despesas).
            numero (str): Número identificador do registro.
            data (str, optional): Nova data do registro.
            descricao (str, optional): Nova descrição do registro.
            origem (str, optional): Nova origem do registro.
            valor (float, optional): Novo valor do registro.

        Raises:
            ValueError: Se o registro não for encontrado.
        """
        registro = self.buscar_registro(produtor, tipo, numero)
        if not registro:
            raise ValueError("Registro não encontrado.")
        if data is not None:
            registro.data = data
        if descricao is not None:
            registro.descricao = descricao
        if origem is not None:
            registro.origem = origem
        if valor is not None:
            registro.valor = valor

    def listar_registros(self, produtor, tipo):
        """
        Lista os registros financeiros de um produtor conforme o tipo especificado.

        Args:
            produtor (Produtor): O produtor do qual os registros serão listados.
            tipo (int): Define a categoria dos registros. Se for maior que 0, retorna receitas;
                        caso contrário, retorna despesas.

        Returns:
            list[Registro]: Lista dos registros financeiros correspondentes.
        """
        if tipo > 0:
            return produtor.receitas
        else:
            return produtor.despesas

    # Gestão de Rebanhos

    def buscar_rebanho(self, produtor, inscricao):
        """
        Busca um rebanho associado a um produtor com base na inscrição do rebanho.

        Args:
            produtor (Produtor): O produtor onde o rebanho será buscado.
            inscricao (str): Número de inscrição do rebanho.

        Returns:
            Rebanho: O rebanho encontrado ou None se não houver correspondência.
        """
        for rebanho in produtor.rebanho:
            if rebanho.inscricao == inscricao:
                return rebanho
        return None

    def adicionar_rebanho(self, produtor, rebanho):
        """
        Adiciona um novo rebanho ao produtor.

        Args:
            produtor (Produtor): O produtor que receberá o novo rebanho.
            rebanho (Rebanho): O rebanho a ser adicionado.

        Raises:
            ValueError: Se o objeto não for uma instância da classe Rebanho.
        """
        if not isinstance(rebanho, Rebanho):
            raise ValueError("O objeto deve ser uma instância da classe Rebanho.")
        produtor.rebanho.append(rebanho)

    def remover_rebanho(self, produtor, inscricao):
        """
        Remove um rebanho do produtor com base na inscrição.

        Args:
            produtor (Produtor): O produtor do qual o rebanho será removido.
            inscricao (str): Inscrição do rebanho a ser removido.

        Raises:
            ValueError: Se o rebanho não for encontrado.
        """
        rebanho = self.buscar_rebanho(produtor, inscricao)
        if rebanho:
            produtor.rebanho.remove(rebanho)
        else:
            raise ValueError("Rebanho não encontrado.")

    def atualizar_rebanho(self, produtor, inscricao, nome=None, entradas=None, saidas=None, consumo_mortes=None, nascimentos=None):
        """
        Atualiza os atributos de um rebanho associado a um produtor.

        Apenas os atributos cujo novo valor não seja None serão atualizados.

        Args:
            produtor (Produtor): O produtor cujo rebanho será atualizado.
            inscricao (str): Inscrição do rebanho que será atualizado.
            nome (str, optional): Novo nome do rebanho.
            entradas (int, optional): Nova quantidade de entradas.
            saidas (int, optional): Nova quantidade de saídas.
            consumo_mortes (int, optional): Nova quantidade de mortes/consumos.
            nascimentos (int, optional): Nova quantidade de nascimentos.

        Raises:
            ValueError: Se o rebanho não for encontrado.
        """
        rebanho = self.buscar_rebanho(produtor, inscricao)
        if not rebanho:
            raise ValueError("Rebanho não encontrado.")
        if nome is not None:
            rebanho.nome = nome
        if entradas is not None:
            rebanho.entradas = entradas
        if saidas is not None:
            rebanho.saidas = saidas
        if consumo_mortes is not None:
            rebanho.consumo_mortes = consumo_mortes
        if nascimentos is not None:
            rebanho.nascimentos = nascimentos

    def listar_rebanhos(self, produtor):
        """
        Lista todos os rebanhos associados a um produtor.

        Args:
            produtor (Produtor): O produtor do qual se deseja listar os rebanhos.

        Returns:
            list[Rebanho]: Lista dos rebanhos do produtor.
        """
        return produtor.rebanho