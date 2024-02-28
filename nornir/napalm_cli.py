from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result


nr=InitNornir(config_file="config.yaml")

wynik=nr.run(napalm_cli,commands=["show run","show ip int br"])

print_result(wynik)
