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
    html.H1("Energy Data Time Series"),

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
])
# Define callback to update time series plot based on dropdown selection
@app.callback(
    Output('time-series-plot', 'figure'),
    [Input('energy-source-dropdown', 'value')]
)
def update_time_series_plot(selected_energy_source):
    # Filter data for a specific country (e.g., 'United States')
    filtered_df = df[df['country'] == 'United States']

    # Create Time Series Line Chart using Plotly Express
    fig = px.line(filtered_df, x='year', y=selected_energy_source,
                  title=f"{selected_energy_source} Over Time for United States")

    # Update layout for better readability
    fig.update_layout(xaxis_title='Year', yaxis_title=selected_energy_source)

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)