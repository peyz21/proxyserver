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
    


url = "http://localhost:8888"
def test200(): # Request that works
    print("Testing Response Code 200:")
    result = requests.get(url)
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 200\n")
    return result.status_code == 200
def test304(): # Request that hasn't been modified
    print("Testing Response Code 304:")
    
    s = Session()

    req = Request('POST', url)
    midwayPoint = req.prepare()
    midwayPoint.headers['If-Modified-Since'] = strftime("%a, %d %b %Y %H:%M:%S",datetime.now())
    print(midwayPoint.headers)
    
    result = s.send(midwayPoint)
    return 
def test403(): # Testing request to forbidden path
    print("Testing Response Code 403:")
    result = requests.get(url+ "/forbiddenpath")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 403\n")
    return result.status_code == 403
def test404(): # Test response when requesting a nonexistent resource
    print("Testing Response Code 404:")
    result = requests.get(url + "/8thwonderoftheworld")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 404\n")
    return result.status_code == 404
def test411(): # Test response when content length is not given
    print("Testing Response Code 411:")
    
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 411\n")
    return result.status_code == 411
if __name__ == "__main__":
    print("test200 Passed? : " + str(test200()))
    print("test304 Passed? : " + str(test304()))
    print("test403 Passed? : " + str(test403()))
    print("test404 Passed? : " + str(test404()))
    print("test411 Passed? : " + str(test411()))
    send_malformed_request()