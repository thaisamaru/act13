import pytest
from pytest_bdd import scenarios, given, when, then
from src.gerenciador_recursos import GerenciadorRecursosMarte

scenarios('features/solicitacao_oxigenio.feature')

@pytest.fixture
def context():
    return {}

@given("que o habitat possui 300 litros de oxigenio disponiveis")
def contexto_inicial(context):
    context["gerenciador"] = GerenciadorRecursosMarte(estoque_oxigenio=300.0, estoque_agua=500.0, num_astronautas=3)

@when("o astronauta solicita 50 litros extras")
def solicitar_oxigenio(context):
    context["gerenciador"].consumir_oxigenio(50.0)

@then("o estoque de oxigenio atualizado deve ser de 250 litros")
def validar_estoque(context):
    assert context["gerenciador"].estoque_oxigenio == 250.0