import socket

def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Set timeout for faster scanning
        result = s.connect_ex((target, port))  # Returns 0 if open, otherwise an error code
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    port_scanner(target_ip, start_port, end_port)