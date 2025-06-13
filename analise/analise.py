import pandas as pd
import matplotlib.pyplot as plt

# Nome do arquivo CSV com os dados copiados do Monitor Serial
NOME_ARQUIVO_CSV = 'dados_motor.csv'

try:
    # Carrega os dados usando o pandas
    df = pd.read_csv(NOME_ARQUIVO_CSV)

    print("Dados carregados com sucesso!")
    print("Cabeçalho dos dados:")
    print(df.head())
    
    print("\nInformações básicas sobre os dados:")
    df.info()

    # --- Criação dos Gráficos ---

    # Gráfico 1: Temperatura ao longo do tempo
    plt.figure(figsize=(14, 6))
    plt.plot(df['timestamp_ms'], df['temperatura_C'], label='Temperatura (°C)', color='red', marker='o', linestyle='-')
    plt.title('Monitoramento de Temperatura do Motor ao Longo do Tempo')
    plt.xlabel('Tempo (milissegundos)')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.legend()
    plt.savefig('grafico_temperatura.png') # Salva o gráfico
    plt.show()

    # Gráfico 2: Vibração (usando o eixo X da aceleração como exemplo)
    plt.figure(figsize=(14, 6))
    plt.plot(df['timestamp_ms'], df['acel_x'], label='Vibração (Eixo X)', color='blue', marker='.')
    plt.title('Monitoramento de Vibração do Motor (Eixo X) ao Longo do Tempo')
    plt.xlabel('Tempo (milissegundos)')
    plt.ylabel('Aceleração (m/s^2)')
    plt.grid(True)
    plt.legend()
    plt.savefig('grafico_vibracao.png') # Salva o gráfico
    plt.show()

except FileNotFoundError:
    print(f"Erro: Arquivo '{NOME_ARQUIVO_CSV}' não encontrado.")
    print("Por favor, execute a simulação, copie os dados do Monitor Serial e salve-os neste arquivo.")