class OxigenioInsuficienteError(Exception):
    pass

class NivelEmergenciaInvalidoError(Exception):
    pass

class GerenciadorRecursosMarte:
    def __init__(self, estoque_oxigenio: float, estoque_agua: float, num_astronautas: int):
        self.estoque_oxigenio = estoque_oxigenio
        self.estoque_agua = estoque_agua
        self.num_astronautas = num_astronautas

    def calcular_consumo_diario(self, consumo_por_pessoa: float) -> float:
        return self.num_astronautas * consumo_por_pessoa

    def consumir_oxigenio(self, quantidade: float, telemetria_servico=None) -> None:
        if quantidade > self.estoque_oxigenio:
            if telemetria_servico:
                telemetria_servico.enviar_alerta_crise("Oxigênio crítico abaixo do limite!")
            raise OxigenioInsuficienteError("Estoque de oxigênio insuficiente para o consumo.")
        self.estoque_oxigenio -= quantidade