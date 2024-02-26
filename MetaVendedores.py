import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

dataframe = pd.read_excel('X:\\INFORMATICA\\8- TEMP\\Vendas Gerencial.xlsx', sheet_name='Ranking Geral - K')
dataframe = dataframe.iloc[5:29, 4:13]
novo_dataframe = dataframe.copy()

novo_dataframe['Unnamed: 5'] = pd.to_numeric(novo_dataframe['Unnamed: 5'], errors='coerce')
novo_dataframe['Unnamed: 6'] = pd.to_numeric(novo_dataframe['Unnamed: 6'], errors='coerce')

novo_dataframe['Diferenca'] = novo_dataframe['Unnamed: 6'] - novo_dataframe['Unnamed: 5']
novo_dataframe['fat'] = novo_dataframe['Unnamed: 6'] / novo_dataframe['Unnamed: 5'] * 100

novo_dataframe = novo_dataframe.drop(columns=novo_dataframe.columns[3:5])
novo_dataframe = novo_dataframe.sort_values(by='Unnamed: 6', ascending=False)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('Aprendendo : )'),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("graph", "id")] 
)

def update_figure(_):
    fig = go.Figure(
        data=go.Bar(
            x=novo_dataframe['fat'],
            y=novo_dataframe['Unnamed: 4'],
            marker_color='red' 
        )
    )
    fig.update_layout(
        title='Ranking de Vendas por Vendedor',
        xaxis_title='Total de Vendas',
        yaxis_title='Vendedor',
        yaxis={'categoryorder': 'total ascending'} 
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
