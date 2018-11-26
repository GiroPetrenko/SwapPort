# Client

import socket
import random

def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

class sp_client:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.s.sendall(b"SwapPort:" + ip.encode("UTF-8") + b":" + str(port).encode("UTF-8")) # Handshake, format: "SwapPort:127.0.0.1:10086"
        data = self.s.recv(1024)
        if data.decode("UTF-8") != "OK":
            self.s.close()
            print("CONNECTION FAILED")
        print("HANDSHAKE COMPLETE. STARTING TRANSFER...")

    def send(self, ip, data):
        __randp = random.randint(10087, 12000)
        print("SWAP!")
        print("CURRENT PORT: "+str(__randp))
        self.s.sendall(b"SwapPort:" + ip.encode("UTF-8") + b":" + str(__randp).encode("UTF-8"))
        #self.s.close()
        new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_s.connect((ip, __randp))
        new_s.sendall(data.encode("UTF-8"))
        new_s.close()

f = open("dummy.txt", "r")
foo = f.read()
fileblock = []
fileblock = list(split_by_n(foo, 512))

client = sp_client("127.0.0.1", 10086)
for i in range(len(fileblock)):
    client.send("127.0.0.1", fileblock[i])


