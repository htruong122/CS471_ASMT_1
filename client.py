from socket import *
import sys

# Check for correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python3 client.py <server_host> <server_port> <filename>")
    sys.exit()

# Get command line arguments
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP client socket
client_socket = socket(AF_INET, SOCK_STREAM)

print(f"📡 Connecting to {server_host}:{server_port}...")

try:
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print("✅ Connected to the server.")

    # Create HTTP GET request
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    print(f"➡️ Sending HTTP GET request for '{filename}'...")
    print("---- REQUEST START ----")
    print(request.strip())
    print("---- REQUEST END ----")

    # Send the request
    client_socket.send(request.encode())

    # Receive and print the response
    print("📥 Waiting for response from the server...")
    response = client_socket.recv(4096)
    print("✅ Response received:")
    print("---- RESPONSE START ----")
    while response:
        print(response.decode(), end='')  # Print response without extra newlines
        response = client_socket.recv(4096)
    print("\n---- RESPONSE END ----")

    client_socket.close()
    print("🔌 Connection closed.")

except Exception as e:
    print(f"❌ Error: {e}")
    client_socket.close()
