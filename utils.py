import numpy as np
from matplotlib import colors

cm_sm = colors.LinearSegmentedColormap.from_list('BrownBlue',
    np.array([[134, 80, 16],
            [164, 117, 13],
            [219, 190, 24],
            [250, 249, 156],
            [144, 202, 240],
            [4, 145, 251],
            [8, 83, 211],
            [13, 37, 161]]) / 255.)