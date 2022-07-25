# Evan Anthopoulos
# 3D Plotly Stuff

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
    