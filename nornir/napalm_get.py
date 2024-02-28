from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from pprint import pprint

nr = InitNornir(config_file="config.yaml")
wynik= nr.run(napalm_get,getters=["facts","interfaces"])
print_result(wynik)
