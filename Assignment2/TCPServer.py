from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#소켓 생성
def socket_create():
    try:
        global host
        global serverPort
        global serverSocket
        host = ''
        serverPort = 12000
        serverSocket = socket()
        serverSocket.connect(("127.0.0.1", serverPort))
    except error as msg:
        print("soket creation error: " + str(msg))

#바인딩
def socket_bind():
    try:
        global host
        global serverPort
        global serverSocket
        print("Binding socket to serverPort: " + str(serverPort))
        print("The server is ready to receive")
        serverSocket.bind(('', serverPort))
        #serverSocket.bind((host, serverPort))
        serverSocket.listen(5)  # 왜 1이어야 함?
    except error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()

#연결 수용
def socket_accept():
    connectionSocket, address = serverSocket.accept()
    print("Connection has been established|"+"IP: "+address[0]+"| serverPort: "+str(address[1]))
    send_commands(connectionSocket)
    connectionSocket.close()

#명령
def send_commands(connectionSocket):
    while 1:
        sentence = str(connectionSocket.recv(1024), "utf=8")     # 1024, 2048 무슨 의미.
        capitalizedSentence = sentence.upper() 
        print(capitalizedSentence, end="")
        connectionSocket.send(capitalizedSentence.encode()) # encode 왜 하는거?
        

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
