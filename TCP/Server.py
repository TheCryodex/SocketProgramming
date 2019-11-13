from socket import *

class TCPServer:
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print("Server is ready to recieve")
    while True:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(2048).decode()
        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage.encode())
        connectionSocket.close()
           
b = TCPServer()