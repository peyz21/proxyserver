# Simple Web and Web Proxy Server

## Introduction
This project involves the implementation of a simple web server and a basic web proxy server using Python's socket programming. The primary focus is to understand and apply concepts of network communication, server-client architecture, and HTTP protocol handling without the use of high-level HTTP modules.

### Features
- **Web Server**: Handles basic HTTP requests and returns appropriate responses including status codes like:
     - 200 OK
     - 304 Not Modified
     - 400 Bad Request
     - 403 Forbidden
     - 404 Not Found
     - 411 Length Required
  
- **Web Proxy Server**: Acts as an intermediary for requests from clients seeking resources from other servers.

## Installation

### Prerequisites
- Python 3.x

### Setup
Clone the repository to your local machine:
```bash
git clone https://github.com/peyz21/proxyserver.git
cd proxyserver
```

## Usage

### Running the Web Server
Navigate to the project directory and run:

```bash
python proxyserver.py 
```
change later ^ 

## Testing
Access the web server via a web browser at http://localhost:[PORT]/test.html.
Configure your web browser or a separate client to send requests to the proxy server.
