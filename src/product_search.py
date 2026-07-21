import pandas as pd

from src.config import EXCEL_PATH


def buscar_producto(nombre):

    df = pd.read_excel(EXCEL_PATH)

    resultados = df[
        df["Producto"]
        .str.contains(
            nombre,
            case=False,
            na=False
        )
    ]

    if resultados.empty:
        return "No encontré ese producto."

    respuesta = ""

    for _, fila in resultados.iterrows():

        respuesta += (
            f"Producto: {fila['Producto']}\n"
            f"Precio: ${fila['Precio']}\n\n"
        )

    return respuesta