import requests
from bs4 import BeautifulSoup

class ArtisanProduct:
    def __init__(self, link: str):
        self.link = link
        self.request = requests.get(link)
        self.status = self.request.status_code
        self.soup = BeautifulSoup(self.request.text, 'html.parser')

    def get_product_price(self) -> float:
        try:
            price = self.soup.find(id="product_price_with_tax").get_text()
            price = float(price.replace(",", "."))
            return price
        except:
            return "Some error"

    def get_product_name(self) -> str:
        try:
            name = self.soup.h1
            return name.text
        except:
            return "Some error"