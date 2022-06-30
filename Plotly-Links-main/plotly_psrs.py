import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from pandas import DataFrame

data = pd.read_csv('filtered.csv', header=None, sep="~", engine='python')
pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

psr_name = 0
psrs_available_col = 0
period_col = 4
magnetic_col = 23

jnames = data.iloc[:,psr_name]
periods = data.iloc[:,period_col]
magnetic_fields = data.iloc[:,magnetic_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]

periods_cleaned = []
magnetic_fields_cleaned = []
jnames_cleaned = []
available_or_not = []
for i in range(len(periods)):
    if '*' not in str(periods[i]) and '*' not in str(magnetic_fields[i]):
        period = float(str(periods[i]).strip())
        periods_cleaned.append(period)
        magnetic_field = float(str(magnetic_fields[i]).strip())
        magnetic_fields_cleaned.append(magnetic_field)
        jname = str(jnames[i]).strip()
        jnames_cleaned.append(jname)

psrs_available_cleaned = []
for i in range(len(psrs_available)):
    psr = str(psrs_available[i]).strip()
    psrs_available_cleaned.append(psr)

for jname in jnames_cleaned:
    if psrs_available_cleaned.count(jname) > 0:
        available_or_not.append("Yes")
    else:
        available_or_not.append("No")


print(len(available_or_not))
print(len(jnames_cleaned))
print(len(periods_cleaned))
print(len(magnetic_fields_cleaned))


source = {
    'Name': jnames_cleaned,
    'Period': periods_cleaned,
    'Magnetic Field Strength': magnetic_fields_cleaned,
    "Available Or Not": available_or_not
}

df = DataFrame(data=source)

fig = px.scatter(df, x="Period", y="Magnetic Field Strength", color="Available Or Not", log_x=True, log_y=True, hover_name="Name", hover_data=["Period", "Magnetic Field Strength"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"})
fig.update_traces(marker=dict(
    size=7,
    opacity=0.5
))
fig.show()
fig.write_html("period_vs_magnetic_field_strength.html")