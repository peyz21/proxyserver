import socket

def send_malformed_request():
    try:
        with socket.create_connection(('localhost', 8080)) as s:
            # Send a malformed request
            s.sendall(b'GET\n\n')
            response = s.recv(1024)
            print(response.decode())
    except Exception as e:
        print(f"Error: {e}")

send_malformed_request()