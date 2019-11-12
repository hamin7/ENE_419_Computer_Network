# This is a simple port-forward / proxy, written using only the default python
# library. If you want to make a suggestion or fix something you can contact-me
# at voorloop_at_gmail.com
# Distributed over IDC(I Don't Care) license
import socket
import select
import time
import sys

# Changing the buffer_size and delay, you can improve the speed and bandwidth.
# But when buffer get to high or delay go too down, you can broke things
buffer_size = 4096
delay = 0.0001
forward_to = ('smtp.zaz.ufsk.br', 25)

# Foward 클래스는 프록시와 원격서버(원래의 타겟) 사이의 연결을 확립을 담당.
class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception, e:
            print e
            return False

class TheServer:
    # input_list는 select.selct에 의해 관리되고 있는 사용할 수 있는 모든 소켓을 저장. 처음에는 서버소켓이 저장.
    input_list = []
    channel = {}

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(200)

    def main_loop(self):
        self.input_list.append(self.server)
        while 1:
            time.sleep(delay)
            ss = select.select
            inputready, outputready, exceptready = ss(self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.server:
                    # 소켓의 각각의 새로운 연결은 on_accept() 메소드를 트리거.
                    self.on_accept()
                    break

                # 만약 현재의 소켓이 선택되어 리턴 된 새로운 연결이 아니라면 이것은 수신되는 데이터(서버로부터 or 클라이언트로부터)로서 고려되어야 한다.
                self.data = self.s.recv(buffer_size)
                # 만약 데이터의 길이가 0이라면 요청을 닫고, 패킷은 올바른 목적지로 포워딩 되어야한다.
                if len(self.data) == 0:
                    self.on_close()
                    break
                else:
                    self.on_recv()

    def on_accept(self):
        forward = Forward().start(forward_to[0], forward_to[1])
        clientsock, clientaddr = self.server.accept()
        if forward:
            print clientaddr, "has connected"
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print "Can't establish connection with remote server.",
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_close(self):
        print self.s.getpeername(), "has disconnected"
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        data = self.data
        # here we can parse and/or modify the data before send forward
        print data
        self.channel[self.s].send(data)

if __name__ == '__main__':
        server = TheServer('', 9090)
        try:
            server.main_loop()
        except KeyboardInterrupt:
            print "Ctrl C - Stopping server"
            sys.exit(1)