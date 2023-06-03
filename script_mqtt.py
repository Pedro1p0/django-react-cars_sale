import time
import random
import paho.mqtt.client as mqtt

# Configurações do MQTT
broker = 'test.mosquitto.org'  # Endereço do servidor MQTT
port = 1883  # Porta do servidor MQTT
topic = 'Teste_Loja1'  # Tópico para publicação das mensagens

# Função para tratar evento de publicação bem-sucedida
def on_publish(client, userdata, mid):
    print('Mensagem publicada com sucesso')

# Criação do cliente MQTT
client = mqtt.Client()

# Configuração das funções de retorno de chamada
client.on_publish = on_publish

# Conexão ao servidor MQTT
client.connect(broker, port)

# Loop de publicação de mensagens
while True:
    # Gera uma mensagem aleatória
    mensagem = 'Mensagem aleatoria: ' + str(random.randint(1, 100))
    
    # Publica a mensagem no tópico
    client.publish(topic, mensagem, placa_do_carro)
    
    # Aguarda 5 segundos
    time.sleep(5)
