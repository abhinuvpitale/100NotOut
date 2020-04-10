from socket import *
import math

BUFFERSIZE = 10	

def getHttpRequest(query):
    query = 'GET '+ query + ' HTTP/1.0'
    return query

def sendData(data, sendSocket, buffer_size=10):
    data = data.encode()
    size = len(data)
    numberOfPackets = int(math.ceil((size*1.0/buffer_size)))
    sendSocket.send(str(numberOfPackets))
    packetNumber = 0
    while packetNumber < numberOfPackets:
        sendSocket.send(data[buffer_size*packetNumber:buffer_size*(packetNumber+1)])
        packetNumber = packetNumber + 1

def receiveData(clientSocket, buffer_size=10):
    n = int(clientSocket.recv(buffer_size))
    data = ''
    while n > 0:
        data = data + clientSocket.recv(BUFFERSIZE)
        n = n - 1
    return data.decode()
	
################################# Start of main Program #################################

#User Input for 
#serverName = raw_input('Enter Server Host Name : ')
#if (serverName == ''):
#	serverName = 'localhost'
serverName = 'localhost'
serverPort = 1001
	
#Create a TCP socket. 
clientSocket = socket(AF_INET, SOCK_STREAM)

#connect to the server
clientSocket.connect((serverName,serverPort))

print("connected on port {}".format(serverPort))


#get Response
data = receiveData(clientSocket)

#input User Query
first_data = raw_input(data)

#send query via the Socket
sendData(first_data,clientSocket)