import dash
from dash import dcc, html, dash_table
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import base64

def get_logo():
    with open('Z:\\Logo Stik\\Logo_Stik_App.png', 'rb') as f:
        logo_base64 = base64.b64encode(f.read()).decode()
    return logo_base64

dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Media de Vendas 2.xlsx')
dataframe = dataframe.dropna()

top_produto = dataframe.groupby('Produto')['Qtd1'].sum().reset_index()
top_produto = top_produto.sort_values(by='Qtd1', ascending=False).head(10)

palette_colors = ['#b90011', '#cb2026', '#dc403c', '#ee5f51', '#ff7f66' , '#9A031E']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

background_gradient = {
    'background': 'linear-gradient(to right, #576574, #576574)',
}

content_max_width = '1800px'

content_style = {'maxWidth': content_max_width, 'margin': '0 auto'}

app.layout = html.Div(style=background_gradient, children=[
    html.Img(src='data:image/png;base64,{}'.format(get_logo()), style={'height': '100px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),

    dbc.Row(children=[
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='grafico-top-produtos',
                    figure={
                        'data': [
                            go.Bar(
                                x=top_produto['Qtd1'],
                                orientation='h',
                                marker=dict(color='#5F8670'), 
                                name='Quantidade Vendida'
                            ),
                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Quantidade Vendida'},
                            title='Produtos mais vendidos',
                            hovermode='closest',
                            plot_bgcolor='#B6BBC4',
                            paper_bgcolor='#B6BBC4',
                            font=dict(color='#ffffff'),
                        )
                    }
                ),
                className='mx-auto',  
            ),
            width=5,
             style={'margin-bottom': '10px', 'margin-top': '8px', 'margin-left': '150px'},
        ),

        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='cliente-mais-gastou',
                    figure={
                        'data': [
                            go.Pie(
                                labels=dataframe['Cliente'],
                                values=dataframe['Vlr'],
                                pull=[0, 0, 0, 0, 0, 0.2],
                                textinfo='label+percent',
                                hole=0.2,
                               marker=dict(
                                    colors=palette_colors,
                                    line=dict(color='#ffffff', width=2)),
                            )
                        ],
                        'layout': go.Layout(
                            title='Cliente por lucro',
                            plot_bgcolor='#B6BBC4',
                            paper_bgcolor='#B6BBC4',
                            font=dict(color='#ffffff'),
                        )   
                    }
                ),
               className='mx-auto',  
                 
            ),
            width=5,
            style={'margin-bottom': '10px', 'margin-top': '10px',},
        ),
    ]),

    dbc.Row(children=[
        dbc.Col(
            html.Div(
                dcc.Graph(
                    id='pagamentos-e-produtos-por-cliente',
                    figure={
                        'data': [
                            go.Bar(
                                x=dataframe['Cliente'],
                                y=dataframe['Vlr'],
                                text=dataframe['Vlr'],
                                marker=dict(color='#5F8670'),
                                name='Valor Pago'
                            ),
                            go.Bar(
                                x=dataframe['Cliente'],
                                y=dataframe['Qtd'],
                                text=dataframe['Qtd'],
                                marker=dict(color='#9A031E'),
                                name='Quantidade de Produtos'
                            ),
                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Clientes'},
                            barmode='group',
                            hovermode='closest',
                            showlegend=True,
                            plot_bgcolor='#B6BBC4',
                            paper_bgcolor='#B6BBC4',
                            font=dict(color='#ffffff'),
                        )
                    }
                ),
              className='mx-auto',
            ),
            width=10,
            style={'margin-bottom': '8px', 'margin-top': '8px', 'margin-left': '150px'},
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
