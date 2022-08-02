# @author: Evan Anthopoulos
# 3D Plotly Stuff

import pandas as pd
from astropy.visualization import quantity_support
from plotly import express as px
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from pandas import DataFrame
import re
from plotly.offline import plot

class Survey:
    
    def survey_name(self, filename, counter: int) -> str:
        name_str = str(survey_name_list[counter]).strip()
        return name_str

    
    
    def year_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        year_list = []
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            df_year_str = str(df_year_list[i]).strip()
            if '*' not in df_survey_str:
                if ',' in df_survey_str:
                    first_comma = df_survey_str.index(',')
                    first_survey = df_survey_str[:first_comma].strip()
                else:
                    first_survey = df_survey_str.strip()
            if survey == first_survey:
                year_list.append(df_year_str)
        if '1089806188' in str(year_list):
            year_list.remove('1089806188')
        return year_list
    
    
    
    def num_years_detected(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        survey_count = 0
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            if '*' not in df_survey_str:
                if survey in df_survey_str:
                    survey_count += 1
        return survey_count
                
    
    
    def fastest_slowest_period(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        fastest = None
        slowest = None
        fastest_psr = ''
        slowest_psr = ''
        for i in range(len(df_psr_list)):
            if '*' not in str(df_period_list[i]):
                df_survey_str = str(df_survey_list[i]).strip()
                df_period_float = float(df_period_list[i]) * 1000
                if ',' in df_survey_str:
                    first_comma = df_survey_str.index(',')
                    first_survey = df_survey_str[:first_comma].strip()
                else:
                    first_survey = df_survey_str.strip()
                if survey == first_survey:
                    if (slowest is None) or (df_period_float > slowest):
                        slowest = df_period_float
                        slowest = round(slowest, 5)
                        slowest_psr = str(df_psr_list[i]).strip()
                    if (fastest is None) or (df_period_float < fastest):
                        fastest = df_period_float
                        fastest = round(fastest, 5)
                        fastest_psr = str(df_psr_list[i]).strip()
        if fastest != None:
            if fastest >= 1000:
                fastest /= 1000
                fastest = round(fastest, 5)
                fast_unit = 'seconds'
            else:
                fast_unit = 'milliseconds'
        else:
            fast_unit = ''
        if slowest != None:
            if slowest >= 1000:
                slowest /= 1000
                slowest = round(slowest, 5)
                slow_unit = 'seconds'
            else:
                slow_unit = 'milliseconds'
        else:
            slow_unit = ''
        return 'The fastest pulsar discovered was ' + '<a '+ 'target="_blank" ' + 'href="' + url_template + fastest_psr + '">' + fastest_psr + '</a>' + ' with a ' + '<a '+ 'target="_blank" ' + 'href="' + 'https://astronomy.swin.edu.au/cosmos/P/Period' + '">' +  'period' + '</a>' + ' of ' + str(fastest) + ' ' + fast_unit + ' and the slowest pulsar was ' + '<a '+ 'target="_blank" ' + 'href="' + url_template + slowest_psr + '">' + slowest_psr + '</a>' + ' with a period of ' + str(slowest) + ' ' + slow_unit + '.'
                    
                    
                    
    def small_largest_dm(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        smallest = None
        largest = None
        smallest_psr = ''
        largest_psr = ''
        dm_unit = 'pc/cc'
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            dm = str(df_dm_list[i])
            if '*' not in dm:
                if ',' in df_survey_str:
                    first_comma = df_survey_str.index(',')
                    first_survey = df_survey_str[:first_comma].strip()
                else:
                    first_survey = df_survey_str.strip()
                dm = dm.replace('D', 'E')
                df_dm_float = float(dm)
                if survey == first_survey:
                    if (largest is None) or (df_dm_float > largest):
                        largest = df_dm_float
                        largest = round(largest, 5)
                        largest_psr = str(df_psr_list[i]).strip()
                    if (smallest is None) or (df_dm_float < smallest):
                        smallest = df_dm_float
                        smallest = round(smallest, 5)
                        smallest_psr = str(df_psr_list[i]).strip()
        return 'The smallest ' + '<a '+ 'target="_blank" ' + 'href="' + 'https://astronomy.swin.edu.au/cosmos/P/Pulsar+Dispersion+Measure' + '">' + 'pulsar dispersion measure ' + '</a>' + 'was ' + '<a '+ 'target="_blank" ' + 'href="' + url_template + smallest_psr + '">' + smallest_psr + '</a>' + ' with a DM of ' + str(smallest) + ' ' + dm_unit + ' and the largest pulsar dispersion measure was ' + '<a '+ 'target="_blank" ' + 'href="' + url_template + largest_psr + '">' + largest_psr + '</a>' + ' with a DM of ' + str(largest) + ' ' + dm_unit + '.'
        

    
    def total_psrs_before_discovered(self, xl_file, df_file, counter: int):
        year_disc_list = year
        year_disc_list = list(dict.fromkeys(year_disc_list))
        year_count = 0
        if '1089806188' in str(year_disc_list):
            year_disc_list.remove('1089806188')
        if len(year_disc_list) >= 1:
            year_min = min(year_disc_list)
            year_min = int(year_min)
            for i in range(len(df_psr_list)):
                if '*' not in str(df_year_list[i]):
                    year_temp = int(df_year_list[i])
                    if year_temp < year_min:
                        year_count += 1
        return year_count
                    
    

    def psr_percentage_increased(self, xl_file, df_file, counter: int):
        discovered1 = float(len(discovered))
        year_count = float(tpbd)
        if discovered1 != 0 and year_count != 0:
            psr_percent = (discovered1 / year_count) * 100
            if psr_percent >= 0.5:
                psr_percent = round(psr_percent, 0)
            else:
                psr_percent = round(psr_percent, 1)
        else:
            psr_percent = ''
        return psr_percent



    # This returns the list of psrs discovered by the survey at "counter"
    def psrs_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        discovered_indices = []
        for i in range(len(df_psr_list)):
            df_survey = str(df_survey_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                    if first_survey == survey:
                        discovered_indices.append(i)
                elif survey == df_survey:
                    discovered_indices.append(i)
        return discovered_indices
        
    

    # This returns the list of psrs detected by the survey at "counter"
    def psrs_detected(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        detected_indices = []
        first_survey = 'Null'
        for i in range(len(df_psr_list)):
            df_survey = str(df_survey_list[i]).strip()
            if ',' in df_survey:
                first_comma = df_survey.index(',')
                first_survey = df_survey[:first_comma]
            else:
                first_survey = df_survey
            if (survey != first_survey) and (survey in str(df_survey_list[i])):
                detected_indices.append(i)
        return detected_indices
    



    # Assigns a label to determine point color
    def in_or_out(self, counter: int):
        det_disc_list = []
        for i in range(len(df_psr_list)):
            if i in discovered:
                det_disc_list.append("PSRs Discovered - Click to View / Hide")
            elif i in detected:
                det_disc_list.append("PSRs Detected - Click to View / Hide")
            else:
                det_disc_list.append("All Known Pulsars - Click to View / Hide")
        return det_disc_list
        


    def link_str(self, counter: int):
        row = xl.iloc[counter,3:]
        link_count = 0
        start_link = 'https://ui.adsabs.harvard.edu/abs/'
        end_link = '/abstract'
        link_temp = ''
        link_temp_final = ''
        link_final = ''
        for link in row:
            if 'nan' not in str(link):
                link_count += 1
                link = str(link).replace('https://ui.adsabs.harvard.edu/abs/', '')
                link = str(link).replace('/abstract', '')
                link_str = '<a '+ 'target="_blank" ' + 'href="' + start_link + str(link).strip() + end_link + '">' + str(link).strip() + '</a>'
                link_temp = link_str + ', '
                link_temp_final += link_temp
        link_final = link_temp_final
        if link_count > 1:
            final_str = ' There were ' + str(link_count) + ' papers written about the discoveries of this survey: ' + link_final + '. '
        elif link_final == 1:
            final_str = 'There was 1 paper written about the discoveries in this survey: ' + link_final + '. '
        else:
            final_str = ''
        final_str = final_str.replace(', .', '.')
        return final_str



    def plotly_load(self, counter: int):
        psrs_available_cleaned = []
        jnames_cleaned = []
        available_or_not = []
        psr_links = []
        clickable = []
        for i in range(len(df_psr_list)):
            jname = str(df_psr_list[i].strip())
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
            elif str(available_or_not[i]).strip() == 'No':
                jname_temp = jnames_cleaned[i]
                clickable.append(jname_temp + ':   This pulsar is not clickable.')
        return [clickable, available_or_not, psr_links]


    def plotly_per_survey(self, xl_file, df_file, counter: int, html_file):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        raj = []
        decj = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
            raj_temp = str(df_raj_list[i]).strip()
            decj_temp = str(df_decj_list[i]).strip()
            if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list[i]):
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
            'raj': ranew2,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lon='raj', lat='decj', color="Legend (RA (J2000) vs Dec (J2000))", width=1000, height=500, title='Pulsars discovered in the ' + survey_name + ' in Equatorial Coordinates', hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars - Click to View / Hide": "#B0B0B0"}, custom_data=["URLs"],
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
        if len(detected) == 0 and len(discovered) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)



    def plotly_gl_gb(self, xl_file, df_file, counter: int, html_file):
        det_disc_list = det_disc_real
        survey_name = str(survey_name_list[counter]).strip()
        gl = []
        gb = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
            gl_temp = str(gl_list[i]).strip()
            gb_temp = str(gb_list[i]).strip()
            if '*' not in str(gl_list[i]) and '*' not in str(gb_list[i]):
                gb_temp = str(float(gb_temp)*(-1))
                gl.append(gl_temp)
                gb.append(gb_temp)
            else:
                gl.append('null')
                gb.append('null')
                        
        source = {
            'Name': clickable,
            'gl': gl,
            'gb': gb,
            'Legend (gl vs gb)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }

        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lat='gl', lon='gb', labels=dict(lat='gl', lon='gb'), color="Legend (gl vs gb)", width=1000, height=500, title='Pulsars discovered by ' + survey_name + ' in Galactic Coordinates', hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime" : "#BFEFFF", "All Known Pulsars - Click to View / Hide": "#B0B0B0"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False, lonaxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'), lataxis=dict(showgrid=True, gridwidth=0.9, gridcolor='rgb(102, 102, 102)'))
        fig.update_traces(marker=dict(size=4))
        fig.update_xaxes(title_text='raj (rad)')
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
        if len(gl) == 0 and len(gb) == 0:
                return 'None'
        else:
            print('<center>\n' + html_str + '</center>', file = html_file)


    
    def yy_xx_zoomed(self, xl_file, df_file, counter: int, html_file):
        survey_name = str(survey_name_list[counter]).strip()
        xx = []
        yy = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
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
            'Legend (x vs y)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='y-distance (kpc)', color="Legend (x vs y)", width=1000, height=500, title='Zoomed in: x-distance' + ' vs y-distance for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime" : "#BFEFFF", "All Known Pulsars - Click to View / Hide" : "#B0B0B0", "PSRs Discovered - Click to View / Hide": "#FF0000"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_layout(autotypenumbers='convert types')
        fig.update_traces(marker=dict(size=4))
        fig.update_xaxes(range=[-10, 10])
        fig.update_yaxes(range=[-10, 10])
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
        if len(detected) == 0 and len(discovered) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)



    def yy_xx_reg(self, xl_file, df_file, counter: int, html_file):
         survey_name = str(survey_name_list[counter]).strip()
         xx = []
         yy = []
         clickable = plotly_load[0]
         det_disc_list = det_disc_real
         available_or_not = plotly_load[1]
         psr_links = plotly_load[2]
         for i in range(len(df_psr_list)):
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
             'Legend (x vs y)': det_disc_list,
             'Available PSR': available_or_not,
             "URLs": psr_links
         }
         dafr = DataFrame(data=source)
         fig = px.scatter(dafr, x='x-distance (kpc)', y='y-distance (kpc)', color="Legend (x vs y)", width=1000, height=500, title='x-distance' + ' vs y-distance for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime" : "#BFEFFF", "All Known Pulsars - Click to View / Hide" : "#B0B0B0", "PSRs Discovered - Click to View / Hide": "#FF0000"}, custom_data=["URLs"],
                               # size of markers, "pop" is one of the columns of gapminder
                              )
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
         if len(detected) == 0 and len(discovered) == 0:
                 return 'None'
         else:
             print('<center>' + html_str + '</center>', file = html_file)



    def p_pdot(self, counter: int):
        survey_name = str(survey_name_list[counter]).strip()
        p0 = []
        p1 = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
            p0_temp = str(df_period_list[i]).strip()
            p1_temp = str(p1_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(zz_list[i]):
                p0.append(p0_temp)
                p1.append(p1_temp)
            else:
                p0.append('null')
                p1.append('null')
        source = {
            'Name': clickable,
            'Spin Period': p0,
            'Period Derivative': p1,
            'Legend (Spin Period vs Period Derivative)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }

        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='Spin Period', y='Period Derivative', color="Legend (Spin Period vs Period Derivative)", log_x=True, log_y=True, width=1000, height=500, title='Spin Period vs Period Derivative for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime": "#BFEFFF", "All Known Pulsars - Click to View / Hide" : "#B0B0B0"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_layout(autotypenumbers='convert types')
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
        if len(detected) == 0 and len(discovered) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)



    def zz_xx_zoomed(self, xl_file, df_file, counter: int, html_file):
        survey_name = str(survey_name_list[counter]).strip()
        xx = []
        zz = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
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
            'Legend (x vs z)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='z-distance (kpc)', color="Legend (x vs z)", width=1000, height=500, title='Zoomed in: x-distance' + ' vs z-distance for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime": "#BFEFFF", "All Known Pulsars - Click to View / Hide" : "#B0B0B0"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_layout(autotypenumbers='convert types')
        fig.update_traces(marker=dict(size=4))
        fig.update_xaxes(range=[-10, 10])
        fig.update_yaxes(range=[-5, 5])
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
        if len(detected) == 0 and len(discovered) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)
            
            
    
    def zz_xx_reg(self, xl_file, df_file, counter: int, html_file):
        survey_name = str(survey_name_list[counter]).strip()
        xx = []
        zz = []
        clickable = plotly_load[0]
        det_disc_list = det_disc_real
        available_or_not = plotly_load[1]
        psr_links = plotly_load[2]
        for i in range(len(df_psr_list)):
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
            'Legend (x vs z)': det_disc_list,
            'Available PSR': available_or_not,
            "URLs": psr_links
        }
 
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='z-distance (kpc)', color="Legend (x vs z)", width=1000, height=500, title='x-distance' + ' vs z-distance for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars in MeerTime": "#BFEFFF", "All Known Pulsars - Click to View / Hide" : "#B0B0B0"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
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
        if len(detected) == 0 and len(discovered) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file) 
    
    
    
    # def test_3D(self, counter: int):
    #     quantity_support()
    #     survey_name = str(survey_name_list[counter]).strip()
    #     psrs_available_cleaned = []
    #     psr_links = []
    #     xx = []
    #     yy = []
    #     zz = []
    #     jname = []
    #     jnames_cleaned = []
    #     available_or_not = []
    #     clickable = []
    #     survey_data = []
    #     det_disc_list = det_disc_real
    #     for i in range(len(df_psr_list)):
    #         xx_temp = str(xx_list[i]).strip()
    #         yy_temp = str(yy_list[i]).strip()
    #         zz_temp = str(zz_list[i]).strip()
    #         if '*' not in str(xx_list[i]) and '*' not in str(yy_list[i]) and '*' not in str(zz_list[i]):
    #             jname = str(jnames_list[i].strip())
    #             jnames_cleaned.append(jname)
    #             survey_p = str(df_survey_list[i]).strip()
    #             survey_data.append(survey_p)
    #             xx.append(xx_temp)
    #             yy.append(yy_temp)
    #             zz.append(zz_temp)
    #     for i in range(len(psrs_available)):
    #         psr = str(psrs_available[i]).strip()
    #         psrs_available_cleaned.append(psr)
    #     for jname in jnames_cleaned:
    #         if psrs_available_cleaned.count(jname) > 0:
    #             available_or_not.append("Yes")
    #             psr_link = url_template + jname
    #             psr_links.append(psr_link)
    #         else:
    #             available_or_not.append("No")
    #             psr_links.append('null')
    #     for i in range(len(available_or_not)):
    #         if str(available_or_not[i]).strip() == 'Yes':
    #             jname_temp = jnames_cleaned[i]
    #             clickable.append(jname_temp + ':   Click on this pulsar to be taken to the MeerTime portal.')
    #         elif str(available_or_not[i]).strip() == 'No':
    #             jname_temp = jnames_cleaned[i]
    #             clickable.append(jname_temp + ':   This pulsar is not clickable.')
                
    #     source = {
    #         'Name': clickable,
    #         'x-distance (kpc)': xx,
    #         'y-distance (kpc)': yy,
    #         'z-distance (kpc)': zz,
    #         'Legend (x vs y vs z)': det_disc_list,
    #         'survey': survey_data,
    #         "URLs": psr_links
    #     }

    #     dafr = DataFrame(data=source)
    #     fig = px.scatter_3d(dafr, x='x-distance (kpc)', y='y-distance (kpc)', z='z-distance (kpc)', color="Legend (x vs y vs z)", width=1000, height=500, title='x-distance' + ' vs y-distance' + ' vs z-distance for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "PSRs Detected - Click to View / Hide": "#228B22", "All Known Pulsars - Click to View / Hide" : "#B0B0B0", "All Known Pulsars in MeerTime" : "#BFEFFF"}, custom_data=["URLs"]
    #                           # size of markers, "pop" is one of the columns of gapminder
    #                          )

    #     fig.update_layout(autotypenumbers='convert types')
    #     fig.update_traces(marker=dict(size=4))
    #     fig.show()
        
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    #     res = re.search('<div id="([^"]*)"', plot_div)
    #     div_id = res.groups()[0]

    #     js_callback = """
    #     <script>
    #     var plot_element = document.getElementById("{div_id}");
    #     plot_element.on('plotly_click', function(data){{
    #         console.log(data);
    #         var point = data.points[0];
    #         if (point) {{
    #             if (point.customdata.toString() != 'null') {{
    #                 console.log(point.customdata);
    #                 window.open(point.customdata);
    #             }}
    #         }}
    #     }})
    #     </script>
    #     """.format(div_id=div_id)

    #     # Build HTML string
    #     html_str = """
    #            {plot_div}
    #            {js_callback}
    #     """.format(plot_div=plot_div, js_callback=js_callback)

    #     # Write out HTML file
    #     if len(detected) == 0 and len(discovered) == 0:
    #             return 'None'
    #     else:
    #         print('<center>' + html_str + '</center>', file = html_file)
    
    
    
    # def bsurf_pb(self, counter: int):
    #     survey_name = str(survey_name_list[counter]).strip()
    #     psrs_available_cleaned = []
    #     psr_links = []
    #     bsurf = []
    #     p0 = []
    #     jname = []
    #     jnames_cleaned = []
    #     available_or_not = []
    #     survey_data = []
    #     clickable = []
    #     det_disc_list = det_disc_real
    #     for i in range(len(df_psr_list)):
    #         bsurf_temp = str(bsurf_list[i]).strip()
    #         p0_temp = str(df_period_list[i]).strip()
    #         if '*' not in bsurf_temp and '*' not in p0_temp:
    #             bsurf.append(bsurf_temp)
    #             p0.append(p0_temp)
    #             jname = str(jnames_list[i].strip())
    #             jnames_cleaned.append(jname)
    #             survey_p = str(df_survey_list[i]).strip()
    #             survey_data.append(survey_p)
    #         else:
    #             bsurf.append('null')
    #             p0.append('null')
    #             jname = str(jnames_list[i].strip())
    #             jnames_cleaned.append(jname)
    #             survey_p = str(df_survey_list[i]).strip()
    #             survey_data.append(survey_p)
    #     for i in range(len(psrs_available)):
    #         psr = str(psrs_available[i]).strip()
    #         psrs_available_cleaned.append(psr)
    #     for jname in jnames_cleaned:
    #         if psrs_available_cleaned.count(jname) > 0:
    #             available_or_not.append("Yes")
    #             psr_link = url_template + jname
    #             psr_links.append(psr_link)
    #         else:
    #             available_or_not.append("No")
    #             psr_links.append('null')
    #     for i in range(len(available_or_not)):
    #         if str(available_or_not[i]).strip() == 'Yes':
    #             jname_temp = jnames_cleaned[i]
    #             clickable.append(jname_temp + ':   Click on this pulsar to be taken to the MeerTime portal.')
    #         elif str(available_or_not[i]).strip() == 'No':
    #             jname_temp = jnames_cleaned[i]
    #             clickable.append(jname_temp + ':   This pulsar is not clickable.')
    #     source = {
    #         'Name': jnames_cleaned,
    #         'Magnetic Field Strength (G)': bsurf,
    #         'p0': p0,
    #         'Clickable': clickable,
    #         'Legend (Magnetic Field Strength (G) vs Spin Period (s))': det_disc_list,
    #         'URLs': psr_links
    #     }
        
    #     print(len(bsurf),len(p0),len(jnames_cleaned),len(det_disc_list),len(psr_links),'ok')
    #     dafr = DataFrame(data=source)
    #     fig = px.scatter(dafr, x='p0', y='Magnetic Field Strength (G)', color="Legend (Magnetic Field Strength (G) vs Spin Period (s))",log_x=True, log_y=True, width=1000, height=500, title='Magnetic Field Strength vs Spin Period for the ' + survey_name, hover_name="Clickable", color_discrete_map={"PSRs Discovered - Click to View / Hide": "#FF0000", "All Known Pulsars in MeerTime": "#BFEFFF", "All Known Pulsars - Click to View / Hide": "#B0B0B0", "PSRs Detected - Click to View / Hide": "#228B22"}, custom_data=["URLs"]
    #                           # size of markers, "pop" is one of the columns of gapminder
    #                           )
    #     fig.update_layout(autotypenumbers='convert types')
    #     fig.update_traces(marker=dict(size=4))
    #     fig.update_layout(
    #     xaxis={'title': 'Spin Period (s)', 'showexponent': 'all', 'exponentformat': 'e', 'rangemode': 'tozero',
    #            'ticks': 'outside'},
    #     yaxis={'title': 'Magnetic Field Strength (G)', 'showexponent': 'all', 'exponentformat': 'e', 'rangemode': 'tozero',
    #            'ticks': 'outside'},)
    #     fig.show()
        
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    #     res = re.search('<div id="([^"]*)"', plot_div)
    #     div_id = res.groups()[0]

    #     js_callback = """
    #     <script>
    #     var plot_element = document.getElementById("{div_id}");
    #     plot_element.on('plotly_click', function(data){{
    #         console.log(data);
    #         var point = data.points[0];
    #         if (point) {{
    #             if (point.customdata.toString() != 'null') {{
    #                 console.log(point.customdata);
    #                 window.open(point.customdata);
    #             }}
    #         }}
    #     }})
    #     </script>
    #     """.format(div_id=div_id)

    #     # Build HTML string
    #     html_str = """
    #             {plot_div}
    #             {js_callback}
    #     """.format(plot_div=plot_div, js_callback=js_callback)

    #     # Write out HTML file
    #     # with open('survey_plots.html', 'w+') as f:
    #     #f.write(html_file)
    #     if len(detected) == 0 and len(discovered) == 0:
    #             return 'None'
    #     else:
    #         print('<center>\n' + html_str + '</center>\n', file = html_file)





survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file, header=None)

survey_col = 0
survey_name_col = 1
assoc_survey_col = 2
psrs_available_col = 0


df_psr_col = 0
df_survey_col = 10
df_year_col = 11
df_period_col = 4
df_dm_col = 7
df_raj_col = 32
df_decj_col = 35
gl_col = 31
gb_col = 30
assoc_col = 47
xx_col = 48
yy_col = 49
zz_col = 50
bsurf_col = 22
pb_col = 12
minmass_col = 18
ecc_col = 15
p1_col = 19


pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')
df = pd.read_csv('databasev4.csv', header=None, sep='~', engine='python')


xl_survey_list = xl.iloc[:,survey_col]
survey_name_list = xl.iloc[:,survey_name_col]
assoc_survey_list = xl.iloc[:,assoc_survey_col]


df_psr_list = df.iloc[:,df_psr_col]
df_survey_list = df.iloc[:,df_survey_col]
df_year_list = df.iloc[:,df_year_col]
df_period_list = df.iloc[:,df_period_col]
df_dm_list = df.iloc[:,df_dm_col]
df_raj_list = df.iloc[:,df_raj_col]
df_decj_list = df.iloc[:,df_decj_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]
jnames_list = df.iloc[:,df_psr_col]
gl_list = df.iloc[:,gl_col]
gb_list = df.iloc[:,gb_col]
xx_list = df.iloc[:,xx_col]
yy_list = df.iloc[:,yy_col]
zz_list = df.iloc[:,zz_col]
assoc_list = df.iloc[:,assoc_col]
bsurf_list = df.iloc[:,bsurf_col]
pb_list = df.iloc[:,pb_col]
minmass_list = df.iloc[:,minmass_col]
ecc_list = df.iloc[:,ecc_col]
p1_list = df.iloc[:,p1_col]

