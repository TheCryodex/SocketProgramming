from socket import *
class TCPClient:
    serverName = '127.0.0.1'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = input("Enter a lower case message: ")
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    print("From Server: {} ".format(modifiedMessage.decode()))
    clientSocket.close()

a = TCPClient()