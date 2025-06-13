// sensor_dht22.ino
// Leitura do sensor DHT22 com ESP32 usando a biblioteca DHTesp
// Sensor conectado no pino GPIO 15

#include "DHTesp.h"

const int PINO_DHT = 15;
DHTesp dhtSensor;

void setup() {
  Serial.begin(115200);                       // Inicializa comunicação serial
  dhtSensor.setup(PINO_DHT, DHTesp::DHT22);  // Configura o sensor DHT22 no pino 15
}

void loop() {
  float temperatura = dhtSensor.getTemperature();  // Lê temperatura em °C
  float umidade = dhtSensor.getHumidity();         // Lê umidade relativa em %

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print(" °C\t");
  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.println(" %");

  delay(2000);  // Aguarda 2 segundos antes da próxima leitura
}

