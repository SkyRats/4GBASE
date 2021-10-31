from paho.mqtt import client as mqtt_client
from pydub import AudioSegment
from mqtt_common import skyMqtt
#from pydub.playback import play
import io

def callback1(client, usrData, msg):
    print('Recebido...')
    data= msg.payload.read()
    song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
    song.export("../temp/HAPPYaudio.mp3", format="mp3")
    #play(song)
    print('Audio salvo')


def main():
    mqtt = skyMqtt()
    while True:
        mqtt.client.subscribe('skyrats')
        mqtt.client.message_callback_add('skyrats', callback1)
        mqtt.client.loop(1)

if __name__ == "__main__":
    main()