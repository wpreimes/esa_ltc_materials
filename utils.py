from matplotlib import colors
import numpy as np

cm_sm = colors.LinearSegmentedColormap.from_list('BrownBlue',
    np.array([[134, 80, 16],
            [164, 117, 13],
            [219, 190, 24],
            [250, 249, 156],
            [144, 202, 240],
            [4, 145, 251],
            [8, 83, 211],
            [13, 37, 161]]) / 255.)

europe_countries = [
    'Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herz.',
    'Bulgaria', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland',
    'Italy', 'Kosovo', 'Latvia', 'Lithuania', 'Luxembourg',
    'Macedonia', 'Moldova', 'Montenegro', 'Netherlands', 'Norway',
    'Poland', 'Portugal', 'Romania', 'Serbia', 'Slovakia', 'Slovenia',
    'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'
]

sampling = {'daily': '1D', '10-daily': '10D', 'monthly': 'M', '3-monthly': '3M', 'yearly': 'A'}