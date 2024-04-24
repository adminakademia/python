from flask import Flask
from flask import render_template
import yaml
from yaml.loader import SafeLoader
from jinja2 import Environment, FileSystemLoader
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_inspect import nornir_inspect



app = Flask(__name__)

routes={}
routes["Automatyzacja App"]=[["/urzadzenia_nornir","Spis urządzeń z jakimi łączy się Nornir","","warning"]]



@app.route('/')
def podstawowa_strona():
    return render_template('podstawa_strona.html',routes=routes)

@app.route('/urzadzenia_nornir')
def urzadzenia_nornir():
    urzadzenia=yaml.safe_load(open("nornirconf/hosts.yaml","r"))
    return render_template('urzadzenia_nornir.html',urzadzenia=urzadzenia)

@app.route('/nornir_informacje/<urzadzenie>')
def nornir_informacje(urzadzenie):
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name=urzadzenie)
    wynik = nr.run(napalm_get,getters=["facts"])
    nornirnapalm_facts=wynik[urzadzenie][0].result["facts"]
    return render_template('nornir_informacje.html',nornirnapalm_facts=nornirnapalm_facts,urzadzenie=urzadzenie)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")


