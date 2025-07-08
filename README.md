# Programming Assignment 1: Socket Programming Web Server and Client

## Author(s)
- Jovani Antonio
- Ryan Trinh
- Helen Truong

---

## Description
This project implements a simple HTTP web server and a client in Python. The server listens for incoming HTTP requests and responds with the requested file if available or a `404 Not Found` error if the file does not exist. The client connects to the server, sends an HTTP GET request, and displays the server's response.

---

### Part A: Web Server
The web server (`webserver.py`):
- Accepts TCP connections on a specified port.
- Parses incoming HTTP GET requests.
- Returns the requested HTML file if it exists.
- Returns a `404 Not Found` message for missing files.
- Handles one request at a time.

---

### Part B: HTTP Client
The client (`client.py`):
- Connects to the server using TCP.
- Sends a properly formatted HTTP GET request.
- Prints the server's HTTP response (headers and content) to the terminal.

---

## Files Included
- `webserver.py`: Python script for the web server.
- `client.py`: Python script for the HTTP client.
- `HelloWorld.html`: Test HTML file served by the server.
- `README.txt`: This file.

---

## How to Run

### Start the Server:
1. Open a terminal.
2. Navigate to the folder containing `webserver.py`.
3. Run the server:  python3 webserver.py
4. The server will display: Ready to serve...

---

### Test the Server in a Web Browser:
1. Open your web browser.
2. In the address bar, enter:  http://localhost:6789/HelloWorld.html
✅ You should see the contents of `HelloWorld.html`.
3. To test a missing file (404 error), enter:  http://localhost:6789/NotAFile.html
❌ You should see a `404 Not Found` message.

---

### Start the Client Program:
1. Open a second terminal in the same folder.
2. Run the client program: 
Formate: 
    '''python3 client.py <server_host> <server_port> <filename>'''
Example:
    'python3 client.py 127.0.0.1 6789 HelloWorld.html'
3. The client will display the server’s HTTP response (headers and file contents) in the terminal.
4. To test a missing file with the client, run:  
    python3 client.py 127.0.0.1 6789 NotAFile.html

