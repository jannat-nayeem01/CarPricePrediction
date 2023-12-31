# Import packages
from dash import Dash, html, callback, Output, Input, State, dcc
import math
import numpy as np
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import pickle

# import csv file and preprocess data
df = pd.read_csv("/root/code/Cars.csv")
df["brand"] = df["name"].str.split(" ").str[0]
df.drop(["name"], axis=1, inplace=True)
df[["mileage_value","mileage_unit"]] = df["mileage"].str.split(pat=' ', expand = True)
df[["engine_value","engine_unit"]] = df["engine"].str.split(pat=' ', expand = True)
df[["max_power_value","max_power_unit"]] = df["max_power"].str.split(pat=' ', expand = True)
df.drop(["mileage","engine","max_power"], axis=1, inplace=True)
df = df.loc[(df["fuel"] != 'LPG') & (df["fuel"] != 'CNG')]
df[["mileage","engine","max_power"]] = df[["mileage_value","engine_value","max_power_value"]].astype('float64')
df.drop(["mileage_value","engine_value","max_power_value",
        "mileage_unit","engine_unit","max_power_unit"], axis=1, inplace = True)
dict_owner = {'First Owner':1, 'Second Owner':2, 'Third Owner':3, 'Fourth & Above Owner':4,
            'Test Drive Car':5}
df["owner"] = df["owner"].map(dict_owner)
df = df[df["owner"] != 5]

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.JOURNAL]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Create app layout
app.layout = html.Div([
        html.H1("Car Price Prediction"),
        html.Br(),
        html.H3("Welcome to Website"),
        html.Br(),
        html.H6("By entering numbers into the parameters, you may estimate the cost of the car here. The three features that depend on each other to predict car prices are"),
        html.H6("Maximum power, Mileage and Kilometers driven. Firstly, Please fill up at least one input boxes, and then click submit to get result."),
        html.H6("bellow the submit button. Please make sure that filled number are not negative."),
        html.Br(),
        html.H4("Definition:"),
        html.Br(),
        html.H6("Maximum power: Maximum power of a car in bhp"),
        html.H6("Mileage: The fuel efficieny of a car or ratio of distance which a car could move per unit of fuel consumption measuring in km/l"),
        html.H6("Kilometers driven: Total distance driven in a car by previous owner in km"),
        html.Br(),
        html.Div(["Maximum power",dbc.Input(id = "max_power", type = 'number', min = 0, placeholder="please insert"),
        dbc.FormText("Please do not put nagative numbers.",color="secondary"), html.Br()]),
        html.Div(["Mileage", dbc.Input(id = "mileage", min = 0, type = 'number', placeholder ="please insert"),
        dbc.FormText("Please do not put nagative numbers.",color="secondary"), html.Br()]),
        html.Div(["Kilometers driven", dbc.Input(id = "km_driven", type = 'number', min = 0, placeholder="please insert"),
        dbc.FormText("Please do not put nagative numbers.",color="secondary"), html.Br()]),
        dbc.Button(id="submit", children="submit", color="primary", className="me-1"),
        html.Div(id="output", children = '')
])

# callback input and output
@callback(
    Output(component_id = "output", component_property = "children"),
    State(component_id = "max_power", component_property = "value"),
    State(component_id = "mileage", component_property = "value"),
    State(component_id = "km_driven", component_property = "value"),
    Input(component_id = "submit", component_property = "n_clicks"),
    prevent_initial_call=True
)

# function for finding estimated car price
def prediction (max_power, mileage, km_driven, submit):
    if max_power == None:
        max_power = df["max_power"].median()
    if mileage == None:
        mileage = df["mileage"].mean()
    if km_driven == None:
        km_driven = df["km_driven"].median()
    model = pickle.load(open("/root/code/car_prediction.model", 'rb'))
    sample = np.array([[max_power, mileage, math.log(km_driven)]])
    result = np.exp(model.predict(sample))
    return f"The predictive car price is {round(result[0],2)}"

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:8051/