from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import pprint

cmd="show ip int br"
nr = InitNornir(config_file="config.yaml")
wynik = nr.run(task=netmiko_send_command,command_string=cmd)
print_result(wynik["S1"])
