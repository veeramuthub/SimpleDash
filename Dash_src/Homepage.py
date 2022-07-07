import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import dash

navbar = dbc.NavbarSimple(
    children=[
        html.P(id="Reportportal"),
    ],
    color="primary",
    dark=False,
    fluid=True,
)


def generateHomeContent():
    return html.Div(
        [
            dbc.Card(
                [
                    html.H1("Report dashboard portal", className="display-2"),
                    html.Hr(className="my-2"),
                    html.P(
                        "https://github.com/veeramuthub", className="font-italic"
                    ),
                ]
            ),

        ]
    )
