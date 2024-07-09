from ArtisanProduct import ArtisanProduct
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
smtp = os.getenv('SMTP_ADDRESS')
port = int(os.getenv('SMTP_PORT'))

email_to = os.getenv('EMAIL_TO')


def check_file_exists() -> None:
    try:
        with open('data.csv', 'r') as f:
            f.read()
            return None
    except:
        with open("data.csv", "w") as f:
            f.write("date;name;price\n")
            return None


def save_current_price(name, price) -> None:
    with open("data.csv", "a", encoding="utf-8") as f:
        date = datetime.date.today()
        f.write(f"{date};{name};{price}\n")
    df = pd.read_csv("data.csv", sep=";", encoding='utf-8')
    df = df.drop_duplicates(subset=["date", "name", "price"], keep="first")
    df.to_csv("data.csv", sep=";", index=False, encoding="utf-8")


def get_min_price(name: str) -> float:
    df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
    min_price_df = df.loc[df["name"] == name]
    min_price = min_price_df["price"].min()
    return float(min_price)


def get_last_price(name: str) -> float:
    df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
    last_price = df.loc[df["name"] == name]
    last_price = last_price.tail(2)
    return float(last_price.price.iloc[0])


def show_data():
    df = pd.read_csv("data.csv", sep=";", encoding="utf-8")
    df = df.drop_duplicates(subset=["date", "name"], keep="first")
    print(df)

def send_info_mail(email_to: str, email_from: str, message: str, password:str, smtp: str, port: int) -> None:

    email_to = email_to
    email_address = email_from
    email_password = password

    with smtplib.SMTP(smtp, port) as server:
        server.starttls()
        server.login(email_address, email_password)

        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_to
        msg['Subject'] = 'Artisan'
        body = message
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        server.sendmail(email_address, email_to, text)


if __name__ == "__main__":
    check_file_exists()

    # --- first product ------
    kvh40x100x500 = ArtisanProduct("https://www.artisan.cz/kvh-hranoly-delka-5000-40x100x5000-m")
    price100 = kvh40x100x500.get_product_price()
    name100 = "kvh40x100x500"
    save_current_price(name100, price100)

    # --- second product ------
    kvh40x120x500 = ArtisanProduct("https://www.artisan.cz/kvh-hranoly-delka-5000-40x120x5000-u")
    price120 = kvh40x120x500.get_product_price()
    name120 = "kvh40x120x500"
    save_current_price(name120, price120)

# ------------------------------------------------------------
    min_price100 = get_min_price(name100)
    last_price100 = get_last_price(name100)
    min_price120 = get_min_price(name120)
    last_price120 = get_last_price(name120)

    # --- compare current and last price ------
    if price100 < last_price100:
        price_diff = last_price100-price100
        message = f"Produkt {name100} je levnejsi o {price_diff} Kc\n"
        send_info_mail(email_to, email, message, password, smtp, port)
        print(f"Produkt {name100} je levnejsi o {price_diff} Kc\n")
        print("Email odeslan")

    if price120 < last_price120:
        price_diff = last_price120-price120
        message = f"Produkt {name120} je levnejsi o {price_diff} Kc\n"
        send_info_mail(email_to, email, message, password, smtp, port)
        print(f"Produkt {name120} je levnejsi o {price_diff} Kc\n")
        print("Email odeslan")

    # --- compare current and min price ------
    if price100 < min_price100:
        price_diff = min_price100 - price100
        message = f"Produkt {name100} je nejlevnejsi v historii. Levnejsi o {price_diff} Kc\n"
        send_info_mail(email_to, email, message, password, smtp, port)
        print(f"Produkt {name100} je nejlevnejsi v historii. Levnejsi o {price_diff} Kc\n")
        print("Email odeslan")

    if price120 < min_price120:
        price_diff = min_price120 - price120
        message = f"Produkt {name120} je nejlevnejsi v historii. Levnejsi o {price_diff} Kc\n"
        send_info_mail(email_to, email, message, password, smtp, port)
        print(f"Produkt {name120} je nejlevnejsi v historii. Levnejsi o {price_diff} Kc\n")
        print("Email odeslan")

    print(f"Historicka nejnizsi cena [{name100}]: {min_price100} Kc")
    print(f"Predesla cena [{name100}]: {last_price100} Kc\n")

    print(f"Historicka nejnizsi cena [{name120}]: {min_price120} Kc")
    print(f"Predesla cena [{name120}]: {last_price120} Kc\n")

    # --- show dataframe ------
    show_data()



