import yaml
from yaml.loader import SafeLoader


with open("C:/VS/YAML_JINJA/wsad.yaml") as file:
    wynik = yaml.safe_load(file)
    print(wynik)
    type(wynik)

