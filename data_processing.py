import base64
import pandas as pd

def get_logo():
    with open('Z:\\Logo Stik\\Logo_Stik_App.png', 'rb') as f:
        logo_base64 = base64.b64encode(f.read()).decode()
    return logo_base64

def process_data():
    # Recebendo a planilha
    dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Media de Vendas 2.xlsx')
    dataframe = dataframe.dropna()

    # Calculando os 10 produtos mais vendidos
    top_produto = dataframe.groupby('Produto')['Qtd1'].sum().reset_index()
    top_produto = top_produto.sort_values(by='Qtd1', ascending=False).head(10)

    return dataframe, top_produto
