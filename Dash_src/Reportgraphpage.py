from dash import dcc
from dash import html
import dash
import dash_bootstrap_components as dbc
import os
import pandas as pd
import plotly.express as px


def update_line_chart(data):
    df = data  # replace with your own data source
    fig = px.line(df)
    # x="year", y="lifeExp", color='country')
    return fig


def AnalysisPageContent(pathname, reportfoldername):
    reportname = pathname.split('/')[1]
    reportpath = os.path.join(reportfoldername, reportname)
    df = pd.read_csv(reportpath)

    return html.Div([
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4('Cumulative confirmed covid cases in india'),
                        html.Div(  # content for corridor width left
                            [
                                dcc.Graph(
                                    id="graphcum",
                                    figure=update_line_chart(
                                        df.set_index('Date')['confirmed']),
                                ),
                            ]),

                    ],
                ),
                dbc.Col(
                    [
                        html.H4('Perday confirmed covid cases in india'),
                        dcc.Graph(id="graphpd",
                                  figure=update_line_chart(
                                      df.set_index('Date')['confirmed'].diff()),
                                  ),

                    ],
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4('Cumulative deaths covid cases in india'),
                        html.Div(  # content for corridor width left
                            [
                                dcc.Graph(
                                    id="graphcumd",
                                    figure=update_line_chart(
                                        df.set_index('Date')['deaths']),
                                ),
                            ]),

                    ],
                ),
                dbc.Col(
                    [
                        html.H4('Perday deaths covid cases in india'),
                        dcc.Graph(id="graphpdd",
                                  figure=update_line_chart(
                                      df.set_index('Date')['deaths'].diff()),
                                  ),

                    ],
                ),
            ],
        ),
    ]

    )
    # print(reportfoldername)
    pass
