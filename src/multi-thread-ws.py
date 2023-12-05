import threading
import requests

def make_request(url, thread_num):
    print(f"Thread {thread_num} making request...")
    response = requests.get(url)
    print(f"Thread {thread_num} received response: {response.status_code}")

def main():
    test_url = 'http://localhost:8080/test.html'  # URL to your test page
    threads = []

    for i in range(5):  # Number of concurrent requests
        thread = threading.Thread(target=make_request, args=(test_url, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
