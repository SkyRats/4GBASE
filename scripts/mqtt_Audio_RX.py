from paho.mqtt import client as mqtt_client
from pydub import AudioSegment
from mqtt_common import SkyMqtt as sm
#from pydub.playback import play
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
    data= msg.payload.read()
    song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
    song.export("HAPPYaudio.mp3", format="mp3")
    #play(song)
    print('Audio salvo')


def main():
    client = connect()
    #pc=sm()
    while True:
        client.subscribe('/topic/1')
        client.message_callback_add('/topic/1', callback1)
        client.loop(1)

if __name__ == "__main__":
    main()