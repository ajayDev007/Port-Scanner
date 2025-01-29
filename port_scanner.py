import socket
import threading

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"Scanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
