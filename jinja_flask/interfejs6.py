from jinja2 import Environment, FileSystemLoader
import yaml
from yaml.loader import SafeLoader

ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("no_http.j2")

with open('C:/VS/JINJA/dane.yaml', 'r') as file:
    lista_int = yaml.safe_load(file)
    print(lista_int)
    print(template.render(interface_list=lista_int))

