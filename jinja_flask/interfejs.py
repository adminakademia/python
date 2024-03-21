from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("interfejs3.j2")

interfejs_slownik = {
    "name": "GigabitEthernet0/1",
    "description": "Port_Serwera",
    "vlan": 10,
    "uplink": True
    }

print(template.render(interface=interfejs_slownik))
