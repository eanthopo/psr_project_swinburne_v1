import pandas as pd
import plotly.graph_objs as go
from pandas import DataFrame
import plotly.express as px
import re
from plotly.offline import plot

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
psr_links = []
url_template = 'https://pulsar.org.au/fold/meertime/'

for i in range(len(psrs_available)):
    psr = str(psrs_available[i]).strip()
    psrs_available_cleaned.append(psr)

for jname in jnames_cleaned:
    if psrs_available_cleaned.count(jname) > 0:
        available_or_not.append("Yes")
        psr_link = url_template + jname
        psr_links.append(psr_link)
    else:
        available_or_not.append("No")
        psr_links.append('null')

source = {
    'Name': jnames_cleaned,
    'Period': periods_cleaned,
    'Magnetic Field Strength': magnetic_fields_cleaned,
    "Available Or Not": available_or_not,
    "URLs": psr_links
}

df = DataFrame(data=source)

fig = px.scatter(df, x="Period", y="Magnetic Field Strength", color="Available Or Not", log_x=True, log_y=True, hover_name="Name", hover_data=["Period", "Magnetic Field Strength"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"])
fig.update_traces(marker=dict(
    size=7,
    opacity=0.5
))

plot_div = plot(fig, output_type='div', include_plotlyjs=True)

res = re.search('<div id="([^"]*)"', plot_div)
div_id = res.groups()[0]

js_callback = """
<script>
var plot_element = document.getElementById("{div_id}");
plot_element.on('plotly_click', function(data){{
    console.log(data);
    var point = data.points[0];
    if (point) {{
        if (point.customdata.toString() != 'null') {{
            console.log(point.customdata);
            window.open(point.customdata);
        }}
    }}
}})
</script>
""".format(div_id=div_id)

# Build HTML string
html_str = """
<html>
<body>
{plot_div}
{js_callback}
</body>
</html>
""".format(plot_div=plot_div, js_callback=js_callback)

# Write out HTML file
with open('hyperlink_fig.html', 'w') as f:
    f.write(html_str)
