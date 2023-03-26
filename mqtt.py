import paho.mqtt.client as mqtt
import time

#definir configurações broker
broker_address = "localhost"
broker_port = 1883

#definir callback
def on_message(client, userdata, message):
    print("Mensagem recebida: ", str(message.payload.decode("utf-8")))

#mqtt client callback
client = mqtt.client("Python")
client.on_message = on_message

#client-broker
client.connect(broker_address, broker_port)

client.subscribe("teste/topico")

#loop de escuta para recber msg
client.loop_star()

#enviar msg para topico
client.publish("teste/topico", "teste")

time.sleep(4)

client.loop_stop()
client.disconnect()
