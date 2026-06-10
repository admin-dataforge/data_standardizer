import pandas as pd

class Saver:

    @staticmethod
    def guardar(path:str, datos:list):
        df = pd.DataFrame(datos)

        df.to_parquet(path)