from mqtt_common import skyMqtt
import urllib.request
import os

def main():
    mqtt = skyMqtt('../credentials.txt')
    global_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    mqtt.client.publish("skyrats_mavproxy", global_ip)


if __name__ == "__main__":
    main()