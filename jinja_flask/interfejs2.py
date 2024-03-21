from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader("C:/VS/JINJA/templates"))
template = ENV.get_template("interfejs4.j2")

interfejs_slownik = {
    "name": "GigabitEthernet0/1",
    "description1": "Interfejs_Trunk",
    "description2": "Interfejs_Dostepowy",
    "vlan": 10,
    "uplink": False
    }

print(template.render(interface=interfejs_slownik))