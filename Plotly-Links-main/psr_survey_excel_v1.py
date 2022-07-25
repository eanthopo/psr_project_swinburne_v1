# Evan Anthopoulos
# Excel Survey Loader

import pandas as pd
from astropy.visualization import quantity_support
from plotly import express as px
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from matplotlib import pyplot as plt
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
                        slowest_psr = str(df_psr_list[i])
                    if (fastest is None) or (df_period_float < fastest):
                        fastest = df_period_float
                        fastest = round(fastest, 5)
                        fastest_psr = str(df_psr_list[i])
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
        return 'The fastest pulsar discovered was ' + 'a href="' + url_template + fastest_psr + '">' + fastest_psr + '</a>' + 'with a period of ' + str(fastest) + ' ' + fast_unit + ' and the slowest pulsar was ' + 'a href="' + url_template + slowest_psr + '">' + slowest_psr + '</a>' + 'with a period of ' + str(slowest) + ' ' + slow_unit + '.'
                    
                    
                    
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
                        largest_psr = str(df_psr_list[i])
                    if (smallest is None) or (df_dm_float < smallest):
                        smallest = df_dm_float
                        smallest = round(smallest, 5)
                        smallest_psr = str(df_psr_list[i])
        # print('The largest pulsar discovered by ' + survey + ' was ' + largest_psr + 'with a dm of ' + str(largest) + ' and the smallest pulsar discovered by ' + survey + ' was ' + smallest_psr + 'with a dm of ' + str(smallest))
        return 'The smallest pulsar dispersion measure was ' + 'a href="' + url_template + smallest_psr + '">' + smallest_psr + '</a>' + 'with a dm of ' + str(smallest) + ' ' + dm_unit + ' and the largest pulsar dispersion measure was ' + 'a href="' + url_template + largest_psr + '">' + largest_psr + '</a>' + 'with a dm of ' + str(largest) + ' ' + dm_unit + '.'
            
        
    
    # def plot_in_sky(self):
    #     quantity_support()
    #     plot.figure(figsize=(8,6))
    #     raj_plt_list = []
    #     decj_plt_list = []
    #     for i in range(len(df_psr_list)):
    #         if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list):
    #             raj = str(df_raj_list[i]).strip()
    #             decj = str(df_decj_list[i]).strip()
    #             raj_plt_list.append(raj)
    #             decj_plt_list.append(decj)
    #     c = SkyCoord(ra=raj_plt_list,dec=decj_plt_list, unit=(u.hourangle,u.deg), frame='icrs')
    #     ranew = coord.Angle(c.ra.rad,unit=u.rad)
    #     ranew2 = ranew.wrap_at('180d', inplace=False)
    #     decnew = coord.Angle(c.dec.rad,unit=u.degree)
    #     fig = plot.figure(figsize=(8,6))
    #     ax = fig.add_subplot(111, projection="mollweide")
    #     ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    #     ax.grid(True)
    #     s_plot = ax.scatter(ranew2, decnew)
    #     return s_plot
        

    
    def total_psrs_before_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        year_disc_list = year
        year_disc_list = list(dict.fromkeys(year_disc_list))
        if '1089806188' in str(year_disc_list):
            year_disc_list.remove('1089806188')
        year_count = 0
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
            if '*' not in gl_temp and '*' not in gb_temp:
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
                    first_survey = df_survey[:first_comma]
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



    def link_survey(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        



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
        det_disc_list = []
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
        for r in raj:
            if r in first_raj and r not in in_raj:
                det_disc_list.append("PSRS Detected")
            elif r not in in_raj and r not in first_raj:
                det_disc_list.append("All Known Pulsars")
            elif r in in_raj and r not in first_raj:
                det_disc_list.append("PSRS Discovered")
            else:
                det_disc_list.append('null')
                
        print(len(det_disc_list))
        c = SkyCoord(ra=raj,dec=decj, unit=(u.hourangle,u.deg))
        ranew = coord.Angle(c.ra.deg,unit=u.deg)
        ranew2 = ranew.wrap_at('180d', inplace=False)
        decnew = coord.Angle(c.dec.deg,unit=u.degree)
        source = {
            'Name': jnames_cleaned,
            'raj': ranew2,
            'decj': decnew,
            'detected': det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lon='raj', lat='decj', color="detected", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRS Discovered": "#FF6103", "PSRS Detected": "#00EEEE", "All Known Pulsars" : "#333"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False)
        fig.update_traces(marker=dict(size=4))
        # tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
        # tick_labels_y = np.array([-75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75])
        # fig.set_xticklabels(tick_labels, zorder = 15)
        # fig.set_yticklabels(tick_labels_y, zorder = 15)
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
            print(html_str, file = html_file)



    def plotly_gl_gb(self, xl_file, df_file, counter: int, html_file):
        quantity_support()
        survey_name = str(survey_name_list[counter]).strip()
        psrs_available_cleaned = []
        psr_links = []
        gl = []
        gb = []
        jname = []
        jnames_cleaned = []
        available_or_not = []
        survey_data = []
        first_gl = g_discovered[0] # list of gl discovered by specific survey
        in_gl = g_detected[0] # list of gl detected by specific survey
        g_det_disc_list = []
        for i in range(len(df_psr_list)):
            gl_temp = str(gl_list[i]).strip()
            gb_temp = str(gb_list[i]).strip()
            if '*' not in str(gl_list[i]) and '*' not in str(gb_list[i]):
                jname = str(jnames_list[i].strip())
                jnames_cleaned.append(jname)
                survey_p = str(df_survey_list[i]).strip()
                survey_data.append(survey_p)
                gl.append(gl_temp)
                gb.append(gb_temp)
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
        for g in gl:
            if g in in_gl and g not in first_gl:
                g_det_disc_list.append("PSRS Detected")
            elif g not in in_gl and g not in first_gl:
                g_det_disc_list.append("All Known Pulsars")
            elif g in first_gl and g not in in_gl:
                g_det_disc_list.append("PSRS Discovered")
            else:
                g_det_disc_list.append('null')

                        
        source = {
            'Name': jnames_cleaned,
            'gl': gl,
            'gb': gb,
            'Legend (gl vs gb)': g_det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }
        
        dafr = DataFrame(data=source)
        fig = px.scatter_geo(dafr, lat='gl', lon='gb', color="Legend (gl vs gb)", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRS Detected": "#00EEEE", "All Known Pulsars" : "#333", "PSRS Discovered": "#FF6103"}, custom_data=["URLs"],
                              projection="mollweide" # size of markers, "pop" is one of the columns of gapminder
                              )

        fig.update_geos(showframe=True, visible=False)
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
        if len(gl) == 0 and len(gb) == 0:
                return 'None'
        else:
            print(html_str, file = html_file)


    
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
        yx_det_disc_list = []
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
        for x in xx:
            if x in in_xx and x not in first_xx:
                yx_det_disc_list.append("PSRS Detected")
            elif x not in in_xx and x not in first_xx:
                yx_det_disc_list.append("All Known Pulsars")
            elif x in first_xx and x not in in_xx:
                yx_det_disc_list.append("PSRS Discovered")
            else:
                yx_det_disc_list.append('null')
                
        print(len(yx_det_disc_list))
        source = {
            'Name': jnames_cleaned,
            'xx': xx,
            'yy': yy,
            'Legend (yy vs xx)': yx_det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, log_x='xx', log_y='yy', color="Legend (yy vs xx)", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRS Detected": "#00EEEE", "All Known Pulsars" : "#333", "PSRS Discovered": "#FF6103"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False)
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
            print(html_str, file = html_file)



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
        zx_det_disc_list = []
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
        for z in zz:
            if z in in_zz and z not in first_zz:
                zx_det_disc_list.append("PSRS Detected")
            elif z not in in_zz and z not in first_zz: 
                zx_det_disc_list.append("All Known Pulsars")
            elif z in first_zz and z not in in_zz:
                zx_det_disc_list.append("PSRS Discovered")
            else:
                zx_det_disc_list.append('null')
                
        source = {
            'Name': jnames_cleaned,
            'xx': xx,
            'zz': zz,
            'Legend (zz vs xx)': zx_det_disc_list,
            'survey': survey_data,
            "URLs": psr_links
        }
        dafr = DataFrame(data=source)
        fig = px.scatter(dafr, log_x='xx', log_y='zz', color="Legend (zz vs xx)", width=500, height=500, title=survey_name, hover_name="Name", color_discrete_map={"PSRS Detected": "#00EEEE", "All Known Pulsars" : "#333", "PSRS Discovered": "#FF6103"}, custom_data=["URLs"],
                              # size of markers, "pop" is one of the columns of gapminder
                             )
        fig.update_geos(showframe=True, visible=False)
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
            print(html_str, file = html_file)



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
xx_col = 49
yy_col = 50
zz_col = 51

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

url_template = 'https://pulsars.org.au/fold/meertime/'

s = Survey()

# html_file = open('survey_plots.html', 'w+')
final_str = ''
html_start_str = '<html>\n' + ' <head>\n' + ' <title>\n' + ' Second attempt.' + '  </title>' + ' </head>' + ' <body> \n'
html_end_str = '\n</body>' + '\n</html>'

for j in range(len(xl_survey_list)):
# j = 16

    survey = str(xl_survey_list[j]).strip()
    survey2 = str(xl_survey_list[j]).strip()
    
    html_file_str = survey + "_plots.html"
    html_file = open(html_file_str, 'w+')
    print(html_start_str, file = html_file)
    
    name = s.survey_name(xl, j)
    year = s.year_discovered(xl, df, j)
    n_span = s.num_years_detected(j)
    fastest_slowest = s.fastest_slowest_period(j)
    sal_dm = s.small_largest_dm(j)
    tpbd = s.total_psrs_before_discovered(xl, df, j)
    detected = s.psrs_detected(xl, df, j)
    discovered = s.psrs_discovered(xl, df, j)
    num_detected = s.num_psrs_detected(xl, df, j)
    num_discovered = s.num_psrs_discovered(xl, df, j)
    percent = s.psr_percentage_increased(xl, df, j)
    # s_plots = s.plot_per_survey(xl, df, j)
    g_detected = s.galactic_detected(xl, df, j)
    g_discovered = s.galactic_discovered(xl, df, j)
    yx_discovered = s.yx_discovered(xl, df, j)
    yx_detected = s.yx_detected(xl, df, j)
    zx_discovered = s.zx_discovered(xl, df, j)
    zx_detected = s.zx_detected(xl, df, j)
    s_plots = s.plotly_per_survey(xl, df, j, html_file)
    g_plots = s.plotly_gl_gb(xl, df, j, html_file)
    yy_xx = s.yy_xx(xl, df, j, html_file)
    zz_xx = s.zz_xx(xl, df, j, html_file)
    
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
    final_str = '<br>' + 'The ' + name_str + ' (' + survey2 + ') ' + ' published its results in ' + str(year_str) + ' with a total of ' + str(num_discovered) + ' new pulsars discovered.\n\n' + 'It' + ' detected a total of ' + str(num_detected) + ' pulsars.\n\n' + fastest_slowest_str + '\n\n' + sal_dm_str + min_str + '<hr>'
    #img_str = '<img src="plots_pngs/' + survey2 + '.png"' + " alt=" + '"' + survey2+ '">'
    p_ref = '<p id="' + survey2 + '"></p>'
    if s_plots == 'None':
        pass
    else:
        print(p_ref, file = html_file)
        #  'src="plots_pngs/' + survey2 + '.png
        print(final_str + '\n\n\n\n', file = html_file)
        print('\n\n\n\n\n' + '<hr>' + '\n', file = html_file)
        print(html_end_str, file = html_file)
# skyplot = s.plot_in_sky()

# print(skyplot, file = html_file)
html_file.close()

    















