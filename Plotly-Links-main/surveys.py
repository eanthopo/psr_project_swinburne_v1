# @author: Evan Anthopoulos
# Surveys Page for the Swinburne Pulsar Encyclopedia of Radio Pulsar Astronomy !

import pandas as pd

class Surveys:
    
    # This returns the list of psrs discovered by the survey at "counter" (aka nth survey)
    def psrs_discovered(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        discovered_indices = []
        for i in range(len(jname_list)):
            df_survey = str(survey_list[i]).strip()
            if survey in df_survey:
                if ',' in df_survey:
                    first_comma = df_survey.index(',')
                    first_survey = df_survey[:first_comma]
                    if first_survey == survey:
                        discovered_indices.append(i)
                elif survey == df_survey:
                    discovered_indices.append(i)
        return discovered_indices
        
    
    
    # This returns the list of psrs detected by the survey at "counter" (aka nth survey)
    def psrs_detected(self, xl_file, df_file, counter: int):
        survey = str(xl_survey_list[counter]).strip()
        detected_indices = []
        first_survey = 'Null'
        for i in range(len(jname_list)):
            df_survey = str(survey_list[i]).strip()
            if ',' in df_survey:
                first_comma = df_survey.index(',')
                first_survey = df_survey[:first_comma]
            else:
                first_survey = df_survey
            if (survey != first_survey) and (survey in str(survey_list[i])):
                detected_indices.append(i)
        return detected_indices




survey_file = 'Surveys.xlsx'
xl = pd.read_excel(survey_file, header=None)

pulsars_available = pd.read_csv('pulsars-links_available.csv', header=None, sep=",", engine='python')

df = pd.read_csv('databasev4.csv', header=None, sep='~', engine='python')

xl_survey_col = 0
xl_survey_name_col = 1
jname_col = 0
survey_col = 10

survey_list = df.iloc[:,survey_col]
jname_list = df.iloc[:,jname_col]
xl_survey_list = xl.iloc[:,xl_survey_col]
xl_survey_name_list = xl.iloc[:,xl_survey_name_col]

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
html_header_str = """
<center>
    <h1>
    Radio Pulsar Surveys
    </h1>
</center>
"""
padding_str = """
<style>
    .indent-all {
	padding-left: 50px;
    padding-right: 50px;
    }
  </style>
"""

html_paragraph_one = """
    <p class="indent-all">
    The first radio pulsar was discovered by Jocelyn Bell in 1967 using a radio telescope at Cambridge designed to study the scintillation of quasars in the interplanetary medium.
    
    <br>
    
    The pulsar catalogue currently hosts 37 surveys. The number of pulsars each survey detected and/or discovered is in the table below.
    
    <br>
    
    For more information, click on the survey name to be taken to a more detailed description.
    
    <hr>
    <br>
"""

s = Surveys()

table_style_str = '<style>\n table, th, td { border:1px solid black;} h2 {text-align: center;}\n</style>' + '<table style="width:100%">\n'
survey_table_header = table_style_str + '<tr> \n<th>SURVEYS</th>' + '<th>NUMBER OF PSRs DISCOVERED</th>' + '<th>NUMBER OF PSRs DETECTED</th>' + '\n</tr>\n\n'
table_contents_str = survey_table_header
for j in range(len(xl_survey_list)):
    survey = str(xl_survey_list[j]).strip()
    survey_name = str(xl_survey_name_list[j]).strip()
    discovered = len(list(s.psrs_discovered(xl, df, j)))
    detected = len(list(s.psrs_detected(xl, df, j)))
    if detected == 0 and discovered == 0:
        pass
    else:
        table_contents_str += '<style>\n td {text-align: center;}\n </style>' + '<tr>\n' + '<td><a target="_blank" href="https://astronomy.swin.edu.au/~mbailes/encyc/' + survey + '_plots.html">' + survey_name + '</a>\n</td>\n' + '<td>' + str(discovered) + '</td>\n' + '<td>' + str(detected) + '</td>\n' + '</tr>\n'
table_contents_str += '\n</table>'
html_file = open('surveys.html', 'w+')
print(html_css_navbar_str + html_header_str, file = html_file)
print(padding_str + html_paragraph_one, file = html_file)
print(table_contents_str, file = html_file)

