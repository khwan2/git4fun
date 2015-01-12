#!/usr/bin/env python

'''
    post_plot_process.py

    Process a group of plots. The processing includes crop, 
    shrink, annotate and pasting together.

    Kam Wan, NWRA/CoRA
    Mar 23, 2012.

'''
import os

def crop_n_shrink(in_fn, out_fn, crop_x, crop_y, x_off, y_off, new_x, new_y):
    '''
        in_fn, out_fn : File name of the input and output images.
        Crop the image to (crop_x, crop_y), with off-set (x_off, y_off).
        Then resize it to (nex_x, new_y).

        convert command (of ImageMagick) is used.

        *** ALL input parameters ARE STRING. ***
        '''

    crop_comm = 'convert -crop ' + crop_x + 'x' + crop_y + '+' + x_off + '+' + y_off + ' ' + in_fn + ' tmp.png' 
    shrk_comm = 'convert -resize ' + new_x + 'x' + new_y + ' tmp.png ' + out_fn
    os.system (crop_comm)
    os.system (shrk_comm)

def annot_it(in_fn, out_fn, annot_str, annot_size, annot_off):
    '''
        Write the input string (annot_str) at location
        (annot_size, annot_off)
        annot_size : String in 'width x height' format.
        annot_off: String for the off-set, in '+x_off+y_off' format.
        '''

    annot_label_comm = 'convert -background gray -fill black -font Helvetica -size ' + annot_size + ' -gravity center label:"' + annot_str + '" label.png'
    annot_comm = 'composite -geometry ' + annot_off + ' label.png ' + in_fn + ' ' + out_fn
    os.system (annot_label_comm)
    os.system (annot_comm)

def glue_image_rc (in_list, out_fn, row_or_colm = 'r'):
    '''
        Glue the image files in the in_list to row_or_colm.
        row_or_colm = 'r' (in a row, by default) or 'c' (in a column).
        out_fn : File name of the resulting image.

        Note: 
            1. A border of 4 pixels is added to each of images in the in_list.
            2. The image could consist of row or column of images in itself.
        '''
    
    # First, do the first member of each image by itself. 
    border_comm = 'convert -bordercolor white -border 4x4 ' + in_list[0] + ' ' + out_fn
    os.system (border_comm)

    num_image = len (in_list)
    for i_image in range(num_image-1):
        border_comm = 'convert -bordercolor white -border 4x4 ' + in_list[i_image+1] + ' tmp.png'
        os.system (border_comm)
        if row_or_colm == 'r':
            glue_comm = 'convert +append ' + out_fn + ' tmp.png ' + out_fn
        if row_or_colm == 'c':
            glue_comm = 'convert -append ' + out_fn + ' tmp.png ' + out_fn

        os.system (glue_comm)

    # After all is done, name the final jpg.
    os.system ('rm tmp.png')


#if __name__ == '__main__':





