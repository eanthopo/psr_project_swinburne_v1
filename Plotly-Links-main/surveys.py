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
    <head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}

.navbar {
  overflow: hidden;
  background-color: #333;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar-right {
  float: right;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>
</head>
<body>

<div class="navbar">
  <a href="https://astronomy.swin.edu.au/~mbailes/encyc/home.html">Home</a>
  <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pulsars.html">Pulsars</a>
  <div class="dropdown">
    <button class="dropbtn">Surveys
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/surveys.html">Surveys Page</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ar1_plots.html">1st Arecibo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ar2_plots.html">2nd Arecibo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ar3_plots.html">3rd Arecibo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ar4_plots.html">4th Arecibo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/palfa_plots.html">Arecibo Multibeam Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ar327_plots.html">Arecibo 327 MHz Drift-Scan Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/FermiBlind_plots.html">Fermi Gamma-Ray Observatory blind survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/FermiAssoc_plots.html">Searches of Unidentified Fermi gamma-ray Sources</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gb1_plots.html">Green Bank Northern Hemisphere Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gb2_plots.html">Princeton-NRAO Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gb3_plots.html">Green Bank short-period Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gb4_plots.html">Green Bank fast pulsar Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gbt350_plots.html">Green Bank 350 MHz drift-scan Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/gbncc_plots.html">Green Bank North Celestial Cap Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/ghrss_plots.html">GMRT High Resolution Southern Sky Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/htru_eff_plots.html">Parkes High Time Resolution Universe Survey (HTRU) - Effelsberg</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/htru_pks_plots.html">Parkes High Time Resolution Universe Survey (HTRU)</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/jb1_plots.html">Jodrell A Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/jb2_plots.html">Jodrell B Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/mol1_plots.html">1st Molonglo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/mol2_plots.html">2nd Molonglo Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pks1_plots.html">Parkes 20-cm Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pks70_plots.html">Parkes Southern Sky Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pkshl_plots.html">Parkes high-latitude multibeam pulsar Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pksgc_plots.html">Parkes globular cluster Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pksmb_plots.html">Parkes multibeam pulsar Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pkssw_plots.html">Parkes Swinburne intermediate latitude pulsar Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pkspa_plots.html">Parkes Perseus Arm multibeam Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pksngp_plots.html">Parkes deep northern Galactic Plane Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/pks_superb_plots.html">Parkes survey for pulsars and extragalactic radio bursts</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/lotaas_plots.html">LOFAR Tied Array All-sky Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/fast_uwb_plots.html">FAST UWB Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/fast_gpps_plots.html">FAST GPPS Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/chime_plots.html">CHIME Pulsar Survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/meerkat_trapum_plots.html">MeerKAT TRAPUM survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/fast_mb_plots.html">FAST 19-beam L-Band survey</a>
        <a href="https://astronomy.swin.edu.au/~mbailes/encyc/misc_plots.html">Several Minor Surveys (misc)</a>
      </div>
    </div>

  <div class="navbar-right">
    <a href="https://astronomy.swin.edu.au/~mbailes/encyc/about.html">About</a>
    </div>
  </div> 
</div>
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

