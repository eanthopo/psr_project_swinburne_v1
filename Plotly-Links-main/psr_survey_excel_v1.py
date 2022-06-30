# Evan Anthopoulos
# Excel Survey Loader

import pandas as pd
# import pulsar_project_v3 as v3
from astropy.visualization import quantity_support
from astropy.coordinates import SkyCoord
from astropy import units as u
import astropy.coordinates as coord
from matplotlib import pyplot as plt

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
        if '1089806188' in str(year_list):
            year_list.remove('1089806188')
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
                    if (slowest is None) or (df_period_float > slowest):
                        slowest = df_period_float
                        slowest_psr = str(df_psr_list[i])
                    if (fastest is None) or (df_period_float < fastest):
                        fastest = df_period_float
                        fastest_psr = str(df_psr_list[i])
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
        quantity_support()
        plt.figure(figsize=(8,6))
        raj_plt_list = []
        decj_plt_list = []
        for i in range(len(df_psr_list)):
            if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list):
                raj = str(df_raj_list[i]).strip()
                decj = str(df_decj_list[i]).strip()
                raj_plt_list.append(raj)
                decj_plt_list.append(decj)
        c = SkyCoord(ra=raj_plt_list,dec=decj_plt_list, unit=(u.hourangle,u.deg), frame='icrs')
        ranew = coord.Angle(c.ra.rad,unit=u.rad)
        ranew2 = ranew.wrap_at('180d', inplace=False)
        decnew = coord.Angle(c.dec.rad,unit=u.degree)
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection="mollweide")
        s_plot = ax.scatter(ranew2, decnew)
        return s_plot
        
        
    
    def plot_per_survey(self, xl_file, df_file, counter):
        quantity_support()
        first_survey = str(s.first_assoc_survey(xl_file, df_file, counter)).strip()
        survey = str(xl_survey_list[counter]).strip()
        plt.figure(figsize=(8,6))
        raj = [] # list of all raj
        first_raj = [] # list of raj discovered by specific survey
        in_raj = [] # list of raj detected by specific survey
        decj = [] # list of all decj
        first_decj = [] # list of decj discovered by specific survey
        in_decj = [] # list of decj detected by specific survey
        for i in range(len(df_psr_list)):
            if '*' not in str(df_raj_list[i]) and '*' not in str(df_decj_list):
                if survey == first_survey:
                    raj_temp = str(df_raj_list[i]).strip()
                    decj_temp = str(df_decj_list[i]).strip()
                    first_raj.append(raj_temp)
                    first_decj.append(decj_temp)
                elif (survey != first_survey) and (survey in str(df_survey_list[i])):
                    raj_temp = str(df_raj_list[i]).strip()
                    decj_temp = str(df_decj_list[i]).strip()
                    in_raj.append(raj_temp)
                    in_decj.append(decj_temp)
        c = SkyCoord(ra=raj,dec=decj, unit=(u.hourangle,u.deg), frame='icrs')
        ranew = coord.Angle(c.ra.rad,unit=u.rad)
        ranew2 = ranew.wrap_at('180d', inplace=False)
        decnew = coord.Angle(c.dec.rad,unit=u.degree)
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection="mollweide")
        survey_plot = ax.scatter(ranew2, decnew)
        return survey_plot
                

    
    def total_psrs_before_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        year_disc_list = s.year_discovered(xl_file, df_file, counter)
        year_count = 0
        if len(year_disc_list) > 1:
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

html_file = open('survey_plots.html', 'w+')
html_start_str = '<html>\n' + ' <head>\n' + '  <title>\n' + ' Second attempt.' + '  </title>' + ' </head>' + ' <body>' + '  This is my second webpage.\n'
html_end_str = '\n</body>' + '\n</html>'
print(html_start_str, file = html_file)

for j in range(len(xl_survey_list)):
    name = s.survey_name(xl, j)
    # a = s.first_assoc_survey(xl, df, j)
    year = s.year_discovered(xl, df, j)
    n_span = s.num_years_detected(j)
    fastest_slowest = s.fastest_slowest_period(j)
    sal_dm = s.small_largest_dm(j)
    s_plots = s.plot_per_survey(xl, df, j)
    tpbd = s.total_psrs_before_discovered(xl, df, j)
    
skyplot = s.plot_in_sky()


    