import socket

host = '192.168.0.1'
ports = [20,53,143,443]

def portscan(host, ports):
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                print(f'open port:{port}')
        except (socket.timeout, socket.error):
            pass

portscan(host, ports)
