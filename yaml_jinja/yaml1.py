import yaml
from yaml.loader import SafeLoader

yaml_file = """
# Ponizej plik YAML:
---
nazwahosta: 'S1'
interfejsy:
    nazwa: 'GigabitEthernet0/1'
    description: 'polaczenie_z_S2'
    trunk: true
...
"""
 
x = yaml.safe_load(yaml_file)
print(x)
print(type(x))