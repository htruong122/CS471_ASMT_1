from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Fill in start
serverPort = 6789  # or any port number not already in use
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept()  # Accept a client connection
    #Fill in end
    try:
        #Fill in start
        message = connectionSocket.recv(1024).decode()  # Receive and decode HTTP request
        print("📥 Received request from client:")
        print(message)  # <-- shows the raw HTTP request
        #Fill in end
        filename = message.split()[1]  # Get the requested file name
        f = open(filename[1:])  # Open the file, remove '/' from path
        #Fill in start
        outputdata = f.read()  # Read file content
        #Fill in end

        # Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())  # Send HTTP response header
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
        #Fill in end

        # Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
        
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
    






