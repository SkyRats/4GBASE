from paho.mqtt import client as mqtt_client
from mqtt_common import skyMqtt as sm
import os

def main():
    pasta = '../temp/' # '/var/tmp/'
    pc = sm()
    topic = '/skyrats/mapeamento/imgs/1'
    while True:
        for photo in os.listdir(pasta):
            if photo.startswith("image"):
                file = open(pasta + photo, 'rb')
                bytes = bytearray(file.read())
                print(len(bytes))
                pc.client.publish(topic, bytes)
                os.system('rm ' + pasta + photo)
                pc.client.loop(1)
            pc.client.loop(1)
        pc.client.loop(1)

if __name__ == "__main__":
    main()