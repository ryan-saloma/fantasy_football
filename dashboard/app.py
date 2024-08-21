from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)
df = pd.read_csv('data/cleaned_fantasy_1970.csv')
df100 = df.sort_values('ppr_points', ascending=False).head(100)
fig = px.pie(df100, df100['position'], title = 'Top 100 Fantasy Football Players by Position')
app.layout = [html.Title('Fantasy Football Dashboard'),
              html.Div(children=[
                html.H1('Fantasy Fantasy Football Dashboard'),
                dcc.Graph(id='fantasy-football-graph',figure=fig)])
            ]

if __name__ == '__main__':
    app.run(debug=True)