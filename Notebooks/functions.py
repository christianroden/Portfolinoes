'''Project's custom functions:
    - plot_roc (draws ROC curve)
    - f_divline (draws the divider line in the cell's output)
'''



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# horizontal divider line

def f_divline(pad_before=True, pad_after=True):
    '''Draws (prints) a simple horizontal line
    Args.:
        pad_before (bool): add pading before the line
        pad_after (bool): add padding after the line
    '''
    line = str('- '*40)
    if pad_before:
        line = '\n'+line
    if pad_after:
        line = line+'\n'
    
    return print(line)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ROC visualization
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Referrenced modules
from sklearn.metrics import roc_curve, auc
from global_settings import *
import global_settings
import matplotlib.ticker as ticker

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def plot_roc(pipe, Xtest, ytest):
    
    yscores = pipe.predict_proba(Xtest)[:,1]
    fpr, tpr, _ = roc_curve(ytest, yscores)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(9, 6))
    plt.plot(fpr, tpr, color=color_palette[1], lw=1.2, label='ROC curve (area = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=1.2, linestyle=(0, (8,10)))
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate (recall)')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    
    plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
    
    # return plt.figure()

    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -