# @author: Evan Anthopoulos
# About Page for the Swinburne Pulsar Encyclopedia of Radio Pulsar Astronomy !



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
Acknowledgements
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

about_str = """
    <p class="indent-all">
    
    This project was written by the summer student <em>Evan Anthopoulos</em> while at the Swinburne University of Technology in 2022 under the supervision of <em>Professor Matthew Bailes</em>. 
    <br>


    <p class="indent-all">
    
    It was based upon earlier prototypes by <em>Rudra Sekhri</em>, <em>Olivia Young</em> and <em>Gabriella Agazie</em> and uses information
    from version 1.67 of the <a target="_blank" href="https://www.atnf.csiro.au/research/pulsar/psrcat/">ATNF pulsar catalogue</a>, <a target="_blank" href="https://ui.adsabs.harvard.edu/">NASA ADS</a> and the <a target="_blank" href="https://pulsars.org.au">Swinburne Pulsar Portal</a> maintained by ADACS. 
    <br>
 
    
    <p class="indent-all">
    
    It was coded entirely in Python. The package used to create the plots is <a target="_blank" href="https://plotly.com/python/">plotly</a>.
    All of the information contained in the website was extracted from version 1.67 of the <a target="_blank" href="https://www.atnf.csiro.au/research/pulsar/psrcat/">ATNF Pulsar Catalogue</a>. 
    <br>


    <p class="indent-all">
    
    Special thanks to <em>Rudra Sekhri</em> for plotting tips, <em>Andrew Jameson</em> for help with the data portal,
    and <em>Ryan Shannon</em> for pulsar help. The source code that was used to produce this website is available upon request from Professor Bailes.
    <br>


    <p class="indent-all">
    
    Evan is very grateful for <em>NANOGrav's International Research Experiences for Students</em> <a target="_blank href="http://nanograv.org/outreach/research_abroad/">(IRES)</a> program for sponsoring the trip, for West Virgina University who directly provided the funding, 
    and for <a target="_blank" href="https://www.ozgrav.org/">OzGrav</a>, the ARC Centre of Excellence for Gravitational Wave Discovery.
    <br>
</html>

"""

html_file = open('about.html', 'w+')
print(html_css_navbar_str + html_header_str, file = html_file)
print(padding_str + about_str, file = html_file)







