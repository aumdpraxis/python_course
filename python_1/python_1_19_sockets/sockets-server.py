import socketserver

"""
Five clases in an inheritance diagram; four represent synchronous
servers.

+------------+
| BaseServer |
+------------+
      |
      v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
      |
      v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+

more info:
https://docs.python.org/2/library/socketserver.html
"""
class ServerTCP(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote: {self.data.decode()}")
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 5000
    server = socketserver.TCPServer((HOST,PORT),ServerTCP)
    print(f"Server listening on port {PORT} by {HOST}") 
    server.serve_forever()
