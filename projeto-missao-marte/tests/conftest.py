import pytest
from src.gerenciador_recursos import GerenciadorRecursosMarte
from src.servico_telemetria import ServicoTelemetriaEspacial

@pytest.fixture(scope="session")
def parametros_iniciais():
    return {
        "oxigenio_inicial": 500.0,
        "agua_inicial": 1000.0,
        "astronautas": 4}

@pytest.fixture
def gerenciador(parametros_iniciais):
    gerenciador = GerenciadorRecursosMarte(
        estoque_oxigenio=parametros_iniciais["oxigenio_inicial"],
        estoque_agua=parametros_iniciais["agua_inicial"],
        num_astronautas=parametros_iniciais["astronautas"]
    )
    yield gerenciador
    del gerenciador