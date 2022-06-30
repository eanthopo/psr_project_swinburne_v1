# Evan Anthopoulos
# Survey Name Extraction


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.atnf.csiro.au/research/pulsar/psrcat/psrcat_ref.html")
driver.get("https://ui.adsabs.harvard.edu/")
assert "harvard" in driver.title