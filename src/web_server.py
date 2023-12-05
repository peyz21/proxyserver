import socket
import os
import datetime
import traceback
import threading

def generate_http_response(status_code, path=''):
    """ Generate an HTTP response based on the given status code. """
    content_type = "Content-Type: text/html\n\n"
    if status_code == 200 and path:
        last_modified = f"Last-Modified: {last_modified_time(path)}\n"
    else:
        last_modified = ""

    responses = {
        200: f"HTTP/1.1 200 OK\n{last_modified}{content_type}{read_file(path)}",
        304: "HTTP/1.1 304 Not Modified\n\n",
        400: f"HTTP/1.1 400 Bad Request\n{content_type}<html><body><h1>400 Bad Request</h1></body></html>",
        403: f"HTTP/1.1 403 Forbidden\n{content_type}<html><body><h1>403 Forbidden</h1></body></html>",
        404: f"HTTP/1.1 404 Not Found\n{content_type}<html><body><h1>404 Not Found</h1></body></html>",
        411: f"HTTP/1.1 411 Length Required\n{content_type}<html><body><h1>411 Length Required</h1></body></html>"
    }
    return responses.get(status_code, f"HTTP/1.1 500 Internal Server Error\n{content_type}")

def read_file(path):
    """ Helper function to read file content """
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

def last_modified_time(path):
    """ Helper function to get the last modified time of a file """
    try:
        mod_time = os.path.getmtime(path)
        return datetime.datetime.fromtimestamp(mod_time).strftime('%a, %d %b %Y %H:%M:%S GMT')
    except OSError:
        return ''

def handle_request(request):
    """ Handle the incoming request and determine the status code. """
    if not request.strip(): 
        return 400, ''  # Return Bad Request for empty or whitespace-only requests 400

    headers = request.split("\n")
    first_line = headers[0]
    parts = first_line.split()

    if len(parts) != 3: 
        return 400, ''  # Return Bad Request for malformed request lines 400 

    method, path, _ = parts

    
    if path == "/forbiddenpath":
        return 403, ''  # Return 403 Forbidden for this specific path

    if method == "GET":
        if path == "/":
            path = "/test.html"  

        file_path = f'.{path}'
        if not os.path.exists(file_path):
            return 404, ''  # Return 404 Not Found for nonexistent files

        
        for header in headers:
            if header.startswith('If-Modified-Since:'):
                last_mod_client = header.split(': ')[1].strip()
                last_mod_server = last_modified_time(file_path)
                if last_mod_server <= last_mod_client:
                    return 304, ''  # Return 304 Not Modified if applicable

        return 200, file_path  # Return 200 OK for successful GET requests

    elif method == "POST":
        if 'Content-Length:' not in request:
            return 411, ''  

    return 403, ''  # Return 403 Forbidden for all other cases

def handle_client_connection(client_socket, address):
    """Handle individual client connection."""
    try:
        request = client_socket.recv(1024).decode()
        print(f"Received request from {address}:\n{request}")

        status_code, file_path = handle_request(request)
        response = generate_http_response(status_code, file_path)
        client_socket.sendall(response.encode())
    except Exception as e:
        print(f"Error handling request from {address}: {e}")
        traceback.print_exc()
    finally:
        client_socket.close()

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 8080))
        server_socket.listen(5)

        print("Server is listening on port 8080...")

        while True:
            try:
                client_socket, address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, address))
                client_thread.start()
            except Exception as e:
                print(f"Error accepting connection: {e}")
                traceback.print_exc()
    except Exception as e:
        print(f"Fatal error in server: {e}")
        traceback.print_exc()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
