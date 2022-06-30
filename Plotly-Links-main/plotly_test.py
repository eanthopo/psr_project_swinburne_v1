# Plotly Test

import pandas as pd
from pandas import DataFrame
import plotly.express as px
import re
from plotly.offline import plot

data = pd.read_csv('filtered.csv', header=None, sep="~", engine='python')
pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

psr_col = 0
psrs_available_col = 0
period_col = 4
p1_col = 13

jnames_list = data.iloc[:,psr_col]
period_list = data.iloc[:,period_col]
p1_list = data.iloc[:,p1_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]

periods_cleaned = []
p1_cleaned = []
jnames_cleaned = []
available_or_not = []
for i in range(len(period_list)):
    if ('*' not in str(period_list[i])) and ('*' not in str(p1_list[i])):
        period = float(str(period_list[i]).strip())
        periods_cleaned.append(period)
        p1 = float(str(p1_list[i]).strip())
        p1_cleaned.append(p1)
        jname = str(jnames_list[i].strip())
        jnames_cleaned.append(jname)
        
psrs_available_cleaned = []
psr_links = []
url_template = 'https://pulsars.org.au/fold/meertime/'

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
    'p0': periods_cleaned,
    'p1': p1_cleaned,
    "Available Or Not": available_or_not,
    "URLs": psr_links
}

df = DataFrame(data=source)

fig = px.scatter(df, x="p0", y="p1", color="Available Or Not", log_x=True, log_y=True, hover_name="Name", hover_data=["p0", "p1"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"])
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




























