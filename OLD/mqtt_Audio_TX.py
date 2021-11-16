from paho.mqtt import client as mqtt_client
from mqtt_common import skyMqtt


def fileTransfer(mqtt, audio): ##### NOT WORKING!!!! #####
    file = open(audio, 'rb')
    bytes = bytearray(file.read())
    file.close()
    mqtt.client.publish("skyrats_audio_status", 1)
    mqtt.client.publish("skyrats_audio_length", int(len(bytes)/10000))
    print("Size: " + str(int(len(bytes)/10000)))
    for i in range(int(len(bytes)/10000)):
        mqtt.client.publish("skyrats", bytes[(i)*10000:(i+1)*10000])
        mqtt.client.publish("skyrats_audio_i", i)
    mqtt.client.publish("skyrats", bytes[(i+1)*10000:])    
    mqtt.client.publish("skyrats_audio_status", 0)
    mqtt.client.publish("skyrats_log", "Áudio publicado")

def audioTransfer(mqtt, audio)


    
def connectCallback():
    print("Connected")

def main():
    mqtt = skyMqtt()
    fileTransfer(mqtt, '../temp/teste.wav')


if __name__ == "__main__":
    main()