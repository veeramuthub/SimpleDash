from flask import Flask
from random import Random
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import os
from logging.handlers import RotatingFileHandler
import logging
from dash.dependencies import Input, Output, State
from Homepage import generateHomeContent, navbar
from sidebar import generatesidebar
from Utils import *
from Reportgraphpage import *

# App Paths
server = Flask(__name__)
Currentdirname = os.path.basename(os.path.dirname(__file__))
reportfoldername = os.path.join(os.path.dirname(__file__), '..', 'Myreports')

app = dash.Dash(server=server, external_stylesheets=[
                dbc.themes.SPACELAB], title='Reporting Dashboards', suppress_callback_exceptions=True)
handler = RotatingFileHandler(os.path.join(
    reportfoldername, 'logs', 'error_log.log'), maxBytes=102400, backupCount=10)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)

sidebar = generatesidebar([])

print(reportfoldername)


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# Main Content definition tag
MainContent = html.Div(id="page-content", style=CONTENT_STYLE)

# Main content page renderer.


@app.callback(Output("page-content", "children"), Output("sidebarcontainer", "children"), [Input("url", "pathname"), State("sidebarcontainer", "children")])
def render_page_content(pathname, dynsidebar):
    dynsidebar = generatesidebar(getreportlist(reportfoldername))
    if pathname == "/":
        # check for app first run //Permanent state of web app cycle.
        #
        return generateHomeContent(), dynsidebar,
    elif pathname.split('/')[1] in getreportlist(reportfoldername):
        return AnalysisPageContent(pathname, reportfoldername), dynsidebar
    # If the user tries to reach a different page, return a 404 message
    return dbc.Card(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    ), dynsidebar


# End of all Content definition and layout stitching.
app.layout = html.Div([dcc.Location(id="url"), navbar,
                      sidebar, MainContent])

if __name__ == "__main__":
    app.run_server(debug=True, port=80)  # ,host="0.0.0.0")
