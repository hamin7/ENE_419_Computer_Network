### 1. Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and applicationlayer protocols besides HTTP are needed in this scenario?
지정된 URL에서 웹 문서를 검색하려는 HTTP 클라이언트를 고려하십시오. 그 HTTP 서버의 IP 주소를 처음에 알 수 없다. 이 시나리오에서 HTTP 외에 어떤 전송 및 애플리케이션 계층 프로토콜이 필요한가?

https://wiki.eecs.yorku.ca/course_archive/2012-13/W/3214/_media/chapter2_examples_problems_1slide.pdf

### 2. Write a simple TCP program for a server that accepts lines of input from a client and prints the lines onto the server’s standard output. (Please modify the following TCPServer.py program) Compile and execute your program. On any other machine that contains a Web browser, set the proxy server in the browser to the host that is running your server program (localhost); also configure the port number appropriately. Your browser should now send its GET request messages to your server, and your server should display the messages on its standard output. Use this platform to determine whether your browser generates conditional GET messages for objects that are locally cached. Write your server code and the output result from your server in execution.

클라이언트에서 입력 라인을 수신하여 해당 라인을 서버의 표준 출력으로 인쇄하는 서버에 대한 간단한  TCP program를 작성하십시오. (다음 TCPServer.py 프로그램을 수정하십시오) 프로그램을 컴파일하여 실행하십시오. 웹 브라우저가 포함된 다른 시스템에서 브라우저의 프록시 서버를 서버 프로그램(localhost)을 실행하는 호스트로 설정하고 포트 번호도 적절하게 구성하십시오. 이제 브라우저가 GET 요청 메시지를 서버로 보내고, 서버가 표준 출력에 메시지를 표시해야 한다. 이 플랫폼을 사용하여 브라우저가 로컬로 캐시된 개체에 대해 조건부 GET 메시지를 생성하는지 여부를 확인하십시오. 서버 코드와 실행 중인 서버의 출력 결과를 기록하십시오.

TCPServer.py
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((‘’,serverPort))
serverSocket.listen(1)
print ‘The server is ready to receive’
while 1:
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(1024)
capitalizedSentence = sentence.upper()
connectionSocket.send(capitalizedSentence)
connectionSocket.close()

https://www.keycdn.com/blog/http-cache-headers
https://stonerain.tistory.com/8
https://itstory.tk/entry/Spring-MVC-LastModified-IfModifiedSince-%EC%BA%90%EC%8B%9C-%EC%84%A4%EC%A0%95

### 3. With the SR protocol, it is possible for the sender to receive an ACK for a packet that falls outside of its current window. Is this true of false? Justify your answer briefly.
SR 프로토콜을 사용하면 송신자가 현재 창 밖에 있는 패킷에 대한 ACK를 수신할 수 있다. 이게 거짓인가? 대답을 짧게 정당화하라.

True.

Suppose the sender has a window size of 3 and sends packets 1, 2, 3 at 𝑡0. 

At 𝑡1 (𝑡1 > 𝑡0) the receiver ACKs 1, 2, 3. 

At 𝑡2 (𝑡2 > 𝑡1) the sender times out and resends 1, 2, 3. 

At 𝑡3 the receiver receives the duplicates and re-acknowledges 1, 2, 3. 

At 𝑡4 the sender receives the ACKs that the receiver sent at 𝑡1 and advances its window to 4, 5, 6. 

At 𝑡5 the sender receives the ACKs 1, 2, 3 the receiver sent at 𝑡2. 

These ACKs are outside its window.

http://www.cmlab.csie.ntu.edu.tw/~rod24574575/CN2015/homeworks/hw4_sol.pdf
