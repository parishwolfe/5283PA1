import socket
import sys
import datetime
import locale
locale.setlocale(locale.LC_TIME, 'en_US')


class server():
    def __init__(self, port, directory, host="0.0.0.0"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        print(f"Listening on port: {port}")
        self.sock = sock

    def serve(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"Connection from {addr}")
            request = conn.recv(1024)
            request = request.decode()
            print(f"Request: {request}")
            self.handle(request, conn)
            conn.close()


    def handle(self, request, conn):
        request = request.split(" ")
        if request[0] == "GET":
            self.get(request[1], conn)
        elif request[0] == "HEAD":
            self.head(request[1], conn)
        else:
            self.error(conn)

    def default_headers(self, status_code=200, content_len=None):
        headers = f"HTTP/1.1 {status_code} \r\n"
        headers += f"Date: {datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n"
        headers += "Content-Type: text/html\r\n"
        headers += "Server: Parish Wolfe\r\n"
        if content_len is not None:
            headers += f"Content-Length: {content_len}\r\n"
        headers += "\r\n"
        return headers

    def head(self, path, conn):
        if path == "/":
            path = "/index.html"
        try:
            with open(path[1:], "rb") as file:
                data = file.read()
                size = len(data)
                conn.send(self.default_headers(content_len=size).encode())
        except FileNotFoundError:
            conn.send((self.default_headers(status_code=404) + "<h1>Error 404: Not Found</h1>").encode())


    def get(self, path, conn):
        if path == "/":
            path = "/index.html"
        try:
            with open(path[1:], "rb") as file:
                data = file.read()
                size = len(data)
                conn.send(self.default_headers(content_len=size).encode())
                conn.send(data)
        except FileNotFoundError:
            conn.send((self.default_headers(status_code=404) + "<h1>Error 404: Not Found</h1>").encode())

    def error(self, conn):
        error_response = self.default_headers(status_code=501)
        error_response += "<h1>Error 501: Not Implemented</h1>"
        conn.send(error_response.encode())





if __name__ == "__main__":
    """python web_server.py PORT DIRECTORY"""
    if len(sys.argv) != 3:
        print("Usage: python web_server.py PORT DIRECTORY")
        sys.exit(1)
    else:
        port = int(sys.argv[1])
        directory = sys.argv[2]
        server(port, directory).serve()