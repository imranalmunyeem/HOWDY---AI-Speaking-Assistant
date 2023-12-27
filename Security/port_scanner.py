import socket
import pyttsx3

def init_engine():
    return pyttsx3.init()

def speak(engine, text, print_message=True):
    if print_message:
        print(text)
    engine.say(text)
    engine.runAndWait()

def get_user_input(engine, prompt):
    speak(engine, prompt, print_message=False)
    return input(prompt)

def scan_ports(engine, target, start_port, end_port):
    speak(engine, f"Scanning ports on {target}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            speak(engine, f"Port {port} is open")
        else:
            speak(engine, f"Port {port} is closed")

        sock.close()

def perform_port_scan():
    engine = init_engine()

    target_ip = get_user_input(engine, "Enter target IP address: ")
    start_port = int(get_user_input(engine, "Enter starting port: "))
    end_port = int(get_user_input(engine, "Enter ending port: "))

    scan_ports(engine, target_ip, start_port, end_port)

if __name__ == "__main__":
    perform_port_scan()
