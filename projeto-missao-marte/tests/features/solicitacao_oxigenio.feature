Feature: Solicitação de suprimentos de oxigênio no habitat de Marte

  Scenario: Solicitação de 50 litros de oxigênio reduz o estoque disponível para 250 litros no habitat de Marte
    Given que o habitat possui 300 litros de oxigenio disponiveis
    When o astronauta solicita 50 litros extras
    Then o estoque de oxigenio atualizado deve ser de 250 litros