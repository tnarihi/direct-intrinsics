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
    gs = np.repeat(imgs[ss].mean(axis=2, keepdims=True), 3, 2)
    rgs = imgs[sa] * gs
    path_o = join(dir_img, paths[sc][i].replace('clean/', 'RGS/'))
    dir_o = dirname(path_o)
    if not os.path.isdir(dir_o):
        os.makedirs(dir_o)
    imsave(path_o, rgs)
    path_o = join(dir_img, paths[ss][i].replace('shading/', 'gray_shading/'))
    dir_o = dirname(path_o)
    if not os.path.isdir(dir_o):
        os.makedirs(dir_o)
    imsave(path_o, gs)

paths_clean = glob.glob(join(args.dir_data, 'sources_*/source_clean_*.txt'))
for path_clean in paths_clean:
    path_rs = path_clean.replace('_clean_', '_RGS_')
    lines = map(lambda x: x.replace('clean/', 'RGS/'), open(path_clean, 'r').readlines())
    with open(path_rs, 'w') as fd:
        for l in lines:
            print(l, file=fd, end='')

paths_shading = glob.glob(join(args.dir_data, 'sources_*/source_shading_*.txt'))
for path_shading in paths_shading:
    path_gs = path_shading.replace('source_shading_', 'source_gray_shading_')
    lines = map(lambda x: x.replace('shading/', 'gray_shading/'), open(path_shading, 'r').readlines())
    with open(path_gs, 'w') as fd:
        for l in lines:
            print(l, file=fd, end='')
