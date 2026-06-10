from data_standardizer.extractors import *
from data_standardizer.filter import filtrar_atributos

class DataMapper:

    @staticmethod
    def map_card(card):

        lista_atributos = get_atributos(card)
        resultado_filtro = filtrar_atributos(lista_atributos)
        precio_str   =  get_precio_str(card)

        return {
            "href" : get_href(card),
            "url_img" : get_url_img(card),
            "alt_img" : get_alt_img(card),
            "barrio" : get_barrio(card),
            "titulo" : get_titulo(card),
            "precio" : get_precio(precio_str),
            "area" : get_area(resultado_filtro),
            "hab" : get_habitaciones(resultado_filtro),
            "bano" : get_bano(resultado_filtro),
            "parq_cant" : get_parq_cant(resultado_filtro)
        }