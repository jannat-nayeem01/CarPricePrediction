# main_new.py
import dash
import dash_core_components as dbc
import dash_html_components as html
import pickle

app_new = dash.Dash(__name__)

# App layout with centered content
app_new.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Welcome to Car Price Prediction System", className="text-center"),  # Centered text
            html.H5("Insert the following value for automatic prediction...", className="text-center"),  # Centered text
            html.H6("You must need to know 3 features for predicting car price.", className="text-center"),  # Centered text
        ], width=12, className="mb-3 text-center"),  # Centered text and added margin at the bottom

        dbc.Row([
            dbc.Col([
                dbc.Label("Max Power(bhp)", className="mb-2"),  # Label with margin at the bottom
                dcc.Input(id="max_power", type="number", placeholder="Enter max power", debounce=True),
            ], width=4, className="mx-auto"),  # Centered column horizontally

            dbc.Col([
                dbc.Label("Mileage(kmpl)", className="mb-2"),  # Label with margin at the bottom
                dcc.Input(id="mileage", type="number", placeholder="Enter mileage", debounce=True),
            ], width=4, className="mx-auto"),  # Centered column horizontally

            dbc.Col([
                dbc.Label("Kilometers Driven(km)", className="mb-2"),  # Label with margin at the bottom
                dcc.Input(id="km_driven", type="number", placeholder="Enter kilometers driven", debounce=True),
            ], width=4, className="mx-auto"),  # Centered column horizontally
        ]),

        dbc.Row([
            dbc.Col([
                html.Label("Predicted Price:", className="text-center mt-3"),  # Centered label with margin at the top
                html.Div(id="predicted_price", className="lead text-center"),  # Centered text
            ], width=12),
        ]),
    ]),
], fluid=True, className="mt-5")  # Add margin from the top

@app_new.callback(
    Output("predicted_price", "children"),
    Input("max_power", "value"),
    Input("mileage", "value"),
    Input("km_driven", "value"),
)
def predict(max_power, mileage, km_driven):
    if max_power is not None and mileage is not None and km_driven is not None:
        # Scale the input data
        input_data = np.array([[max_power, mileage, km_driven]])
        scaled_input = scaler.transform(input_data)

        # Make a prediction
        predicted_price = np.exp(loaded_model.predict(scaled_input))[0]
        return f"Predicted Price: ${predicted_price:.2f}"
    if max_power is None or mileage is None or km_driven is None:
        return "Enter value to predict..."
    else:
        return "Enter valid input"

if __name__ == '__main__':
    app_new.run_server(debug=True)
