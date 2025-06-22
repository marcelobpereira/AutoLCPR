from controller.Controller import Controller
from model.Produtor import Produtor

# Cria uma instância do controlador
controller = Controller()

#testes de insercoes
def test_insercao_produtor():
    # Cria um produtor válido
    produtor = Produtor(1, "João da Silva", None, [], [])
    controller.produtores.append(produtor)
    # Verifica se o produtor foi adicionado corretamente
    assert len(controller.produtores) == 1 
def test_insercao_produtor_invalido():
    # Tenta criar um produtor inválido (sem nome)
    try:
        produtor_invalido = Produtor(2, "", None, [], [])
        controller.produtores.append(produtor_invalido)
    except ValueError as e:
        assert str(e) == "Nome do produtor não pode ser vazio."
#testes de exclusoes

#testes de consultas

#testes de atualizacoes