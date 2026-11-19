from unittest.mock import MagicMock
import pytest
from src.gerenciador_recursos import OxigenioInsuficienteError
from src.servico_telemetria import ServicoTelemetriaEspacial

def test_calculo_consumo_diario(gerenciador):
    consumo = gerenciador.calcular_consumo_diario(2.5)
    assert consumo == 10.0

@pytest.mark.parametrize("estoque, consumo, esperado", [
    (100.0, 50.0, 50.0),
    (200.0, 200.0, 0.0),
])
def test_consumir_oxigenio_parametrizado(gerenciador, estoque, consumo, esperado):
    gerenciador.estoque_oxigenio = estoque
    gerenciador.consumir_oxigenio(consumo)
    assert gerenciador.estoque_oxigenio == esperado

def test_excecao_oxigenio_insuficiente(gerenciador):
    telemetria_mock = MagicMock(spec=ServicoTelemetriaEspacial)
    gerenciador.estoque_oxigenio = 10.0
    
    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.consumir_oxigenio(50.0, telemetria_servico=telemetria_mock)
    telemetria_mock.enviar_alerta_crise.assert_called_once_with("Oxigênio crítico abaixo do limite!")