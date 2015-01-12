#!/usr/bin/env python

'''
    plot_3ZY.py


    Kam Wan, GATS, Inc. 

'''
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import bin_io as bio
import pylab as pl

def plot_1(in_fn, out_fn):
    xx = bio.read_2d(in_fn, 360, 120, 'd', 0)
    p1 = pl.contourf(xx, 200)
    pl.axis('off')
    for c in p1.collections:
        c.set_antialiased(False)
    ax = pl.axes()
    ax.set_aspect(1.0)
    cax = pl.axes([0.85,0.3,0.03,0.4],axisbg='w')
    pl.colorbar (p1,cax=cax, orientation='vertical') 
    pl.savefig(out_fn)
    pl.close()

plot_1 ('bgd_1', 'bgd.png')
plot_1 ('no_bgd_first_plane', 'no_bg.png')
plot_1 ('with__2pi_first_plane','with__2pi_bg.png')
plot_1 ('bgd_1_first_plane', 'with_1_bg.png')

