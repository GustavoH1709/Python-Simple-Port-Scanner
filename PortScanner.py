import socket
import time

def scan(target, ports):
        print('\n'+' Starting To Scan Target: '+ str(target))
        for port in range(1, ports):
                scan_port(target, port)
        print('\n' + ' Finished Scanning Target: ' + str(target))


def scan_port(ipaddress, port):
        try:
                sock = socket.socket()
                sock.connect((ipaddress, port))
                print("[+] Port Opened: " + str(port))
                sock.close()
        except:
                pass

targets = input("[*] Enter Target to Scan: ")
ports = int(input("[*] Enter Ports To Be Scanned: "))

if ',' in targets:
        print("[*] Scanning Multiple Targets")
        for ip_addr in targets.split(','):
                scan(ip_addr.strip(' '), ports)
else:
        scan(targets, ports)

input('\n' + ' Press Enter To Close...')

