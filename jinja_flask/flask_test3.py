from flask import Flask, render_template

app = Flask(__name__)

max_punktow = 100
nazwa_zadania = "Zadanie do samodzielnej realizacji 1"
studenci = [
    {"imie_nazwisko": "Jacek Gula",  "wynik": 77},
    {"imie_nazwisko": "Witold Sup", "wynik": 81},
    {"imie_nazwisko": "Anna Nowak", "wynik": 100},
    {"imie_nazwisko": "Marek Kowalski", "wynik": 32},
    {"imie_nazwisko": "Julia Szary", "wynik": 44},
]

@app.route("/")
def start():
    return render_template("stronaflask.html", tytul="Jinja oraz Flask")


@app.route("/wyniki")
def wyniki():
    context = {
        "tytul": "Wyniki",
        "studenci": studenci,
        "nazwa_zadania": nazwa_zadania,
        "max_punktow": max_punktow,
    }
    return render_template("wyniki.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
