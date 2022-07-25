import plotly.graph_objects as go
from plotly import express as px
import plotly
import pandas as pd
from pandas import DataFrame
from astropy.visualization import quantity_support
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from matplotlib import pyplot as plt
import re
from plotly.offline import plot

# fig = go.Figure(go.Scattergeo())
# fig.update_geos(projection_type="mollweide")
# fig.update_geos(visible=False)
# fig.update_geos(showframe=True)
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.write_html("project_test.html")
# plotly.offline.plot(fig)
# fig.show()

quantity_support()

data = pd.read_csv('filtered.csv', header=None, sep="~", engine='python')
pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

psr_col = 0
df_raj_col = 33
df_decj_col = 36
psrs_available_col = 0

jnames_list = data.iloc[:,psr_col]
df_raj_list = data.iloc[:,df_raj_col]
df_decj_list = data.iloc[:,df_decj_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]

df_psr_list = data.iloc[:,0]

raj = []
decj = []
jnames_cleaned = []
available_or_not = []

psrs_available_cleaned = []
psr_links = []
url_template = 'https://pulsars.org.au/fold/meertime/'

for i in range(len(psrs_available)):
    psr = str(psrs_available[i]).strip()
    psrs_available_cleaned.append(psr)
    
for i in range(len(df_psr_list)):
    if '*' not in str(df_raj_list) and '*' not in str(df_decj_list):
        raj_temp = str(df_raj_list[i]).strip()
        decj_temp = str(df_decj_list[i]).strip()
        raj.append(raj_temp)
        decj.append(decj_temp)
        jname = str(jnames_list[i].strip())
        jnames_cleaned.append(jname)
        
        
for jname in jnames_cleaned:
    if psrs_available_cleaned.count(jname) > 0:
        available_or_not.append("Yes")
        psr_link = url_template + jname
        psr_links.append(psr_link)
    else:
        available_or_not.append("No")
        psr_links.append('null')


c = SkyCoord(ra=raj,dec=decj, unit=(u.hourangle,u.deg))
ranew = coord.Angle(c.ra.deg,unit=u.deg)
ranew2 = ranew.wrap_at('180d', inplace=False)
decnew = coord.Angle(c.dec.deg,unit=u.degree)
# print(ranew2,decnew)

source = {
    'Name': jnames_cleaned,
    'raj': ranew2,
    'decj': decnew,
    "Available Or Not": available_or_not,
    "URLs": psr_links
}
# print(len(jnames_cleaned),len(ranew2),len(decnew), len(available_or_not),len(psr_links))

df = DataFrame(data=source)

# df = px.data.gapminder().query("year == 2007")

fig = px.scatter_geo(df, lon='raj', lat='decj', color="Available Or Not", projection="mollweide", hover_name="Name", color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"] 
                       # size of markers, "pop" is one of the columns of gapminder
                     )
    
fig.update_geos(showframe=True, visible=False)

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
with open('temp-plot.html', 'w') as f:
    f.write(html_str)
fig.show()
# plotly.offline.plot(fig)
