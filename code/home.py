# index.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from main import app as app_old
from main_new import app_new

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Homepage"),
    dcc.Link("Old App", href='/old'),
    dcc.Link("New App", href='/new'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/new':
        return app_new.layout
    else:
        return app_old.layout

if __name__ == '__main__':
    app.run_server(debug=True)

