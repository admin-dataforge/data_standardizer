from data_standardizer.reader import read_html
from data_standardizer.parser import DataParser
from data_standardizer.mapper import DataMapper
from bs4 import BeautifulSoup
from data_standardizer.writer import Saver


def main(html_path: str,parquet_path:str):
    # 1. leer html
    datos : str =  read_html(html_path)

    # 2. configurar las cards
    cards : BeautifulSoup = DataParser.get_cards(datos)

    # 3. pasar los datos
    data_rows = [ DataMapper.map_card(card) for card in cards ]

    # 4. guardar los datos
    Saver.guardar(parquet_path,data_rows)

