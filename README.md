# Port-Scanner
Python program to scan ports

Single threaded Port scanner(can be slow compared to multi threaded):

import socket
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Timeout for connection attempt
        result = s.connect_ex((ip, port))  # Returns 0 if open, error code otherwise
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"Scanning {target} from port {start_port} to {end_port}...")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)


