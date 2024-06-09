import ipaddress
import socket

host = input('Input Target IP address:')

def validate_ip(host):
    try:
        ipaddress.ip_address(host)
        portscan(host)
        return True
        
    except ValueError:
        print(f"ERROR: {host} is not a valid IP address")
        return False

def portscan(host):
    for port in range(1,101):
        try:
            s = socket.socket()
            s.connect((host, port))
            print('open port:%d' % port)
            s.close()
        except: pass

if __name__ == '__main__':
    host = input('Input Target IP address: ')
    validate_ip(host)