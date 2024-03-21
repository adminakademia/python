from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("interfejs6.j2")

lista_int = {
"GigabitEthernet0/1": "Port_numer_jeden",
"GigabitEthernet0/2": "Port_numer_dwa",
"GigabitEthernet0/3": "Port_numer_trzy"
}

print(template.render(interface_list=lista_int))