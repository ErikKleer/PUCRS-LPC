# PUCRS-LPC
Projeto final da matéria: Lógica e Programação de Computadores.

Neste projeto a leitura do .CSV é automática. Ele deve estar na mesma pasta do arquivo .PY e manter o nome atual.

# Análise de Dados Climáticos

Este projeto realiza a análise de dados climáticos a partir de um arquivo CSV, permitindo a filtragem e visualização de dados de precipitação, temperatura, umidade e vento em um período especificado. O código inclui um menu interativo que facilita o uso das funcionalidades descritas abaixo.

## Funcionalidades Principais

- **Carregar dados**: Lê um arquivo CSV e converte informações de data e valores numéricos para fácil manipulação.
- **Filtrar dados por período**: Extrai dados com base em um intervalo de tempo específico, fornecido pelo usuário.
- **Exibir dados filtrados**: Mostra os dados de acordo com a escolha do usuário:
  - Precipitação
  - Temperatura (máxima e mínima)
  - Umidade e velocidade do vento
- **Calcular mês mais chuvoso**: Identifica o mês com a maior quantidade de precipitação.
- **Calcular média de temperatura mínima**: Calcula a média da temperatura mínima para um mês específico, entre os anos de 2006 e 2016.
- **Exibir média geral de temperatura mínima**: Calcula e exibe a média geral da temperatura mínima para um determinado mês nos últimos 11 anos.
- **Gerar gráfico**: Cria um gráfico de barras que mostra a temperatura mínima média por ano para um mês selecionado.

## Menu Interativo

O código inclui um menu interativo que permite ao usuário:
1. Visualizar dados por período
2. Exibir o mês mais chuvoso
3. Calcular a média de temperatura mínima para um mês entre 2006 e 2016
4. Exibir a média geral de temperatura mínima para um mês específico
