# Evan Anthopoulos
# 3D Plotly Stuff

import pandas as pd
from astropy.visualization import quantity_support
from plotly import express as px
import plotly.graph_objects as go
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from pandas import DataFrame
import re
from plotly.offline import plot
import numpy as np

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
        # num_new_pulsars = len(year_list)
        return year_list
    
    
    
    def num_years_detected(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        survey_count = 0
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            if '*' not in df_survey_str:
                if survey in df_survey_str:
                    survey_count += 1
        # print('Survey ' + survey + ' detected pulsars a total of ' + str(survey_count) + ' times.')
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
        # print('The fastest pulsar discovered by ' + survey + ' was ' + fastest_psr + 'with a period of ' + str(fastest) + ' and the slowest pulsar discovered by ' + survey + ' was ' + slowest_psr + 'with a period of ' + str(slowest))
        return 'The fastest pulsar discovered was ' + '<a href="' + url_template + fastest_psr + '">' + fastest_psr + '</a>' + ' with a period of ' + str(fastest) + ' ' + fast_unit + ' and the slowest pulsar was ' + '<a href="' + url_template + slowest_psr + '">' + slowest_psr + '</a>' + ' with a period of ' + str(slowest) + ' ' + slow_unit + '.'
                    
                    
                    
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
        # print('The largest pulsar discovered by ' + survey + ' was ' + largest_psr + 'with a dm of ' + str(largest) + ' and the smallest pulsar discovered by ' + survey + ' was ' + smallest_psr + 'with a dm of ' + str(smallest))
        return 'The smallest pulsar dispersion measure was ' + '<a href="' + url_template + smallest_psr + '">' + smallest_psr + '</a>' + ' with a DM of ' + str(smallest) + ' ' + dm_unit + ' and the largest pulsar dispersion measure was ' + '<a href="' + url_template + largest_psr + '">' + largest_psr + '</a>' + ' with a DM of ' + str(largest) + ' ' + dm_unit + '.'
        

    
    def total_psrs_before_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
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
        else:
            psr_str = ''
        # print(survey + ' ' + str(year_count) + ' ' + str(year))
        return year_count
                    
    

    def psr_percentage_increased(self, xl_file, df_file, counter: int):
        discovered1 = float(num_discovered)
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



    def psrs_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        first_raj = [] # list of raj discovered by specific survey
        first_decj = [] # list of decj discovered by specific survey
        for i in range(len(df_psr_list)):
            df_survey = str(df_survey_list[i]).strip()
            raj_temp = str(df_raj_list[i]).strip()
            decj_temp = str(df_decj_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                    if first_survey == survey:
                        first_raj.append(raj_temp)
                        first_decj.append(decj_temp)
                elif survey == df_survey:
                    first_raj.append(raj_temp)
                    first_decj.append(decj_temp)
        return [first_raj, first_decj]
        


    def psrs_detected(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        in_raj = [] # list of raj detected by specific survey
        in_decj = [] # list of decj detected by specific survey
        first_survey = 'Null'
        for i in range(len(df_psr_list)):
            df_survey = str(df_survey_list[i]).strip()
            if ',' in df_survey:
                first_comma = df_survey.index(',')
                first_survey = df_survey[:first_comma]
            else:
                first_survey = df_survey
            if (survey != first_survey) and (survey in str(df_survey_list[i])):
                raj_temp = str(df_raj_list[i]).strip()
                decj_temp = str(df_decj_list[i]).strip()
                in_raj.append(raj_temp)
                in_decj.append(decj_temp)
        return [in_raj, in_decj]



    def galactic_detected(self, xl_file, df_dile, counter: int):
        survey= str(xl_survey_list[counter]).strip()
        in_gl = []
        in_gb = []
        first_survey = 'Null'
        for i in range(len(gl_list)):
            df_survey = str(df_survey_list[i]).strip()
            gl_temp = str(gl_list[i]).strip()
            gb_temp = str(gb_list[i]).strip()
            if ',' in df_survey:
                first_comma = df_survey.index(',')
                first_survey = df_survey[:first_comma]
            else:
                first_survey = df_survey
            if (survey != first_survey) and (survey in str(df_survey_list[i])):
                in_gl.append(gl_temp)
                in_gb.append(gb_temp)
        return [in_gl, in_gb]
    
    
    
    def galactic_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        first_gl = []
        first_gb = []
        for i in range(len(gb_list)):
            df_survey = str(df_survey_list[i]).strip()
            gl_temp = str(gl_list[i]).strip()
            gb_temp = str(gb_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = str(df_survey[:first_comma]).strip()
                    if first_survey == survey:
                        first_gl.append(gl_temp)
                        first_gb.append(gb_temp)
                elif survey == df_survey:
                    first_gl.append(gl_temp)
                    first_gb.append(gb_temp)
        return [first_gl, first_gb]
                
    
    
    def yx_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        first_xx = []
        first_yy = []
        for i in range(len(xx_list)):
            df_survey = str(df_survey_list[i]).strip()
            xx_temp = str(xx_list[i]).strip()
            yy_temp = str(yy_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                    if first_survey == survey:
                        first_xx.append(xx_temp)
                        first_yy.append(yy_temp)
                elif survey == df_survey:
                    first_xx.append(xx_temp)
                    first_yy.append(yy_temp)
        return [first_xx, first_yy]
    
    
    
    def yx_detected(self, xl_file, df_file, counter: int):
        survey= str(xl_survey_list[counter]).strip()
        in_xx = []
        in_yy = []
        first_survey = 'Null'
        for i in range(len(xx_list)):
            df_survey = str(df_survey_list[i]).strip()
            xx_temp = str(xx_list[i]).strip()
            yy_temp = str(yy_list[i]).strip()
            if '*' not in xx_temp and '*' not in yy_temp:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                else:
                    first_survey = df_survey
                if (survey != first_survey) and (survey in str(df_survey_list[i])):
                    in_xx.append(xx_temp)
                    in_yy.append(yy_temp)
        return [in_xx, in_yy]
    
    
    
    def zx_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        first_xx = []
        first_zz = []
        for i in range(len(xx_list)):
            df_survey = str(df_survey_list[i]).strip()
            xx_temp = str(xx_list[i]).strip()
            zz_temp = str(zz_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                    if first_survey == survey:
                        first_xx.append(xx_temp)
                        first_zz.append(zz_temp)
                elif survey == df_survey:
                    first_xx.append(xx_temp)
                    first_zz.append(zz_temp)
        return [first_xx, first_zz]
    
    
    
    def zx_detected(self, xl_file, df_file, counter: int):
        survey= str(xl_survey_list[counter]).strip()
        in_xx = []
        in_zz = []
        first_survey = 'Null'
        for i in range(len(xx_list)):
            df_survey = str(df_survey_list[i]).strip()
            xx_temp = str(xx_list[i]).strip()
            zz_temp = str(zz_list[i]).strip()
            if '*' not in xx_temp and '*' not in zz_temp:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                else:
                    first_survey = df_survey
                if (survey != first_survey) and (survey in str(df_survey_list[i])):
                    in_xx.append(xx_temp)
                    in_zz.append(zz_temp)
        return [in_xx, in_zz]



    def num_psrs_detected(self, xl_file, df_file, counter: int):
        det = detected
        disc = discovered
        in_raj = len(det[0]) # list of raj detected by specific survey
        first_raj = len(disc[0])
        total = in_raj + first_raj
        return total



    def num_psrs_discovered(self, xl_file, df_file, counter: int):
        disc = discovered
        first_raj = len(disc[0]) # list of raj discovered by specific survey
        return first_raj



    # def link_survey(self, xl_file, df_file, counter: int):
    #     survey = str(xl_survey_list[counter]).strip()
    def in_or_out(self, counter: int):
        raj = []
        decj = []
        jnames_cleaned = []
        psrs_available_cleaned = []
        available_or_not = []
        det = detected
        disc = discovered
        det_disc_list = []
        first_raj = disc[0] # list of raj discovered by specific survey
        in_raj = det[0] # list of raj detected by specific survey
        for i in range(len(df_psr_list)):
            raj_temp = str(df_raj_list[i]).strip()
            decj_temp = str(df_decj_list[i]).strip()
            if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list[i]):
                raj.append(raj_temp)
                decj.append(decj_temp)
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
        for i in range(len(psrs_available)):
            psr = str(psrs_available[i]).strip()
            psrs_available_cleaned.append(psr)
        for i in range(len(jnames_cleaned)):
            if str(jnames_cleaned[i]) in str(psrs_available_cleaned):
                available_or_not.append(str(df_raj_list[i]).strip())
            else:
                available_or_not.append("Null")
        for r in raj:
            if r in first_raj and r not in in_raj:
                det_disc_list.append("PSRs Discovered")
            elif r not in in_raj and r not in first_raj and r in available_or_not:
                det_disc_list.append("All Known Pulsars in MeerTime")
            elif r not in in_raj and r not in first_raj:
                det_disc_list.append("All Known Pulsars")
            elif r in in_raj and r not in first_raj:
                det_disc_list.append("PSRs Detected")
            else:
                det_disc_list.append('null')
        return det_disc_list
        


    def plotly_per_survey(self, xl_file, df_file, counter: int, html_file):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        raj = []
        decj = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        disc = discovered
        det = detected
        first_raj = disc[0] # list of raj discovered by specific survey
        in_raj = det[0] # list of raj detected by specific survey
        first_decj = disc[1] # list of decj discovered by specific survey
        in_decj = det[1] # list of decj detected by specific survey
        det_disc_list = det_disc_real
        for i in range(len(df_psr_list)):
            raj_temp = str(df_raj_list[i]).strip()
            decj_temp = str(df_decj_list[i]).strip()
            if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list[i]):
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
                raj.append(raj_temp)
                decj.append(decj_temp)
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
                
        print(len(det_disc_list))
        c = SkyCoord(ra=raj,dec=decj, unit=(u.hourangle,u.deg))
        ranew = coord.Angle(c.ra.deg,unit=u.deg)
        ranew2 = ranew.wrap_at('180d', inplace=False)
        decnew = coord.Angle(c.dec.deg,unit=u.degree)
        source = {
            'Name': jnames_cleaned,
            'raj': ranew2,
            'decj': decnew,
            'Legend (RA (J2000) vs Dec (J2000))': det_disc_list,
            'Available PSR': available_or_not,
            'survey': survey_data,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lon='raj', lat='decj', labels=dict(lat='raj (rad)', lon='decj(deg)'), color="Legend (RA (J2000) vs Dec (J2000))", width=1000, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered": "#FF6103", "PSRs Detected": "#00EEEE", "All Known Pulsars in MeerTime" : "#333", "All Known Pulsars": "#DCDCDC"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                             )
        # fig.update_layout(color='Availabe PSR', color_discrete_map={'Yes':'#333', 'No': '#DCDCDC'})
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
        # with open('survey_plots.html', 'w+') as f:
        #f.write(html_file)
        if len(in_raj) == 0 and len(in_decj) == 0 and len(first_raj) == 0 and len(first_decj) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)



    # def plotly_gl_gb(self, xl_file, df_file, counter: int, html_file):
    #     quantity_support()
    #     det_disc_list = det_disc_real
    #     survey_name = str(survey_name_list[counter]).strip()
    #     psrs_available_cleaned = []
    #     psr_links = []
    #     gl = []
    #     gl_in = []
    #     gl_first = []
    #     gb = []
    #     gb_in = []
    #     gb_first = []
    #     jname = []
    #     jnames_cleaned = []
    #     available_or_not = []
    #     survey_data = []
    #     first_raj = discovered[0]
    #     first_decj = discovered[1]
    #     in_raj = detected[0]
    #     in_decj = detected[1]
    #     for i in range(len(df_psr_list)):
    #         gl_temp = str(gl_list[i]).strip()
    #         gb_temp = str(gb_list[i]).strip()
    #         raj_temp = str(df_raj_list[i]).strip()
    #         decj_temp = str(df_decj_list[i]).strip()
    #         if '*' not in str(gl_list[i]) and '*' not in str(gb_list[i]):
    #             if '*' not in str(df_raj_list[i]).strip() and '*' not in str(df_decj_list[i]).strip():
    #                 if raj_temp in first_raj:
    #                     gl_first.append(gl_temp)
    #                     gb_first.append(gb_temp)
    #                     gl.append('null')
    #                     gb.append('null')
    #                     jname = str(jnames_list[i].strip())
    #                     jnames_cleaned.append(jname)
    #                     survey_p = str(df_survey_list[i]).strip()
    #                     survey_data.append(survey_p)
    #                 elif raj_temp in in_raj:
    #                     gl_in.append(gl_temp)
    #                     gb_in.append(gb_temp)
    #                     gl.append('null')
    #                     gb.append('null')
    #                     jname = str(jnames_list[i].strip())
    #                     jnames_cleaned.append(jname)
    #                     survey_p = str(df_survey_list[i]).strip()
    #                     survey_data.append(survey_p)
    #                 else:
    #                     gl.append(gl_temp)
    #                     gb.append(gb_temp)
    #                     jname = str(jnames_list[i].strip())
    #                     jnames_cleaned.append(jname)
    #                     survey_p = str(df_survey_list[i]).strip()
    #                     survey_data.append(survey_p)
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

                        
    #     source = {
    #         'Name': jnames_cleaned,
    #         'gl': gl,
    #         'gb': gb,
    #         'Legend (gl vs gb)': det_disc_list,
    #         'survey': survey_data,
    #         "URLs": psr_links
    #     }
    #     test_list = [1,2,3,4,5,6,7,8,9]
    #     test_list2 = [9,8,7,6,5,4,3,2,1]
    #     source2 = {
    #         'gl_in': gl_in,
    #         'gb_in': gb_in
    #         }
    #     source3 = {
    #         'gl_first': gl_first,
    #         'gb_first': gb_first
    #         }

    #     dafr3 = DataFrame(data=source3)
    #     dafr2 = DataFrame(data=source2)
    #     dafr = DataFrame(data=source)
    #     fig = go.Figure()
    #     fig.add_trace(go.Scattergeo(lat=dafr['gl'], lon=dafr['gb'], marker={'size':10,'color':'khaki'}, customdata=dafr["URLs"], hoverinfo=None))
    #     fig.add_trace(go.Scattergeo(lon=dafr2['gl_in'],lat=dafr2['gb_in']))
    #     fig.add_trace(go.Scattergeo(lon=dafr3['gl_first'], lat=dafr3['gb_first']))
    #     fig.update_layout(  title_text=survey_name,
    #                         showlegend=True,
    #                         geo = dict(
    #                         showland = False,
    #                         showcountries = False,
    #                         showocean = False,
    #                         projection = dict(
    #                         type = 'orthographic'
    #                             ),
    #                     lonaxis = dict(
    #                     showgrid = True,
    #                     gridcolor = 'rgb(102, 102, 102)',
    #                     gridwidth = 0.5
    #                 ),
    #                     lataxis = dict(
    #                     showgrid = True,
    #                     gridcolor = 'rgb(102, 102, 102)',
    #                     gridwidth = 0.5
    #         )
    #         )
    #         )
    #     # fig = px.scatter_geo(dafr, lat='gl', lon='gb', color="Legend (gl vs gb)", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRs Detected": "#00EEEE", "All Known Pulsars" : "#333", "PSRs Discovered": "#FF6103"}, custom_data=["URLs"],
    #     #                       projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
    #     #                       )
        
    #     fig.update_geos(showframe=True, visible=False)
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
    #             {plot_div}
    #             {js_callback}
    #     """.format(plot_div=plot_div, js_callback=js_callback)

    #     # Write out HTML file
    #     # with open('survey_plots.html', 'w+') as f:
    #     #f.write(html_file)
    #     if len(gl) == 0 and len(gb) == 0:
    #             return 'None'
    #     else:
    #         print(html_str, file = html_file)


    
    def yy_xx(self, xl_file, df_file, counter: int, html_file):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        xx = []
        yy = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        disc = yx_discovered
        det = yx_detected
        first_xx = disc[0] # list of raj discovered by specific survey
        in_xx = det[0] # list of raj detected by specific survey
        first_yy = disc[1] # list of decj discovered by specific survey
        in_yy = det[1] # list of decj detected by specific survey
        det_disc_list = det_disc_real
        for i in range(len(df_psr_list)):
            xx_temp = str(xx_list[i]).strip()
            yy_temp = str(yy_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(yy_list[i]):
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
                xx.append(xx_temp)
                yy.append(yy_temp)
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
                
        print(len(det_disc_list))
        source = {
            'Name': jnames_cleaned,
            'x-distance (kpc)': xx,
            'y-distance (kpc)': yy,
            'Legend (x vs y)': det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='y-distance (kpc)', color="Legend (x vs y)", width=1000, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRs Detected": "#00EEEE", "All Known Pulsars in MeerTime" : "#333", "All Known Pulsars" : "#DCDCDC", "PSRs Discovered": "#FF6103"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        # fig.update_geos(showframe=True, visible=False)
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
        # with open('survey_plots.html', 'w+') as f:
        #f.write(html_file)
        if len(in_xx) == 0 and len(in_yy) == 0 and len(first_xx) == 0 and len(first_yy) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)



    def zz_xx(self, xl_file, df_file, counter: int, html_file):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        xx = []
        zz = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        disc = zx_discovered
        det = zx_detected
        first_xx = disc[0] # list of raj discovered by specific survey
        in_xx = det[0] # list of raj detected by specific survey
        first_zz = disc[1] # list of decj discovered by specific survey
        in_zz = det[1] # list of decj detected by specific survey
        det_disc_list = det_disc_real
        for i in range(len(df_psr_list)):
            xx_temp = str(xx_list[i]).strip()
            zz_temp = str(zz_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(zz_list[i]):
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
                xx.append(xx_temp)
                zz.append(zz_temp)
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
            'x-distance (kpc)': xx,
            'z-distance (kpc)': zz,
            'Legend (x vs z)': det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }

        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='x-distance (kpc)', y='z-distance (kpc)', color="Legend (x vs z)", width=1000, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered": "#FF6103", "PSRs Detected": "#00EEEE", "All Known Pulsars in MeerTime": "#333", "All Known Pulsars" : "#DCDCDC"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        # color="Legend (zz vs xx)", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRS Detected": "#00EEEE", "All Known Pulsars" : "#333", "PSRS Discovered": "#FF6103"}, custom_data=["URLs"],
        # for i in range(10): # DEBUG
        #     print('i:' + str(i), 'xx ' + str(xx[i]),'zz ' + str(zz[i]))
        # print('Length: ' + str(len(zx_det_disc_list)))
        # fig.update_geos(showframe=True, visible=False)
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
        # with open('survey_plots.html', 'w+') as f:
        #f.write(html_file)
        if len(in_xx) == 0 and len(in_zz) == 0 and len(first_xx) == 0 and len(first_zz) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)
            
    
    
    def test_3D(self, counter: int):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        xx = []
        yy = []
        zz = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        disc = zx_discovered
        det = zx_detected
        first_xx = disc[0] # list of raj discovered by specific survey
        in_xx = det[0] # list of raj detected by specific survey
        first_zz = disc[1] # list of decj discovered by specific survey
        in_zz = det[1] # list of decj detected by specific survey
        det_disc_list = det_disc_real
        for i in range(len(df_psr_list)):
            xx_temp = str(xx_list[i]).strip()
            yy_temp = str(yy_list[i]).strip()
            zz_temp = str(zz_list[i]).strip()
            if '*' not in str(xx_list[i]) and '*' not in str(yy_list[i]) and '*' not in str(zz_list[i]):
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
                xx.append(xx_temp)
                yy.append(yy_temp)
                zz.append(zz_temp)
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
            'x-distance (kpc)': xx,
            'y-distance (kpc)': yy,
            'z-distance (kpc)': zz,
            'Legend (x vs y vs z)': det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }

        dafr = DataFrame(data=source)
        fig = px.scatter_3d(dafr, x='x-distance (kpc)', y='y-distance (kpc)', z='z-distance (kpc)', color="Legend (x vs y vs z)", width=1000, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered": "#FF6103", "PSRs Detected": "#00EEEE", "All Known Pulsars" : "#DCDCDC", "All Known Pulsars in MeerTime" : "#333"}, custom_data=["URLs"]
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
        if len(in_xx) == 0 and len(in_zz) == 0 and len(first_xx) == 0 and len(first_zz) == 0:
                return 'None'
        else:
            print('<center>' + html_str + '</center>', file = html_file)
    
    
    
    def bsurf_pb(self, counter: int):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        bsurf = []
        p0 = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        disc = discovered
        det = detected
        first_raj = disc[0] # list of raj discovered by specific survey
        in_raj = det[0] # list of raj detected by specific survey
        fist_p0 = disc[1] # list of decj discovered by specific survey
        in_p0 = det[1] # list of decj detected by specific survey
        det_disc_list = det_disc_real
        test_list = []
        for i in range(len(df_psr_list)):
            bsurf_temp = str(bsurf_list[i]).strip()
            p0_temp = str(df_period_list[i]).strip()
            #print(bsurf)
            if '*' not in bsurf_temp and '*' not in p0_temp:
                bsurf.append(bsurf_temp)
                p0.append(p0_temp)
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
            else:
                bsurf.append('null')
                p0.append('null')
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
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
        print(bsurf,p0)
    
        source = {
            'Name': jnames_cleaned,
            'Magnetic Field Strength (G)': bsurf,
            'p0': p0,
            'Legend (Magnetic Field Strength vs Spin Period (s))': det_disc_list,
            'URLs': psr_links
        }
    
        print(len(bsurf),len(p0),len(jnames_cleaned),len(det_disc_list),len(psr_links),'ok')
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, x='p0', y='Magnetic Field Strength (G)', color="Legend (Magnetic Field Strength vs Spin Period (s)))",log_x=True, log_y=True, width=1000, height=500, title='Magnetic Field Strength vs Spin Period for the ' + survey_name, hover_name="Name", color_discrete_map={"PSRs Discovered": "#FF6103", "All Known Pulsars in MeerTime": "#333", "All Known Pulsars": "#DCDCDC", "PSRs Detected": "#00EEEE"}, custom_data=["URLs"]
                              # size of markers, "pop" is one of the columns of gapminder
                              )
        fig.update_layout(autotypenumbers='convert types')
        fig.update_traces(marker=dict(size=4))
        fig.show()
        print("here")
        
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
        # with open('survey_plots.html', 'w+') as f:
        #f.write(html_file)
        if len(bsurf) == 0 and len(p0) == 0:
                return 'None'
        else:
            print('<center>\n' + html_str + '</center>\n', file = html_file)





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


pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')
df = pd.read_csv('databasev2.csv', header=None, sep='~', engine='python')


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

url_template = 'https://pulsars.org.au/fold/meertime/'

s = Survey()

# html_file = open('survey_plots.html', 'w+')
final_str = ''
table_start_str = '<table>' + '\n<tr>'

html_start_str = '<html>\n' + ' <head>\n' + ' <title>\n' + ' Second attempt.' + '  </title>' + ' </head>' + ' <body> \n'
html_end_str = '\n</body>' + '\n</html>'

for j in range(len(xl_survey_list)):
# j = 16

    survey = str(xl_survey_list[j]).strip()
    survey2 = str(xl_survey_list[j]).strip()
    survey_name = str(survey_name_list[j]).strip()
    html_style_str = '<style> h1 {text-align: center;} </style>'
    html_header_str = html_style_str + '<h1>' + survey_name + '</h1>'
    
    html_file_str = survey + "_plots.html"
    html_file = open(html_file_str, 'w+')
    print(html_header_str + html_start_str, file = html_file)
    
    name = s.survey_name(xl, j)
    year = s.year_discovered(xl, df, j)
    n_span = s.num_years_detected(j)
    fastest_slowest = s.fastest_slowest_period(j)
    sal_dm = s.small_largest_dm(j)
    tpbd = s.total_psrs_before_discovered(xl, df, j)
    detected = s.psrs_detected(xl, df, j)
    discovered = s.psrs_discovered(xl, df, j)
    det_disc_real = s.in_or_out(j)
    num_detected = s.num_psrs_detected(xl, df, j)
    num_discovered = s.num_psrs_discovered(xl, df, j)
    percent = s.psr_percentage_increased(xl, df, j)
    g_detected = s.galactic_detected(xl, df, j)
    g_discovered = s.galactic_discovered(xl, df, j)
    yx_discovered = s.yx_discovered(xl, df, j)
    yx_detected = s.yx_detected(xl, df, j)
    zx_discovered = s.zx_discovered(xl, df, j)
    zx_detected = s.zx_detected(xl, df, j)
    # tbl = s.disc_table(j)
    # tbl2 = s.det_table(j)
    
    period_unit_ms = 'milliseconds'
    period_unit_s = 'seconds'
    dm_unit = 'pc/cc'
    bsurf_unit = 'G'
    first_raj = discovered[0]
    in_raj = detected[0]
    jname_disc = []
    period_disc = []
    dm_disc = []
    bsurf_disc = []
    table_disc_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2>PSRs discovered by ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_disc = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' '\n</tr>\n\n'
    table_disc_contents_str = table_disc_str + table_header_disc
    
    jname_disc_bin = []
    period_disc_bin = []
    dm_disc_bin = []
    bsurf_disc_bin = []
    table_disc_bin_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2>Binary PSRs discovered by ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_disc_bin = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' '\n</tr>\n\n'
    table_disc_bin_contents_str = table_disc_bin_str + table_header_disc_bin
    
    jname_det = []
    period_det = []
    dm_det = []
    bsurf_det = []
    table_det_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style> \n\n<h2>PSRs detected by ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_det = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' '\n</tr>\n\n'
    table_det_contents_str = table_det_str + table_header_det
    
    jname_det_bin = []
    period_det_bin = []
    dm_det_bin = []
    bsurf_det_bin = []
    table_det_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;} \n</style> \n\n<h2>Binary PSRs detected by ' + survey_name_list[j].strip() + '</h2>\n\n' + '<table style="width:100%">\n'
    table_header_det = '<tr> \n<th>JNAME</th>' + '<th>SPIN PERIOD</th>' + '<th>DM</th>' + '<th>MAGNETIC FIELD STRENGTH</th>' '\n</tr>\n\n'
    table_det_bin_contents_str = table_det_str + table_header_det
    
    # TABLES FOR DISCOVERED and BINARY DISCOVERED
    for psr in first_raj:
        for i in range(len(df_psr_list)):
            if str(psr).strip() in df_raj_list[i] and '*' not in minmass_list[i]:
                if '*' not in str(df_period_list[i]):
                    period_temp = float(df_period_list[i]) * 1000
                    period_temp = round(period_temp, 3)
                    if period_temp >= 1000:
                        period_temp /= 1000
                        period_temp = round(period_temp, 3)
                        period_temp = str(period_temp) + ' ' + period_unit_s
                    else:
                        period_temp = str(period_temp) + ' ' + period_unit_ms
                else:
                    period_temp = '*'
                if '*' not in str(df_dm_list[i]):
                    dm_temp = round(float(df_dm_list[i]), 2)
                    dm_temp = str(dm_temp) + ' ' + dm_unit
                else:
                    dm_temp = '*'
                if '*' not in str(bsurf_list[i]):
                    bsurf_temp = str(bsurf_list[i]) + ' ' + bsurf_unit
                else:
                    bsurf_temp = '*'
                jname_temp = '<a href="' + url_template + str(df_psr_list[i]).strip() + '">' + str(df_psr_list[i]).strip() + '</a>' 
                jname_disc_bin.append(jname_temp)
                period_disc_bin.append(period_temp)
                dm_disc_bin.append(dm_temp)
                bsurf_disc_bin.append(bsurf_temp)
            elif str(psr).strip() in df_raj_list[i]:
                if '*' not in str(df_period_list[i]):
                    period_temp = float(df_period_list[i]) * 1000
                    period_temp = round(period_temp, 3)
                    if period_temp >= 1000:
                        period_temp /= 1000
                        period_temp = round(period_temp, 3)
                        period_temp = str(period_temp) + ' ' + period_unit_s
                    else:
                        period_temp = str(period_temp) + ' ' + period_unit_ms
                else:
                    period_temp = '*'
                if '*' not in str(df_dm_list[i]):
                    dm_temp = round(float(df_dm_list[i]), 2)
                    dm_temp = str(dm_temp) + ' ' + dm_unit
                else:
                    dm_temp = '*'
                if '*' not in str(bsurf_list[i]):
                    bsurf_temp = str(bsurf_list[i]) + ' ' + bsurf_unit
                else:
                    bsurf_temp = '*'
                jname_temp = '<a href="' + url_template + str(df_psr_list[i]).strip() + '">' + str(df_psr_list[i]).strip() + '</a>' 
                jname_disc.append(jname_temp)
                period_disc.append(period_temp)
                dm_disc.append(dm_temp)
                bsurf_disc.append(bsurf_temp)
    for k in range(len(jname_disc)):
        table_disc_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_disc[k].strip() + '</td>\n' + '<td>' + period_disc[k].strip() + '</td>\n' + '<td>' + dm_disc[k].strip() + '</td>\n' + '<td>' + bsurf_disc[k].strip() + '</td>' + '</tr>\n'
    table_disc_contents_str += '\n</table>'
    for l in range(len(jname_disc_bin)):
        table_disc_bin_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_disc_bin[l].strip() + '</td>\n' + '<td>' + period_disc_bin[l].strip() + '</td>\n' + '<td>' + dm_disc_bin[l].strip() + '</td>\n' + '<td>' + bsurf_disc_bin[l].strip() + '</td>' + '</tr>\n'
    table_disc_bin_contents_str += '\n</table>\n\n\n'
    if len(jname_disc) == 0:
        table_disc_contents_str = ''
    if len(jname_disc_bin) == 0:
        table_disc_bin_contents_str = ''
    
    #TABLES FPR DETECTED AND BINARY DETECTED
    for psr in in_raj:
        for i in range(len(df_psr_list)):
            if str(psr).strip() in df_raj_list[i] and '*' not in minmass_list[i]:
                if '*' not in str(df_period_list[i]):
                    period_temp = float(df_period_list[i]) * 1000
                    period_temp = round(period_temp, 3)
                    if period_temp >= 1000:
                        period_temp /= 1000
                        period_temp = round(period_temp, 3)
                        period_temp = str(period_temp) + ' ' + period_unit_s
                    else:
                        period_temp = str(period_temp) + ' ' + period_unit_ms
                else:
                    period_temp = '*'
                if '*' not in str(df_dm_list[i]):
                    dm_temp = round(float(df_dm_list[i]), 2)
                    dm_temp = str(dm_temp) + ' ' + dm_unit
                else:
                    dm_temp = '*'
                if '*' not in str(bsurf_list[i]):
                    bsurf_temp = str(bsurf_list[i]) + ' ' + bsurf_unit
                else:
                    bsurf_temp = '*'
                jname_temp = '<a href="' + url_template + str(df_psr_list[i]).strip() + '">' + str(df_psr_list[i]).strip() + '</a>' 
                jname_det_bin.append(jname_temp)
                period_det_bin.append(period_temp)
                dm_det_bin.append(dm_temp)
                bsurf_det_bin.append(bsurf_temp)
            elif str(psr).strip() in df_raj_list[i]:
                if '*' not in str(df_period_list[i]):
                    period_temp = float(df_period_list[i]) * 1000
                    period_temp = round(period_temp, 3)
                    if period_temp >= 1000:
                        period_temp /= 1000
                        period_temp = round(period_temp, 3)
                        period_temp = str(period_temp) + ' ' + period_unit_s
                    else:
                        period_temp = str(period_temp) + ' ' + period_unit_ms
                else:
                    period_temp = '*'
                if '*' not in str(df_dm_list[i]):
                    dm_temp = round(float(df_dm_list[i]), 2)
                    dm_temp = str(dm_temp) + ' ' + dm_unit
                else:
                    dm_temp = '*'
                if '*' not in str(bsurf_list[i]):
                    bsurf_temp = str(bsurf_list[i]) + ' ' + bsurf_unit
                else:
                    bsurf_temp = '*'
                jname_temp = '<a href="' + url_template + str(df_psr_list[i]).strip() + '">' + str(df_psr_list[i]).strip() + '</a>' 
                jname_det.append(jname_temp)
                period_det.append(period_temp)
                dm_det.append(dm_temp)
                bsurf_det.append(bsurf_temp)
    for k in range(len(jname_det)):
        table_det_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_det[k].strip() + '</td>\n' + '<td>' + period_det[k].strip() + '</td>\n' + '<td>' + dm_det[k].strip() + '</td>\n' + '<td>' + bsurf_det[k].strip() + '</td>' + '</tr>\n'
    table_det_contents_str += '\n</table>'
    for l in range(len(jname_det_bin)):
        table_det_bin_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td>' + jname_det_bin[l].strip() + '</td>\n' + '<td>' + period_det_bin[l].strip() + '</td>\n' + '<td>' + dm_det_bin[l].strip() + '</td>\n' + '<td>' + bsurf_det_bin[l].strip() + '</td>' + '</tr>\n'
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
    # if g_plots == None:
    #     g_plot_str = ''
    # else:
    #     g_plots = ''
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
        # print('Survey ' + survey + ' reported new pulsars in the year(s): ' + str(year_list) + ' with a total of ' + str(num_new_pulsars) + ' new pulsars discovered.')
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
    final_str = '<br>' + 'The ' + name_str + ' (' + survey2 + ') ' + ' published its results in ' + str(year_str) + ' with a total of ' + str(num_discovered) + ' new pulsars discovered.\n\n' + 'It' + ' detected a grand total of ' + str(num_detected) + ' pulsars.\n\n' + fastest_slowest_str + '\n\n' + sal_dm_str + min_str + '<hr>'
    #img_str = '<img src="plots_pngs/' + survey2 + '.png"' + " alt=" + '"' + survey2+ '">'
    p_ref = '<p id="' + survey2 + '"></p>'
    print(len(detected[0]))
    if len(detected[0]) == 0:
        pass
    else:
        print(p_ref, file = html_file)
        #  'src="plots_pngs/' + survey2 + '.png
        print(final_str + '\n\n\n\n', file = html_file)
        print('\n\n\n\n\n' + '\n', file = html_file)
        print(html_end_str, file = html_file)
        s_plots = s.plotly_per_survey(xl, df, j, html_file)
        bsurf_pb = s.bsurf_pb(j)
        # g_plots = s.plotly_gl_gb(xl, df, j, html_file)
        yy_xx = s.yy_xx(xl, df, j, html_file)
        zz_xx = s.zz_xx(xl, df, j, html_file)
        xx_yy_zz = s.test_3D(j)
        print(table_disc_contents_str, file = html_file)
        print(table_disc_bin_contents_str, file = html_file)
        print(table_det_contents_str, file = html_file)
        print(table_det_bin_contents_str, file = html_file)
        html_file.close()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        