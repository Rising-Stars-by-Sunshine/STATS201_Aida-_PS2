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
    
    # Dropdown for selecting anomaly variables
    dcc.Dropdown(
        id='anomaly-variable-dropdown',
        options=[
            {'label': 'Energy Consumption Change Percentage', 'value': 'energy_cons_change_pct'},
            {'label': 'Renewables Consumption Change Percentage', 'value': 'renewables_cons_change_pct'},
        ],
        value='energy_cons_change_pct',
        style={'width': '50%'}
    ),
    
    # Dropdown for selecting countries
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        multi=True,
        value=['United States'],  # Default selected countries
        style={'width': '50%'}
    ),
    
    # Anomaly Detection Line Plot
    dcc.Graph(id='anomaly-line-plot'),
])

# Define callback to update anomaly line plot based on dropdown selections
@app.callback(
    Output('anomaly-line-plot', 'figure'),
    [Input('anomaly-variable-dropdown', 'value'),
     Input('country-dropdown', 'value')]
)
def update_anomaly_line_plot(selected_anomaly_variable, selected_countries):
    # Filter the data based on selected countries
    filtered_df = df[df['country'].isin(selected_countries)]
    
    # Create Anomaly Detection Line Plot using Plotly Express
    fig = px.line(filtered_df, x='year', y=selected_anomaly_variable, 
                  color='country', 
                  title=f"{selected_anomaly_variable} Over Time",
                  labels={'year': 'Year', selected_anomaly_variable: 'Anomaly Variable'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)


