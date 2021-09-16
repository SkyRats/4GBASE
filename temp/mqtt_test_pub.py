from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = '/topic/1'
username = 'Felipe'
password = 'skyrats'


def connect():
    client = mqtt_client.Client()
    client.username_pw_set(username, password)
    client.on_connect = connectCallback
    client.connect(broker, port)
    return client

def fileTransfer(client):
    file = open('/home/felipe/HAPPYDRONE.png', 'rb')
    bytes = bytearray(file.read())
    client.publish(topic, bytes)

def connectCallback():
    print("Connected")

def main():
    client = connect()
    fileTransfer(client)


if __name__ == "__main__":
    main()