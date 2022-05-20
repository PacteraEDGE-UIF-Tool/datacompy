import numpy as np
from matplotlib import colors as mcolors 
import matplotlib.pyplot as plt


category_names = ['match','unmatch']
results = {
    'win 10': [10, 15, 17, 32, 26, 100],
    'win 11': [26, 22, 29, 10, 13, 100],
}


def survey(results:dict, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    #category_colors = plt.colormaps['RdYlGn'](
    #    np.linspace(0.15, 0.85, data.shape[1]))

    color1="#00FFFF"
    color2="#00008B"
    key_color_dict=dict()
    #results is dictionary
    for key, value in results.items():
        category_colors=[]
        data_len=len(value)
        for i in range(0, data_len):
            if i % 2==0:
                category_colors.append(color1)
            else:
                category_colors.append(color2)
        print(category_colors)
        key_color_dict[key]=category_colors

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    #for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    for i, (key, value) in enumerate(key_color_dict.items()): 
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.2,
                        label=colname, color=mcolors.to_rgba(color))

        r, g, b, _ = mcolors.to_rgba(color)
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, category_names)
plt.show()
