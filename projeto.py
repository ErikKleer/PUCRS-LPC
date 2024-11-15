import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# Função para carregar os dados do arquivo CSV
def carregar_dados(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        cabecalho = next(leitor)  # Ignora o cabeçalho
        for linha in leitor:
            linha[0] = datetime.strptime(linha[0], '%d/%m/%Y')
            linha[1] = float(linha[1])
            linha[3] = float(linha[3])
            dados.append(linha)
    return dados, cabecalho

# Função para filtrar os dados por um intervalo de tempo
def filtrar_dados_por_periodo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim):
    data_inicio = datetime(ano_inicio, mes_inicio, 1)
    data_fim = datetime(ano_fim, mes_fim, 28)
    dados_filtrados = [linha for linha in dados if data_inicio <= linha[0] <= data_fim]
    return dados_filtrados

# Função para mostrar os dados filtrados
def mostrar_dados(dados_filtrados, opcao):
    print("Exibindo dados filtrados:")
    if opcao == 1:
        for linha in dados_filtrados:
            print(linha)
    elif opcao == 2:
        for linha in dados_filtrados:
            print(f"Data: {linha[0].strftime('%Y-%m-%d')}, Precipitação: {linha[1]} mm")
    elif opcao == 3:
        for linha in dados_filtrados:
            print(f"Data: {linha[0].strftime('%Y-%m-%d')}, Temp Máx: {linha[2]}°C, Temp Mín: {linha[3]}°C")
    elif opcao == 4:
        for linha in dados_filtrados:
            print(f"Data: {linha[0].strftime('%Y-%m-%d')}, Umidade: {linha[4]}%, Vento: {linha[5]} m/s")

# Função que calcula o mês mais chuvoso
def mes_mais_chuvoso(dados):
    precip_por_mes = defaultdict(float)

    for linha in dados:
        mes_ano = linha[0].strftime('%m/%Y')  # Obtém o mês e ano no formato mm/aaaa
        precip_por_mes[mes_ano] += linha[1]

    mes_mais_chuvoso = max(precip_por_mes, key=precip_por_mes.get)
    maior_precipitacao = precip_por_mes[mes_mais_chuvoso]

    print(f"Mês mais chuvoso: {mes_mais_chuvoso}")
    print(f"Precipitação total: {maior_precipitacao:.2f} mm")

# Função para calcular a média da temperatura mínima para um mês entre 2006 e 2016
def calcular_media_temperatura_minima_por_mes(dados, mes):
    temp_minima_por_ano = defaultdict(list)

    for linha in dados:
        ano = linha[0].year
        if 2006 <= ano <= 2016 and linha[0].month == mes:
            temp_minima_por_ano[ano].append(linha[3])

    medias_temperatura_minima = {}
    for ano, temps in temp_minima_por_ano.items():
        medias_temperatura_minima[ano] = sum(temps) / len(temps)

    return medias_temperatura_minima

# Função que calcula a média geral das temperaturas mínimas do mês informado
def calcular_media_geral_temperatura_minima(medias_temperatura_minima):
    soma_medias = sum(medias_temperatura_minima.values())
    quantidade = len(medias_temperatura_minima)
    media_geral = soma_medias / quantidade if quantidade > 0 else 0
    print(f"\nMédia geral da temperatura mínima: {media_geral:.2f}°C")
    return media_geral

# Função para criar o gráfico de barras
def criar_grafico_barras(medias_temperatura_minima, mes):
    anos = list(medias_temperatura_minima.keys())
    temperaturas = list(medias_temperatura_minima.values())

    plt.bar(anos, temperaturas, color='blue')
    plt.xlabel('Ano')
    plt.ylabel('Temperatura Mínima Média (°C)')
    plt.title(f'Média da Temperatura Mínima por Ano - Mês {mes}')
    plt.show()

# Função que valida o mês informado pelo usuário
def obter_mes_usuario():
    while True:
        try:
            mes = int(input("Informe o mês (1-12): "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Mês inválido. Digite um valor entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Função que executa o menu interativo
def menu_interativo(dados):
    while True:
        try:
            print("Digite o mês e ano de início (MM/AAAA): ")
            mes_inicio, ano_inicio = map(int, input().split('/'))

            print("Digite o mês e ano de fim (MM/AAAA): ")
            mes_fim, ano_fim = map(int, input().split('/'))

            dados_filtrados = filtrar_dados_por_periodo(dados, mes_inicio, ano_inicio, mes_fim, ano_fim)

            print("Escolha uma das opções:")
            print("1 - Todos os dados")
            print("2 - Apenas precipitação")
            print("3 - Apenas temperatura (máxima e mínima)")
            print("4 - Umidade e vento")

            opcao = int(input())
            if opcao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue

            mostrar_dados(dados_filtrados, opcao)

        except ValueError:
            print("Entrada inválida. Tente novamente.")

        continuar = input("Deseja realizar outra consulta? (s/n): ")
        if continuar.lower() != 's':
            break

# Função principal
def main():
    caminho_arquivo = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'
    dados, cabecalho = carregar_dados(caminho_arquivo)

    while True:
        print("\nMenu:")
        print("1 - Visualizar dados por período")
        print("2 - Exibir mês mais chuvoso")
        print("3 - Calcular média da temperatura mínima para um mês entre 2006 e 2016")
        print("4 - Calcular média geral da temperatura mínima de um determinado mês nos últimos 11 anos")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_interativo(dados)
        elif opcao == '2':
            mes_mais_chuvoso(dados)
        elif opcao == '3':
            mes = obter_mes_usuario()
            medias_temperatura_minima = calcular_media_temperatura_minima_por_mes(dados, mes)
            for ano, media in medias_temperatura_minima.items():
                print(f"{ano}: {media:.2f}°C")
        elif opcao == '4':
            mes = obter_mes_usuario()
            medias_temperatura_minima = calcular_media_temperatura_minima_por_mes(dados, mes)
            calcular_media_geral_temperatura_minima(medias_temperatura_minima)
            criar_grafico_barras(medias_temperatura_minima, mes)
        else:
            print("Opção inválida.")

        continuar = input("Deseja voltar ao menu? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
