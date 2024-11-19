from scapy.all import sniff
from scapy.layers.inet import IP  # Імпортуємо IP з scapy.layers.inet
from collections import defaultdict
import time
import threading

THRESHOLD_PACKETS = 100  # Кількість запитів для виявлення підозрілої активності
ALERT_INTERVAL = 10      # Інтервал аналізу у секундах

traffic_data = defaultdict(int)

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        traffic_data[src_ip] += 1

def monitor_traffic():
    while True:
        time.sleep(ALERT_INTERVAL)
        for ip, count in list(traffic_data.items()):
            if count > THRESHOLD_PACKETS:
                print(f"[ALERT] Підозріло висока активність з {ip}: {count} пакетів.")
        traffic_data.clear()

def start_sniffing(interface):
    print(f"Починаємо перехоплення трафіку на інтерфейсі {interface}...")
    monitor_thread = threading.Thread(target=monitor_traffic, daemon=True)
    monitor_thread.start()
    sniff(iface=interface, prn=packet_handler)

# Виклик функції
# start_sniffing("eth0")  # Вкажіть ваш інтерфейс
