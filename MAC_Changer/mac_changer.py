#!/usr/bin/env python3
# Run this script in CLI

###MAC Change


import subprocess # To execute linux commands in python
import optparse # Help menu creation
import re #Using regex


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--netadapter", dest="net_adp", help="Network Adapter to change the MAC address")
    parser.add_option("-m", "--macadr", dest="mac_adr", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.net_adp:
        #code to handle error
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.mac_adr:
        #code to handle error
        parser.error("[-] Please specify a Mac, use --help for more info")
    return options


def mac_change(net_adp, mac_adr):
    print("[+] Changing MAC address for " + options.net_adp + " to " + options.mac_adr)
    subprocess.call(["ifconfig", options.net_adp, "down"])
    subprocess.call(["ifconfig", options.net_adp, "hw", "ether", options.mac_adr])
    subprocess.call(["ifconfig", options.net_adp, "up"])


def return_mac(net_adp):
    result = subprocess.check_output(["ifconfig", net_adp], encoding='UTF-8')
    mac_address = re.search(r'([0-9a-fA-F]{2}.){5}[0-9a-fA-F0]{2}', result)
    if mac_address:
        return mac_address.group(0)
    else:
        print("[-] No such MAC address")



options = get_args()
current_mac = return_mac(options.net_adp)
print("[-] Current Mac is: " + str(current_mac))
mac_change(options.net_adp, options.mac_adr)
current_mac = return_mac(options.net_adp)
if current_mac == options.mac_adr:
    print("[-] MAC changed successfully to " + current_mac)
else:
    print("[!] Action failed")