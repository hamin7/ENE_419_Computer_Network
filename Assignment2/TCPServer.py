from socket import *
#import requests
#from httpcache import CachingHTTPAdapter
#from httpcache import HTTPcache

#s = requests.Session()
#s.mount('http://', CachingHTTPAdapter())

#cache = httpcache(capacity=50)
#cache.store(response)

#cached_response = cache.retrieve(requests)

#print(cached_response)

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connection has been established|"+"IP: "+addr[0]+"| serverPort: "+str(addr[1]))
    sentence = str(connectionSocket.recv(1024), "utf=8")
    capitalizedSentence = sentence.upper()
    print(capitalizedSentence, end="")
    connectionSocket.send(capitalizedSentence.encode()) 
    connectionSocket.close()
