import os
from glob import glob
from os.path import join, basename, dirname

import numpy as np
from scipy.misc import imread, imsave

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')

args = parser.parse_args()

dir_mask = join(args.dir_data, 'images', 'albedo_defect_mask')
dir_albedo = join(args.dir_data, 'images', 'albedo')


for dir_scene in sorted(glob(join(dir_albedo, '*'))):
    for path_albedo in sorted(glob(join(dir_scene, '*.png'))):
        albedo = imread(path_albedo)
        mask = np.repeat((albedo.mean(2) != 0).astype(np.uint8)[..., np.newaxis] * 255, 3, 2)
        dir_out = join(dir_mask, basename(dir_scene))
        try: os.makedirs(dir_out)
        except: pass
        imsave(join(dir_out, basename(path_albedo)), mask)
