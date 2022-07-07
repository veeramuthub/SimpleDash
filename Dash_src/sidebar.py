from dash import dcc
from dash import html
import dash
import dash_bootstrap_components as dbc
REPORT_LIST = {
    "overflow-y": "auto",
    "max-height": "400px",
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f5f5f5",

}


def generatesidebar(reportlist):
    return html.Div(
        [
            html.H3("Processed Reports"),
            html.Hr(),
            html.P(
                "Reports portal ", className="lead"
            ),

            html.Div(
                [
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink(
                                "Home", href="/", active="exact")),
                            dbc.NavItem(html.H5("Reports")),
                        ] +
                        [dbc.NavItem(dbc.NavLink(
                            report, href="/" + report, active="exact")) for report in reportlist],
                        vertical=True,
                        pills=True,
                    ),
                ],
                style=REPORT_LIST,
            ),
        ],
        id="sidebarcontainer",
        style=SIDEBAR_STYLE,
    )
