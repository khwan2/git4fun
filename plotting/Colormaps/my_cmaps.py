#!/usr/bin/env python

'''
    my_cmaps.py

    1. As a container for color dictionaries.
    2. Return a cmap value used by, e.g. contourf's cmap arguement.
    
    Kam Wan, NWRA/CoRA
    May 29, 2012.

'''

# Define the color dictionaries.
#
# #41 in may22_07_Colors.tbl.
# This is used in most of the IDL Doppler vel profile plots.
cdict41 = {'red': ((0.0, 0.0, 0.0), (0.004, 0.004, 0.004), (0.157, 0.212, 0.212), 
            (0.275,  0.231, 0.231), (0.502,0.0,0.0), (0.667,0.741,0.741 ), 
            (0.996, 1.0, 1.0), (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 0.0),(0.004,0.004, 0.004), (0.157, 0.263, 0.263 ), 
             (0.275, 0.353, 0.353), (0.502,0.0,0.0), (0.667,0.247,0.247), (0.996, 1.0, 1.0), (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),(0.004,0.988,0.988), (0.157,0.561,0.561),  
             (0.275, 0.169, 0.169), (0.502,0.0,0.0), (0.667,0.0,0.0), (0.996, 0.0, 0.0), (1.0,1.0, 1.0))
         }

# #42 in may22_07_Colors.tbl.
# This must be an experimental colormap; try to have 'ligher' color for -ve
# velocity.
cdict42 = {'red': ((0.0, 0.0, 0.0), (0.187, 0.0, 0.0  ), (0.333,  0.0, 0.0 ), (0.5,  0.0, 0.0), (0.667,1.0,1.0  ), (0.823,1.0,1.0 ), (1.0, 1.0, 1.0)),
         'green': ((0.0, 1.0, 1.0),(0.187,  0.5, 0.5 ), (0.333, 0.4, 0.4  ),  (0.5, 0.0, 0.0), (0.667,0.0,0.0  ), (0.823,0.0,0.0 ),  (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),(0.187,0.75,0.5  ), (0.333,0.5,0.5  ),  (0.5, 0.0, 0.0), (0.667,1.0,1.0  ), (0.823,0.0,0.0 ),  (1.0, 0.0, 0.0))}


# Grn, blue, black, red, yellow. This is similar to the above #42, but
# smoother.
cdict01 =  {'red': ((0.0, 0.0, 0.0), (0.187, 0.0, 0.0  ), (0.333,  0.0, 0.0 ), (0.5,  0.0, 0.0), 
                    (0.667,1.0,1.0  ), (0.823,1.0,1.0 ), (1.0, 1.0, 1.0)),
         'green': ((0.0, 1.0, 1.0),(0.187,  0.5, 0.5 ), (0.333, 0.4, 0.4 ),  (0.5, 0.0, 0.0), 
                    (0.667,0.0,0.0  ), (0.823,0.0,0.0 ),  (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),(0.187,0.75,0.5  ), (0.333,0.5,0.5  ),  (0.5, 0.0, 0.0), 
                    (0.667,1.0,1.0  ), (0.823,0.0,0.0 ),  (1.0, 0.0, 0.0))
         }

# IDL's id=4 color table
cdict_idl4 = { 'red': ((0.000, 0.0, 0.0), (0.125, 0.0, 0.0), (0.188, 0.0, 0.0),
    (0.314, 0.0, 0.0), (0.376, 0.0, 0.0), (0.439, 0.0, 0.0),  (0.502,0.471, 0.471), 
    (0.565, 0.784, 0.784), (1.0, 1.0, 1.0)),
               'green': ((0.000, 0.0, 0.0), (0.125, 0.0, 0.0), (0.188, 0.196, 0.196), 
                   (0.314, 0.588, 0.588), (0.376, 0.588, 0.588), (0.439, 0.549, 0.549), 
                   (0.502, 0.392, 0.392),  (0.565, 0.0, 0.0),  (1.0, 1.0, 1.0)),
               'blue': ((0.0, 0.0, 0.0), (0.125, 0.259, 0.259), (0.188, 0.392, 0.392), 
                   (0.314, 0.392, 0.392), (0.376, 0.196, 0.196), (0.439, 0.0, 0.0), 
                   (0.502, 0.0, 0.0), (0.565, 0.0, 0.0), (1.000, 0.0, 0.0))
             }

def get_cdict (dict_num = '41'):
    '''
        Return a color dictionary, corresponding to the input string parameter.
        '41' == #41 in may22_07_Colors.tbl.
        '42' == #42 in may22_07_Colors.tbl.
        '01' == Grn, blue, black, red, yellow. This is similar to the above #42, but smoother.
        'idl4' == IDL default colortable #4 
    '''
    
    cdict = {'41': cdict41, '42':cdict42, '01':cdict01, 'idl4':cdict_idl4}
    return (cdict[dict_num])

def get_cmap (dict_num = '01'):
    '''
        Return a cmap object corresponding to the input dict_num value.
        '41' == #41 in may22_07_Colors.tbl.
        '42' == #42 in may22_07_Colors.tbl.
        '01' == Grn, blue, black, red, yellow. This is similar to the above #42, but smoother.
    '''
    cdict = get_cdict(dict_num)
    import pylab as pl
    cmap = pl.matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 256)
    return (cmap)
