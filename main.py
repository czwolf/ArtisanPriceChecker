from ArtisanProduct import ArtisanProduct
import pandas as pd
import datetime


def check_file_exists() -> None:
    try:
        with open('data.csv', 'r') as f:
            data = f.read()
            return None
    except:
        with open("data.csv", "w") as f:
            f.write("date;name;price")
            return None

def save_current_price(name, price) -> None:
    with open("data.csv", "w") as f:
        date = datetime.date.today()
        f.write(f"{date};{name};{price}\n")

if __name__ == "__main__":
    check_file_exists()

    kvh40x100x500 = ArtisanProduct("https://www.artisan.cz/kvh-hranoly-delka-5000-40x100x5000-m")
    max_price100 = 0
    min_price100 = 0
    price100 = kvh40x100x500.get_product_price()
    name100 = kvh40x100x500.get_product_name()

    kvh40x120x500 = ArtisanProduct("https://www.artisan.cz/kvh-hranoly-delka-5000-40x120x5000-u")

    price120 = kvh40x120x500.get_product_price()
    name120 = kvh40x120x500.get_product_name()

    save_current_price(name100, price100)

    with open("data.csv", "r") as f:
        print(f.read())



