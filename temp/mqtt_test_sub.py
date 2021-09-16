from paho.mqtt import client as mqtt_client
import PIL.Image as Image
import base64
import io

broker = 'localhost'
port = 1883
topic = '/topic/1'
username = 'Felipe'
password = 'skyrats'

def connect():
    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    #client.on_connect = connectCallback
    client.connect(broker, port)
    return client

def connectCallback():
    print("Connected")

def callback1(client, usrData, msg):
    print('Recebido...')
    img = Image.open(io.BytesIO(msg.payload))
    img.save('../temp/HAPPYDRONE.png')
    print('Imagem salva')


def main():
    client = connect()
    while True:
        client.subscribe('/topic/1')
        client.message_callback_add('/topic/1', callback1)
        client.loop(1)

if __name__ == "__main__":
    main()