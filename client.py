import socket
from threading import Thread
import datetime
import pytz


class Client():

    def __init__(self):
        self.host = "127.0.01"
        self.port = 8080
        self.s = socket.socket()
        self.s.connect((self.host, self.port))

        self.name = raw_input("User name : ")
        self.s.send(self.name)

        self.t = Thread(target=self.get_msg)
        self.t.start()

        while True:
            self.data = raw_input("{} [{}] : ".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :'), self.name))
            self.s.send(self.data)
            if str(self.data) == "q":
                break

    def get_msg(self):
        while True:
            self.cname = self.s.recv(1024)
            if str(self.cname) == "q" or str(self.cname) == "":
                print("{} You have successfully logged out...".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :')))
                break
            self.cdata = self.s.recv(1024)
            print("{} [{}] : {}".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :'), str(self.cname), str(self.cdata)))
        self.s.close()


def Main():
    Client()


if __name__ == "__main__":
    Main()
