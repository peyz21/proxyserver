import requests
from requests import Request, Session
url = "http://localhost:8888"
def test200(): # Request that works
    print("Running test200:")
    result = requests.get(url)
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 200\n")
    return result.status_code == 200
def test304(): # Request that hasn't been modified
    print("Running test304:")
    return 
def test403(): # Testing request to forbidden path
    print("Running test403:")
    result = requests.get(url+ "/forbiddenpath")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 403\n")
    return result.status_code == 403
def test404(): # Test response when requesting a nonexistent resource
    print("Running test404:")
    result = requests.get(url + "/8thwonderoftheworld")
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 404\n")
    return result.status_code == 404
def test411(): # Test response when content length is not given
    print("Running test411:")
    s = Session()

    req = Request('POST', url)
    midwayPoint = req.prepare()
    del midwayPoint.headers['Content-Length']
    result = s.send(midwayPoint)
    print("Resulting Code : " + str(result.status_code) + " Expected Code: 411\n")
    return result.status_code == 411
if __name__ == "__main__":
    print("test200 Passed? : " + str(test200()))
    print("test304 Passed? : " + str(test304()))
    print("test403 Passed? : " + str(test403()))
    print("test404 Passed? : " + str(test404()))
    print("test411 Passed? : " + str(test411()))