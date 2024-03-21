from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("interfejs7.j2")

lista_int = [
{
"name": "GigabitEthernet0/1",
"desc": "Port_uplink",
"uplink": True
},
{
"name": "GigabitEthernet0/2",
"desc": "Port_numer_jeden",
"vlan": 10
},
{
"name": "GigabitEthernet0/3",
"desc": "Port_numer_dwa",
"vlan": 20
}
]

print(template.render(interface_list=lista_int))