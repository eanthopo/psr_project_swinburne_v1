# Evan Anthopoulos
# Excel Survey Loader

import pandas as pd
# import pulsar_project_v3 as v3
import astropy as ap
import matplotlib as plt
from pandas import DataFrame
import plotly.express as px
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
        num_new_pulsars = len(year_list)
        year_list = list(dict.fromkeys(year_list))
        print('Survey ' + survey + ' reported new pulsars in the year(s): ' + str(year_list) + ' with a total of ' + str(num_new_pulsars) + ' new pulsars discovered.')
        return year_list
    
    
    
    def num_years_detected(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        survey_count = 0
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            if '*' not in df_survey_str:
                if survey in df_survey_str:
                    survey_count += 1
        print('Survey ' + survey + ' detected pulsars a total of ' + str(survey_count) + ' times.')
        return str(survey_count)
                
    
    
    def fastest_slowest_period(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        fastest = None
        slowest = None
        fastest_psr = ''
        slowest_psr = ''
        for i in range(len(df_psr_list)):
            if '*' not in str(df_period_list[i]):
                df_period_float = float(df_period_list[i])
                if survey in str(df_survey_list[i]):
                    if (fastest is None) or (df_period_float > fastest):
                        fastest = df_period_float
                        fastest_psr = str(df_psr_list[i])
                    if (slowest is None) or (df_period_float < slowest):
                        slowest = df_period_float
                        slowest_psr = str(df_psr_list[i])
        print('The fastest pulsar discovered by ' + survey + ' was ' + fastest_psr + 'with a period of ' + str(fastest) + ' and the slowest pulsar discovered by ' + survey + ' was ' + slowest_psr + 'with a period of ' + str(slowest))
        return 'The fastest pulsar discovered by ' + survey + ' was ' + fastest_psr + 'with a period of ' + str(fastest) + ' and the slowest pulsar discovered by ' + survey + ' was ' + slowest_psr + 'with a period of ' + str(slowest)
                    
                    
                    
                    
    def small_largest_dm(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        smallest = None
        largest = None
        smallest_psr = ''
        largest_psr = ''
        for i in range(len(df_psr_list)):
            dm = str(df_dm_list[i])
            if '*' not in dm:
                dm = dm.replace('D', 'E')
                df_dm_float = float(dm)
                if survey in str(df_survey_list[i]):
                    if (largest is None) or (df_dm_float > largest):
                        largest = df_dm_float
                        largest_psr = str(df_psr_list[i])
                    if (smallest is None) or (df_dm_float < smallest):
                        smallest = df_dm_float
                        smallest_psr = str(df_psr_list[i])
        print('The largest pulsar discovered by ' + survey + ' was ' + largest_psr + 'with a dm of ' + str(largest) + ' and the smallest pulsar discovered by ' + survey + ' was ' + smallest_psr + 'with a dm of ' + str(smallest))
        return 'The largest pulsar discovered by ' + survey + ' was ' + largest_psr + 'with a dm of ' + str(largest) + ' and the smallest pulsar discovered by ' + survey + ' was ' + smallest_psr + 'with a dm of ' + str(smallest)
                    
    
    
    
    def first_assoc_survey(self, filename, locate_file, counter: int) -> str:
        surv = str(s.locate_survey(locate_file, counter)).strip()
        if 'None' != str(surv):
            row_count, column_count = filename.shape
            for i in range(row_count):
                survey = str(xl_survey_list[i]).strip()
                if surv == survey:
                    assoc_survey = str(assoc_survey_list[i]).strip()
                    if ',' in assoc_survey:
                        first_comma = assoc_survey.index(',')
                        first_assoc_survey = assoc_survey[:first_comma]
                        return first_assoc_survey
                    else:
                        return assoc_survey
        else:
            return ':('
        
    
    
    def plot_in_sky(self):
        raj_cleaned = []
        decj_cleaned = []
        jnames_cleaned = []
        available_or_not = []
        for i in range(len(df_psr_list)):
            if ('*' not in str(df_raj_list[i])) and ('*' not in str(df_decj_list[i])):
                raj = float(str(df_raj_list[i]).strip())
                raj_cleaned.append(raj)
                decj = float(str(df_decj_list[i]).strip())
                decj_cleaned.append(decj)
                jname = str(df_psr_list[i].strip())
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
                'p0': raj_cleaned,
                'p1': decj_cleaned,
                "Available Or Not": available_or_not,
                "URLs": psr_links
            }

            df = DataFrame(data=source)

            fig = px.scatter(df, x="raj", y="decj", color="Available Or Not", log_x=True, log_y=True, hover_name="Name", hover_data=["raj", "decj"], color_discrete_map={"Yes": "#FA7D25", "No" : "#333"}, custom_data=["URLs"])
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

    
    def total_psrs_before_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        year_disc_list = s.year_discovered(xl_file, df_file, counter)
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
            final_str = ''
        final_str = 'For survey ' + survey + ', there were a total of ' + str(year_count) + ' pulsars known before the first survey was published.'
        print(final_str)
        return final_str
                    



survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file, header=None)

survey_col = 0
survey_name_col = 1
assoc_survey_col = 2
psrs_available_col = 0


df_psr_col = 0
df_survey_col = 10
df_year_col = 12
df_period_col = 4
df_dm_col = 7
df_raj_col = 33
df_decj_col = 36

xl_survey_list = xl.iloc[:,survey_col]
survey_name_list = xl.iloc[:,survey_name_col]
assoc_survey_list = xl.iloc[:,assoc_survey_col]

pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')
df = pd.read_csv('filtered.csv', header=None, sep='~', engine='python')

df_psr_list = df.iloc[:,df_psr_col]
df_survey_list = df.iloc[:,df_survey_col]
df_year_list = df.iloc[:,df_year_col]
df_period_list = df.iloc[:,df_period_col]
df_dm_list = df.iloc[:,df_dm_col]
df_raj_list = df.iloc[:,df_raj_col]
df_decj_list = df.iloc[:,df_decj_col]
psrs_available = pulsars_available.iloc[:, psrs_available_col]

s = Survey()

for j in range(len(xl_survey_list)):
    l = s.survey_name(xl, j)
    # a = s.first_assoc_survey(xl, df, j)
    y = s.year_discovered(xl, df, j)
    n = s.num_years_detected(j)
    fas = s.fastest_slowest_period(j)
    sal = s.small_largest_dm(j)
    tpbd = s.total_psrs_before_discovered(xl, df, j)
p = s.plot_in_sky()

    