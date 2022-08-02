# Evan Anthopoulos
# Plotly to HTML with Astropy

import pandas as pd
from astropy.visualization import quantity_support
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from matplotlib import pyplot as plt
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import re
from plotly.offline import plot

quantity_support()

data = pd.read_csv('filtered.csv', header=None, sep="~", engine='python')
pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

psr_col = 0
period_col = 4
p1_col = 13
raj_col = 33
decj_col = 36

psrs_available_col = 0

jnames_list = data.iloc[:,psr_col]
period_list = data.iloc[:,period_col]
p1_list = data.iloc[:,p1_col]
raj_list = data.iloc[:,raj_col]
decj_list = data.iloc[:,decj_col]

psrs_available = pulsars_available.iloc[:, psrs_available_col]

raj_cleaned = []
decj_cleaned = []
jnames_cleaned = []
available_or_not = []
for i in range(len(period_list)):
    if ('*' not in str(raj_list[i])) and ('*' not in str(decj_list[i])):
        raj = str(raj_list[i]).strip()
        raj_cleaned.append(raj)
        decj = str(decj_list[i]).strip()
        decj_cleaned.append(decj)
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
    'raj': raj_cleaned,
    'decj': decj_cleaned,
    "Available Or Not": available_or_not,
    "URLs": psr_links
}

df = DataFrame(data=source)

c = SkyCoord(ra=raj_list,dec=decj_list, unit=(u.hourangle,u.deg), frame='icrs')
ranew = coord.Angle(c.ra.rad,unit=u.rad)
ranew2 = ranew.wrap_at('180d', inplace=False)
decnew = coord.Angle(c.dec.rad,unit=u.degree)


fig = px.scatter(df, x="raj", y="decj", color="Available Or Not", log_x=True, log_y=True, hover_name="Name", hover_data=["raj", "decj", "Available Or Not"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"])
# fig = px.choropleth(df, color="Available Or Not", hover_name="Name", hover_data=["raj", "decj"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"])
# fig.update_traces(marker=dict(
#     size=7,
#     opacity=0.5
# ))



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