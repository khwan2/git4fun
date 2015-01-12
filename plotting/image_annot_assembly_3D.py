#!/usr/bin/env python

This should be modified to make use of the new post_plot_process.py


'''
    image_annot_assembly_3D.py

    Trim and annotate images, and then glue them in different configurations.

    The '3D' indicates that it can handle plots along one of the (time, advection, angle) axes.

    Kam Wan, NWRA/CoRA
    Mar 2, 2012.

'''
import os

#import pdb

def crop_n_shrink():
    '''
        Crop the image to (crop_x, crop_y).
        Then resize it to (nex_x, new_y).
        '''

    crop_x = '3700'
    crop_y = '3200'
    new_x = '740'
    new_y = '640'
    pow_crop_comm = 'convert -crop ' + crop_x + 'x' + crop_y + '+0+0 power.jpg crop_power.jpg'
    dv_crop_comm = 'convert -crop ' + crop_x + 'x' + crop_y + '+0+0 dop_vel.jpg crop_dop_vel.jpg'
    pow_shrk_comm = 'convert -resize ' + new_x + 'x' + new_y + ' crop_power.jpg shrk_pow.jpg'
    dv_shrk_comm = 'convert -resize ' + new_x + 'x' + new_y + ' crop_dop_vel.jpg shrk_dv.jpg'
    os.system (pow_crop_comm)
    os.system (dv_crop_comm)
    os.system (pow_shrk_comm)
    os.system (dv_shrk_comm)

def annot_it(annot_str):
    '''
        Write the input string (annot_str) at location
        (annot_size, annot_off)
        '''

    annot_size = '240x50'
    annot_off = '+20+20'
    annot_label_comm = 'convert -background gray -fill black -font Helvetica -size ' + annot_size + ' -gravity center label:"' + annot_str + '" label.jpg'
    annot_pow_comm = 'composite -geometry ' + annot_off + ' label.jpg shrk_pow.jpg lab_pow.jpg'
    annot_dv_comm = 'composite -geometry ' + annot_off + ' label.jpg shrk_dv.jpg lab_dv.jpg'
    os.system (annot_label_comm)
    os.system (annot_pow_comm)
    os.system (annot_dv_comm)

def image_assembly (runs_list, n_runs):
    '''
        Glue the lab_pow.jpg (power profile with label) in each of the run-directories
        in the runs_list to a row. Do the same for lab_dv.jpg.
        The output file names are pow_row.jpg and dv_row.jpg.

        Do the same to form columns.

        Finally pair power and Dopp vel together.

        '''
    
    # First, do the first member of each image by itself. 
    pow_jpg = runs_list[0] + '/lab_pow.jpg'
    border_comm = 'convert -bordercolor white -border 4x4 ' + pow_jpg + ' pow_row.jpg'
    os.system (border_comm)
    border_comm = 'convert -bordercolor white -border 4x4 ' + pow_jpg + ' pow_colm.jpg'
    os.system (border_comm)
    dv_jpg = runs_list[0] + '/lab_dv.jpg'
    border_comm = 'convert -bordercolor white -border 4x4 ' + dv_jpg + ' dv_row.jpg'
    os.system (border_comm)
    border_comm = 'convert -bordercolor white -border 4x4 ' + dv_jpg + ' dv_colm.jpg'
    os.system (border_comm)

    for i_run in range(n_runs-1):
        pow_jpg = runs_list[i_run+1] + '/lab_pow.jpg'
        border_comm = 'convert -bordercolor white -border 4x4 ' + pow_jpg + ' tmp_pow1.jpg'
        os.system (border_comm)
        glue_comm = 'convert +append pow_row.jpg tmp_pow1.jpg pow_row.jpg'
        os.system (glue_comm)
        glue_comm = 'convert -append pow_colm.jpg tmp_pow1.jpg pow_colm.jpg'
        os.system (glue_comm)

        dv_jpg = runs_list[i_run+1] + '/lab_dv.jpg'
        border_comm = 'convert -bordercolor white -border 4x4 ' + dv_jpg + ' tmp_dv1.jpg'
        os.system (border_comm)
        glue_comm = 'convert +append dv_row.jpg tmp_dv1.jpg dv_row.jpg'
        os.system (glue_comm)
        glue_comm = 'convert -append dv_colm.jpg tmp_dv1.jpg dv_colm.jpg'
        os.system (glue_comm)

    # After all is done, name the final jpg.
    os.system ('rm tmp_*.jpg')

    # To power and Dopp vel pairs.
    row_pair_comm = 'convert -append pow_row.jpg dv_row.jpg pow_dv_row.jpg'
    os.system (row_pair_comm)

    colm_pair_comm = 'convert +append pow_colm.jpg dv_colm.jpg pow_dv_colm.jpg'
    os.system (colm_pair_comm)


