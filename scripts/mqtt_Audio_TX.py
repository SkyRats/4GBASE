from paho.mqtt import client as mqtt_client
from mqtt_common import skyMqtt

def fileTransfer(mqtt):
    file = open('../temp/teste.wav', 'rb')
    bytes = bytearray(file.read())
    mqtt.client.publish("skyrats", bytes)
    mqtt.client.publish("skyrats/log", "Áudio publicado")
    
def connectCallback():
    print("Connected")

def main():
    mqtt = skyMqtt()
    fileTransfer(mqtt)


if __name__ == "__main__":
    main()