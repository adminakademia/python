from jinja2 import Environment, FileSystemLoader

max_punktow = 100
nazwa_zadania = "Zadanie do samodzielnej realizacji 1"
studenci = [
    {"imie_nazwisko": "Jacek Gula",  "wynik": 77},
    {"imie_nazwisko": "Witold Sup", "wynik": 81},
    {"imie_nazwisko": "Anna Nowak", "wynik": 100},
    {"imie_nazwisko": "Marek Kowalski", "wynik": 32},
    {"imie_nazwisko": "Julia Szary", "wynik": 44},
]

environment = Environment(loader=FileSystemLoader("C:/VS/JINJA/szablony_jinja/"))
szablon = environment.get_template("wiadomosc2.txt")

for student in studenci:
    nazwa_pliku = f"message_{student['imie_nazwisko'].lower()}.txt"
    zawartosc = szablon.render(
        student,
        max_punktow=max_punktow,
        nazwa_zadania=nazwa_zadania
    )
    with open(nazwa_pliku, mode="w", encoding="utf-8") as wiadomosc:
        wiadomosc.write(zawartosc)
        print(f"... zapisano {nazwa_pliku}")


plik_wyniki = "wyniki_studentow.html"
wyniki_szablon = environment.get_template("wyniki.html")
zawartosc = {
    "studenci": studenci,
    "nazwa_zadania": nazwa_zadania,
    "max_punktow": max_punktow,
}
with open(plik_wyniki, mode="w", encoding="utf-8") as wynikowy_plik:
    wynikowy_plik.write(wyniki_szablon.render(zawartosc))
    print(f"... zapisano {plik_wyniki}")
