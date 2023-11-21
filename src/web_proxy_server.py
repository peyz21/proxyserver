import socket

def forward_request_to_server(request, server_address, server_port):
    """ Forward the request to the web server and return the response. """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((server_address, server_port))
        server_socket.sendall(request.encode())
        response = server_socket.recv(4096)
    return response

def main():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(('localhost', 8888))
    proxy_socket.listen(5)

    print("Proxy Server is listening on port 8888...")

    while True:
        client_socket, address = proxy_socket.accept()
        request = client_socket.recv(1024).decode()
        print(f"Proxy Server received request:\n{request}")

        # Forward the request to the actual web server
        response = forward_request_to_server(request, 'localhost', 8080)
        client_socket.sendall(response)
        client_socket.close()

if __name__ == "__main__":
    main()
