from jinja2 import Environment, FileSystemLoader
import yaml
from yaml.loader import SafeLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/YAML_JINJA"))
template = ENV.get_template("szablon_interfejsy.j2")


with open('C:/VS/YAML_JINJA/interfejsy.yaml', 'r') as file:
    konfiguracja = yaml.safe_load(file)
    lista_interfejsow = konfiguracja["interfaces"]
    nazwa_hosta = konfiguracja["hostname"]
    konfiguracja_ospf = konfiguracja["ospf"]
    print(lista_interfejsow)
    print(nazwa_hosta)
    print(konfiguracja_ospf)

    print(template.render(lista_interfejsow_do_szablonu=lista_interfejsow, nazwa_hosta_do_szablonu=nazwa_hosta, konfiguracja_ospf=konfiguracja_ospf))

