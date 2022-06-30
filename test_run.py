# Evan Anthopoulos
# Excel Survey Loader

import pandas as pd
# import pulsar_project_v3 as v3

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
        year_list = list(dict.fromkeys(year_list))
        print('Survey ' + survey + ' reported new pulsars in the year(s): ' + str(year_list))
        return str(year_list)
    
    
    
    def num_years_discovered(self, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        survey_count = 0
        for i in range(len(df_psr_list)):
            df_survey_str = str(df_survey_list[i]).strip()
            if '*' not in df_survey_str:
                if survey in df_survey_str:
                    survey_count += 1
        print('Survey ' + survey + ' detected pulsars a total of ' + str(survey_count) + ' times.')
        return str(survey_count)
                
    
    
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
        
    




survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file)

survey_col = 0
survey_name_col = 1
assoc_survey_col = 2
df_psr_col = 0
df_survey_col = 10
df_year_col = 12

xl_survey_list = xl.iloc[:,survey_col]
survey_name_list = xl.iloc[:,survey_name_col]
assoc_survey_list = xl.iloc[:,assoc_survey_col]

df = pd.read_csv('filtered.csv', header=None, sep='~', engine='python')

df_psr_list = df.iloc[:,df_psr_col]
df_survey_list = df.iloc[:,df_survey_col]
df_year_list = df.iloc[:,df_year_col]

s = Survey()

for j in range(len(xl_survey_list)):
    l = s.survey_name(xl, j)
    # a = s.first_assoc_survey(xl, df, j)
    y = s.year_discovered(xl, df, j)
    n = s.num_years_discovered(j)
    # print('PSR ' + str(df_psr_list[j]) + 'appeared in a new survey in the following years: ' + str(y))
    