
import pprint
import pandas as pd
from ggplot import *
import sys

INPUT_FILE ='pandas_generated.csv'
MARGIN= 0.010 # margin in percents related to average
SSUM =0
COUNT=0
YMIN = sys.maxint
YMAX = 0

spowd = pd.read_csv(INPUT_FILE)

for i in range(0,len(spowd)):
    if (spowd["Watts"][i]>YMAX):
        YMAX = spowd["Watts"][i]
    if (spowd["Watts"][i]<YMIN):
        YMIN = spowd["Watts"][i]
    COUNT+=1
    SSUM+=spowd["Watts"][i]

SSAVERAGE = SSUM/COUNT

HIGH_MARGIN= SSAVERAGE + SSAVERAGE * MARGIN
LOW_MARGIN = SSAVERAGE - SSAVERAGE * MARGIN


pprint.pprint(spowd)
#works with color="category" but not with color="Volts"
print ggplot(aes(x='TIME', y='Watts', shape="Volts", color="category", ymin=YMIN, ymax=YMAX), data=spowd) + \
    geom_point() + \
    ggtitle(INPUT_FILE.split(".")[0]) + \
    xlab("Time") + \
    ylab("Watts")

plt.show(1)
