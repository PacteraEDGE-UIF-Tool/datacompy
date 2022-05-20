import matplotlib.pyplot as plt


match_interval_start=[0, 20, 40, 60, 80, 100]
match_width_list=[10,10,10,10,10,10]
unmatch_interval_start=[10, 30, 50, 70, 90]
unmatch_width_list=[10,10,10,10,10]

                 
column_name_set=["unmatch","match","reserve"]
column_names=["match","unmatch","match","unmatch","match","unmatch"]

labels=["win10"]



fig, ax = plt.subplots(figsize=(15, 5))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, max(match_interval_start))

color1="#00FFFF"
color2="#00008B"
rects = ax.barh(labels, match_width_list, left=match_interval_start, height=0.1,
    label="match", color=color1)
rects = ax.barh(labels, unmatch_width_list, left=unmatch_interval_start, height=0.1,
    label="match", color=color2)
'''
    #show text on the bar
    text_color = 'white'
    ax.bar_label(rects, label_type='center', color=text_color)
'''

ax.legend(ncol=len(column_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
plt.show()