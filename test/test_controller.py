import pytest
from controller.Controller import Controller
from model.Produtor import Produtor
from model.Registro import Registro
from model.Rebanho import Rebanho

# Cria uma instância do controlador
controller = Controller()
#CREATE
## Criar novo item com dados validos

def test_criar_produtor_valido(): #OK
    resultado = controller.criar_produtor(1, "Produtor Teste", [], [], [])
    assert resultado == True

def test_criar_registro_valido(): 
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    registro = Registro(1, "Registro Teste", "2023-10-01", 1, 1)
    resultado = controller.criar_registro(registro)
    assert resultado == True

def test_criar_rebanho_valido():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    resultado = controller.criar_rebanho(1, "123.123, ""Rebanho Teste", 1, 100)
    assert resultado == True

## Criar novo item com dados invalidos (falha)
def test_criar_produtor_invalido(): #OK
    with pytest.raises(ValueError) as exc_info:
        controller.criar_produtor(1, "", [], [], [])
    assert str(exc_info.value) == "Erro: Dados inválidos para criar produtor"

def test_criar_registro_sem_numero():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar registro com numero vazio
    with pytest.raises(ValueError) as exc_info:
            controller.criar_registro(Registro(1, "", "2023-10-01", "Registro Teste", 1, 1))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar registro"
def test_criar_registro_com_descricao_invalida():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar registro com descricao vazia
    with pytest.raises(ValueError) as exc_info:
            controller.criar_registro(Registro(1, "123.123", "2023-10-01", "", 1, 1))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar registro"  
def test_criar_registro_com_descricao_vazia():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar registro com descricao vazia
    with pytest.raises(ValueError) as exc_info:
            controller.criar_registro(Registro(1, "123.123", "2023-10-01", None, 1, 1))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar registro"  
def test_criar_registro_data_vazia():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar registro com numero vazio
    with pytest.raises(ValueError) as exc_info:
            controller.criar_registro(Registro(1, "", "2023-10-01", 1, 1))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar registro"          

def test_criar_rebanho_nome_invalido():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar rebanho com nome vazio
    with pytest.raises(ValueError) as exc_info:
        controller.criar_rebanho(Rebanho(1, "12.123.123-2","", 1, 100))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar rebanho"
def test_criar_rebanho_inscricao_invalida():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar rebanho com inscricao vazia
    with pytest.raises(ValueError) as exc_info:
        controller.criar_rebanho(Rebanho(1, "", "Rebanho Teste", 1, 100))
    assert str(exc_info.value) == "Erro: Dados inválidos para criar rebanho"

def test_criar_produtor_sem_campos_obrigatorios(): #OK
    with pytest.raises(ValueError) as exc_info:
        controller.criar_produtor(None, "Produtor Teste", [], [], [])
    assert str(exc_info.value) == "Erro: Dados inválidos para criar produtor"

def test_criar_registro_sem_campos_obrigatorios():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    # tenta criar registro com campos obrigatorios ausentes
    with pytest.raises(ValueError) as exc_info:
        controller.criar_registro(None, "Registro Teste", "2023-10-01", 1, 1) 
    assert str(exc_info.value) == "Erro: Dados inválidos para criar registro"

def test_criar_rebanho_sem_campos_obrigatorios():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.criar_rebanho(1, None, "Rebanho Teste", 1, 100)
    assert str(exc_info.value) == "Erro: Dados inválidos para criar rebanho"

## Criar novo item com dados duplicados (falha)
def test_criar_produtor_duplicado(): #OK
    controller.produtores.append(Produtor(1, "Produtor Teste", None, [], []))  # Adiciona um produtor para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.criar_produtor(1, "Produtor Teste", [], [], [])
    assert str(exc_info.value) == "Erro: Produtor já existe"

