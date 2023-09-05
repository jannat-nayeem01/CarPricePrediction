from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')

import matplotlib
np.__version__, pd.__version__, sns.__version__, matplotlib.__version__

df = pd.read_csv('data/Life_Expectancy_Data.csv')
df.head()