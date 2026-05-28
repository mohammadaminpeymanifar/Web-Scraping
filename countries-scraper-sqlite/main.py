import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "https://www.scrapethissite.com/pages/simple/"

def fetch_countries():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    countries = []

    country_cards = soup.find_all("div", class_="country")

    for country in country_cards[:20]:
        name = country.find("h3", class_="country-name").text.strip()
        capital = country.find("span", class_="country-capital").text.strip()

        population = country.find("span", class_="country-population").text.strip()
        area = country.find("span", class_="country-area").text.strip()

        countries.append({
            "name": name,
            "capital": capital,
            "population": int(population),
            "area": int(float(area))
        })

    return countries


def create_db():
    conn = sqlite3.connect("countries.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_name TEXT NOT NULL,
            capital TEXT,
            population INTEGER,
            area INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_data(countries):
    conn = sqlite3.connect("countries.db")
    cursor = conn.cursor()

    for c in countries:
        cursor.execute("""
            INSERT INTO countries (country_name, capital, population, area)
            VALUES (?, ?, ?, ?)
        """, (c["name"], c["capital"], c["population"], c["area"]))

    conn.commit()
    conn.close()


def show_results():
    conn = sqlite3.connect("countries.db")
    cursor = conn.cursor()

    print("\n📌 First 5 records:\n")
    for row in cursor.execute("SELECT * FROM countries LIMIT 5"):
        print(row)

    cursor.execute("SELECT SUM(population) FROM countries")
    total_population = cursor.fetchone()[0]

    print("\n🌍 Total population of 20 countries:", total_population)

    conn.close()


if __name__ == "__main__":
    create_db()
    data = fetch_countries()
    insert_data(data)

    print("✅ Data extraction completed successfully!")
    show_results()