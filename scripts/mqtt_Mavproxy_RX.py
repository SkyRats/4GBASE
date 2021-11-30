from mqtt_common import skyMqtt
import os

def callback_mavproxy(client, usrData, msg):
    mavproxy_command = "mavproxy.py --master=/dev/ttyACM0,57600 --out=udpbcast:" + msg.payload + ":14550"
    os.system(mavproxy_command)

def main():
    mqtt = skyMqtt('../credentials.txt')
    while True:
        mqtt.client.subscribe('skyrats_mavproxy')
        mqtt.client.message_callback_add('skyrats_mavproxy', callback_mavproxy)
        mqtt.client.loop(1)


if __name__ == "__main__":
    main()