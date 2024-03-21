from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("interfejs5.j2")

lista_int = [
"GigabitEthernet0/1",
"GigabitEthernet0/2",
"GigabitEthernet0/3"
]

print(template.render(interface_list=lista_int))