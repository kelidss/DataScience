import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objects as go
from data_processing import get_logo, process_data

# Obtendo o logo em base64
logo_base64 = get_logo()

# Processando os dados
dataframe, top_produto = process_data()
palette_colors = ['#b90011', '#cb2026', '#dc403c', '#ee5f51', '#ff7f66', '#9A031E']

# Estilo para o fundo
background_gradient = {'background': 'linear-gradient(to right, #576574, #576574)'}

# Definindo o layout do aplicativo
layout = html.Div(style=background_gradient, children=[
html.Img(src='data:image/png;base64,{}'.format(get_logo()),
style={'height': '100px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),

#adicionando o grafico e o layout
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
                    marker=dict(color='#387ADF'), 
                    name='Quantidade Vendida'),],

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

        #adicionando o grafico e o layout
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
                            line=dict(color='#ffffff', width=2)),)
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

    #adicionando o grafico e o layout
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
                            #adicionando outra coluna no mesmo grafico
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