from paho.mqtt import client as mqtt_client

class skyMqtt():
    def __init__(self, creds):
        file = open(creds, 'r')
        self.creds = (file.read()).split()
        self.client = mqtt_client.Client()
        self.client.username_pw_set(self.creds[3], self.creds[4])
        print('Connecting on: ' + self.creds[0] + ':' + self.creds[1])
        self.client.connect(self.creds[0], int(self.creds[1]))

    def singleHeartbeat(self):
        self.client.publish('/skyrats/heartbeat', 'Connected ' + self.creds[4])

if __name__ == "__main__":
    pass