url_template = 'https://pulsars.org.au/fold/meertime/'

s = Survey()

# html_file = open('survey_plots.html', 'w+')
final_str = ''
table_start_str = '<table>' + '\n<tr>'
html_end_str = '\n</body>' + '\n</html>'
padding_str = """
<style>
    .indent-all {
	padding-left: 50px;
    padding-right: 100px;
    }
  </style>
"""

for j in range(len(xl_survey_list)):
# j = 16

    survey = str(xl_survey_list[j]).strip()
    survey2 = str(xl_survey_list[j]).strip()
    survey_name = str(survey_name_list[j]).strip()
    html_css_navbar_str = '<head>\n' + '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + '<style>\n' + 'body {\n margin: 0;\n font-family: Arial, Helvetica, sans-serif;\n}\n\n.topnav {\n overflow: hidden;\n background-color: #005CD;\n}\n\n.topnav a {\n float: left\n color: #00C5CD\n text-align: center;\n padding: 30px 16px;\n text-decoration: none;\n font-size: 17px;\n}\n\n.topnav a:hover {\n padding: 30px 16px;\n background-color: #005CD;\n color: black;\n}\n\n.topnav a.active {\n background-color: #00C5CD;\n color: white;\n}\n</style>\n</head>\n<body>\n\n<div class="topnav">\n ' + '<a ' + 'target="_blank" ' +  'class="active" href="https://astronomy.swin.edu.au/~mbailes/encyc/home.html">Home</a>\n ' + '<a ' + 'target="_blank" ' + 'href="https://astronomy.swin.edu.au/~mbailes/encyc/pulsars.html">Pulsars</a>\n ''<a ' + 'target="_blank" ' + 'href="https://astronomy.swin.edu.au/~mbailes/encyc/surveys.html">Surveys</a>\n</div>\n\n<div style="padding-left:16px">\n</div>\n\n</body>'
    html_style_str = '<html>\n' + '<style> h1 {text-align: center;} </style>'
    html_header_str = html_style_str + '<h1>' + survey_name + '</h1>'
    html_start_str = ' <head>\n' + ' <title>\n' + str(survey_name) + '  </title>' + ' </head>' + ' <body> \n'
    
    html_file_str = survey + "_plots.html"
    html_file = open(html_file_str, 'w+')
    print(html_css_navbar_str + html_header_str + html_start_str, file = html_file)
    
    name = s.survey_name(xl, j)
    year = s.year_discovered(xl, df, j)
    n_span = s.num_years_detected(j)
    fastest_slowest = s.fastest_slowest_period(j)
    sal_dm = s.small_largest_dm(j)
    tpbd = s.total_psrs_before_discovered(xl, df, j)
    detected = s.psrs_detected(xl, df, j)
    discovered = s.psrs_discovered(xl, df, j)
    det_disc_real = s.in_or_out(j)
    percent = s.psr_percentage_increased(xl, df, j)
    link_str = s.link_str(j)
    plotly_load = s.plotly_load(j)
    
    period_unit_ms = 'milliseconds'
    period_unit_s = 'seconds'
    dm_unit = 'pc/cc'
    bsurf_unit = 'G'
    pb_unit_hrs = 'hrs'
    pb_unit_d = 'days'
    pb_unit_yr = 'years'
    jname_disc = []
    period_disc = []
    dm_disc = []
    bsurf_disc = []
    table_disc_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2><p id="discovered">PSRs discovered by the ' + survey_name_list[j].strip() + '</a></h2>\n\n' + '<table style="width:100%">\n'
    table_header_disc = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' + '\n</tr>\n\n'
    table_disc_contents_str = table_disc_str + table_header_disc
    
    jname_disc_bin = []
    period_disc_bin = []
    dm_disc_bin = []
    bsurf_disc_bin = []
    pb_disc_bin = []
    ecc_disc_bin = []
    table_disc_bin_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2>Binary PSRs discovered by the ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_disc_bin = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' +'<th>ORBITAL PERIOD</th>' + '<th>ECCENTRICITY</th>' + '\n</tr>\n\n'
    table_disc_bin_contents_str = table_disc_bin_str + table_header_disc_bin
    
    jname_det = []
    period_det = []
    dm_det = []
    bsurf_det = []
    table_det_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2><p id="detected">PSRs detected by the ' + survey_name_list[j].strip() + '</a></h2>\n\n' + '<table style="width:100%">\n'
    table_header_det = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' + '\n</tr>\n\n'
    table_det_contents_str = table_det_str + table_header_det
    
    jname_det_bin = []
    period_det_bin = []
    dm_det_bin = []
    bsurf_det_bin = []
    pb_det_bin = []
    ecc_det_bin = []
    table_det_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;} \n</style> \n\n<h2>Binary PSRs detected by the ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_det = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' + '<th>ORBITAL PERIOD</th>' + '<th>ECCENTRICITY</th>' + '\n</tr>\n\n'
    table_det_bin_contents_str = table_det_str + table_header_det
    
    # TABLES FOR DISCOVERED and BINARY DISCOVERED
    psrs_available = list(psrs_available) # Needs to be converted to list first
    df_psr_list = list(df_psr_list) # Also needs to be converted to list first
    for index in discovered:
        if '*' not in minmass_list[index]:
            if '*' not in str(df_period_list[index]):
                period_temp = float(df_period_list[index]) * 1000
                period_temp = round(period_temp, 3)
                if period_temp >= 1000:
                    period_temp /= 1000
                    period_temp = round(period_temp, 3)
                    period_temp = str(period_temp) + ' ' + period_unit_s
                else:
                    period_temp = str(period_temp) + ' ' + period_unit_ms
            else:
                period_temp = '*'
            if '*' not in str(df_dm_list[index]):
                dm_temp = round(float(df_dm_list[index]), 2)
                dm_temp = str(dm_temp) + ' ' + dm_unit
            else:
                dm_temp = '*'
            if '*' not in str(bsurf_list[index]):
                bsurf_temp = str(bsurf_list[index]) + ' ' + bsurf_unit
            else:
                bsurf_temp = '*'
            if str(df_psr_list[index]).strip() not in psrs_available:
                jname_temp = str(df_psr_list[index]).strip()
                jname_disc_bin.append(jname_temp)
            else:
                jname_temp = '<a '+ 'target="_blank" ' + 'href="' + url_template + str(df_psr_list[index]).strip() + '">' + str(df_psr_list[index]).strip() + '</a>' 
                jname_disc_bin.append(jname_temp)
            if '*' not in str(pb_list[index]):
                pb_temp = float(str(pb_list[index]).strip())
                if 0 < pb_temp < 1:
                    pb_temp *= 24
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_hrs
                elif 1 < pb_temp < 365:
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_d
                elif 365 < pb_temp < 1e99:
                    pb_temp *= 0.002737850787
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_yr
            else:
                pb_temp = '*'
            if '*' not in str(ecc_list[index]):
                ecc_temp = str(ecc_list[index]).strip()
                ecc_temp = str(round(float(ecc_temp), 3)).strip()
            else:
                ecc_temp = '*'
            pb_disc_bin.append(pb_temp)
            ecc_disc_bin.append(ecc_temp)
            period_disc_bin.append(period_temp)
            dm_disc_bin.append(dm_temp)
            bsurf_disc_bin.append(bsurf_temp)
        else:
            if '*' not in str(df_period_list[index]):
                period_temp = float(df_period_list[index]) * 1000
                period_temp = round(period_temp, 3)
                if period_temp >= 1000:
                    period_temp /= 1000
                    period_temp = round(period_temp, 3)
                    period_temp = str(period_temp) + ' ' + period_unit_s
                else:
                    period_temp = str(period_temp) + ' ' + period_unit_ms
            else:
                period_temp = '*'
            if '*' not in str(df_dm_list[index]):
                dm_temp = round(float(df_dm_list[index]), 2)
                dm_temp = str(dm_temp) + ' ' + dm_unit
            else:
                dm_temp = '*'
            if '*' not in str(bsurf_list[index]):
                bsurf_temp = str(bsurf_list[index]) + ' ' + bsurf_unit
            else:
                bsurf_temp = '*'
            if str(df_psr_list[index]).strip() not in psrs_available:
                jname_temp = str(df_psr_list[index]).strip()
                jname_disc.append(jname_temp)
            else:
                jname_temp = '<a '+ 'target="_blank" ' + 'href="' + url_template + str(df_psr_list[index]).strip() + '">' + str(df_psr_list[index]).strip() + '</a>' 
                jname_disc.append(jname_temp)
            period_disc.append(period_temp)
            dm_disc.append(dm_temp)
            bsurf_disc.append(bsurf_temp)
    for k in range(len(jname_disc)):
        table_disc_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_disc[k].strip() + '</td>\n' + '<td>' + period_disc[k].strip() + '</td>\n' + '<td>' + dm_disc[k].strip() + '</td>\n' + '<td>' + bsurf_disc[k].strip() + '</td>' + '</tr>\n'
    table_disc_contents_str += '\n</table>'
    for l in range(len(jname_disc_bin)):
        table_disc_bin_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_disc_bin[l].strip() + '</td>\n' + '<td>' + period_disc_bin[l].strip() + '</td>\n' + '<td>' + dm_disc_bin[l].strip() + '</td>\n' + '<td>' + bsurf_disc_bin[l].strip() + '</td>\n' + '<td>' + pb_disc_bin[l].strip() + '</td>\n' + '<td>' + ecc_disc_bin[l].strip() + '</td>\n' + '</tr>\n'
    table_disc_bin_contents_str += '\n</table>\n\n\n'
    if len(jname_disc) == 0:
        table_disc_contents_str = ''
    if len(jname_disc_bin) == 0:
        table_disc_bin_contents_str = ''
    
    #TABLES FPR DETECTED AND BINARY DETECTED
    for index in detected:
        if '*' not in minmass_list[index]:
            if '*' not in str(df_period_list[index]):
                period_temp = float(df_period_list[index]) * 1000
                period_temp = round(period_temp, 3)
                if period_temp >= 1000:
                    period_temp /= 1000
                    period_temp = round(period_temp, 3)
                    period_temp = str(period_temp) + ' ' + period_unit_s
                else:
                    period_temp = str(period_temp) + ' ' + period_unit_ms
            else:
                period_temp = '*'
            if '*' not in str(df_dm_list[index]):
                dm_temp = round(float(df_dm_list[index]), 2)
                dm_temp = str(dm_temp) + ' ' + dm_unit
            else:
                dm_temp = '*'
            if '*' not in str(bsurf_list[index]):
                bsurf_temp = str(bsurf_list[index]) + ' ' + bsurf_unit
            else:
                bsurf_temp = '*'
            if str(df_psr_list[index]).strip() not in psrs_available:
                jname_temp = str(df_psr_list[index]).strip()
                jname_det_bin.append(jname_temp)
            else:
                jname_temp = '<a '+ 'target="_blank" ' + 'href="' + url_template + str(df_psr_list[index]).strip() + '">' + str(df_psr_list[index]).strip() + '</a>' 
                jname_det_bin.append(jname_temp)
            if '*' not in str(pb_list[index]):
                pb_temp = float(str(pb_list[index]).strip())
                if 0 < pb_temp < 1:
                    pb_temp *= 24
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_hrs
                elif 1 < pb_temp < 365:
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_d
                elif 365 < pb_temp < 1e99:
                    pb_temp *= 0.002737850787
                    pb_temp = str(round(pb_temp, 3))
                    pb_temp += ' ' + pb_unit_yr
            else:
                pb_temp = '*'
            if '*' not in str(ecc_list[index]):
                ecc_temp = str(ecc_list[index]).strip()
            else:
                ecc_temp = '*'
            pb_det_bin.append(pb_temp)
            ecc_det_bin.append(ecc_temp)
            period_det_bin.append(period_temp)
            dm_det_bin.append(dm_temp)
            bsurf_det_bin.append(bsurf_temp)
        else:
            if '*' not in str(df_period_list[index]):
                period_temp = float(df_period_list[index]) * 1000
                period_temp = round(period_temp, 3)
                if period_temp >= 1000:
                    period_temp /= 1000
                    period_temp = round(period_temp, 3)
                    period_temp = str(period_temp) + ' ' + period_unit_s
                else:
                    period_temp = str(period_temp) + ' ' + period_unit_ms
            else:
                period_temp = '*'
            if '*' not in str(df_dm_list[index]):
                dm_temp = round(float(df_dm_list[index]), 2)
                dm_temp = str(dm_temp) + ' ' + dm_unit
            else:
                dm_temp = '*'
            if '*' not in str(bsurf_list[index]):
                bsurf_temp = str(bsurf_list[index]) + ' ' + bsurf_unit
            else:
                bsurf_temp = '*'
            if str(df_psr_list[index]).strip() not in psrs_available:
                jname_temp = str(df_psr_list[index]).strip()
                jname_det.append(jname_temp)
            else:
                jname_temp = '<a '+ 'target="_blank" ' + 'href="' + url_template + str(df_psr_list[index]).strip() + '">' + str(df_psr_list[index]).strip() + '</a>' 
                jname_det.append(jname_temp)
            period_det.append(period_temp)
            dm_det.append(dm_temp)
            bsurf_det.append(bsurf_temp)
    for k in range(len(jname_det)):
        table_det_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_det[k].strip() + '</td>\n' + '<td>' + period_det[k].strip() + '</td>\n' + '<td>' + dm_det[k].strip() + '</td>\n' + '<td>' + bsurf_det[k].strip() + '</td>' + '</tr>\n'
    table_det_contents_str += '\n</table>'
    for l in range(len(jname_det_bin)):
        table_det_bin_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_det_bin[l].strip() + '</td>\n' + '<td>' + period_det_bin[l].strip() + '</td>\n' + '<td>' + dm_det_bin[l].strip() + '</td>\n' + '<td>' + bsurf_det_bin[l].strip() + '</td>\n' + '<td>' + pb_det_bin[l].strip() + '</td>\n' + '<td>' + ecc_det_bin[l].strip() + '</td>\n' + '</tr>\n'
    table_det_bin_contents_str += '\n</table>\n\n\n'
    if len(jname_det) == 0:
        table_det_contents_str = ''
    if len(jname_det_bin) == 0:
        table_det_bin_contents_str = ''
    
    
    if 'None' not in str(name):
        name_str = str(name)
    else:
        name_str = ''
    if 'None' not in str(n_span):
        n_span_str = str(n_span)
    else:
        n_span_str = ''
    if 'None' not in str(fastest_slowest):
        fastest_slowest_str = str(fastest_slowest)
    else:
        fastest_slowest_str = ''
    if 'None' not in str(sal_dm):
        sal_dm_str = str(sal_dm)
    else:
        sal_dm_str = ''
    if 'None' not in str(tpbd):
        tpbd_str = str(tpbd)
    else:
        tpbd_str = ''
    if 'None' not in str(percent):
        percent_str = str(percent)
    else:
        percent_str = ''
    if 'None' not in str(year):
        year_str = ''
        year_list = year
        num_new_pulsars = len(year_list)
        year_list = list(dict.fromkeys(year_list))
        if '1089806188' in str(year_list):
            year_list.remove('1089806188')
        year_list.sort()
        min_year = ''
        if len(year_list) >= 1:
            min_year = min(year_list)
            min_year = str(min_year)
        if '1968' in min_year:
            min_str = ' This survey detected a pulsar in 1968, the first year of pulsar astronomy.'
        else:
            min_str = ' There were a total of ' + tpbd_str + ' pulsars known before the first discovery was published. This survey increased the total amount of known pulsars by ' + percent_str + '%.'
        if len(year_list) == 1:
            for year in year_list:
                year_str += str(year)
        elif len(year_list) == 2:
                year_str += str(year_list[0]) + ' and ' + str(year_list[1])
        elif len(year_list) > 2:
            year_str += 'papers published from ' + str(year_list[0]) + ' to ' + str(year_list[len(year_list)-1])
        else:
            year_str = ''
    else:
        year_str = ''
        num_new_pulsars = ''
    final_str = '<br>' + 'The ' + name_str + ' (' + survey2 + ') ' + ' published its results in ' + str(year_str) + ' with a total of ' + str(len(discovered)) + ' new ' + '<a '+ 'target="_blank" ' + 'href="' + 'https://astronomy.swin.edu.au/cosmos/P/Pulsar' + '">' + 'pulsars' + '</a>' + ' ' + '<a ' + 'href="' + '#discovered">' + 'discovered' + '</a>' + '. ' + 'It ' + '<a ' + 'href="#detected">' + 'detected' + '</a>' ' a grand total of ' + str(len(detected)) + ' pulsars.' + fastest_slowest_str + '\n\n' + sal_dm_str + min_str + link_str + '<hr>'
    p_ref = '<p id="' + survey2 + '"></p>'
    if len(detected) == 0 and len(discovered) == 0:
        pass
    else:
        print(padding_str, file = html_file)
        print(p_ref, file = html_file)
        print('<p class="indent-all">\n' + final_str + '\n\n\n\n', file = html_file)
        print('\n\n\n\n\n' + '\n', file = html_file)
        print(html_end_str, file = html_file)
        s_plots = s.plotly_per_survey(xl, df, j, html_file)
        # bsurf_pb = s.bsurf_pb(j)
        g_plots = s.plotly_gl_gb(xl, df, j, html_file)
        p_pdot = s.p_pdot(j)
        yy_xx_zoomed = s.yy_xx_zoomed(xl, df, j, html_file)
        yy_xx_reg = s.yy_xx_reg(xl, df, j, html_file)
        zz_xx_zoomed = s.zz_xx_zoomed(xl, df, j, html_file)
        zz_xx_reg = s.zz_xx_reg(xl, df, j, html_file)
        # xx_yy_zz = s.test_3D(j)
        print(table_disc_contents_str, file = html_file)
        print(table_disc_bin_contents_str, file = html_file)
        print(table_det_contents_str, file = html_file)
        print(table_det_bin_contents_str, file = html_file)
        print(survey_name + ' Done')
        html_file.close()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        