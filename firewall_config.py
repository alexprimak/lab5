import os

def block_ip(ip):
    print(f"Блокуємо IP: {ip}")
    os.system(f"iptables -A INPUT -s {ip} -j DROP")

def allow_ip(ip):
    print(f"Дозволяємо IP: {ip}")
    os.system(f"iptables -A INPUT -s {ip} -j ACCEPT")

def restrict_port(port):
    print(f"Обмежуємо доступ до порту: {port}")
    os.system(f"iptables -A INPUT -p tcp --dport {port} -j DROP")

# Приклад використання:
# block_ip("192.168.1.100")
# restrict_port(22)
