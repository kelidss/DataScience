import dash
import layout  
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout.layout

if __name__ == '__main__':
    app.run_server(debug=True)
