from controller.Controller import Controller
from model.Produtor import Produtor
from model.Registro import Registro
from model.Rebanho import Rebanho

# Cria uma instância do controlador
controller = Controller()
#CREATE
## Criar novo item com dados validos
def test_criar_produtor_valido():
    produtor = Produtor(1, "Produtor Teste", None, [], [])
    resultado = controller.criar_produtor(produtor)
    assert resultado == "Produtor criado com sucesso"
def test_criar_registro_valido():
    registro = Registro(1, "Registro Teste", "2023-10-01", 1, 1)
    resultado = controller.criar_registro(registro)
    assert resultado == "Registro criado com sucesso"
def test_criar_rebanho_valido():
    rebanho = Rebanho(1, "Rebanho Teste", 1, 100)
    resultado = controller.criar_rebanho(rebanho)
    assert resultado == "Rebanho criado com sucesso"
## Criar novo item com dados invalidos (falha)
def test_criar_produtor_invalido():
    produtor = Produtor(1, "", None, [], [])  # Nome vazio
    resultado = controller.criar_produtor(produtor)
    assert resultado == "Erro: Dados inválidos para criar produtor"
def test_criar_registro_invalido():
    registro = Registro(1, "", "2023-10-01", 1, 1)  # Nome vazio
    resultado = controller.criar_registro(registro)
    assert resultado == "Erro: Dados inválidos para criar registro"
def test_criar_rebanho_invalido():
    rebanho = Rebanho(1, "", 1, 100)  # Nome vazio
    resultado = controller.criar_rebanho(rebanho)  
    assert resultado == "Erro: Dados inválidos para criar rebanho"
## Criar novo item sem campos obrigatórios (falha)
def test_criar_produtor_sem_campos_obrigatorios():
    produtor = Produtor(None, "Produtor Teste", None, [], [])  # id ausente
    resultado = controller.criar_produtor(produtor)
    assert resultado == "Erro: Dados inválidos para criar produtor"
def test_criar_registro_sem_campos_obrigatorios():
    registro = Registro(None, "Registro Teste", "2023-10-01", 1, 1)  # numero ausente
    resultado = controller.criar_registro(registro)
    assert resultado == "Erro: Dados inválidos para criar registro"
def test_criar_rebanho_sem_campos_obrigatorios():
    rebanho = Rebanho(None, "Rebanho Teste", 1, 100)  # inscricao ausente
    resultado = controller.criar_rebanho(rebanho)
    assert resultado == "Erro: Dados inválidos para criar rebanho"
## Criar novo item com dados duplicados (falha)
def test_criar_produtor_duplicado():
    produtor = Produtor(1, "Produtor Teste", None, [], [])  # ID já existe
    resultado = controller.criar_produtor(produtor)
    assert resultado == "Erro: Produtor já existe"
def test_criar_registro_duplicado():
    registro = Registro(1, "Registro Teste", "2023-10-01", 1, 1)  # numero já existe
    resultado = controller.criar_registro(registro)
    assert resultado == "Erro: Registro já existe" 
def test_criar_rebanho_duplicado():
    rebanho = Rebanho(1, "Rebanho Teste", 1, 100)  # inscricao já existe
    resultado = controller.criar_rebanho(rebanho)
    assert resultado == "Erro: Rebanho já existe"
#READ
## Buscar item existente
def test_buscar_produtor_existente():
    resultado = controller.buscar_produtor(1)
    assert resultado is not None and resultado.id == 1
def test_buscar_registro_existente():
    resultado = controller.buscar_registro(1)
    assert resultado is not None and resultado.numero == 1
def test_buscar_rebanho_existente():
    resultado = controller.buscar_rebanho(1)
    assert resultado is not None and resultado.inscricao == 1
## Buscar item inexistente (falha)
def test_buscar_produtor_inexistente():
    resultado = controller.buscar_produtor(999)  # ID inexistente
    assert resultado is None
def test_buscar_registro_inexistente():
    resultado = controller.buscar_registro(999)  # numero inexistente
    assert resultado is None
def test_buscar_rebanho_inexistente():
    resultado = controller.buscar_rebanho(999)  # inscricao inexistente
    assert resultado is None   
## Listar todos os itens
def test_listar_produtores():
    resultado = controller.listar_produtores()
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros():
    resultado = controller.listar_registros(1)  # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_rebanhos():
    resultado = controller.listar_rebanhos(1)  # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
## Listar itens filtrados por atributo
def test_listar_produtores_filtrados():
    # Devemos criar uma opcao de listar produtores filtrados por nome
    resultado = controller.listar_produtores(1) # ID do produtor
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_produtores_filtrados_nome():
    resultado = controller.listar_produtores("Produtor Teste")  # ID do produtor e nome
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros_filtrados():
    resultado = controller.listar_registros(1, 1)  # ID do produtor e tipo de registro
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_registros_data():
    resultado = controller.listar_registros(1, 1, "2023-10-01")  # ID do produtor e data
    assert isinstance(resultado, list)  # Deve retornar uma lista
