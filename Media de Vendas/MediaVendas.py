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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

background_gradient = {
    'background': 'linear-gradient(to right, #61677A, #61677A)'
}

app.layout = html.Div(style=background_gradient, children=[
    html.Img(src='data:image/png;base64,{}'.format(get_logo()), style={'height': '150px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    html.H1('Análise de Vendas', className='text-center mb-4', style={'color': '#61677A'}),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id='grafico-top-produtos',
                figure={
                    'data': [
                        go.Bar(
                            x=top_produto['Qtd1'],
                            orientation='h',
                            marker=dict(color='#9A031E'), 
                            opacity=0.7,
                            name='Quantidade Vendida'
                        ),
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Quantidade Vendida'},
                        title='Produtos mais vendidos',
                        hovermode='closest',
                        showlegend=True,
                        plot_bgcolor='#B6BBC4',
                        paper_bgcolor='#B6BBC4',
                        font=dict(color='#ffffff'),
                    )
                }
            ),
            width=6,
            className='mx-auto',
            style={'margin-bottom': '10px', 'margin-top': '10px'},  
        ),

        dbc.Col(
            dcc.Graph(
                id='cliente-mais-gastou',
                figure={
                    'data': [
                        go.Pie(
                            labels=dataframe['Cliente'],
                            values=dataframe['Vlr'],
                            pull=[0, 0, 0, 0, 0, 0.2],
                            textinfo='label+percent',
                            hole=0.3,
                            marker=dict(colors=['#FF6F61', '#99C24D', '#3B3E4D', '#3099A7', '#FAB133', '#C52D4B']),
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
            width=6,
            className='mx-auto',
            style={'margin-bottom': '10px', 'margin-top': '10px',}, 
        ),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id='pagamentos-e-produtos-por-cliente',
                figure={
                    'data': [
                        go.Bar(
                            x=dataframe['Cliente'],
                            y=dataframe['Vlr'],
                            text=dataframe['Vlr'],
                            marker=dict(color='black'),
                            opacity=0.7,
                            name='Valor Pago'
                        ),
                        go.Bar(
                            x=dataframe['Cliente'],
                            y=dataframe['Qtd'],
                            text=dataframe['Qtd'],
                            marker=dict(color='#9A031E'),
                            opacity=0.7,
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
            width=11,
            className='mx-auto',
            style={'margin-bottom': '30px', 'margin-top': '10px'},  
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
