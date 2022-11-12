#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
gwuse = ['Industrial', 'Agricultural', 'Ecological & Environmental','Domestic']
data2014 = [20.5, 43.5, 15.9, 20.1]
data2021 = [14.7, 28.7, 35.1, 21.5] 
explode = (0, 0, 0.1, 0)  # only "explode" the 3rd slice

# Creating plot
fig, (ax1, ax2) = plt.subplots(1,2, figsize =(10, 7))

ax1.pie(data2014, labels = gwuse, explode=explode, autopct='%1.1f%%', shadow=True, startangle=45)
ax1.axis('equal')
ax1.set_title("2014 Water Uses in Tianjin: 2.62 billion m\u00b3")


ax2.pie(data2021, labels = gwuse, explode=explode, autopct='%1.1f%%', shadow=True, startangle=45)
ax2.axis('equal')
ax2.set_title("2021 Water Uses in Tianjin: 3.23 billion m\u00b3")

#fig.tight_layout(pad=2.0)
#plt.subplots_adjust(left=0.1,
#                    bottom=0.1,
#                    right=0.9,
#                    top=0.9,
#                    wspace=0.4,
#                    hspace=0.4)
plt.subplots_adjust(top=0.7)   # adjust the distance to sub title


plt.savefig('TJ_GWuse_Pier.png', dpi=300) 
plt.savefig('TJ_GWuse_Pier.pdf')

plt.show()
