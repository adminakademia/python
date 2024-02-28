from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result
from nornir_inspect import nornir_inspect
from pprint import pprint

nr=InitNornir(config_file="config.yaml")

wynik=nr.run(napalm_cli,commands=["show run","show ip int br"])

print_result(wynik)
nornir_inspect(wynik)
pprint(wynik["S1"][0].result["show ip int br"])
