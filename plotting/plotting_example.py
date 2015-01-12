#!/usr/bin/env python

'''
    plot_max_ave_vel.py

    To plot max (and average) vel vs off-zenith angle.


    Kam Wan, NWRA/CoRA
    Apr 15, 2012.

'''

import bin_io
import pylab

wkdir_list = ['Apr09a_12_wkdir',
'Apr09b_12_wkdir','Apr09c_12_wkdir','Apr09d_12_wkdir']

angle_list = [-15., -5, 0., 5., 15.]

num_wkdir = len (wkdir_list)
num_angle = len (angle_list)

mark_list = ['o', 's', 'd', '*']
# These labels are to be used by the legend() function.
label1_list = ['t=12, Max.', 't=14, Max.','t=15, Max.','t=17, Max.']
label2_list = ['t=12, Ave.', 't=14, Ave.','t=15, Ave.','t=17, Ave.']

for i_wd in range (num_wkdir):
#for i_wd in range (1):
    max_fn = wkdir_list[i_wd] + '/vel_maxima'
    max_vel = bin_io.read_1d(max_fn, num_angle, 'f', 0)
    ave_fn = wkdir_list[i_wd] + '/vel_ave'
    ave_vel = bin_io.read_1d(ave_fn,  num_angle, 'f', 0)
    p1 = pylab.plot (angle_list, max_vel, color = 'black', marker =
            mark_list[i_wd], label=label1_list[i_wd])
    p2 = pylab.plot (angle_list, ave_vel, color = 'black',linestyle = 'dashed',
            marker = mark_list[i_wd], label=label2_list[i_wd])
# The legend() uses the label arguments in the plot function appeared before it.
pylab.legend()
pylab.title ('Doppler Velocity: Domain Max. And Ave.')
pylab.xlabel ('Off-zenith Angle (Deg.)')
pylab.ylabel ('Doppler Velocity (m/s)')

#pylab.show()

pylab.savefig('max_ave_vel_1st4.jpg')
