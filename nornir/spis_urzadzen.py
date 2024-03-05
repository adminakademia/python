from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from tabulate import tabulate

tablica=[]
nr = InitNornir(config_file="config.yaml")

def get_lldp_neighbors(task):
    lldp_neighbors = task.run(napalm_get, getters=["lldp_neighbors"])
    neighbors = lldp_neighbors.result["lldp_neighbors"]

    for interface, neighbor_list in neighbors.items():
        for neighbor in neighbor_list:
            tablica.append([task.host, interface, neighbor['hostname'], neighbor['port']])
            
            description = f"Connected to {neighbor['hostname']} on port {neighbor['port']}"
            configuration_commands = [f"interface {interface}", f"description {description}"]
            task.run(netmiko_send_config, config_commands=configuration_commands)


result = nr.run(task=get_lldp_neighbors)
spis = tabulate(tablica,headers=["Local Device", "Local Port", "Neighbor", "Remote Port"], tablefmt="grid")
print(spis)
#print_result(result)





