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

europe_countries = [
    'Albania', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herz.',
    'Bulgaria', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 'Finland',
    'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland',
    'Italy', 'Kosovo', 'Latvia', 'Lithuania', 'Luxembourg',
    'Macedonia', 'Moldova', 'Montenegro', 'Netherlands', 'Norway',
    'Poland', 'Portugal', 'Romania', 'Serbia', 'Slovakia', 'Slovenia',
    'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'
]

def count_consecutive(arr2d, val, symmetric=False, rev_first=False):
    """
    For each row, count the number of consecutive values

    e.g. for val=False
    np.array([[True,False,False,False,True],
              [False,False,True,True, False]])
    --> np.array([[0, 1, 2, 3, 0],
                  [1, 2, 0, 0, 1]])

    Parameters
    ----------
    arr2d: np.array
        Array that contains `val`. `val` will be numbered for each row.
    val: Any
        Element of arr2d to count

    Returns
    -------
    count: np.ndarray
        Counts of `val` in arr2d. Same shape as input data.
    """

    a = np.array(arr2d == val).astype(int).copy()
    _a_rev = np.concatenate([1 - np.fliplr(a)[:, 0][:, np.newaxis], np.fliplr(a)], axis=1)
    _a_fwd = np.concatenate([1 - a[:, 0][:, np.newaxis], a], axis=1)
    gapend_row, gapend_col = np.where(np.diff(_a_rev) == 1)
    gapend_col = (_a_rev.shape[1] - 1) - gapend_col
    gapstart_row, gapstart_col = np.where(np.diff(_a_fwd) == 1)
    gapend_col = gapend_col[np.lexsort((gapend_col, gapend_row))]
    gaprow = np.transpose(np.tile(np.arange(a.shape[0]), (a.shape[1], 1)))
    if not np.all(gapstart_row == gapend_row):
        raise ValueError("Unexpected difference in row / cols")
    gapsize = (gapend_col - gapstart_col)
    gapnum = np.arange(a.shape[1])[np.repeat(gapstart_col, gapsize)]
    fill = np.tile(np.arange(a.shape[1]), (a.shape[0], 1))[a == 1] + 1 - gapnum

    des = fill[np.lexsort((-fill, gapnum, gaprow[a == 1]))]

    # to start count from data, not from edge, always when at edge
    idx_gap_beginning = np.where(gapnum == 0)
    idx_gap_end = ((),) if a.shape[1] not in gapend_col else np.where(gapnum == gapstart_col[-1])
    des[idx_gap_end] = fill[idx_gap_end]

    a[a == 1] = fill

    return a
