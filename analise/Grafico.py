import matplotlib.pyplot as plt

# Dados simulados (exemplo)
temperatura = [23, 24, 25, 24, 23, 22, 23, 24, 25, 26]
umidade = [60, 62, 61, 63, 64, 65, 64, 63, 62, 61]
tempo = list(range(1, 11))

plt.figure(figsize=(10,5))
plt.plot(tempo, temperatura, label='Temperatura (°C)', marker='o')
plt.plot(tempo, umidade, label='Umidade (%)', marker='x')
plt.title('Simulação de Dados do Sensor DHT22')
plt.xlabel('Tempo (leituras)')
plt.ylabel('Valores')
plt.legend()
plt.grid(True)
plt.savefig('analise/grafico_simulacao.png')
plt.show()

