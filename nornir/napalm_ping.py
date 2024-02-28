from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result
import pprint
from nornir_inspect import nornir_inspect


nr = InitNornir(config_file="config.yaml")
wynik = nr.run(task=napalm_ping,dest="S1")

nornir_inspect(wynik)
print_result(wynik["R1"])
