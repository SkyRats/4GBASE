from mqtt_common import skyMqtt
import os

audioPath = '../temp/teste.mp3'
sair = 0

def audioTransfer(mqtt):
    mqtt.client.loop(1)
    mqtt.client.publish("skyrats_audio_status", 1) 
    while sair == 0:
        mqtt.client.subscribe('skyrats_audio_status')
        mqtt.client.message_callback_add('skyrats_audio_status', callbackAudioReturn)
        mqtt.client.loop(1)


def callbackAudioReturn(client, usrData, msg):
    global sair
    print("Enviando")
    msg.payload = msg.payload.decode("utf-8")
    mqtt = skyMqtt()
    PUBLISHER = "mosquitto_pub -h " + mqtt.creds[0] + " -p " + mqtt.creds[1] + " -u " + mqtt.creds[3] + " -P " + mqtt.creds[4] + " -t skyrats_audio_file -f " + audioPath
    print(PUBLISHER)
    if msg.payload == '0': #Enviar o arquivo
        mqtt.client.loop(2)
        os.system(PUBLISHER)
        mqtt.client.loop(1)
        mqtt.client.unsubscribe('skyrats_audio_status')
        sair = 1

    

def main():
    mqtt = skyMqtt()
    audioTransfer(mqtt)


if __name__ == "__main__":
    main()