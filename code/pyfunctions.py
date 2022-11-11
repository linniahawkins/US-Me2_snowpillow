import os, glob
import numpy as np
import pandas as pd
from datetime import datetime

def get_datetime(df):
    index = []
    for ij in range(len(df)):
        doy = str(df.loc[ij,2])
        doy.rjust(3 + len(doy), '0')
        year = str(df.loc[ij,1])
        hr = str(round(df.loc[ij,3]/100.0))
        index.append(datetime.strptime(year + "-" + doy + "-" + hr, "%Y-%j-%H"))
    return index