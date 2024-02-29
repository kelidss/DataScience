import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc

# Carregando os dados
dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Media de Vendas 2.xlsx')
dataframe = dataframe.dropna()

# Encontrando os top 10 produtos mais vendidos
top_produto = dataframe.groupby('Produto')['Qtd1'].sum().reset_index()
top_produto = top_produto.sort_values(by='Qtd1', ascending=False).head(10)

# Inicializando o aplicativo Dash com o tema do Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout usando componentes Bootstrap
app.layout = dbc.Container([
    html.H1('Análise de Vendas', className='text-center mb-4'),

    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                id='tabela-top-produtos',
                columns=[
                    {'name': 'Produto', 'id': 'Produto'},
                    {'name': 'Quantidade Vendida', 'id': 'Qtd1'},
                ],
                data=top_produto.to_dict('records'),
                style_table={'height': '300px', 'overflowY': 'auto'},
            ),
            width=6
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
                            marker=dict(colors=['red', 'orange', 'yellow', 'green', 'blue']),
                        )
                    ],
                    'layout': go.Layout(
                        title='Cliente por lucro',
                        plot_bgcolor='#f9f9f9',
                        paper_bgcolor='#f9f9f9',
                    )
                }
            ),
            width=6
        ),
    ], className='mb-4'),

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
                            marker=dict(color='green'),
                            opacity=0.7,
                            name='Valor Pago'
                        ),
                        go.Bar(
                            x=dataframe['Cliente'],
                            y=dataframe['Qtd'],
                            text=dataframe['Qtd'],
                            marker=dict(color='blue'),
                            opacity=0.7,
                            name='Quantidade de Produtos'
                        ),
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Clientes'},
                        barmode='group',
                        hovermode='closest',
                        showlegend=True,
                        plot_bgcolor='#f9f9f9',
                        paper_bgcolor='#f9f9f9',
                    )
                }
            ),
            width=12
        ),
    ]),
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
