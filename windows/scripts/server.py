from scapy.all import ARP, Ether, srp
from time import sleep
import socket as sk


def scan_network(ip):
    

    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3)[0]
	
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        print({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

def sock_factory():

    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sock.bind(("0.0.0.0", 6535))

    sock.listen(1)

    return sock


def main():
    while True:
        sock = sock_factory()
        data = scan_network("192.168.1.253/24")
        
        conn, addr = sock.accept()
        print(addr)

        while True:
            try:
                data = '{}'.format(data)
                conn.send(data.encode())
            
            except Exception as error:
                print(error)
                print("disconnected")
                sock.close()
                break

            else:
                sleep(0.5)

if __name__ == "__main__":
    main()