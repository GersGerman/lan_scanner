import socket as sk

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sock.connect(("127.0.0.1", 6535))

print(sock.recv(1024))

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("", 6365))
# print(s.getsockname()[0])
# s.close()