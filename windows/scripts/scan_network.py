import socket as sk

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sock.connect(("127.0.0.1", 6535))

print(sock.recv(1024))