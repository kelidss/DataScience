import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd


dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Vendas Gerencial.xlsx', sheet_name='Ranking Geral - K')


novo_dataframe = dataframe.iloc[5:29, 4:13]
novo_dataframe['Unnamed: 5'] = pd.to_numeric(novo_dataframe['Unnamed: 5'], errors='coerce')
novo_dataframe['Unnamed: 6'] = pd.to_numeric(novo_dataframe['Unnamed: 6'], errors='coerce')
novo_dataframe['Diferenca'] = novo_dataframe['Unnamed: 6'] - novo_dataframe['Unnamed: 5']
novo_dataframe['fat'] = novo_dataframe['Unnamed: 6'] / novo_dataframe['Unnamed: 5'] * 100
novo_dataframe = novo_dataframe.drop(columns=novo_dataframe.columns[3:5])
novo_dataframe = novo_dataframe.sort_values(by='Unnamed: 6', ascending=False)


total_meta = novo_dataframe['Unnamed: 5'].sum()
total_feito = novo_dataframe['Unnamed: 6'].sum()
geral = total_meta - total_feito


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('Ranking de Vendas por Vendedor', style={'textAlign': 'center', 'color': '#ffffff'}),
    dcc.Graph(id="bar-graph"),
    dcc.Graph(id="pie-chart"),
], style={'fontFamily': 'Arial, sans-serif', 'maxWidth': '200', 'margin': 'left', 'backgroundColor': '#000000', 'color': '#ffffff'})


@app.callback(
    Output("bar-graph", "figure"),
    [Input("bar-graph", "id")]
)
def update_bar_graph(_):
    fig = go.Figure(
        data=go.Bar(
            x=novo_dataframe['Unnamed: 6'],
            y=novo_dataframe['Unnamed: 4'],
            marker_color='#423c9d',  
            orientation='h'
        )
    )
    fig.update_layout(
        xaxis_title='Total vendido',
        yaxis={'categoryorder': 'total ascending'},
        plot_bgcolor='#f9f9f9',  
        paper_bgcolor='#f9f9f9',  
    )
    fig.update_layout(height=len(novo_dataframe) * 40)
    return fig


@app.callback(
    Output("pie-chart", "figure"),
    [Input("pie-chart", "id")]
)
def update_pie_chart(_):
    fig = go.Figure(
        data=go.Pie(
            labels=['Total Realizado', 'Falta para atingir a meta'],
            values=[total_feito, geral],
            hole=0.3,
            marker_colors=['#2ca02c', '#d62728'],  
        )
    )
    fig.update_layout(title='Sobre a meta mensal:')
    fig.update_layout(height=len(novo_dataframe) * 20)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
