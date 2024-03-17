import socket
import threading


class Scanner:
    def __init__(self, ip: str, start_port: int, end_port: int, threads: int, connection_time=1):
        self.ip = ip
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.connection_time = connection_time

    def is_open(self, port: int):
        # Attempting to connect using ip and port.
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect.settimeout(self.connection_time)
        result = connect.connect_ex((self.ip, port))
        connect.close()
        return result

    def check_ports(self, starting_port: int, ending_port: int):
        # Checking range of multiple ports.
        for port in range(int(starting_port), int(ending_port)):
            result = self.is_open(port)
            if result == 0:
                print("Port {} is open".format(port))

    def start(self):
        # Checking range of multiple ports simultaneously.
        # Calculating range of ports for every function.
        num_of_ports = (int(self.end_port) - int(self.start_port)) // int(self.threads)
        # Setting new start and end ports.
        s_port = int(self.start_port)
        e_port = s_port + num_of_ports
        # Running with new start and end ports, according to the calculations above.
        for port in range(int(self.threads)):
            threading.Thread(target=self.check_ports, args=(s_port, e_port)).start()
            s_port = e_port
            e_port += num_of_ports


if __name__ == '__main__':

    print("Welcome to hacking school 101.\n"
          "Today we will find open ports using IP address or URL.\n")
    while True:
        # Attempting to connect with given IP to see if it's valid.
        ip_input = input("Enter IP >>> ")
        try:
            s = Scanner(ip_input, 1, 1, 1)
            s.is_open(445)
        except:
            print("Invalid IP, Enter new IP\n")
            continue

        # Checking for valid input.
        start_input = ""
        while not start_input.isnumeric():
            start_input = input("\nStarting port to scan >>> ")
            if start_input < "0":
                print("Must be above 0")
            elif start_input.isalpha():
                print("Must be a number!")

        # Checking for valid input.
        end_input = ""
        while True:
            end_input = input("\nEnding port to scan >>> ")
            if end_input.isalpha():
                print("Must be a number!!")
                continue
            elif int(end_input) < int(start_input):
                print("Must be bigger then start port!")
                continue
            else:
                break

        # Checking for valid input.
        thread_input = ""
        while not thread_input.isnumeric():
            thread_input = input("\nHow many threads do you want >>> ")
            if thread_input < "0":
                print("Must be above 0")
            elif thread_input.isalpha():
                print("Must be a number!")

        scan = Scanner(ip_input, int(start_input), int(end_input), int(thread_input))
        scan.start()
        print("\nScanning in progress...\n")
        break
