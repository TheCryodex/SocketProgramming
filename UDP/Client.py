from socket import *
class Client:
    servername = 'hostname'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = (input("Enter lowercase characters: "))
    clientSocket.sendto(message.encode(), (servername, serverPort))
    
    modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()
	
	
a = Client()