if __name__ == '__main__':
    work_dir = os.getcwd()
    # Define the global variables when processing along different 'axis'.
    along = '1'
    if (along == 'xxxx1'):
        dim1 = ['_m15', '_m10', '_m05', '_p00', '_p05', '_p10', '_p15']
        annot1 = ['-15', '-10', '-5.', '0.0', '5.0', '10.', '15.']
        n_dim1 = 7
        dim2=['_sht0_std1', '_sht1_std2', '_sht1_std1', '_sht3_std2']
        annot2=['0.0', '3.5', '7.0', '10.']
        n_dim2 = 4
        dim3=['02', '03', '04', '05', '06', '07', '08', '09', '10']
        annot3=[' 54', ' 69', ' 84', '112', '129', '190', '255', '312', '364']
        n_dim3 = 9
        # To build the signal2dop.sh work-dir.
        for d1 in range (n_dim1):
            for d2 in range (n_dim2):
                plt_dir = 'vs_time/adv' + dim2[d2] + dim1[d1] + '/thrd_0.01_samegray/'
                print (" thrd dir = %s \n" % plt_dir)
                # To generate a list of run names
                runs_list = []
                for d3 in range (n_dim3):


                    this_run = 'sept28_run' + dim3[d3] + dim2[d2] + dim1[d1]
                    # Build up the runs_list. This will be used under thrd_0.01_samegray/.
                    runs_list.append (this_run)
                    # Since I am in the work-dir now, may be I need this ('imag_dir')
                    imag_dir = plt_dir + this_run
                    os.chdir (imag_dir)
                    crop_n_shrink()
                    annot_str = annot3[d3] + ', ' + annot2[d2] + ', ' + annot1[d1]
                    annot_it(annot_str)
                    os.chdir (work_dir)

                os.chdir (plt_dir)

                #pdb.set_trace()
                image_assembly (runs_list, n_dim3)
                os.chdir (work_dir)

    os.chdir (work_dir)
    along = '2'
    if (along == 'xxxx2'):
        dim1 = ['_sht0_std1', '_sht1_std2', '_sht1_std1', '_sht3_std2']
        annot1=['0.0', '3.5', '7.0', '10.']
        n_dim1 = 4
        dim2=['02', '03', '04', '05', '06', '07', '08', '09', '10']
        annot2=[' 54', ' 69', ' 84', '112', '129', '190', '255', '312', '364']
        n_dim2 = 9
        dim3=['_m15', '_m10', '_m05', '_p00', '_p05', '_p10', '_p15']
        annot3 = ['-15', '-10', '-5.', '0.0', '5.0', '10.', '15.']
        n_dim3 = 7

        # To build the signal2dop.sh work-dir.
        for d1 in range (n_dim1):
            for d2 in range (n_dim2):
                plt_dir = 'vs_angle/r' + dim2[d2] + dim1[d1] + '/thrd_0.01_samegray/'
                print (" thrd dir = %s \n" % plt_dir)
                # To generate a list of run names
                runs_list = []
                for d3 in range (n_dim3):
                    ##  pdb.set_trace()
                    this_run = 'sept28_run' + dim2[d2] + dim1[d1] + dim3[d3]
                    # Build up the runs_list. This will be used under thrd_0.01_samegray/.
                    runs_list.append (this_run)
                    imag_dir = plt_dir + this_run
                    os.chdir (imag_dir)
                    crop_n_shrink()
                    annot_str = annot2[d2] + ', ' + annot1[d1] + ', ' + annot3[d3]
                    annot_it(annot_str)
                    os.chdir (work_dir)

                os.chdir (plt_dir)

                image_assembly (runs_list, n_dim3)
                os.chdir (work_dir)


    os.chdir (work_dir)
    along = '3'
    if (along == '3'):
        dim1=['02', '03', '04', '05', '06', '07', '08', '09', '10']
        annot1=[' 54', ' 69', ' 84', '112', '129', '190', '255', '312', '364']
        n_dim1 = 9
        dim2=['_m15', '_m10', '_m05', '_p00', '_p05', '_p10', '_p15']
        annot2 = ['-15', '-10', '-5.', '0.0', '5.0', '10.', '15.']
        n_dim2 = 7
        dim3 = ['_sht0_std1', '_sht1_std2', '_sht1_std1', '_sht3_std2']
        annot3=['0.0', '3.5', '7.0', '10.']
        n_dim3 = 4
        # To build the signal2dop.sh work-dir.
        for d1 in range (n_dim1):
            for d2 in range (n_dim2):
                plt_dir = 'vs_advec/r' + dim1[d1] + dim2[d2] + '/thrd_0.01_samegray/'
                print (" thrd dir = %s \n" % plt_dir)
                # To generate a list of run names
                runs_list = []
                for d3 in range (n_dim3):
                    this_run = 'sept28_run' + dim1[d1] + dim3[d3] + dim2[d2]
                    # Build up the runs_list. This will be used under thrd_0.01_samegray/.
                    runs_list.append (this_run)
                    imag_dir = plt_dir + this_run
                    os.chdir (imag_dir)
                    crop_n_shrink()
                    annot_str = annot1[d1] + ', ' + annot3[d3] + ', ' + annot2[d2]
                    annot_it(annot_str)
                    os.chdir (work_dir)

                os.chdir (plt_dir)

                image_assembly (runs_list, n_dim3)
                os.chdir (work_dir)







