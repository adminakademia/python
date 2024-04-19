from flask import Flask
from flask import render_template
import yaml
from yaml.loader import SafeLoader
from jinja2 import Environment, FileSystemLoader


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


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
