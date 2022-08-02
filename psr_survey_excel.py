# @author: Evan Anthopoulos
# Excel Survey Loader
#                       Stratched Project 

import pandas as pd
# import pulsar_project_v3 as v3

class Survey:
    
    def locate_survey(self, filename, counter: int) -> str:
        survey_str = str(df_survey_list[counter]).strip()
        if '*' not in survey_str:
            if ',' in survey_str:
                first_comma = survey_str.index(',')
                first_survey = str(survey_str[:first_comma]).strip()
                return first_survey
            else:
                return survey_str
        else:
            return 'None'
    
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
        
    
    def year_discovered(self, ls, fas, xl_file, counter: int):
        year_list = []
        year_str = ''
        row_count, column_count = xl_file.shape
        for k in range(len(psr_list)):
            for n in range(row_count):
                survey = str(xl_survey_list[n]).strip()
                 
                if ls == str(xl_survey_list[n]).strip():
                    if '*' not in df_year_list[counter]:
                        year_list.append(df_year_list[counter])
        for year in year_list:
            # year_str += str(year) + ' '
            return year_str



survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file)

survey_col = 0
survey_name_col = 1
assoc_survey_col = 2
df_year_col = 12

xl_survey_list = xl.iloc[:,survey_col]
survey_name_list = xl.iloc[:,survey_name_col]
assoc_survey_list = xl.iloc[:,assoc_survey_col]

df = pd.read_csv('filtered.csv', header=None, sep='~', engine='python')

psr_list = df.iloc[:,0]
df_survey_list = df.iloc[:,10]
df_year_list = df.iloc[:,df_year_col]

s = Survey()

for j in range(len(psr_list)):
    l = s.locate_survey(df, j)
    a = s.first_assoc_survey(xl, df, j)
    y = s.year_discovered(l, a, xl, j)
    print('PSR ' + str(psr_list[j]) + 'appeared in a new survey in the following years: ' + str(y))
    