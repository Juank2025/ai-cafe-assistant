import pandas as pd
from src.config import EXCEL_PATH

def cargar_productos():

    df = pd.read_excel(EXCEL_PATH)

    print(df)

    return df