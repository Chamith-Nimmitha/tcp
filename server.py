import socket
from threading import Thread
import datetime
import pytz


class Server_client():
    """ Connet to new client """

    num_of_online_members = 0
    online_members = {}

    def __init__(self, c, addr):
        self.c = c
        self.addr = addr
        self.name = self.c.recv(1024)
        print("##### [{}] [{} online as [{}] #####".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :'), str(self.addr), str(self.name)))
        Server_client.online_members[str(self.name)] = self.c
        Server_client.num_of_online_members += 1
        self.stat = True

    def msg_controller(self):
        while self.stat:
            self.data = self.c.recv(1024)
            if self.data == "q":
                del Server_client.online_members[self.name]
                Server_client.num_of_online_members - +1
                self.data = "{} [{}] was successfylly logged out".format(datetime.datetime.now().strftime('[%Y-%m_%d] [%H:%M:%S] :'), self.name)
                print(self.data)
                self.stat = False
            else:
                print("{} [{}] : {}".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :'), self.name, self.data))

            for self.n, self.x in Server_client.online_members.items():
                if str(self.name) != str(self.n):
                    self.x.send(self.name)
                    self.x.send(self.data)
        self.c.send("q")
        self.c.close()


def Main():
    host = '127.0.0.1'
    port = 8080
    s = socket.socket()
    s.bind((host, port))
    s.listen(3)
    print("{} server start...".format(datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M:%S] :')))
    count = 3
    while count:
        c, addr = s.accept()
        o = Server_client(c, addr)
        t = Thread(target=o.msg_controller)
        t.start()
        count -= 1


if __name__ == "__main__":
    Main()
