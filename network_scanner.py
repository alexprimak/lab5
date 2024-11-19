import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1) as conn:
            print(f"[OPEN] {ip}:{port}")
    except:
        pass

def scan_host(ip, ports):
    print(f"Scanning host: {ip}")
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

def scan_network(ip_range, ports):
    print(f"Scanning network: {ip_range}")
    for ip in ip_range:
        scan_host(ip, ports)

# Function to generate a list of IPs in a range (like 192.168.1.1 to 192.168.1.10)
def generate_ip_range(base_ip, start, end):
    ip_range = []
    for i in range(start, end + 1):
        ip_range.append(f"{base_ip}.{i}")
    return ip_range

# Specify the IP range and the ports you want to scan
ip_range = generate_ip_range("192.168.1", 1, 10)  # Scanning 192.168.1.1 to 192.168.1.10
ports = [80, 443, 22]  # Ports to check (HTTP, HTTPS, SSH)

# Start the network scan
scan_network(ip_range, ports)
