from model.Produtor import Produtor
from model.Rebanho import Rebanho
from model.Registro import Registro

class Controller:
    def __init__ (self):
        self.produtores = []
    def buscar_produtor(self, id):
        """Busca um produtor pelo ID."""
        return next((produtor for produtor in self.produtores if produtor.id == id), None)
    
    """Retorna uma lista com todos os produtores"""
    def listar_produtores(self):
        return list(self.produtores)
    def listar_produtores_por_nome(self, nome):
        """Lista os produtores filtrados por nome."""
        return [produtor for produtor in self.produtores if nome.lower() in produtor.nome.lower()]
    def listar_produtores_por_id(self, id):
        """Lista os produtores filtrados por ID."""
        return [produtor for produtor in self.produtores if produtor.id == id]
    def criar_produtor(self, id, nome, rebanho=None, receitas=None, despesas=None):
        if id is None or not isinstance(id, int):
            raise ValueError("Erro: Dados inválidos para criar produtor")
        if not nome or not nome.strip():
            raise ValueError("Erro: Dados inválidos para criar produtor")
        if self.buscar_produtor(id) is not None:
            raise ValueError("Erro: Produtor já existe")
        rebanho = rebanho if rebanho is not None else []
        receitas = receitas if receitas is not None else []
        despesas = despesas if despesas is not None else []
        produtor = Produtor(id, nome, rebanho, receitas, despesas)
        self.produtores.append(produtor)
        return True  # Retorna True para indicar sucesso

    def excluir_produtor(self, id):
        """Exclui um produtor pelo ID."""
        produtor = self.buscar_produtor(id)
        if produtor is None:
            raise ValueError("Erro: Produtor não encontrado")
        self.produtores.remove(produtor)
        return True  # Retorna True para indicar sucesso

    def atualizar_produtor(self, id, nome=None, rebanho=None, receitas=None, despesas=None):
        # --- 1) se só veio 1 argumento (o próprio Produtor)
        if nome is None and isinstance(id, Produtor):
            prod = id
            id, nome = prod.id, prod.nome
            rebanho, receitas, despesas = prod.rebanho, prod.receitas, prod.despesas
        # --- 2) se vier (id, Produtor) no lugar de (id, nome)
        elif isinstance(nome, Produtor):
            prod = nome
            if prod.id != id:
                raise ValueError("Erro: Não é permitido alterar o ID do produtor")
            nome = prod.nome
            rebanho, receitas, despesas = prod.rebanho, prod.receitas, prod.despesas
        # --- 3) aqui é o caso (id, nome, rebanho, receitas, despesas) mesmo
        # Validações comuns
        if id is None or not isinstance(id, int):
            raise ValueError("Erro: ID inválido para atualizar produtor")
        produtor = self.buscar_produtor(id)
        if produtor is None:
            raise ValueError("Erro: Produtor não encontrado")
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Erro: Dados inválidos para atualizar produtor")
        # Aplica atualização
        produtor.nome     = nome
        produtor.rebanho  = rebanho  if rebanho  is not None else []
        produtor.receitas = receitas if receitas is not None else []
        produtor.despesas = despesas if despesas is not None else []
        return True
