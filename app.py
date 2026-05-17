# app.py
# Prosta aplikacja Flask wyświetlająca stronę z informacją o zbliżających się wakacjach

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Ustalmy datę rozpoczęcia wakacji (np. 22 czerwca bieżącego roku)
    today = datetime.today()
    vacation_start = datetime(today.year, 6, 22)

    # Jeśli wakacje w tym roku już minęły, ustawiamy datę na przyszły rok
    if today > vacation_start:
        vacation_start = datetime(today.year + 1, 6, 22)

    # Przekazujemy datę wakacji do szablonu (jako string, by JS mógł ją łatwo odczytać)
    return render_template("index.html", vacation_start=vacation_start.isoformat())

if __name__ == "__main__":
    # Uruchomienie aplikacji w trybie developerskim
    app.run(debug=True)
