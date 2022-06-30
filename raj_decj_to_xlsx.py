# Evan Anthopoulos

import pandas as pd
from pandas import DataFrame
import matplotlib as plt
from astropy.visualization import quantity_support
from astropy import units as u
from matplotlib import pyplot as plty

df = pd.read_csv('filtered.csv', header=None, sep='~', engine='python')

psr_list = df.iloc[:,0]
raj_list = df.iloc[:,33]
decj_list = df.iloc[:,36]

raj = []
decj = []

file1 = open('raj_decj_astropy.xlsx', 'w+')

for i in range(len(psr_list)):
    if '*' not in str(raj_list[i]) and '*' not in str(decj_list):
        raj_str = str(raj_list[i]).strip()
        decj_str = str(decj_list[i]).strip()
        raj.append(raj_str)
        decj.append(decj_str)
fd = DataFrame({'raj': raj, 'decj': decj})
fd.to_excel('raj_decj_astropy.xlsx', sheet_name='sheet1', index=False)