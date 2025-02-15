import os
from scapy.all import ARP, Ether, srp
from time import sleep
import socket as sk

def get_local_ip():
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def scan_network(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

def sock_factory():
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sock.bind(("0.0.0.0", 6535))
    sock.listen(5)

    return sock


def main():
    while True:
        sock = sock_factory()
        conn, addr = sock.accept()


        while True:
            try:
                data = scan_network(ip=f"{get_local_ip()}/24")
                data = '{}'.format(data)
                conn.send(data.encode())
            
            except Exception as error:
                sock.close()
                break

            else:
                sleep(0.5)


if __name__ == "__main__":
    while True:
        os.system("cls")
        print(main())