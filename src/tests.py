import requests
from requests import Request, Session
import socket
from datetime import datetime
from time import strftime

def send_malformed_request():
    try:
        with socket.create_connection(('localhost', 8080)) as s:
            # Send a malformed request
            s.sendall(b'GET\n\n')
            response = s.recv(1024)
            print("Testing Response Code 400:")
            print("Passed Test? " +  str(("400" in response.decode())))
    except Exception as e:
        print(f"Error: {e}")
    



def test200(url): # Request that works
    print("Testing Response Code 200:")
    result = requests.get(url)
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 200\n")
    return result.status_code == 200

def test403(url): # Testing request to forbidden path
    print("Testing Response Code 403:")
    result = requests.get(url+ "/forbiddenpath")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 403\n")
    return result.status_code == 403
def test404(url): # Test response when requesting a nonexistent resource
    print("Testing Response Code 404:")
    result = requests.get(url + "/8thwonderoftheworld")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 404\n")
    return result.status_code == 404

if __name__ == "__main__":
    for i in ["8080","8888"]:
        print("testing with port: " + i)
        print("--------------------------")
        url = "http://localhost:" + i
        print("test200 Passed? : " + str(test200(url)))
        print("test403 Passed? : " + str(test403(url)))
        print("test404 Passed? : " + str(test404(url)))
        print("--------------------------")
    send_malformed_request()