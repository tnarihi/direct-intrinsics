from __future__ import print_function

import glob
import os
from os.path import join, dirname
import csv
import argparse

from six.moves import range
import numpy as np
from scipy.misc import imread, imsave

parser = argparse.ArgumentParser()
parser.add_argument('--dir_data', default='.')
args = parser.parse_args()

dir_source = join(args.dir_data, 'sources_18')
dir_img = join(args.dir_data, 'images')

sa = 'albedo'
ss = 'shading'
sc = 'clean'
keys = [sc, sa, ss]

sources = {}
for k in keys:
    sources[k] = join(dir_source, 'source_{}_full.txt'.format(k))

def load_list(p):
    return map(lambda x: x[0], csv.reader(open(p)))

paths = {}
for k in keys:
    paths[k] = load_list(sources[k])
    
for i in range(len(paths[sa])):
    imgs = {}
    for k in keys:
        imgs[k] = imread(join(dir_img, paths[k][i])).astype(np.float32) / 255
    rs = imgs[sa] * imgs[ss]
    path_o = join(dir_img, 'RS', paths[sc][i].replace('clean/', ''))
    dir_o = dirname(path_o)
    if not os.path.isdir(dir_o):
        os.makedirs(dir_o)
    imsave(path_o, rs)
