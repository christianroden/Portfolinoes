# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# import essential modules

import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# global variables

random_seed = 42
random_seed_split = 0
pd.options.display.float_format = '{:.2f}'.format

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# color palette

color_palette = {0:'#85d4c8', 1:'#fc6226', 2:'#fc037f'} #db4125 fc6226 0 - main_color, 1 - accent_color
sns_color_palette = {0:'#51ad9f', 1:'#fc6226'}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# visualization settings

plt.style.use('seaborn-v0_8')

plt.rc('xaxis', labellocation='center')
plt.rc('yaxis', labellocation='center')
plt.rc('axes', titlelocation='left')
plt.rc('axes.spines', bottom=True, left=True)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# visualization params - font sizes

plt.rc('font', size=12)
plt.rc('axes', titlesize=12, labelsize=11, titlepad=10)
plt.rc('xtick', labelsize=8)
plt.rc('ytick', labelsize=8)
plt.rc('figure', titlesize=14)
plt.rc('legend', fontsize=11, title_fontsize=11)
sns.set(font_scale=0.9)
sns.set_context('paper', rc={'axes.labelsize':10.5, 'legend.fontsize':10, 'legend.title_fontsize':10,
                            'xtick.labelsize':8, 'ytick.labelsize':8, 'axes.titlesize':11})



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -