from bs4 import BeautifulSoup

class DataParser:

    @staticmethod
    def get_cards(html: str):

        soup = BeautifulSoup(html, "html.parser")

        return soup.find_all(
            "div",
            class_="property-card__container"
        )