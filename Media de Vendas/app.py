import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from callbacks import register_callbacks
from styles import background_gradient
from data_processing import get_logo, process_data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(style=background_gradient, children=[
    html.Img(src='data:image/png;base64,{}'.format(get_logo()), style={'height': '150px', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),
    html.H1('Análise de Vendas', className='text-center mb-4', style={'color': '#61677A'}),
    process_data(),
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
