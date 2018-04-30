# Import socket module
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 1234))
serverSocket.listen(1)
#Fill in end

while True:
    # Establish the connection

    print ('Ready to serve..')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    print 'Client Address: ', str(tuple(addr))
    try:
        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        print ("File requested: " + filename)

        f = open(filename[1:])

        outputdata = f.read()

        f.close()

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
        # Fill in end

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")


    except IOError:
        # Send HTTP response message for file not found
        # Fill in start
        print ("404: File Not Found")
        connectionSocket.send('HTTP/1.0 404 Not Found\r\n\r\n')
        # Fill in end

        # Close the client connection socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()