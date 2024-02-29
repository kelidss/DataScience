from dash import dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from data_processing import process_data


dataframe, top_produto = process_data()

def register_callbacks(app):
    @app.callback(
        Output('grafico-top-produtos', 'figure'),
        [Input('dummy-input', 'children')]
    )
    def update_grafico_top_produtos(_):
        figure = {
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
        return figure
