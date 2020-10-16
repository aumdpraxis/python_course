import socket
import sys

HOST, PORT= "localhost", 5000
message = " ".join(sys.argv[1:])


##  socket protocol families
# socket.AF_INET6 for IPV6
# socket.AF_UNIX // better than pass messages by INET(process to process- only unix)
# .
# .
# .
# and more

## socket types
# socket.SOCK_DGRAM for UDP
# socket.SOCK_STREAM for TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST,PORT))
    message= message+'\n'
    sock.sendall(bytes(message.encode('utf-8')))
    received = sock.recv(1024)
finally:
    sock.close()

if __name__ == "__main__":
    print(f"sent:\t\t{message}")
    print(f"Received:\t{received.decode()}")