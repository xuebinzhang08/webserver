#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    #Fill in start
    HOST = '127.0.0.1'
    PORT = port
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)
    #Fill in end

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            #Send one HTTP header line into socket
            #Fill in start
            header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html; charset=utf-8\nContent-Length: %d\n\n' % (
                len(outputdata))
            connectionSocket.send(header.encode("utf-8"))
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            header = 'HTTP/1.1 404 Found'
            connectionSocket.send(header.encode("utf-8"))
            #Fill in end

            #Close client socket
            #Fill in start
        finally:
            connectionSocket.close()
            #Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
