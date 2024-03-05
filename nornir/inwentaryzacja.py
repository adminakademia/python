from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from pprint import pprint
from tabulate import tabulate
import csv


tablica_informacje=[]

def informacje(zadanie):
    try:
        dane=zadanie.run(task=napalm_get,getters=["get_facts","get_interfaces_ip","lldp_neighbors"])
        #print_result(dane)
    except:
        print(f"{zadanie.host.hostname} - połączenie nie powiodło się.")
        return
    
    facts=dane.result["get_facts"]
    nazwa_hosta=facts["hostname"]
    #print(nazwa_hosta)
    
    ip_prefix_list=[]

    for interfejs,dane_int in dane.result["get_interfaces_ip"].items():
        try:
            for addres,prefix in dane_int["ipv4"].items():
                ip_prefix_list.append(f"{interfejs}: {addres}/{prefix['prefix_length']}")
        except:
            pass
    #print(ip_prefix_list)
    ip_prefix_ladniej=' , '.join(ip_prefix_list)
    #print(ip_prefix_ladniej)

    tablica_informacje.append([facts["hostname"],facts["uptime"],facts["vendor"],facts["model"],facts["os_version"],ip_prefix_ladniej])

   

nr=InitNornir(config_file="config.yaml")

wynik=nr.run(task=informacje)
print(tablica_informacje)
print(tabulate(tablica_informacje))


with open("inwentaryzacja.csv",mode="w",newline="") as csv_file:
    zapis=csv.writer(csv_file,delimiter=";")
    for wiersz in tablica_informacje:
        zapis.writerow(wiersz)

