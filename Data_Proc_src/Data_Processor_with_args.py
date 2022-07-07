
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from Main_argparser import myparser
import os


args = myparser()
covidfilename = "Covid_India_report"
if args.filename:
    covidfilename = args.filename


insurancedata = 'https://raw.githubusercontent.com/veeramuthub/Data/master/insurance.csv'
Covid_Confirmeddata = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
Covid_Deathsdata = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
reportfolder = "Myreports"


timenow = time.strftime("%Y%m%d-%H%M%S")
reportfile = os.path.join(
    "..", reportfolder, f"Insurance_report_{timenow}.xlsx")


insurance = pd.read_csv(insurancedata)
insurance.pivot_table(
    index='region',
    columns='sex',
    values='expenses',
    aggfunc='sum'
).style.background_gradient(cmap='Blues', axis=0).to_excel(reportfile)


confirmed = pd.read_csv(Covid_Confirmeddata)
confirmed_long = confirmed.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
confirmed_long = confirmed_long.rename(
    columns={'variable': 'Date', 'value': 'confirmed'})
confirmed_long['Date'] = pd.to_datetime(confirmed_long['Date'])
confirmed_new = confirmed_long.groupby(
    ['Country/Region', 'Date']).agg(confirmed=('confirmed', 'sum')).reset_index()
confirmed_new = confirmed_new.sort_values(by=['Country/Region', 'Date'])

deaths = pd.read_csv(Covid_Deathsdata)
deaths_long = deaths.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'])
deaths_long = deaths_long.rename(
    columns={'variable': 'Date', 'value': 'deaths'})
deaths_long['Date'] = pd.to_datetime(deaths_long['Date'])
deaths_new = deaths_long.groupby(
    ['Country/Region', 'Date']).agg(deaths=('deaths', 'sum')).reset_index()
deaths_new = deaths_new.sort_values(by=['Country/Region', 'Date'])

covid = pd.merge(
    left=confirmed_new,
    right=deaths_new,
    on=['Country/Region', 'Date'],
    how='left'
)

covid_india = covid[covid['Country/Region'] == 'India']

reportfile = os.path.join("..", reportfolder, f"{covidfilename}_{timenow}.csv")

covid_india.to_csv(reportfile)

# python .\Data_Processor_with_args.py
# python .\Data_Processor_with_args.py -f covidreport
