from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True: #
    connectionSocket, addr = serverSocket.accept()
    print("Connection has been established|"+"IP: "+addr[0]+"| serverPort: "+str(addr[1]))
    sentence = str(connectionSocket.recv(1024), "utf=8")
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence, end="")
    connectionSocket.send(capitalizedSentence.encode()) 
    connectionSocket.close()
