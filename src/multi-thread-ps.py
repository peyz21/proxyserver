import threading
import requests

def make_request_through_proxy(url, proxy, thread_num):
    print(f"Thread {thread_num} making request through proxy...")
    response = requests.get(url, proxies=proxy)
    print(f"Thread {thread_num} received response: {response.status_code}")

def main():
    # Change this URL to the proxy server
    test_url = 'http://localhost:8888/test.html'  # URL to request via the proxy server
    proxy_url = 'http://localhost:8888'           # URL of your proxy server
    proxy_dict = {
        "http": proxy_url,
        "https": proxy_url
    }
    threads = []

    for i in range(5):  # Number of concurrent requests
        thread = threading.Thread(target=make_request_through_proxy, args=(test_url, proxy_dict, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
