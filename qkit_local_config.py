# This is the local qkit configuration.
# Here you can set everything which is non standard.
# This is the only file you should edit.

cfg = {}

#cfg['SomeGlobalVar'] = 42
# e.g. uncomment the following line to use the x version  of qviewkit
#cfg['plot_engine'] = 'qkit.gui.qviewkit_x.main'

# Where is your data located?
cfg['datadir'] = r'C:\Users\Thilo\Desktop\Projekt Promotion\qkit\data'

# Which version of datafolder structuring do you want?
#  1 = YYYYMMDD/HHMMSS_NAME
#  2 = RUN_ID/USERNAME/UUID_NAME
cfg['datafolder_structure'] = 2

# If you are using qkit for measurements, you should install visa and uncomment the following line:
#cfg['load_visa'] = True

# Which version of the circle fit do you want?
#  1 = "classic" circle fit by S. Probst (only version available until 08/2019)
#  2 = updated circle fit by D. Rieger available since 08/2019
# cfg['circle_fit_version'] = 1