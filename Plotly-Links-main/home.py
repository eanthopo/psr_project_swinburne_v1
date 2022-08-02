# @author: Evan Anthopoulos
# Home Page for the Swinburne Encyclpedia of Radio Pulsar Astronomy !

import pandas as pd
from astropy.visualization import quantity_support
from plotly import express as px
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from pandas import DataFrame
import re
from plotly.offline import plot

class Home:
    
    def plotly_load(self):
        psrs_available_cleaned = []
        jnames_cleaned = []
        available_or_not = []
        psr_links = []
        clickable = []
        det_disc_list = []
        for i in range(len(jname_list)):
            jname = str(jname_list[i].strip())
            jnames_cleaned.append(jname)
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
        for i in range(len(available_or_not)):
            if str(available_or_not[i]).strip() == 'Yes':
                jname_temp = jnames_cleaned[i]
                clickable.append(jname_temp + ':   Click on this pulsar to be taken to the MeerTime portal.')
                det_disc_list.append('All Known Pulsars in MeerTime - Click to View / Hide')
            elif str(available_or_not[i]).strip() == 'No':
                jname_temp = jnames_cleaned[i]
                det_disc_list.append('All Known Pulsars - Click to View / Hide')
                clickable.append(jname_temp + ':   This pulsar is not clickable.')
        return [clickable, det_disc_list, available_or_not, psr_links]
                
                
                
    def raj_decj_plt(self):
        quantity_support()
        raj = []
        decj = []
        jname = []
        jnames_cleaned = []
        clickable = plotly_load[0]
        det_disc_list = plotly_load[1]
        available_or_not = plotly_load[2]
        psr_links = plotly_load[3]
        for i in range(len(jname_list)):
            raj_temp = str(raj_list[i]).strip()
            decj_temp = str(decj_list[i]).strip()
            if '*' not in str(raj_list[i]) and '*' not in str(decj_list[i]):
                raj.append(raj_temp)
                decj.append(decj_temp)
        c = SkyCoord(ra=raj,dec=decj, unit=(u.hourangle,u.deg))
        ranew = coord.Angle(c.ra.deg,unit=u.deg)
        ranew2 = ranew.wrap_at('180d', inplace=False) * (-1)
        decnew = coord.Angle(c.dec.deg,unit=u.degree)
        source = {
            'Name': clickable,
            'raj': ranew2,
            'decj': decnew,
            'Legend (RA (J2000) vs Dec (J2000))': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lon='raj', lat='decj', labels=dict(lat='raj (rad)', lon='decj(deg)'), color="Legend (RA (J2000) vs Dec (J2000))", width=1000, height=500, title='All Known Pulsars in Equatorial Coordinates', hover_name="Name", color_discrete_map={"All Known Pulsars in MeerTime - Click to View / Hide" : "#1C86EE", "All Known Pulsars - Click to View / Hide": "#FFA500"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        fig.update_traces(marker=dict(size=4))
        fig.update_xaxes(title_text='raj (rad)')
        fig.update_xaxes(range=[360,-360])
        fig.update_yaxes(title_text='decj (deg)')
        fig.show()

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
               {plot_div}
               {js_callback}
        """.format(plot_div=plot_div, js_callback=js_callback)

        # Write out HTML file
        print('<center>' + html_str + '</center>', file = html_file)
        
        
        
    def gl_gb_plt(self):
        psrs_available_cleaned = []
        psr_links = []
        gl = []
        gb = []
        clickable = plotly_load[0]
        det_disc_list = plotly_load[1]
        available_or_not = plotly_load[2]
        psr_links = plotly_load[3]
        for i in range(len(jname_list)):
            gl_temp = str(gl_list[i]).strip()
            gb_temp = str(gb_list[i]).strip()
            if '*' not in str(gl_list[i]) and '*' not in str(gb_list[i]):
                gb_temp = str(float(gb_temp)*(-1))
                gl.append(gl_temp)
                gb.append(gb_temp)
                
        source = {
            'Name': clickable,
            'gl': gl,
            'gb': gb,
            'Legend (Galactic Latitude vs Galactic Longitude)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lon='gb', lat='gl', labels=dict(lat='gl', lon='gb'), color="Legend (Galactic Latitude vs Galactic Longitude)", width=1000, height=500, title='All Known Pulsars in Galactic Coordinates', hover_name="Name", color_discrete_map={"All Known Pulsars in MeerTime - Click to View / Hide" : "#1C86EE", "All Known Pulsars - Click to View / Hide": "#FFA500"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        fig.update_traces(marker=dict(size=4))
        fig.show()

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
               {plot_div}
               {js_callback}
        """.format(plot_div=plot_div, js_callback=js_callback)

        # Write out HTML file
        print('<center>' + html_str + '</center>', file = html_file)



    def p_pdot_plt(self):
        psrs_available_cleaned = []
        psr_links = []
        period = []
        p1 = []
        clickable = plotly_load[0]
        det_disc_list = plotly_load[1]
        available_or_not = plotly_load[2]
        psr_links = plotly_load[3]
        for i in range(len(jname_list)):
            period_temp = str(period_list[i]).strip()
            p1_temp = str(p1_list[i]).strip()
            if '*' not in str(period_list[i]) and '*' not in str(p1_list[i]):
                period.append(period_temp)
                p1.append(p1_temp)
            else:
                period.append('null')
                p1.append('null')
        source = {
            'Name': clickable,
            'Spin Period (s)': period,
            'Period Derivative (s/s)': p1,
            'Legend (Spin Period (s) vs Period Derivative (s/s))': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='Spin Period (s)', y='Period Derivative (s/s)', log_x=True, log_y=True, color="Legend (Spin Period (s) vs Period Derivative (s/s))", width=1000, height=500, title='Spin Period (s) vs Period Derivative (s/s)', hover_name="Name", color_discrete_map={"All Known Pulsars in MeerTime - Click to View / Hide" : "#1C86EE", "All Known Pulsars - Click to View / Hide": "#FFA500"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        # fig.update_xaxes(type="linear")
        fig.update_layout(
        xaxis={'title': 'Spin Period (s)', 'showexponent': 'all', 'exponentformat': 'e', 'rangemode': 'tozero',
               'ticks': 'outside'},
        yaxis={'title': 'Period Derivative (s/s)', 'showexponent': 'all', 'exponentformat': 'e', 'rangemode': 'tozero',
               'ticks': 'outside'})
        fig.update_traces(marker=dict(size=4))
        fig.show()
   
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
               {plot_div}
               {js_callback}
        """.format(plot_div=plot_div, js_callback=js_callback)
   
        # Write out HTML file
        print('<center>' + html_str + '</center>', file = html_file)



    def xx_yy_plt(self):
        psrs_available_cleaned = []
        psr_links = []
        xx = []
        yy = []
        clickable = plotly_load[0]
        det_disc_list = plotly_load[1]
        available_or_not = plotly_load[2]
        psr_links = plotly_load[3]
        for i in range(len(jname_list)):
            xx_temp = str(xx_list[i]).strip()
            yy_temp = str(yy_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(yy_list[i]):
                xx.append(xx_temp)
                yy.append(yy_temp)
            else:
                xx.append('null')
                yy.append('null')
        source = {
            'Name': clickable,
            'x-distance (kpc)': xx,
            'y-distance (kpc)': yy,
            'Legend (x-distance (kpc) vs y-distance (kpc))': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='y-distance (kpc)', color="Legend (x-distance (kpc) vs y-distance (kpc))", width=1000, height=500, title='x-distance (kpc) vs y-distance (kpc) (Our Sun is at x=8.5 kpc, y=0.0 kpc)', hover_name="Name", color_discrete_map={"All Known Pulsars in MeerTime - Click to View / Hide" : "#1C86EE", "All Known Pulsars - Click to View / Hide": "#FFA500"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        fig.update_layout(autotypenumbers='convert types')
        fig.update_traces(marker=dict(size=4))
        fig.show()
   
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
               {plot_div}
               {js_callback}
        """.format(plot_div=plot_div, js_callback=js_callback)
   
        # Write out HTML file
        print('<center>' + html_str + '</center>', file = html_file)


    def xx_zz_plt(self):
        psrs_available_cleaned = []
        psr_links = []
        xx = []
        zz = []
        clickable = plotly_load[0]
        det_disc_list = plotly_load[1]
        available_or_not = plotly_load[2]
        psr_links = plotly_load[3]
        for i in range(len(jname_list)):
            xx_temp = str(xx_list[i]).strip()
            zz_temp = str(zz_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(zz_list[i]):
                xx.append(xx_temp)
                zz.append(zz_temp)
            else:
                xx.append('null')
                zz.append('null')
        source = {
            'Name': clickable,
            'x-distance (kpc)': xx,
            'z-distance (kpc)': zz,
            'Legend (x-distance (kpc) vs z-distance (kpc))': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='z-distance (kpc)', color="Legend (x-distance (kpc) vs z-distance (kpc))", width=1000, height=500, title='x-distance (kpc) vs z-distance (kpc) (Zoomed In)', hover_name="Name", color_discrete_map={"All Known Pulsars in MeerTime - Click to View / Hide" : "#1C86EE", "All Known Pulsars - Click to View / Hide": "#FFA500"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        fig.update_layout(autotypenumbers='convert types')
        fig.update_xaxes(range=[-10, 15])
        fig.update_yaxes(range=[-2, 2])
        fig.update_traces(marker=dict(size=4))
        fig.show()
   
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
               {plot_div}
               {js_callback}
        """.format(plot_div=plot_div, js_callback=js_callback)
   
        # Write out HTML file
        print('<center>' + html_str + '</center>', file = html_file)



html_file = open('home.html', 'w+')
with open('catalogue.txt') as c: # Version Number of the ATNF PSR Catalogue that was used when this script last ran
    version = str(c.readlines()).strip("'[']")
c.close()

pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

df = pd.read_csv('databasev4.csv', header=None, sep='~', engine='python')

jname_col = 0
period_col = 4
assoc_col = 47
period_col = 4
minmass_col = 18
raj_col = 32
decj_col = 35
gl_col = 31
gb_col = 30
p1_col = 19
xx_col = 48
yy_col = 49
zz_col = 50
psrs_available_col = 0

jname_list = list(df.iloc[:,jname_col])
period_list = df.iloc[:,period_col]
assoc_list = list(df.iloc[:,assoc_col])
minmass_list = df.iloc[:,minmass_col]
raj_list = df.iloc[:,raj_col]
decj_list = df.iloc[:,decj_col]
gl_list = df.iloc[:,gl_col]
gb_list = df.iloc[:,gb_col]
p1_list = df.iloc[:,p1_col]
xx_list = df.iloc[:,xx_col]
yy_list = df.iloc[:,yy_col]
zz_list = df.iloc[:,zz_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]

slowest = None
fastest = None
fastest_jname = ''
slowest_jname = ''

url_template = 'https://pulsars.org.au/fold/meertime/'

psrs_known = str(len(jname_list)).strip()

exgal_count = 0
gc_count = 0
binary_count = 0
for i in range(len(jname_list)):
    if 'EXGAL' in str(assoc_list[i]):
        exgal_count += 1
    if 'GC' in str(assoc_list[i]):
        gc_count += 1
    if '*' not in str(minmass_list[i]):
        binary_count += 1
    if '*' not in str(period_list[i]):
        periodf = float(period_list[i]) * 1000
        if (slowest is None) or (periodf > slowest):
            slowest = periodf
            slowest = round(slowest, 3)
            slowest_jname = str(jname_list[i]).strip()
        if (fastest is None) or (periodf < fastest):
            fastest = periodf
            fastest = round(fastest, 3)
            fastest_jname = str(jname_list[i]).strip()
if fastest != None:
    if fastest >= 1000:
        fastest /= 1000
        fastest = round(fastest, 3)
        fast_unit = 'seconds'
    else:
        fast_unit = 'milliseconds'
else:
    fast_unit = ''
if slowest != None:
    if slowest >= 1000:
        slowest /= 1000
        slowest = round(slowest, 3)
        slow_unit = 'seconds'
    else:
        slow_unit = 'milliseconds'
else:
    slow_unit = ''
psr_difference = 3320 - gc_count - exgal_count

html_css_navbar_str = """
<html>
 <head>
  <meta name="viewport" 
  content="width=device-width, 
  initial-scale=1">
  <style> 
  body {
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
        }
      .topnav {
          overflow: hidden;
          background-color: #005CD;
          }
      
      .topnav a {
          float: left
          color: #00C5CD
          text-align: center;
          padding: 30px 16px;
          text-decoration: none;
          font-size: 17px;
          }
      
      .topnav a:hover {
          padding: 30px 16px;
          background-color: #005CD;
          color: black;
          }
      
      .topnav a.active {
          background-color: #00C5CD;
          color: white;
          }
      </style>
      </head>
      <body>
      
      <div class="topnav">
      <a class="active" href="https://astronomy.swin.edu.au/~mbailes/encyc/home.html">Home</a>
      <a target="_blank" href="https://astronomy.swin.edu.au/~mbailes/encyc/pulsars.html">Pulsars</a>
      <a target="_blank" href="https://astronomy.swin.edu.au/~mbailes/encyc/surveys.html">Surveys</a>
      <a target="_blank" href="https://astronomy.swin.edu.au/~mbailes/encyc/about.html">About</a>
      </div>
      <div style="padding-left:16px">
      </div>
      
      </body>

"""
html_header_str = '<center><body><h1> Welcome to the Swinburne Encyclopedia of Radio Pulsar Astronomy!</h1>\n</center>\n'
html_paragraph_one = """<style>
    .indent-all {
	padding-left: 50px;
    padding-right: 100px;
    }
  </style>
  <p class="indent-all">
  
  The Swinburne encyclopedia of radio pulsar astronomy allows anyone to
  learn about the radio pulsar population, explore the pulsars in the
  <a target="_blank" href="https://www.atnf.csiro.au/research/pulsar/psrcat/">ATNF pulsar catalogue</a>, and even see real observational data suitable
  for actual professional research via the <a target="_blank" href="https://pulsars.org.au">Swinburne Pulsar Portal</a> hosted
  by the <a target="_black" href="https://gwdc.org.au/">Gravitational Wave Data Centre</a> via ADACS, funded by <a target="_blank" href="https://astronomyaustralia.org.au/">Astronomy Australia Limited</a>.

  <br>"""
html_paragraph_two = """ <p class="indent-all">

  In the plots below it is often possible to click on a particular pulsar, and
  be taken to the pulsar portal to see real obser vations of it. For now
  only observations from SARAO's MeerTime project are available for viewing.

  <br>"""

html_paragraph_three = """<p class="indent-all">

  According to version """ + version + """ of the ATNF catalogue there are 3320 pulsars now known. """ + str(binary_count) + """ of these pulsars are binary. """ + str(exgal_count) + """ of these are extragalactic, """ + str(gc_count) + """ are associated with globular clusters, and
  the remaining """ + str(psr_difference) + """ are thought to be part of the galactic plane's population. 1544 of these pulsars have profiles available in the <a target="_blank" href="https://pulsars.org.au">Swinburne Pulsar Portal</a>. 
  <p>
  """
  
html_paragraph_four = """<p>
  <p class="indent-all">
  The shortest-period pulsar is """ + fastest_jname +  """ with a spin period of """ + str(fastest) + ' ' + fast_unit + """ and the
  longest-period pulsar in the catalogue is """  + str(slowest_jname) + """ with a period of """ + str(slowest) + ' ' + slow_unit + """.
  """
  
html_paragraph_five = """ <p class="indent-all">
   Pulsars rotate very regularly, and to help visualise their distribution astronomers
   often plot them in equatorial coordinates:
    """

html_paragraph_six = """<p class="indent-all">
  Because pulsars are a galactic population it is often handy to plot their distribution
  in galactic coordinates.
"""

html_paragraph_seven = """  <p class="indent-all">
  Pulsar astronomers often like to plot the P-Pdot diagram that shows both how
  rapidly a pulsar spins, and how fast it is slowing down (in seconds/second).
  A pulsar's characteristic age is a rough measure of how old it is, and
  is equal to P/(2Pdot).
"""

html_paragraph_eight = """<p class="indent-all">
  A pulsar's <a target="_blank" href="https://astronomy.swin.edu.au/cosmos/P/Pulsar+Dispersion+Measure">dispersion measure</a> gives rise to a frequency sweep as the pulse
  arrives at Earth, and the slope is proportional to the integral of the
  free electron column density along the line of sight. An electron
  content model of the galaxy can be used to estimate the distance to the pulsar
  and we can plot their locations in 3D space.
  <p>
  """

h = Home()

html_end_str = '</body>\n</html>'

str_one = html_css_navbar_str + html_header_str + html_paragraph_one + html_paragraph_two + html_paragraph_three + html_paragraph_four + html_paragraph_five

plotly_load = h.plotly_load()

print(str_one, file = html_file)
raj_decj = h.raj_decj_plt()
print(html_paragraph_six, file = html_file)
gl_gb = h.gl_gb_plt()
print(html_paragraph_seven, file = html_file)
p_pdot = h.p_pdot_plt()
print(html_paragraph_eight, file = html_file)
xx_yy = h.xx_yy_plt()
print(html_end_str, file = html_file)
xx_zz = h.xx_zz_plt()
print('Done')




























