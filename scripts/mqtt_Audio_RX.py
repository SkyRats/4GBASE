from mqtt_common import skyMqtt
import os


def callbackAudioStatus(client, usrData, msg):
    global sair
    msg.payload = msg.payload.decode("utf-8")
    mqtt = skyMqtt()
    SUBSCRIBER = "mosquitto_sub -h " + mqtt.creds[0] + " -p " + mqtt.creds[1] + " -u " + mqtt.creds[3] + " -P " + mqtt.creds[4] + " -t skyrats_audio_file > ~/AUDIO.mp3 -C 1" #mosquitto_sub -h raspberrypi.local -t testando > audio.mp3
    if msg.payload == '1': #Receber o arquivo
        mqtt.client.publish("skyrats_audio_status", 0)
        print("Recebendo")
        os.system(SUBSCRIBER)
        print("Recebido")
        sair = 1
        play()
        os.system("rm ~/AUDIO.mp3")


def play():
    pass

def main():
    mqttMain = skyMqtt()
    while True:
        mqttMain.client.subscribe('skyrats_audio_status')
        mqttMain.client.message_callback_add('skyrats_audio_status', callbackAudioStatus)
        mqttMain.client.loop(1)

if __name__ == "__main__":
    main()