import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/Rising-Stars-by-Sunshine/STATS201_Aida/main/data/owid-energy-data.csv"
df = pd.read_csv(url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Energy Data Analysis Dashboard"),
    
    # Dropdown for selecting energy source
    dcc.Dropdown(
        id='energy-source-dropdown',
        options=[
            {'label': 'Electricity Generation', 'value': 'electricity_generation'},
            {'label': 'Renewables Electricity', 'value': 'renewables_electricity'},
            {'label': 'Fossil Electricity', 'value': 'fossil_electricity'}
        ],
        value='electricity_generation',
        style={'width': '50%'}
    ),
    
    # Time Series Plot
    dcc.Graph(id='time-series-plot'),
    
    # Choropleth Map
    dcc.Graph(id='choropleth-map'),
])

# Define callback to update time series plot based on dropdown selection
@app.callback(
    Output('time-series-plot', 'figure'),
    [Input('energy-source-dropdown', 'value')]
)
def update_time_series_plot(selected_energy_source):
    # Create Time Series Plot using Plotly Express
    fig = px.line(df, x='year', y=selected_energy_source, title=f"{selected_energy_source} Over Time")
    return fig

# Define callback to update choropleth map based on dropdown selection
@app.callback(
    Output('choropleth-map', 'figure'),
    [Input('energy-source-dropdown', 'value')]
)
def update_choropleth_map(selected_energy_source):
    # Create Choropleth Map using Plotly Express
    fig = px.choropleth(df, 
                        locations='country', 
                        locationmode='country names', 
                        color=selected_energy_source,
                        title=f"{selected_energy_source} by Country",
                        color_continuous_scale='Viridis')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
