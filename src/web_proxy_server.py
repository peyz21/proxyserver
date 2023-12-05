import socket
import threading

def modify_request_line(request):
    """ Modify the request line to be suitable for forwarding to the web server. """
    lines = request.split("\n")
    parts = lines[0].split(" ")
    if len(parts) >= 2:
        parts[1] = parts[1].replace("http://localhost:8888", "")
        lines[0] = " ".join(parts)
    return "\n".join(lines)

def forward_request_to_server(request, server_address, server_port):
    """ Forward the request to the web server and return the response. """
    modified_request = modify_request_line(request)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((server_address, server_port))
        server_socket.sendall(modified_request.encode())
        response = server_socket.recv(4096)
    return response

def handle_client_connection(client_socket, address):
    """ Handle individual client connection. """
    try:
        request = client_socket.recv(1024).decode()
        print(f"Proxy Server received request from {address}:\n{request}")

        # Forward the request to the actual web server
        response = forward_request_to_server(request, 'localhost', 8080)
        client_socket.sendall(response)
    except Exception as e:
        print(f"Error in proxy server handling request from {address}: {e}")
    finally:
        client_socket.close()

def main():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind(('localhost', 8888))
    proxy_socket.listen(5)

    print("Proxy Server is listening on port 8888...")

    while True:
        try:
            client_socket, address = proxy_socket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, address))
            client_thread.start()
        except Exception as e:
            print(f"Error accepting connection in proxy server: {e}")

if __name__ == "__main__":
    main()
