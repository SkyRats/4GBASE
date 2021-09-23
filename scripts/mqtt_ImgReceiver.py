from paho.mqtt import client as mqtt_client
from mqtt_common import skyMqtt as sm
import PIL.Image as Image
import base64
import io

imgNumber = 0
pasta = '../temp/teste1'

def setCredentials():
    file = open('../credentials.txt', 'r')
    a = (file.read()).split()
    # broker   = a[0]
    # port     = a[1]
    # topic    = a[2]
    # username = a[3]
    # password = a[4]
    return a

def connect(a):
    client = mqtt_client.Client()
    client.username_pw_set(a[3], a[4])
    print('Connecting on: ' + a[0] + ':' + a[1])
    client.connect(a[0], int(a[1]))
    return client

def callback1(client, usrData, msg):
    global imgNumber, pasta
    print('Recebido...')
    img = Image.open(io.BytesIO(msg.payload))
    img.save(pasta + 'FOTO' + str(imgNumber) + '.jpeg')
    print('Imagem ' + str(imgNumber) + ' salva')
    imgNumber+=1

def main():
    pc = sm('../credentials.txt')
    topic = '/skyrats/mapeamento/imgs/1'
    while True:
        pc.client.subscribe(topic)
        pc.client.message_callback_add(topic, callback1)
        pc.singleHeartbeat()
        pc.client.loop(1)

if __name__ == "__main__":
    main()
