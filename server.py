# Server

import socket
import time

# Server's role is to receive

class sp_server:
    def __init__(self, ip, init_port):
        print("--- * CONF * ---")
        print("IP: " + ip)
        print("PORT: " + str(init_port))
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, init_port))
        self.s.listen(1)
        self.conn, self.addr = self.s.accept()
        print("Got connection.")
        print("Client info: " + str(self.addr))
        data = self.conn.recv(1024)
        if data.decode("UTF-8") == "SwapPort:" + ip + ":" + str(init_port):
            self.conn.sendall(b"OK") # Send OK
        else:
            self.conn.sendall(b"FAIL") # Handshake failed
            self.conn.close()
            print("CLIENT CONNECTION FAIL")
    def receive(self, ip):  # Positive to receive
        data = self.conn.recv(1024)
        data = data.decode("UTF-8")
        data_ = data.split(":")
        #print(data_)
        #print("SWAPPED TO "+data_[2])
        newS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newS.bind((ip, int(data_[2])))
        newS.listen(1)
        conn, addr = newS.accept()
        print(conn.recv(1024).decode("UTF-8"))
        conn.close()

        

server = sp_server("127.0.0.1", 10086)
while True:
    server.receive("127.0.0.1")