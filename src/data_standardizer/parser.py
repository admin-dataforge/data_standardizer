from bs4 import BeautifulSoup

class DataParser:

    def get_cards(self, html: str):

        soup = BeautifulSoup(html, "html.parser")

        return soup.find_all(
            "div",
            class_="property-card__container"
        )