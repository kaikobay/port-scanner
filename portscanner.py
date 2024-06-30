import ipaddress
import socket


def validate_ip(host):
    try:
        ipaddress.ip_address(host)
        return True
        
    except ValueError:
        print(f"ERROR: {host} is not a valid IP address")
        return False

def target_port():
    print('Select target ports\n1 - Common ports\n2 - Well-known ports\n3 - Custom')
    port_mode = int(input())

    if port_mode == 1:
        return [20,21,22,23,25,53,80,110,119,123,143,161,194,443]
    elif port_mode == 2:
        return list(range(1, 1025))
    elif port_mode == 3:
        custom_ports = input("Enter custom ports separated by commas:")
        try:
            return [int(port.strip()) for port in custom_ports.split(',')]
        except ValueError:
            print("ERROR: Invalid custom port numbers")
            return False
    else:
        print(f"ERROR: Invalid option")
        return []


def portscan(host, ports):
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                print(f'open port:{port}')
        except (socket.timeout, socket.error):
            pass


if __name__ == '__main__':
    host = input('Enter Target IP address: ')
    if validate_ip(host):
        ports = target_port()
        if ports:
            portscan(host, ports)