def test_criar_registro_duplicado():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro(1, "123.123","Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.criar_registro(1, "123.123", "Registro Teste", "2023-10-01", 1, 1)
    assert str(exc_info.value) == "Erro: Registro já existe"

def test_criar_rebanho_duplicado():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho(1, "28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.criar_rebanho(1, "28.123.123-1", "Rebanho Teste", 1, 100)  
    assert str(exc_info.value) == "Erro: Rebanho já existe"

#READ
## Buscar item existente
def test_buscar_produtor_existente(): #OK
    produtor = Produtor(1, "Produtor Teste", [], [], [])
    controller.produtores.append(produtor)  # Adiciona o produtor para o teste
    resultado = controller.buscar_produtor(1)
    assert resultado is not None and resultado.id == 1
def test_buscar_registro_existente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro(1, "123.123", "Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    resultado = controller.buscar_registro("123.123")
    assert resultado is not None and resultado.numero == "123.123"
def test_buscar_rebanho_existente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho(1, "28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    resultado = controller.buscar_rebanho("28.123.123-1")
    assert resultado is not None and resultado.inscricao == "28.123.123-1"

## Buscar item inexistente (falha)
def test_buscar_produtor_inexistente(): #OK
    resultado = controller.buscar_produtor(999)  # ID inexistente
    assert resultado is None
def test_buscar_registro_inexistente():
    resultado = controller.buscar_registro(1, 1, "999")  # numero inexistente
    assert resultado is None
def test_buscar_rebanho_inexistente():
    resultado = controller.buscar_rebanho(1, "12.123.123-1")  # inscricao inexistente
    assert resultado is None   
## Listar todos os itens
def test_listar_produtores():#OK
    produtor = Produtor(1, "Produtor Teste", [], [], [])
    controller.produtores.append(produtor)  # Adiciona o produtor para o teste
    resultado = controller.listar_produtores()
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros():
    resultado = controller.listar_registros(1, 1)  # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_rebanhos():
    resultado = controller.listar_rebanhos(1)  # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
## Listar itens filtrados por atributo
def test_listar_produtores_por_id():#OK
    produtor = Produtor(1, "Produtor Teste", [], [], [])
    controller.produtores.append(produtor)  # Adiciona o produtor para o teste
    resultado = controller.listar_produtores_por_id(1)  # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_produtores_filtrados_nome():#OK
    produtor = Produtor(1, "Produtor Teste", [], [], [])
    controller.produtores.append(produtor)  # Adiciona o produtor para o teste
    resultado = controller.listar_produtores_por_nome("Produtor Teste")  # ID do produtor e nome
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros_por_tipo():
    resultado = controller.listar_registros(1, 1)  # ID do produtor e tipo de registro
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros_por_data():
    resultado = controller.listar_registros(1, 1, "2023-10-01")  # ID do produtor e data
    assert isinstance(resultado, list)  # Deve retornar uma lista


#UPDATE
## Atualizar item existente com dados validos
def test_atualizar_produtor_valido(): #OK
    produtor = Produtor(1, "Produtor Teste", None, [], [])
    controller.produtores.append(produtor)  # Adiciona o produtor para o teste
    resultado = controller.atualizar_produtor(1, "Produtor Atualizado", None, [], [])
    assert resultado == True

def test_atualizar_registro_valido():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro(1, "123.123", "Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    resultado = controller.atualizar_registro(1, "123.123", "Registro Atualizado", "2023-10-02", 1, 1)
    assert resultado == True

def test_atualizar_rebanho_valido():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho(1, "28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    resultado = controller.atualizar_rebanho(1, "28.123.123-1", "Rebanho Atualizado", 1, 150)
    assert resultado == True

## Atualizar item existente com dados invalidos (falha)

def test_atualizar_produtor_invalido(): #OK
    produtor = Produtor(1, "", [], [], [])  # Nome vazio
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_produtor(produtor) 
    assert str(exc_info.value) == "Erro: Dados inválidos para atualizar produtor"

def test_atualizar_registro_invalido():
    registro = Registro(1, "123.123", "", "2023-10-01", 1, 1)  # Descricao vazia
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_registro(registro)
    assert str(exc_info.value) == "Erro: Dados inválidos para atualizar registro"

def test_atualizar_rebanho_invalido():
    rebanho = Rebanho(1, "28.123.123-1", "", 1, 100)  # Nome vazio
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_rebanho(rebanho)
    assert str(exc_info.value) == "Erro: Dados inválidos para atualizar rebanho"

## Atualizar item inexistente (falha)
def test_atualizar_produtor_inexistente():#OK
    produtor = Produtor(999, "Produtor Inexistente", None, [], [])  # ID inexistente
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_produtor(produtor)
    assert str(exc_info.value) == "Erro: Produtor não encontrado"

def test_atualizar_registro_inexistente():
    registro = Registro(999, "Registro Inexistente", "2023-10-02", 1, 1)  # numero inexistente
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_registro(registro)
    assert str(exc_info.value) == "Erro: Registro não encontrado"

def test_atualizar_rebanho_inexistente():
    rebanho = Rebanho(999, "Rebanho Inexistente", 1, 150)  # inscricao inexistente
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_rebanho(rebanho)
    assert str(exc_info.value) == "Erro: Rebanho não encontrado"

## Atualizar campos fixos (como ID) (falha)
def test_atualizar_produtor_id_fixo(): #OK
    # 1) registra o produtor original com ID=1
    original = Produtor(1, "Produtor Teste", None, [], [])
    controller.produtores.append(original)

    # 2) cria um novo Produtor (com ID diferente 2)
    novo = Produtor(2, "Produtor Atualizado", None, [], [])

    # 3) chama o método COM O PRODUTOR como segundo argumento
    with pytest.raises(ValueError) as exc_info:
        controller.atualizar_produtor(1, novo)

    assert str(exc_info.value) == "Erro: Não é permitido alterar o ID do produtor"
# Somente o produtor tem um campo fixo, os outros não tem.


#DELETE
## Remover item existente
def test_excluir_produtor_existente(): #OK
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    resultado = controller.excluir_produtor(1)
    assert resultado == True

def test_remover_registro_existente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro("123.123", "Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    resultado = controller.remover_registro(1, 1, "123.123")  # ID do produtor, tipo e numero do registro
    assert resultado == True

def test_remover_rebanho_existente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho("28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    resultado = controller.remover_rebanho(1, "28.123.123-1")  # ID do produtor e inscricao do rebanho
    assert resultado == True
## Remover item inexistente (falha)
def test_excluir_produtor_inexistente(): #OK
    controller.produtores.append(Produtor(1, "Produtor Teste", None, [], []))  # Adiciona um produtor para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.excluir_produtor(999)  # ID inexistente
    assert str(exc_info.value) == "Erro: Produtor não encontrado"

def test_remover_registro_inexistente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro("123.123", "Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    #testa a remocao de um registro de um produtor inexistente
    with pytest.raises(ValueError) as exc_info:
        controller.remover_registro(999, "123.123")
    assert str(exc_info.value) == "Erro: Produtor não encontrado"

def test_remover_registro_inexistente2():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).registros.append(Registro("123.123", "Registro Teste", "2023-10-01", 1, 1))  # Adiciona um registro para o teste
    #testa remocao de um registro inexistente
    with pytest.raises(ValueError) as exc_info:
        controller.remover_registro(1, "999.999") 
    assert str(exc_info.value) == "Erro: Registro não encontrado"

def test_remover_rebanho_inexistente():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho("28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.remover_rebanho(999, "28.123.123-1")  # produtor inexistente
    assert str(exc_info.value) == "Erro: Produtor não encontrado"

def test_remover_rebanho_inexistente2():
    controller.produtores.append(Produtor(1, "Produtor Teste", [], [], []))  # Adiciona um produtor para o teste
    controller.produtores(1).rebanhos.append(Rebanho("28.123.123-1", "Rebanho Teste", 1, 100))  # Adiciona um rebanho para o teste
    with pytest.raises(ValueError) as exc_info:
        controller.remover_rebanho(1, "99.999.999-9") #inscricao do rebanho inexistente
    assert str(exc_info.value) == "Erro: Rebanho não encontrado"