import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output
import main  # Import your main.py
import main_new  # Import your main_new.py

# Initialize the main app
app_main = Dash(__name__)

# Define the layout for the main app
app_main.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Define callback to update the page content based on the URL
@app_main.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/main':
        return main.layout
    elif pathname == '/new':
        return main_new.layout
    else:
        return 'Page not found'

if __name__ == '__main__':
    app_main.run_server(debug=True)