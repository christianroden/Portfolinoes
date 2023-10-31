# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# colormap (charts) definition

colors = ['#bce6df', '#89c9c4', '#408a8f', '#31767a', '#346880']
nodes = [0, .3, .6 ,.75 ,1]
cf_cmap = LinearSegmentedColormap.from_list('TealToBlue', list(zip(nodes, colors)))

# reversed version
cf_cmap_r = cf_cmap.reversed()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# unregister if exists already (to overwrite)

if cf_cmap.name in plt.colormaps():
    mpl.colormaps.unregister(cf_cmap.name)
if cf_cmap_r.name in plt.colormaps():
    mpl.colormaps.unregister(cf_cmap_r.name)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# register a colormap

mpl.colormaps.register(cmap=cf_cmap)
mpl.colormaps.register(cmap=cf_cmap_r)

# cf_cmap

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# local chart settings

plt.rc('ytick', labelsize=10)
plt.rc('axes', edgecolor='#a8a8a8', facecolor='w', axisbelow=True, grid=True,
      titlelocation='left', titlesize=12, labelsize=11, titlepad=10)
plt.rc('figure', facecolor='w')
plt.rc('axes.spines', bottom=True, left=True, top=False, right=False)
plt.rc('grid', color='darkgrey', linestyle=':', linewidth=1, alpha=.5)