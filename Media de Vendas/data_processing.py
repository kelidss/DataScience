import plotly.graph_objects as go
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc
import base64
import pandas as pd

def get_logo():
    with open('Z:\\Logo Stik\\Logo_Stik_App.png', 'rb') as f:
        logo_base64 = base64.b64encode(f.read()).decode()
    return logo_base64

def process_data():
    dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Media de Vendas 2.xlsx')
    dataframe = dataframe.dropna()

    top_produto = dataframe.groupby('Produto')['Qtd1'].sum().reset_index()
    top_produto = top_produto.sort_values(by='Qtd1', ascending=False).head(10)

    return html.Div(children=[
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='grafico-top-produtos'),
                width=6,
                className='mx-auto',
                style={'margin-bottom': '10px', 'margin-top': '10px'},
            ),
        ]),
    ])
