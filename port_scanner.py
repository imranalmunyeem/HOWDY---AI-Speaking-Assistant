import socket
import pyttsx3

engine = pyttsx3.init()

def speak(text, print_message=True):
    if print_message:
        print(text)
    engine.say(text)
    engine.runAndWait()

def get_user_input(prompt):
    speak(prompt, print_message=False)
    return input(prompt)

def scan_ports(target, start_port, end_port):
    speak(f"Scanning ports on {target}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            speak(f"Port {port} is open")
        else:
            speak(f"Port {port} is closed")

        sock.close()

if __name__ == "__main__":
    target_ip = get_user_input("Enter target IP address: ")
    start_port = int(get_user_input("Enter starting port: "))
    end_port = int(get_user_input("Enter ending port: "))

    scan_ports(target_ip, start_port, end_port)