def test_listar_rebanhos_filtrados():
    resultado = controller.listar_rebanhos(1, "28.123.123-1")  # ID do produtor e inscricao do rebanho
    assert isinstance(resultado, list)  # Deve retornar uma lista  
#UPDATE
## Atualizar item existente com dados validos
def test_atualizar_produtor_valido():
    produtor = Produtor(1, "Produtor Atualizado", None, [], [])
    resultado = controller.atualizar_produtor(produtor)
    assert resultado == "Produtor atualizado com sucesso"
def test_atualizar_registro_valido():
    registro = Registro(1, "Registro Atualizado", "2023-10-02", 1, 1)
    resultado = controller.atualizar_registro(registro) 
    assert resultado == "Registro atualizado com sucesso"
def test_atualizar_rebanho_valido():
    rebanho = Rebanho(1, "Rebanho Atualizado", 1, 150)
    resultado = controller.atualizar_rebanho(rebanho)
    assert resultado == "Rebanho atualizado com sucesso"    
## Atualizar item existente com dados invalidos (falha)
def test_atualizar_produtor_invalido():
    produtor = Produtor(1, "", None, [], [])  # Nome vazio
    resultado = controller.atualizar_produtor(produtor)
    assert resultado == "Erro: Dados inválidos para atualizar produtor"
def test_atualizar_registro_invalido():
    registro = Registro(1, "", "2023-10-02", 1, 1)  # Descricao vazia
    resultado = controller.atualizar_registro(registro)
    assert resultado == "Erro: Dados inválidos para atualizar registro"
def test_atualizar_rebanho_invalido():
    rebanho = Rebanho(1, "", 1, 150)  # Nome vazio
    resultado = controller.atualizar_rebanho(rebanho)
    assert resultado == "Erro: Dados inválidos para atualizar rebanho"
## Atualizar item inexistente (falha)
def test_atualizar_produtor_inexistente():
    produtor = Produtor(999, "Produtor Inexistente", None, [], [])  # ID inexistente
    resultado = controller.atualizar_produtor(produtor)
    assert resultado == "Erro: Produtor não encontrado"
def test_atualizar_registro_inexistente():
    registro = Registro(999, "Registro Inexistente", "2023-10-02", 1, 1)  # numero inexistente
    resultado = controller.atualizar_registro(registro)
    assert resultado == "Erro: Registro não encontrado"
def test_atualizar_rebanho_inexistente():
    rebanho = Rebanho(999, "Rebanho Inexistente", 1, 150)  # inscricao inexistente
    resultado = controller.atualizar_rebanho(rebanho)
    assert resultado == "Erro: Rebanho não encontrado"
## Atualizar campos fixos (como ID) (falha)
def test_atualizar_produtor_id_fixo():
    produtor = Produtor(2, "Produtor Atualizando", None, [], [])  # Tentando mudar o ID
    resultado = controller.atualizar_produtor(1, produtor)
    assert resultado == "Erro: Não é permitido alterar o ID do produtor"
# Somente o produtor tem um campo fixo, os outros não tem.
#DELETE
## Remover item existente
def test_remover_produtor_existente():
    resultado = controller.remover_produtor(1)
    assert resultado == "Produtor removido com sucesso"
def test_remover_registro_existente():
    resultado = controller.remover_registro(1, 1)  # ID do produtor e numero do registro
    assert resultado == "Registro removido com sucesso"
def test_remover_rebanho_existente():
    resultado = controller.remover_rebanho(1, "28.123.123-1")  # ID do produtor e inscricao do rebanho
    assert resultado == "Rebanho removido com sucesso"
## Remover item inexistente (falha)
def test_remover_produtor_inexistente():
    resultado = controller.remover_produtor(999)  # ID inexistente
    assert resultado == "Erro: Produtor não encontrado"
def test_remover_registro_inexistente():
    resultado = controller.remover_registro(999, 1)  # ID do produtor inexistente
    assert resultado == "Erro: Registro não encontrado"
def test_remover_registro_inexistente2():
    resultado = controller.remover_registro(1, 999)  # numero do registro inexistente
    assert resultado == "Erro: Registro não encontrado"
def test_remover_rebanho_inexistente():
    resultado = controller.remover_rebanho(999, "28.123.123-1")  # ID do produtor inexistente
    assert resultado == "Erro: Rebanho não encontrado"
def test_remover_rebanho_inexistente2():
    resultado = controller.remover_rebanho(1, "99.999.999-9")  # inscricao do rebanho inexistente
    assert resultado == "Erro: Rebanho não encontrado"